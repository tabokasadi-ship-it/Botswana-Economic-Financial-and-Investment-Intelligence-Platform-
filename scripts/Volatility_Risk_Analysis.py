import pandas as pd

# =====================================================
# LOAD CPI DATA
# =====================================================

df = pd.read_excel("Botswana_CPI_Master.xlsx")

# =====================================================
# CPI CATEGORIES
# =====================================================

categories = {
    "Food & Non-Alcoholic Beverages": "PCPI_CP_01_IX",
    "Housing, Water & Electricity": "PCPI_CP_04_IX",
    "Health": "PCPI_CP_06_IX",
    "Transport": "PCPI_CP_07_IX",
    "Communication": "PCPI_CP_08_IX"
}

results = []

# =====================================================
# CALCULATE VOLATILITY
# =====================================================

for category, code in categories.items():

    temp = df[df["Indicator"] == code].copy()

    temp["Date"] = pd.to_datetime(temp["Date"])

    temp = temp.sort_values("Date")

    temp["Inflation_Rate"] = (
        temp["Value"].pct_change(12) * 100
    )

    volatility = temp["Inflation_Rate"].std()

    avg_inflation = temp["Inflation_Rate"].mean()

    results.append({
        "Category": category,
        "Average_Inflation_%": avg_inflation,
        "Inflation_Volatility": volatility
    })

risk_df = pd.DataFrame(results)

# =====================================================
# RISK CLASSIFICATION
# =====================================================

def classify_risk(x):

    if x >= 10:
        return "High Risk"

    elif x >= 5:
        return "Moderate Risk"

    else:
        return "Low Risk"

risk_df["Risk_Level"] = (
    risk_df["Inflation_Volatility"]
    .apply(classify_risk)
)

risk_df = risk_df.sort_values(
    "Inflation_Volatility",
    ascending=False
)

# =====================================================
# RESULTS
# =====================================================

print("\n")
print("=" * 70)
print("BOTSWANA INFLATION RISK ANALYSIS")
print("=" * 70)

print(risk_df)

# =====================================================
# TOP RISK CATEGORY
# =====================================================

top_risk = risk_df.iloc[0]["Category"]

print("\n")
print(f"Highest Inflation Risk Category: {top_risk}")

# =====================================================
# SAVE
# =====================================================

risk_df.to_excel(
    "Inflation_Risk_Analysis.xlsx",
    index=False
)

summary = pd.DataFrame({
    "Metric": [
        "Highest Inflation Risk Category"
    ],
    "Value": [
        top_risk
    ]
})

summary.to_excel(
    "Inflation_Risk_Summary.xlsx",
    index=False
)

print("\nInflation Risk Analysis saved successfully.")