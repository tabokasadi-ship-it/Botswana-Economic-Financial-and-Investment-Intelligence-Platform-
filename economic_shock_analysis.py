# ======================================================
# BOTSWANA ECONOMIC SHOCK INTELLIGENCE ANALYSIS
# ======================================================

import pandas as pd

# ======================================================
# PART 1: LOAD GDP DATA
# ======================================================

gdp = pd.read_excel("GDP_Analysis.xlsx")

print("GDP Analysis data loaded successfully.")

# ======================================================
# PART 2: CREATE ECONOMIC SHOCK TIMELINE
# ======================================================

shock_timeline = pd.DataFrame({
    "Year": [
        2016,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
        2025
    ],
    "Economic_Shock": [
        "Global investment and trade uncertainty",
        "Slowing global growth",
        "COVID-19 pandemic",
        "Post-COVID economic rebound",
        "Russia-Ukraine war and global inflation",
        "Diamond demand slowdown",
        "Structural diamond market weakness",
        "Lab-grown diamond transition and weak exports"
    ],
    "Shock_Type": [
        "External uncertainty",
        "External demand shock",
        "Extreme external shock",
        "Recovery shock",
        "External price shock",
        "Commodity demand shock",
        "Structural commodity shock",
        "Long-term structural shock"
    ],
    "Transmission_Channel": [
        "Investor confidence and trade sentiment",
        "Weaker global demand and export pressure",
        "Mining, tourism, trade, mobility and fiscal revenue",
        "Reopening, demand recovery and base effects",
        "Fuel prices, food prices, import costs and inflation",
        "Diamond exports, sales and government revenue",
        "Diamond revenue, public investment and GDP growth",
        "Diamond value chain, fiscal revenue and long-term growth"
    ],
    "Impact_Level": [
        "Low",
        "Medium",
        "Extreme",
        "Positive",
        "High",
        "Medium",
        "High",
        "Very High"
    ]
})

# ======================================================
# PART 3: ATTACH GDP GROWTH RATE
# ======================================================

shock_timeline = shock_timeline.merge(
    gdp[["Year", "GDP_Growth_Rate"]],
    on="Year",
    how="left"
)

print("\n")
print("=" * 80)
print("ECONOMIC SHOCK TIMELINE")
print("=" * 80)

print(shock_timeline)

# ======================================================
# PART 4: SHOCK VULNERABILITY INDEX
# ======================================================

vulnerability = pd.DataFrame({
    "Risk_Driver": [
        "Diamond Dependence",
        "Export Dependence",
        "Fiscal Dependence",
        "Economic Concentration",
        "Service Sector Buffer"
    ],
    "Score": [
        85,
        75,
        80,
        70,
        45
    ],
    "Interpretation": [
        "High exposure to diamond market changes",
        "Export earnings remain sensitive to global demand",
        "Government revenue remains linked to diamond performance",
        "GDP has diversified but major sectors still dominate",
        "Services provide some buffer but are not yet large enough"
    ]
})

shock_vulnerability_index = vulnerability["Score"].mean()

if shock_vulnerability_index >= 80:
    vulnerability_status = "Highly Vulnerable"
elif shock_vulnerability_index >= 65:
    vulnerability_status = "Moderately Vulnerable"
elif shock_vulnerability_index >= 50:
    vulnerability_status = "Partially Vulnerable"
else:
    vulnerability_status = "Low Vulnerability"

print("\n")
print("=" * 80)
print("ECONOMIC SHOCK VULNERABILITY INDEX")
print("=" * 80)

print(vulnerability)
print()
print(f"Shock Vulnerability Index: {shock_vulnerability_index:.2f}/100")
print(f"Vulnerability Status: {vulnerability_status}")

# ======================================================
# PART 5: SHOCK TRANSMISSION SUMMARY
# ======================================================

transmission_summary = pd.DataFrame({
    "Transmission_Pathway": [
        "Diamond market shock",
        "Import price shock",
        "Global demand shock",
        "Public finance shock",
        "Labour market shock"
    ],
    "Economic_Channel": [
        "Diamond sales → export earnings → government revenue → public investment → GDP",
        "Fuel and food prices → inflation → household spending → business costs",
        "External demand → exports → mining and trade activity",
        "Lower revenues → lower fiscal space → slower public investment",
        "Sector slowdown → employment pressure → income and consumption effects"
    ],
    "Relevance_to_Botswana": [
        "Very High",
        "High",
        "High",
        "Very High",
        "Medium"
    ]
})

print("\n")
print("=" * 80)
print("SHOCK TRANSMISSION SUMMARY")
print("=" * 80)

print(transmission_summary)

# ======================================================
# PART 6: SAVE OUTPUTS
# ======================================================

shock_timeline.to_excel(
    "Economic_Shock_Timeline.xlsx",
    index=False
)

vulnerability.to_excel(
    "Economic_Shock_Vulnerability_Index.xlsx",
    index=False
)

transmission_summary.to_excel(
    "Economic_Shock_Transmission_Summary.xlsx",
    index=False
)

summary_df = pd.DataFrame({
    "Metric": [
        "Shock Vulnerability Index",
        "Vulnerability Status"
    ],
    "Value": [
        round(shock_vulnerability_index, 2),
        vulnerability_status
    ]
})

summary_df.to_excel(
    "Economic_Shock_Vulnerability_Summary.xlsx",
    index=False
)

print("\nEconomic Shock Intelligence outputs saved successfully.")