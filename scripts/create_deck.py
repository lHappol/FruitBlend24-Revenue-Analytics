import numpy as np
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

# 1. วาดกราฟประกอบสไลด์
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# กราฟสไลด์ 2: Monthly Financials
months = ['2025-09', '2025-10', '2025-11', '2025-12', '2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08']
rev = [1.34, 1.37, 1.57, 1.69, 1.71, 1.62, 2.51, 2.81, 2.44, 1.61, 1.53, 1.56]
op = [-0.19, -0.17, -0.08, -0.04, -0.03, -0.07, 0.12, 0.29, 0.16, -0.23, -0.26, -0.27]

fig, ax1 = plt.subplots(figsize=(8, 4.5), dpi=200)
x = np.arange(len(months))
ax1.bar(x, rev, width=0.55, color='#2563EB', alpha=0.9, label='Net Revenue (M THB)')
ax1.set_ylabel('Net Revenue (M THB)', color='#1E3A8A', fontweight='bold')
ax1.set_ylim(0, 3.5)
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=35, ha='right', fontsize=9)
ax1.axhline(2.7, color='#DC2626', linestyle='--', linewidth=1.5, label='Budget Target (2.7M)')
ax2 = ax1.twinx()
ax2.plot(x, op, color='#059669', linewidth=2.5, marker='o', label='Operating Profit (M THB)')
ax2.axhline(0, color='#64748B', linestyle='-', linewidth=1)
ax2.set_ylabel('Operating Profit (M THB)', color='#059669', fontweight='bold')
ax2.set_ylim(-0.4, 0.4)
ax2.grid(False)
plt.title('Monthly Financial Trend: Net Revenue vs Operating Profit', fontsize=12, fontweight='bold', pad=12)
fig.tight_layout()
plt.savefig('chart_slide2.png')
plt.close()

# กราฟสไลด์ 3: SKU Margins
skus = ['Watermelon', 'Pineapple', 'Guava', 'Passion Fruit', 'Mixed Berry (Prem)']
margins = [41.67, 41.78, 40.42, 30.09, 15.55]
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
colors = ['#10B981', '#10B981', '#10B981', '#F59E0B', '#EF4444']
bars = ax.barh(skus, margins, color=colors, height=0.6)
ax.set_xlabel('Gross Margin (%)', fontweight='bold', fontsize=11)
ax.set_xlim(0, 50)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 1, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", va='center', fontweight='bold', fontsize=10)
ax.set_title('SKU Gross Margin Breakdown (Mixed Berry Deficit)', fontweight='bold', fontsize=12, pad=12)
ax.invert_yaxis()
fig.tight_layout()
plt.savefig('chart_slide3.png')
plt.close()

# กราฟสไลด์ 4: Promo & Platform
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 4.2), dpi=200, gridspec_kw={'width_ratios': [1.3, 1]})
rates = ['RC000 (Standard)', 'RC101-WM', 'RC101-PA', 'RC101-GV', 'RC103 (Seasonal)', 'RC102 (DoubleDay)']
rate_gm = [41.2, 36.8, 35.5, 34.6, 31.8, 28.5]
ax1.barh(rates, rate_gm, color=['#10B981', '#3B82F6', '#3B82F6', '#3B82F6', '#F59E0B', '#EF4444'], height=0.6)
ax1.set_xlabel('Gross Margin (%)', fontweight='bold', fontsize=10)
ax1.set_xlim(0, 48)
for i, v in enumerate(rate_gm):
    ax1.text(v + 0.8, i, f"{v:.1f}%", va='center', fontsize=9)
ax1.set_title('Margin by Promo Code', fontweight='bold', fontsize=11)
ax1.invert_yaxis()
wedges, texts, autotexts = ax2.pie([53.7, 46.3], labels=['Grab (53.7%)', 'LINE MAN (46.3%)'], autopct='%1.1f%%',
                                    colors=['#0284C7', '#1E3A8A'], startangle=90, textprops={'fontsize': 9},
                                    wedgeprops=dict(width=0.45, edgecolor='w'))
for at in autotexts:
    at.set_color('white')
    at.set_fontweight('bold')
ax2.set_title('Platform Revenue Share', fontweight='bold', fontsize=11)
fig.tight_layout()
plt.savefig('chart_slide4.png')
plt.close()

# กราฟสไลด์ 5: Waste Trend
waste_vals = [34.7, 35.6, 40.5, 43.1, 44.5, 42.6, 132.7, 132.6, 111.1, 83.8, 76.3, 78.5]
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
ax.plot(months, waste_vals, color='#DC2626', linewidth=2.5, marker='s', label='Waste Cost (K THB)')
ax.fill_between(range(len(months)), waste_vals, color='#FCA5A5', alpha=0.3)
ax.set_ylabel('Waste Cost (Thousand THB)', fontweight='bold', color='#DC2626')
ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, rotation=35, ha='right', fontsize=9)
ax.set_title('Monthly Spoilage Waste Cost Trend (Surge in Mar-Aug)', fontweight='bold', fontsize=12, pad=12)
ax.axvspan(6, 11, color='#FEF3C7', alpha=0.5, label='High Waste Window')
ax.legend(loc='upper left', fontsize=9)
fig.tight_layout()
plt.savefig('chart_slide5.png')
plt.close()

# 2. สร้างสไลด์ PowerPoint
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

C_DARK_NAVY = RGBColor(15, 23, 42)
C_BLUE = RGBColor(37, 99, 235)
C_WHITE = RGBColor(255, 255, 255)
C_LIGHT_BG = RGBColor(248, 250, 252)
C_TEXT_DARK = RGBColor(30, 41, 59)
C_BORDER = RGBColor(226, 232, 240)

def set_bg(s, color):
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()

def add_header(s, title, cat="FRUITBLEND24 ANALYTICS"):
    box = s.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.3))
    p = box.text_frame.paragraphs[0]
    p.text = cat.upper()
    p.font.size, p.font.bold, p.font.color.rgb = Pt(10), True, C_BLUE
    box_t = s.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.5), Inches(0.7))
    pt = box_t.text_frame.paragraphs[0]
    pt.text = title
    pt.font.size, pt.font.bold, pt.font.color.rgb = Pt(22), True, C_TEXT_DARK

def add_card(s, left, top, w, h, title, points):
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
    card.fill.solid()
    card.fill.fore_color.rgb = C_WHITE
    card.line.color.rgb, card.line.width = C_BORDER, Pt(1)
    tf = card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size, p.font.bold, p.font.color.rgb = Pt(12), True, C_BLUE
    for pt in points:
        p2 = tf.add_paragraph()
        p2.text = "• " + pt
        p2.font.size, p2.font.color.rgb = Pt(10.5), C_TEXT_DARK
        p2.space_before = Pt(4)

# SLIDE 1: Cover
s1 = prs.slides.add_slide(blank)
set_bg(s1, C_DARK_NAVY)
tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(2.2))
tf = tbox.text_frame
tf.paragraphs[0].text = "FRUITBLEND24"
tf.paragraphs[0].font.size, tf.paragraphs[0].font.bold, tf.paragraphs[0].font.color.rgb = Pt(14), True, C_BLUE
p2 = tf.add_paragraph()
p2.text = "Financial Turnaround & Revenue Optimization"
p2.font.size, p2.font.bold, p2.font.color.rgb = Pt(32), True, C_WHITE
p3 = tf.add_paragraph()
p3.text = "12-Month Performance Review, Unit Economics & 3-Month Strategic Outlook"
p3.font.size, p3.font.color.rgb = Pt(15), RGBColor(148, 163, 184)

kpis = [
    ("NET REVENUE (12M)", "22.63M THB", "Missed Budget by -30.2% (-9.77M)", C_BLUE),
    ("TOTAL COGS", "14.12M THB", "Fruit 56% | Pack 26% | Labor 18%", RGBColor(245, 158, 11)),
    ("OPERATING PROFIT", "-404.2K THB", "Net Annual Loss (-1.8% Net Margin)", RGBColor(239, 68, 68))
]
for i, (t, v, sub, col) in enumerate(kpis):
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + i*3.85), Inches(3.8), Inches(3.6), Inches(2.2))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card.line.color.rgb, card.line.width = col, Pt(1.5)
    tf_c = card.text_frame
    tf_c.word_wrap = True
    tf_c.paragraphs[0].text = t
    tf_c.paragraphs[0].font.size, tf_c.paragraphs[0].font.bold, tf_c.paragraphs[0].font.color.rgb = Pt(11), True, RGBColor(148, 163, 184)
    pv = tf_c.add_paragraph()
    pv.text = v
    pv.font.size, pv.font.bold, pv.font.color.rgb = Pt(28), True, C_WHITE
    ps = tf_c.add_paragraph()
    ps.text = sub
    ps.font.size, ps.font.color.rgb = Pt(11), col

# SLIDE 2: P&L
s2 = prs.slides.add_slide(blank)
set_bg(s2, C_LIGHT_BG)
add_header(s2, "Financial Reality vs. Flat Budget Variance", "01. P&L & BUDGET PERFORMANCE")
s2.shapes.add_picture('chart_slide2.png', Inches(0.8), Inches(1.5), width=Inches(6.2))
add_card(s2, Inches(7.3), Inches(1.5), Inches(5.2), Inches(1.75), "1. The Flat Budget Trap", ["Management set a flat 2.70M THB/month budget (32.4M/yr).", "Actual Net Revenue was 22.63M THB (-30.2% variance).", "Ignored seasonality, leading to severe inventory oversupply."])
add_card(s2, Inches(7.3), Inches(3.35), Inches(5.2), Inches(1.75), "2. Severe Rainy Season Slump", ["Only April 2026 beat target (+4.2%) during summer peaks.", "Monsoon months (Jun–Aug) collapsed to 1.55M THB/month.", "Monthly losses accelerated to -230K ~ -268K THB."])
add_card(s2, Inches(7.3), Inches(5.2), Inches(5.2), Inches(1.75), "3. Fixed Overhead Burn", ["Fixed overhead is 670,000 THB/month across 4 kitchens.", "Off-peak gross profits failed to cover this fixed baseline.", "Operating profit closed at -404.2K THB loss."])

# SLIDE 3: Portfolio
s3 = prs.slides.add_slide(blank)
set_bg(s3, C_LIGHT_BG)
add_header(s3, "Menu Portfolio Diagnostics: The Mixed Berry Deficit", "02. PORTFOLIO & PRICING")
s3.shapes.add_picture('chart_slide3.png', Inches(0.8), Inches(1.5), width=Inches(6.2))
add_card(s3, Inches(7.3), Inches(1.5), Inches(5.2), Inches(1.75), "1. Core Foundation: Cash Cows", ["Watermelon & Pineapple represent ~65% of sales volume.", "Healthy Gross Margins above 41.7%.", "Core domestic staples with resilient profitability."])
add_card(s3, Inches(7.3), Inches(3.35), Inches(5.2), Inches(1.75), "2. Mixed Berry Margin Squeeze", ["Priced high at 89 THB, but Gross Margin is only 15.55%.", "High COGS of 55.4 THB (Fruit 40.4B + Pack 8B + Labor 7B).", "Generates only 9.87 THB profit per cup vs 18 THB for staples."])
add_card(s3, Inches(7.3), Inches(5.2), Inches(5.2), Inches(1.75), "3. Spoilage Erosion", ["Mixed Berry caused 330,935 THB in waste (38.7% of all waste).", "Net margin after waste was negative (-53,975 THB).", "Action: Reprice to 99 THB (+10 THB) and enforce daily caps."])

# SLIDE 4: Promo
s4 = prs.slides.add_slide(blank)
set_bg(s4, C_LIGHT_BG)
add_header(s4, "Channel Dynamics & Promotional Cannibalization", "03. CHANNELS & PROMOTIONS")
s4.shapes.add_picture('chart_slide4.png', Inches(0.8), Inches(1.5), width=Inches(6.2))
add_card(s4, Inches(7.3), Inches(1.5), Inches(5.2), Inches(1.75), "1. Promotion Margin Erosion", ["Standard orders (RC000) deliver 41.2% Gross Margin.", "RC102 (Double Day -20%) drops margin to 28.5%.", "RC101 Bundle Deals (-15%) lower margin to 34.6%–36.8%."])
add_card(s4, Inches(7.3), Inches(3.35), Inches(5.2), Inches(1.75), "2. Platform Commission Impact", ["Grab: 53.7% revenue share at 24% platform commission.", "LINE MAN: 46.3% share but charges higher 30% commission.", "6% commission difference extracted ~670,000 THB in margin."])
add_card(s4, Inches(7.3), Inches(5.2), Inches(5.2), Inches(1.75), "3. Strategic Shift", ["Eliminate deep-discount RC102 during low season.", "Replace with minimum-spend vouchers & cross-sell deals.", "Negotiate volume incentive tiers with LINE MAN."])

# SLIDE 5: Operations
s5 = prs.slides.add_slide(blank)
set_bg(s5, C_LIGHT_BG)
add_header(s5, "Operational Inefficiencies & Seasonal Spoilage Surge", "04. OPERATIONS & INVENTORY")
s5.shapes.add_picture('chart_slide5.png', Inches(0.8), Inches(1.5), width=Inches(6.2))
add_card(s5, Inches(7.3), Inches(1.5), Inches(5.2), Inches(1.75), "1. Seasonal Spoilage Surge", ["Waste climbed from ~40K/month in winter to 132K in summer.", "Total waste cost reached 855,848 THB for the year.", "Root cause: Weekly procurement failed to track slowing sales."])
add_card(s5, Inches(7.3), Inches(3.35), Inches(5.2), Inches(1.75), "2. Kitchen Disparity", ["Pattaya_Central generated 7.41M THB (tourist demand).", "BKK_Ladprao lagged at 3.34M THB despite 140K/month overhead.", "Requires localized inventory quotas and staffing."])
add_card(s5, Inches(7.3), Inches(5.2), Inches(5.2), Inches(1.75), "3. 24/7 Idle Hours Discovery", ["02:00–06:00 AM generates only 4.8% of daily sales (~1.5 cups/hr).", "24/7 incurs continuous night wages, AC, and refrigeration.", "Action: Adjust hours to 06:00–02:00, saving ~70K THB/month."])

# SLIDE 6: 3-Month Projections
s6 = prs.slides.add_slide(blank)
set_bg(s6, C_LIGHT_BG)
add_header(s6, "3-Month Outlook (Sep – Nov 2026): As-Is vs Turnaround", "05. STRATEGIC PROJECTIONS")
tbl_shape = s6.shapes.add_table(7, 4, Inches(0.8), Inches(1.5), Inches(11.73), Inches(3.8))
tbl = tbl_shape.table
tbl.columns[0].width, tbl.columns[1].width, tbl.columns[2].width, tbl.columns[3].width = Inches(2.8), Inches(2.8), Inches(2.8), Inches(3.33)
headers = ["Financial Metric", "As-Is Baseline", "Turnaround Plan", "Strategic Impact & Driver"]
for j, h in enumerate(headers):
    c = tbl.cell(0, j)
    c.fill.solid()
    c.fill.fore_color.rgb = C_DARK_NAVY
    p = c.text_frame.paragraphs[0]
    p.text, p.font.size, p.font.bold, p.font.color.rgb = h, Pt(11), True, C_WHITE

data = [
    ("Projected Volume", "130,000 cups (~43.3K/mo)", "130,000 cups (~43.3K/mo)", "Stable demand (Sep: 41.5K, Oct: 42.5K, Nov: 46K)"),
    ("Net Revenue", "4.85M THB", "4.92M THB", "+70K THB from Mixed Berry repricing (89 -> 99 THB)"),
    ("Total COGS", "3.15M THB", "3.15M THB", "Standardized recipe & packaging consistency"),
    ("Spoilage Waste Cost", "240K THB (~80K/month)", "75K THB (~25K/month)", "+165K THB savings via JIT 7-day moving avg orders"),
    ("Fixed Kitchen Overheads", "2.01M THB (670K x 3)", "1.80M THB (600K x 3)", "+210K THB savings by reducing 24/7 to 06:00-02:00"),
    ("Net Operating Profit", "-550K THB (Severe Loss)", "+30K ~ +80K THB (Profitable)", "+445K ~ +500K THB TOTAL VALUE CREATED")
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        c = tbl.cell(i+1, j)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor(241, 245, 249) if i % 2 == 1 else C_WHITE
        p = c.text_frame.paragraphs[0]
        p.text, p.font.size, p.font.color.rgb = val, Pt(10), C_TEXT_DARK
        if j == 2 and i == 5:
            p.font.bold, p.font.color.rgb = True, RGBColor(16, 185, 129)
        elif j == 1 and i == 5:
            p.font.bold, p.font.color.rgb = True, RGBColor(239, 68, 68)

pcard = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.5), Inches(11.73), Inches(1.4))
pcard.fill.solid()
pcard.fill.fore_color.rgb = RGBColor(238, 242, 255)
pcard.line.color.rgb = C_BLUE
pcard.text_frame.word_wrap = True
p = pcard.text_frame.paragraphs[0]
p.text, p.font.size, p.font.bold, p.font.color.rgb = "Procurement Allocation by SKU (130,000 Cups Target):", Pt(11), True, C_BLUE
p_sub = pcard.text_frame.add_paragraph()
p_sub.text = "• Watermelon (42% | 54.6K cups) & Pineapple (23% | 29.9K cups): Procure with 10% safety buffer.\n• Guava (17% | 22.1K cups) & Passion Fruit (13% | 16.9K cups): Order on 3-day replenishment cycle.\n• Mixed Berry Premium (5% | 6.5K cups): Enforce strict daily caps to prevent fruit spoilage."
p_sub.font.size, p_sub.font.color.rgb = Pt(10), C_TEXT_DARK

# SLIDE 7: Roadmap
s7 = prs.slides.add_slide(blank)
set_bg(s7, C_LIGHT_BG)
add_header(s7, "Strategic Recommendations & Implementation Roadmap", "06. EXECUTIVE ROADMAP")
rec_pillars = [
    ("PILLAR 1: PRICING & PORTFOLIO", [
        "Reprice Mixed Berry Premium: Increase retail price from 89 THB to 99 THB (+10 THB/cup), expanding unit margin from 15.5% to ~24%.",
        "Source Frozen Berries (IQF): Shift from fresh imported to IQF frozen fruit to cut raw fruit cost from 40.4 THB to ~28 THB/cup.",
        "Promote Cash Cows: Position Watermelon & Pineapple as high-volume bundle anchors."
    ], C_BLUE),
    ("PILLAR 2: INVENTORY & JIT MODEL", [
        "7-Day Moving Average Ordering: Transition kitchens from weekly bulk guessing to dynamic daily orders matching weather forecasts.",
        "Daily Preparation Caps on Berries: Restrict daily prep to 15 cups/kitchen. Cut berry spoilage by >70% (saving ~50K THB/month).",
        "Centralized Fruit Distribution: Negotiate volume discounts across all 4 kitchens."
    ], RGBColor(16, 185, 129)),
    ("PILLAR 3: OPERATIONS & PROMOTIONS", [
        "Optimize Opening Hours (06:00–02:00): Close during 02:00–06:00 AM (only 4.8% sales), slashing ~70K THB/month in late-night overhead.",
        "Retire RC102 (-20% Discount): Eliminate margin-destroying discounts; replace with combo meals and threshold-based perks.",
        "Ladprao Kitchen Rationalization: Re-evaluate BKK_Ladprao lease/staffing to lower fixed cost burden."
    ], RGBColor(245, 158, 11))
]
for i, (t, pts, col) in enumerate(rec_pillars):
    card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*3.98), Inches(1.5), Inches(3.77), Inches(5.4))
    card.fill.solid()
    card.fill.fore_color.rgb = C_WHITE
    card.line.color.rgb, card.line.width = col, Pt(1.5)
    tf_c = card.text_frame
    tf_c.word_wrap = True
    tf_c.paragraphs[0].text = t
    tf_c.paragraphs[0].font.size, tf_c.paragraphs[0].font.bold, tf_c.paragraphs[0].font.color.rgb = Pt(12), True, col
    for pt in pts:
        p2 = tf_c.add_paragraph()
        p2.text = "• " + pt
        p2.font.size, p2.font.color.rgb = Pt(10), C_TEXT_DARK
        p2.space_before = Pt(8)

prs.save("FruitBlend24_Executive_Presentation.pptx")
print("Saved to FruitBlend24_Executive_Presentation.pptx successfully!")