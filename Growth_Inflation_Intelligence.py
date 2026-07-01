import pandas as pd

# =====================================================
# GROWTH–INFLATION INTELLIGENCE
# Linkage 1: Economic Shocks → Inflation Transmission
# =====================================================

# Existing results from your completed modules
transport_inflation = 28.489633
transport_volatility = 13.239194
headline_inflation = 10.266569
household_pressure_index = 44.83

# =====================================================
# LINKAGE TABLE
# =====================================================

linkage_df = pd.DataFrame({
    "Economic_Growth_Intelligence_Evidence": [
        "Russia-Ukraine war and global inflation",
        "External price shocks",
        "Global supply chain disruption",
        "Economic shock vulnerability"
    ],
    "Transmission_Channel": [
        "Fuel prices and transport costs",
        "Import prices",
        "Logistics and mobility costs",
        "Household affordability pressure"
    ],
    "Cost_of_Living_Intelligence_Evidence": [
        f"Transport inflation = {transport_inflation:.2f}%",
        f"Headline inflation = {headline_inflation:.2f}%",
        f"Transport volatility = {transport_volatility:.2f}",
        f"Household Cost Pressure Index = {household_pressure_index:.2f}/100"
    ],
    "Intelligence_Insight": [
        "External shocks pass into household costs through transport",
        "Imported inflation affects domestic price levels",
        "Transport is the most unpredictable inflation category",
        "Households remain exposed to future global price shocks"
    ]
})

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

summary_df = pd.DataFrame({
    "Insight_Area": [
        "Main Growth-Inflation Linkage",
        "Main Transmission Channel",
        "Highest Inflation Driver",
        "Highest Inflation Risk",
        "Household Impact",
        "Strategic Interpretation"
    ],
    "Finding": [
        "Economic shocks transmit into inflation through transport and import costs",
        "Fuel prices and transport costs",
        "Transport inflation",
        "Transport volatility",
        "Moderate household cost pressure",
        "External shocks are ultimately felt by households through higher transport costs and reduced purchasing power"
    ],
    "Evidence": [
        "Russia-Ukraine war and global inflation pressures",
        "Transport inflation reached 28.49%",
        "Transport was the highest inflation driver",
        "Transport volatility was 13.24",
        "Household Cost Pressure Index was 44.83/100",
        "Cost pressures remain moderate but vulnerable to future global shocks"
    ]
})

# =====================================================
# PRINT RESULTS
# =====================================================

print("\n" + "=" * 80)
print("GROWTH–INFLATION INTELLIGENCE")
print("=" * 80)

print("\nLINKAGE 1: ECONOMIC SHOCKS → INFLATION TRANSMISSION")
print(linkage_df)

print("\n" + "=" * 80)
print("EXECUTIVE SUMMARY")
print("=" * 80)

print(summary_df)

# =====================================================
# SAVE OUTPUTS
# =====================================================

linkage_df.to_excel(
    "Growth_Inflation_Linkage_Analysis.xlsx",
    index=False
)

summary_df.to_excel(
    "Growth_Inflation_Intelligence_Summary.xlsx",
    index=False
)

print("\nGrowth–Inflation Intelligence files saved successfully.")