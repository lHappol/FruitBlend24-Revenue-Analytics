# FruitBlend24 — Financial Turnaround & Commercial Revenue Analytics

An end-to-end commercial performance diagnostics, unit economics modeling, and operational turnaround strategy for **FruitBlend24**, an omni-channel cloud-kitchen smoothie brand operating 4 central kitchens across Bangkok and Pattaya (Pattaya_Central, Pattaya_Beach, BKK_Sukhumvit, and BKK_Ladprao) exclusively via Grab and LINE MAN.

---

## Executive Summary
* **Annual Net Revenue:** 22.63M THB (fell short of management's 32.40M THB flat budget by **-30.2%** / -9.77M THB).
* **Operating Performance:** Closed the 12-month fiscal period with an operating loss of **-404.2K THB** (-1.8% net margin) on 14.12M THB COGS. The loss was driven by severe rainy-season demand contraction, fixed overhead burn (670K THB/month), and high fruit spoilage.
* **Turnaround Potential:** A coordinated strategy encompassing SKU repricing, Just-In-Time (JIT) daily inventory procurement, and operating hour rationalization creates **+445K to +500K THB** in projected commercial value over Q4, returning operations to net profitability.

---

## Repository Structure
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
