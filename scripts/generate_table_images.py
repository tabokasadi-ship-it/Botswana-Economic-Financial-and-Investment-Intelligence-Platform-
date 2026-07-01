import os
import textwrap
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# OUTPUT FOLDER
# ======================================================

output_folder = "report_table_images"
os.makedirs(output_folder, exist_ok=True)

# ======================================================
# STYLE SETTINGS
# ======================================================

BACKGROUND = "#fff7fb"
HEADER = "#f3a9c9"
ROW_1 = "#ffffff"
ROW_2 = "#fdeaf3"
EDGE = "#d79ab7"
TEXT = "#2b2b2b"
FOOTER = "#555555"

# ======================================================
# HELPER FUNCTIONS
# ======================================================

def clean_col_name(col):
    return str(col).replace("_", " ")

def wrap_text(value, width=24):
    if isinstance(value, str):
        return "\n".join(textwrap.wrap(value, width))
    return value

def prepare_df(df, cols=None, max_rows=None):
    df = df.copy()

    if cols:
        existing_cols = [c for c in cols if c in df.columns]
        df = df[existing_cols]

    if max_rows:
        df = df.head(max_rows)

    df.columns = [clean_col_name(c) for c in df.columns]

    for col in df.columns:
        if pd.api.types.is_float_dtype(df[col]):
            df[col] = df[col].map(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
        else:
            df[col] = df[col].map(lambda x: wrap_text(x) if isinstance(x, str) else x)

    return df

def save_table_image(df, title, image_name):
    rows = len(df)
    cols = len(df.columns)

    fig_width = min(max(cols * 3.0, 12), 22)
    fig_height = max(rows * 0.85 + 4.5, 6)

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    fig.patch.set_facecolor(BACKGROUND)
    ax.set_facecolor(BACKGROUND)
    ax.axis("off")

    # Title placed safely above the table
    fig.suptitle(
        title,
        fontsize=24,
        fontweight="bold",
        color=TEXT,
        y=0.96
    )

    # Table moved lower to create clear title spacing
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center",
        bbox=[0.02, 0.15, 0.96, 0.70]
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(EDGE)
        cell.set_linewidth(0.8)

        if row == 0:
            cell.set_facecolor(HEADER)
            cell.set_text_props(weight="bold", color="#1f1f1f")
        else:
            cell.set_facecolor(ROW_1 if row % 2 == 0 else ROW_2)
            cell.set_text_props(color=TEXT)

    plt.figtext(
        0.5,
        0.04,
        "Botswana Economic, Financial & Investment Intelligence Platform | Economic Growth Intelligence",
        ha="center",
        fontsize=10,
        color=FOOTER
    )

    path = os.path.join(output_folder, image_name)
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()

    print(f"Saved: {path}")

def read_excel_if_exists(file_name):
    if os.path.exists(file_name):
        return pd.read_excel(file_name)
    else:
        print(f"Missing file skipped: {file_name}")
        return None

# ======================================================
# 1. GDP ANALYSIS
# ======================================================

df = read_excel_if_exists("GDP_Analysis.xlsx")
if df is not None:
    df = prepare_df(df, max_rows=11)
    save_table_image(df, "GDP Analysis", "01_GDP_Analysis.png")

# ======================================================
# 2. ECONOMIC HEALTH SCORE
# ======================================================

df = read_excel_if_exists("Final_Economic_Health_Score.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Component",
            "Actual_Evidence",
            "Score",
            "Weight",
            "Weighted_Contribution"
        ]
    )
    save_table_image(df, "Final Economic Health Score", "02_Economic_Health_Score.png")

# ======================================================
# 3. DIVERSIFICATION ANALYSIS
# ======================================================

df = read_excel_if_exists("Diversification_Sector_Shares.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=["Sector", "Sector_Share"],
        max_rows=10
    )
    save_table_image(df, "Diversification Analysis: Top 10 Sector Shares", "03_Diversification_Top10.png")

# ======================================================
# 4. TRANSFORMATION TRACKER
# ======================================================

df = read_excel_if_exists("Transformation_Tracker_With_Score.xlsx")
if df is not None:
    top_gain = df.sort_values("Change", ascending=False).head(5)
    top_decline = df.sort_values("Change", ascending=True).head(5)
    summary = pd.concat([top_gain, top_decline])

    summary = prepare_df(
        summary,
        cols=[
            "Sector",
            "Share_2015",
            "Share_2025",
            "Change",
            "Category"
        ]
    )

    save_table_image(summary, "Transformation Tracker: Top Gainers & Decliners", "04_Transformation_Summary.png")

# ======================================================
# 5. FUTURE GROWTH DRIVER RANKING
# ======================================================

df = read_excel_if_exists("Future_Growth_Driver_Ranking_2026_2028.xlsx")

if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Average_Forecast_Growth_2026_2028"
        ]
    )

    save_table_image(
        df,
        "Future Growth Driver Ranking (2026–2028)",
        "05_Future_Growth_Driver_Ranking.png"
    )

# ======================================================
# 6. SECTOR OPPORTUNITY MATRIX
# ======================================================

df = read_excel_if_exists("Sector_Opportunity_Matrix.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Size_2025",
            "Growth_Rate",
            "Opportunity_Category"
        ],
        max_rows=12
    )
    save_table_image(df, "Sector Opportunity Matrix", "06_Sector_Opportunity_Matrix.png")

# ======================================================
# 7. ECONOMIC OPPORTUNITY SCORE
# ======================================================

df = read_excel_if_exists("Economic_Opportunity_Score.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Opportunity_Category",
            "Economic_Opportunity_Score"
        ],
        max_rows=10
    )
    save_table_image(df, "Economic Opportunity Score: Top 10 Sectors", "07_Economic_Opportunity_Top10.png")

# ======================================================
# 8. VOLATILITY RISK ANALYSIS
# ======================================================

df = read_excel_if_exists("Sector_Volatility_Risk_Analysis.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Volatility_Score",
            "Risk_Category"
        ],
        max_rows=10
    )
    save_table_image(df, "Volatility Risk Analysis: Most Volatile Sectors", "08_Volatility_Risk_Top10.png")

# ======================================================
# 9. OPPORTUNITY & RISK ASSESSMENT
# ======================================================

df = read_excel_if_exists("Final_Opportunity_Risk_Assessment.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Economic_Opportunity_Score",
            "Volatility_Score",
            "Priority_Index",
            "Verdict"
        ],
        max_rows=10
    )
    save_table_image(df, "Opportunity & Risk Assessment: Top 10 Priority Sectors", "09_Opportunity_Risk_Top10.png")

# ======================================================
# 10. BOTSWANA ECONOMIC RESILIENCE INDEX
# ======================================================

resilience_df = pd.DataFrame({
    "Pillar": [
        "Diversification",
        "Transformation",
        "Opportunity Depth",
        "Growth Stability",
        "Risk Structure"
    ],
    "Score": [80, 60, 80, 60, 80],
    "Weight": [0.25, 0.20, 0.20, 0.20, 0.15],
    "Weighted Contribution": [20, 12, 16, 12, 12]
})

resilience_df = prepare_df(resilience_df)
save_table_image(resilience_df, "Botswana Economic Resilience Index", "10_Resilience_Index.png")

# ======================================================
# 11. GDP FORECAST CENTRE
# ======================================================

df = read_excel_if_exists("GDP_Real_Nominal_Forecast_2026_2028.xlsx")
if df is not None:
    df = prepare_df(df)
    save_table_image(df, "GDP Forecast Centre", "11_GDP_Forecast_Centre.png")

# ======================================================
# 12. STRATEGIC SECTOR FORECASTS
# ======================================================

df = read_excel_if_exists("Strategic_Sector_Forecasts_2026_2028.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Year",
            "Forecast_Value_Constant_Prices",
            "Forecast_Growth_Rate_%"
        ],
        max_rows=12
    )
    save_table_image(df, "Strategic Sector Forecasts", "12_Strategic_Sector_Forecasts.png")

# ======================================================
# 13. FUTURE GROWTH DRIVER RANKING
# ======================================================

df = read_excel_if_exists("Future_Growth_Driver_Ranking_2026_2028.xlsx")
if df is not None:
    df = prepare_df(df)
    save_table_image(df, "Future Growth Driver Ranking", "13_Future_Growth_Driver_Ranking.png")

# ======================================================
# 14. FORECAST CONFIDENCE ASSESSMENT
# ======================================================

df = read_excel_if_exists("Forecast_Confidence_Assessment.xlsx")
if df is not None:
    df = prepare_df(df)
    save_table_image(df, "Forecast Confidence Assessment", "14_Forecast_Confidence_Assessment.png")

# ======================================================
# 15. FULL 18-SECTOR FORECAST ENGINE
# ======================================================

df = read_excel_if_exists("Full_18_Sector_Forecast_With_Confidence.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Sector",
            "Value_2025",
            "Forecast_2028",
            "Growth_2025_2028_%",
            "Forecast_Confidence"
        ],
        max_rows=10
    )
    save_table_image(df, "Full 18-Sector Forecast Engine: Top 10", "15_Full_18_Sector_Forecast_Top10.png")

# ======================================================
# 16. ECONOMIC FUTURE SIMULATOR
# ======================================================

df = read_excel_if_exists("Economic_Future_Simulator_Results.xlsx")
if df is not None:
    df = prepare_df(
        df,
        cols=[
            "Scenario",
            "GDP_Impact",
            "GDP_Impact_%"
        ]
    )
    save_table_image(df, "Economic Future Simulator", "16_Economic_Future_Simulator.png")

print("\nClean report-ready table images generated successfully.")
