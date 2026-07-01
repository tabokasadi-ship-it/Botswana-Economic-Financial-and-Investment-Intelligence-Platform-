# ======================================================
# BOTSWANA ECONOMIC INTELLIGENCE PLATFORM
# ECONOMIC FUTURE SIMULATOR
# ======================================================

import pandas as pd

# ======================================================
# PART 1: LOAD FULL 18-SECTOR FORECAST
# ======================================================

forecast_file = "Full_18_Sector_Forecast_With_Confidence.xlsx"

forecast_df = pd.read_excel(forecast_file)

print("Full sector forecast loaded successfully.")

# ======================================================
# PART 2: BASELINE 2028 GDP
# ======================================================

baseline_2028_gdp = forecast_df["Forecast_2028"].sum()

print("\nBaseline 2028 Forecast GDP:")
print(f"P{baseline_2028_gdp:,.2f} million")

# ======================================================
# PART 3: SCENARIO FUNCTION
# ======================================================

def run_scenario(sector_name, shock_percent):

    scenario_df = forecast_df.copy()

    sector_mask = scenario_df["Sector"] == sector_name

    original_value = scenario_df.loc[
        sector_mask,
        "Forecast_2028"
    ].iloc[0]

    adjusted_value = original_value * (1 + shock_percent / 100)

    scenario_df.loc[
        sector_mask,
        "Forecast_2028"
    ] = adjusted_value

    scenario_gdp = scenario_df["Forecast_2028"].sum()

    gdp_impact = scenario_gdp - baseline_2028_gdp

    gdp_impact_percent = (
        gdp_impact / baseline_2028_gdp
    ) * 100

    return {
        "Scenario": f"{sector_name} {shock_percent:+.0f}%",
        "Sector": sector_name,
        "Shock_%": shock_percent,
        "Original_2028_Value": original_value,
        "Adjusted_2028_Value": adjusted_value,
        "Baseline_2028_GDP": baseline_2028_gdp,
        "Scenario_2028_GDP": scenario_gdp,
        "GDP_Impact": gdp_impact,
        "GDP_Impact_%": gdp_impact_percent
    }

# ======================================================
# PART 4: DEFINE SCENARIOS
# ======================================================

scenarios = [
    run_scenario("Mining & Quarrying", -10),
    run_scenario("Mining & Quarrying", 10),
    run_scenario("Finance, Insurance & Pension Funding", 10),
    run_scenario("Information & Communication Technology", 20),
    run_scenario("Wholesale & Retail", 10),
]

scenario_df = pd.DataFrame(scenarios)

# ======================================================
# PART 5: DISPLAY RESULTS
# ======================================================

print("\n")
print("=" * 80)
print("ECONOMIC FUTURE SIMULATOR RESULTS")
print("=" * 80)

print(scenario_df)

# ======================================================
# PART 6: SAVE RESULTS
# ======================================================

scenario_df.to_excel(
    "Economic_Future_Simulator_Results.xlsx",
    index=False
)

print("\nEconomic Future Simulator results saved successfully.")