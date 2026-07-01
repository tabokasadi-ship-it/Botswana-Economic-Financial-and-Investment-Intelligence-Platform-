import pandas as pd

# ==========================================
# LOAD CPI DATA
# ==========================================

df = pd.read_excel("Botswana_CPI_Master.xlsx")

# ==========================================
# CPI CATEGORIES
# ==========================================

drivers = {
    "Food & Non-Alcoholic Beverages": "PCPI_CP_01_IX",
    "Housing, Water & Electricity": "PCPI_CP_04_IX",
    "Health": "PCPI_CP_06_IX",
    "Transport": "PCPI_CP_07_IX",
    "Communication": "PCPI_CP_08_IX"
}

results = []

for category, code in drivers.items():

    temp = df[df["Indicator"] == code].copy()

    if len(temp) > 12:

        temp["Date"] = pd.to_datetime(temp["Date"])

        temp = temp.sort_values("Date")

        temp["Inflation_Rate"] = (
            temp["Value"].pct_change(12) * 100
        )

        latest = temp["Inflation_Rate"].dropna().iloc[-1]

        results.append({
            "Category": category,
            "Latest_Inflation_%": latest
        })

# ==========================================
# DRIVER RANKING
# ==========================================

driver_df = pd.DataFrame(results)

driver_df = driver_df.sort_values(
    "Latest_Inflation_%",
    ascending=False
)

# ==========================================
# PRESSURE CLASSIFICATION
# ==========================================

def classify(x):

    if x >= 10:
        return "Very High"

    elif x >= 7:
        return "High"

    elif x >= 4:
        return "Moderate"

    else:
        return "Low"

driver_df["Pressure_Level"] = (
    driver_df["Latest_Inflation_%"]
    .apply(classify)
)

# ==========================================
# RESULTS
# ==========================================

print("\n")
print("="*70)
print("BOTSWANA INFLATION DRIVER ANALYSIS")
print("="*70)

print(driver_df)

# ==========================================
# SAVE
# ==========================================

driver_df.to_excel(
    "Inflation_Driver_Analysis.xlsx",
    index=False
)

print("\nInflation Driver Analysis saved successfully.")

print(df["Date"].max())