# FruitBlend24 — Financial Turnaround & Commercial Revenue Analytics

An end-to-end commercial performance diagnostics, unit economics modeling, and operational turnaround strategy for **FruitBlend24**, an omni-channel cloud-kitchen smoothie brand operating 4 central kitchens across Bangkok and Pattaya (Pattaya_Central, Pattaya_Beach, BKK_Sukhumvit, and BKK_Ladprao) exclusively via Grab and LINE MAN.

---

##  Executive Summary
* **Annual Net Revenue:** 22.63M THB (fell short of management's 32.40M THB flat budget by **-30.2%** / -9.77M THB).
* **Operating Performance:** Closed the 12-month fiscal period with an operating loss of **-404.2K THB** (-1.8% net margin) on 14.12M THB COGS. The loss was driven by severe rainy-season demand contraction, fixed overhead burn (670K THB/month), and high fruit spoilage.
* **Turnaround Potential:** A coordinated strategy encompassing SKU repricing, Just-In-Time (JIT) daily inventory procurement, and operating hour rationalization creates **+445K to +500K THB** in projected commercial value over Q4, returning operations to net profitability.

---

##  Repository Structure
```text
FruitBlend24-Revenue-Analytics/
│
├── data/           # Raw Excel dataset and dictionary (FruitBlend24_Intern_Case_Data.xlsx)
├── sql/            # P&L Data Mart views & joins (02_database_queries.sql)
├── scripts/        # Python ETL pipeline & automated slide generator (01_data_cleaning.py, create_deck.py)
├── bi/             # Interactive 4-page Power BI data model (FruitBlend24_Dashboard.pbix)
├── presentation/   # Executive slide deck & PDF export (.pptx, .pdf)
├── .gitignore
└── README.md
```

---

##  Tech Stack & Analytical Methodology
1. **Python (Pandas, python-pptx, Matplotlib):** Sanitized 124,000+ raw hourly records, normalized bilingual and variant SKU names, filtered non-core test items, and programmatically compiled executive slide decks.
2. **PostgreSQL:** Modeled relational data marts (`vw_order_profitability`, `vw_monthly_pl_summary`) integrating platform commission structures (24% Grab, 30% LINE MAN), weekly fluctuating fruit costs, daily waste logs, and fixed facility overheads.
3. **Power BI:** Built a 4-page interactive executive suite analyzing high-level financial variances, portfolio gross margins, promotion cannibalization, and kitchen-level spoilage trends.

---

##  Key Business Insights

### 1. The Flat Budget Trap & Weather Seasonality
Management instituted a static run-rate budget of 2.70M THB/month without seasonal adjustments. Only April 2026 exceeded the monthly target (+4.2% / 2.81M THB) during peak summer heat. During the monsoon months (Jun–Aug), monthly revenue dropped to an average of 1.55M THB (-42.4% vs budget), causing monthly operating losses of -230K to -268K THB against fixed kitchen overheads (670K THB/month).

### 2. The Mixed Berry Unit Margin Squeeze
Despite a premium retail price of 89 THB, Mixed Berry Premium generated a critically low **15.55% Gross Margin** due to imported fruit (40.4 THB) and specialized packaging (8 THB). Furthermore, Mixed Berry accounted for **38.7% of total company fruit waste (330.9K THB)**. Factoring in discarded inventory, the SKU operated at an overall net operating loss of -53,975 THB.

### 3. Promotion Cannibalization & Platform Margins
Orders placed under standard menu pricing (RC000) yielded healthy 41.2% gross margins. In contrast, aggressive discount campaigns such as RC102 (-20% Double Day) compressed margins down to 28.5% without generating enough volume elasticity to offset the margin loss. Meanwhile, Grab represented 53.7% of net volume at a 24% take rate, whereas LINE MAN represented 46.3% of volume at a 30% take rate.

### 4. 24/7 Operational Inefficiencies
Hourly order distributions revealed that the 02:00–06:00 AM operating window contributed only **4.8% of daily sales** (~1.5 cups/hour per kitchen). Operating continuously around the clock incurred disproportionate utility, air conditioning, and overnight labor costs within fixed facility overhead.

---

##  Strategic Recommendations

| Strategic Pillar | Actionable Initiative | Financial & Operational Impact |
| :--- | :--- | :--- |
| **Pillar 1: Pricing & Portfolio** | Increase Mixed Berry Premium price from 89 to 99 THB (+10 THB); transition from fresh imports to Individual Quick Freezing (IQF) fruit. | Expands unit gross margin from 15.5% toward ~24%, contributing +70K THB in net margin. |
| **Pillar 2: Inventory & JIT Procurement** | Shift from weekly batch ordering to a 7-day moving average daily JIT replenishment model; enforce strict daily preparation caps (15 cups/day/kitchen) for berries. | Cuts seasonal spoilage by up to 70%, yielding ~165K THB in direct waste cost savings over 3 months. |
| **Pillar 3: Operations & Channel Mix** | Curtail kitchen operating hours from 24/7 to 06:00–02:00 (closing 4 off-peak hours); retire margin-dilutive RC102 (-20%) discounts in favor of minimum-spend bundle incentives. | Reduces fixed facility overhead by ~70K THB/month (~210K THB savings over 3 months) while sacrificing less than 5% of low-margin volume. |

---

##  3-Month Financial Outlook (Sep – Nov 2026)

A baseline versus turnaround scenario model demonstrates the impact of operational restructuring over the upcoming off-peak quarter:

| Financial Metric | As-Is Baseline (Status Quo) | Turnaround Strategy Plan | Net Financial Impact |
| :--- | :---: | :---: | :--- |
| **Projected Demand Volume** | 130,000 cups (~43.3K/month) | 130,000 cups (~43.3K/month) | Stable volume (Sep: 41.5K, Oct: 42.5K, Nov: 46K) |
| **Net Revenue** | 4.85M THB | 4.92M THB | **+70K THB** (Mixed Berry repricing) |
| **Cost of Goods Sold (COGS)** | 3.15M THB | 3.15M THB | Controlled unit recipe standards |
| **Spoilage Waste Cost** | 240K THB (~80K/month) | 75K THB (~25K/month) | **+165K THB** (JIT daily ordering savings) |
| **Fixed Facility Overheads** | 2.01M THB (670K x 3) | 1.80M THB (600K x 3) | **+210K THB** (Reduced overnight hours) |
| **Net Operating Profit** | **-550K THB (Severe Loss)** | **+30K to +80K THB (Profitable)** | **+445K to +500K THB Total Value Created** |

### Recommended Procurement Allocation (130,000 Cups Target)
* **Watermelon (42% | 54,600 cups):** Procure with a 10% safety buffer; primary volume driver.
* **Pineapple (23% | 29,890 cups):** Stable margin contributor; procure on weekly rotation.
* **Guava (17% | 22,100 cups):** Local sourcing; 3-day replenishment cycle.
* **Passion Fruit (13% | 16,910 cups):** Monitor regional price volatility.
* **Mixed Berry Premium (5% | 6,500 cups):** Implement strict daily caps to prevent fruit spoilage.

---

##  Further Explorations
* **Dynamic Daypart Pricing:** Evaluate real-time platform markup algorithms during off-peak afternoon windows (14:00–16:00) rather than blanket platform-wide discounts.
* **Footprint Consolidation:** Assess lease renegotiation and kitchen downsizing for lower-volume branches (e.g., BKK_Ladprao, 3.34M THB net revenue) to reduce fixed overhead drag.
* **Supplier Forward Contracts:** Negotiate fixed seasonal contracts with fruit suppliers to hedge against price volatility for domestic staple fruits.
