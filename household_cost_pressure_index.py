import pandas as pd

# =====================================================
# LOAD CPI DATA
# =====================================================

df = pd.read_excel("Botswana_CPI_Master.xlsx")

# =====================================================
# FUNCTION TO CALCULATE LATEST YOY INFLATION
# =====================================================

def latest_inflation(indicator_code):

    temp = df[df["Indicator"] == indicator_code].copy()

    temp["Date"] = pd.to_datetime(temp["Date"])

    temp = temp.sort_values("Date")

    temp["Inflation_Rate"] = (
        temp["Value"].pct_change(12) * 100
    )

    return temp["Inflation_Rate"].dropna().iloc[-1]

# =====================================================
# COMPONENTS
# =====================================================

headline_inflation = latest_inflation("PCPI_IX")

food_inflation = latest_inflation("PCPI_CP_01_IX")

housing_inflation = latest_inflation("PCPI_CP_04_IX")

transport_inflation = latest_inflation("PCPI_CP_07_IX")

# =====================================================
# NORMALISE TO 100 SCALE
# =====================================================

headline_score = min(max(headline_inflation * 5, 0), 100)

food_score = min(max(food_inflation * 5, 0), 100)

transport_score = min(max(transport_inflation * 3, 0), 100)

housing_score = min(max(housing_inflation * 5, 0), 100)

# =====================================================
# HOUSEHOLD COST PRESSURE INDEX
# =====================================================

hcpi = (
    headline_score * 0.40
    + food_score * 0.25
    + transport_score * 0.20
    + housing_score * 0.15
)

# =====================================================
# STATUS
# =====================================================

if hcpi >= 80:
    status = "Severe Pressure"

elif hcpi >= 60:
    status = "High Pressure"

elif hcpi >= 40:
    status = "Moderate Pressure"

else:
    status = "Low Pressure"

# =====================================================
# COMPONENT TABLE
# =====================================================

components = pd.DataFrame({
    "Component": [
        "Headline Inflation",
        "Food Inflation",
        "Transport Inflation",
        "Housing Inflation"
    ],
    "Inflation_%": [
        headline_inflation,
        food_inflation,
        transport_inflation,
        housing_inflation
    ],
    "Weight": [
        0.40,
        0.25,
        0.20,
        0.15
    ]
})

# =====================================================
# RESULTS
# =====================================================

print("\n")
print("=" * 70)
print("HOUSEHOLD COST PRESSURE INDEX")
print("=" * 70)

print(components)

print("\n")
print(f"Household Cost Pressure Index: {hcpi:.2f}/100")
print(f"Pressure Status: {status}")

# =====================================================
# SAVE OUTPUTS
# =====================================================

components.to_excel(
    "Household_Cost_Pressure_Components.xlsx",
    index=False
)

summary = pd.DataFrame({
    "Metric": [
        "Household Cost Pressure Index",
        "Pressure Status"
    ],
    "Value": [
        round(hcpi, 2),
        status
    ]
})

summary.to_excel(
    "Household_Cost_Pressure_Index.xlsx",
    index=False
)

print("\nHousehold Cost Pressure Index saved successfully.")