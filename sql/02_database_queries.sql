-- =============================================================================
-- FruitBlend24: Commercial Analytics & P&L Data Mart Queries
-- File: 02_database_queries.sql
-- Description: ETL views to sanitize raw orders, calculate unit margins,
--              incorporate platform commissions, and aggregate monthly P&L.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. VIEW: vw_order_profitability
-- Cleans SKU naming, calculates COGS, net revenue, and gross profit per order.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW public.vw_order_profitability AS
WITH clean_orders AS (
    SELECT
        o.date,
        o.hour,
        o.day_of_week,
        TO_CHAR(o.date, 'YYYY-MM') AS month_year,
        o.kitchen,
        o.rate_code,
        LEFT(o.rate_code, 2) AS platform_code,
        o.price_thb AS unit_price,
        o.units_sold,
        o.gross_revenue_thb AS gross_revenue,
        -- Standardize raw Thai/English item names to core SKUs
        CASE
            WHEN o.item_name_raw IN ('Watermelon Ice', 'Watermelon smoothy', 'Watermelon Smoothie',
                                     'watermelon ice', 'แตงโมปั่นสด', 'แตงโมปั่น', 'แตงโมปั่น (ไซส์ M)')
                THEN 'Watermelon'
            WHEN o.item_name_raw IN ('Pineapple Ice', 'pineapple ice', 'สับปะรดปั่น',
                                     'สัปปะรดปั่น', 'Pineapple Smoothie', 'Pineapple smoothie')
                THEN 'Pineapple'
            WHEN o.item_name_raw IN ('Guava Ice', 'Guava Smoothie', 'ฝรั่งปั่น (ใส่เกลือ)',
                                     'guava ice', 'ฝรั่งปั่น')
                THEN 'Guava'
            WHEN o.item_name_raw IN ('Passion Fruit Smoothie', 'เสาวรสปั่น', 'Passion Fruit Ice',
                                     'เสาวรสปั่นเข้มข้น', 'passionfruit ice')
                THEN 'PassionFruit'
            WHEN o.item_name_raw IN ('เบอร์รี่ปั่นพรีเมียม', 'berry premium smoothie',
                                     'Mixed Berry (Premium)', 'เบอร์รี่รวมพรีเมียม', 'Mixed Berry Premium')
                THEN 'MixedBerryPremium'
            ELSE NULL
        END AS sku,
        -- Truncate order date to Monday to join weekly fruit costs
        DATE_TRUNC('week', o.date)::DATE AS week_start
    FROM public.orders_hourly o
    WHERE o.item_name_raw NOT IN ('น้ำส้มปั่น (เมนูทดลอง)', 'Combo Set A (2 แก้ว)', 'แก้วเปล่า')
),
cost_enriched AS (
    SELECT
        co.*,
        p.commission_rate,
        wfc.fruit_cost_per_cup_thb AS unit_fruit_cost,
        ca.packaging_cost_per_cup_thb AS unit_packaging_cost,
        ca.labor_cost_per_cup_thb AS unit_labor_cost
    FROM clean_orders co
    LEFT JOIN public.platform_commission_rate p
        ON co.platform_code = p.platform_code
    LEFT JOIN public.weekly_fruit_cost wfc
        ON co.week_start = wfc.week_start AND co.sku = wfc.sku
    LEFT JOIN public.cost_assumptions ca
        ON co.sku = ca.sku
    WHERE co.sku IS NOT NULL
)
SELECT
    date,
    hour,
    day_of_week,
    month_year,
    kitchen,
    rate_code,
    platform_code,
    sku,
    unit_price,
    units_sold,
    gross_revenue,
    commission_rate,
    -- Financial metrics
    (gross_revenue * (1 - commission_rate)) AS net_revenue,
    unit_fruit_cost,
    unit_packaging_cost,
    unit_labor_cost,
    ((unit_fruit_cost + unit_packaging_cost + unit_labor_cost) * units_sold) AS total_cogs,
    ((gross_revenue * (1 - commission_rate)) - ((unit_fruit_cost + unit_packaging_cost + unit_labor_cost) * units_sold)) AS gross_profit
FROM cost_enriched;


-- -----------------------------------------------------------------------------
-- 2. VIEW: vw_monthly_pl_summary
-- Aggregates monthly revenue, COGS, waste, and applies fixed kitchen overhead.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW public.vw_monthly_pl_summary AS
WITH monthly_orders AS (
    SELECT
        month_year,
        SUM(gross_revenue) AS total_gross_revenue,
        SUM(net_revenue) AS total_net_revenue,
        SUM(total_cogs) AS total_cogs,
        SUM(gross_profit) AS total_gross_profit
    FROM public.vw_order_profitability
    GROUP BY month_year
),
monthly_waste AS (
    SELECT
        TO_CHAR(date, 'YYYY-MM') AS month_year,
        SUM(est_waste_cost_thb) AS total_waste_cost
    FROM public.waste_daily
    GROUP BY TO_CHAR(date, 'YYYY-MM')
)
SELECT
    mo.month_year,
    mo.total_gross_revenue,
    mo.total_net_revenue,
    mo.total_cogs,
    mo.total_gross_profit,
    COALESCE(mw.total_waste_cost, 0) AS total_waste_cost,
    (mo.total_gross_profit - COALESCE(mw.total_waste_cost, 0)) AS gross_profit_after_waste,
    -- Fixed overhead: 180k (Central) + 150k (Beach) + 200k (Sukhumvit) + 140k (Ladprao) = 670k/mo
    670000.00 AS fixed_overhead,
    ((mo.total_gross_profit - COALESCE(mw.total_waste_cost, 0)) - 670000.00) AS operating_profit
FROM monthly_orders mo
LEFT JOIN monthly_waste mw
    ON mo.month_year = mw.month_year
ORDER BY mo.month_year;