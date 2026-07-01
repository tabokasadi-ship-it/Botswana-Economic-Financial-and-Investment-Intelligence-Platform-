import pandas as pd

# =====================================================
# COST OF LIVING INTELLIGENCE INSIGHTS
# =====================================================

# Key results from completed analysis
latest_inflation = 10.27
average_inflation = 5.22
peak_inflation = 14.60

transport_inflation = 28.49
food_inflation = 5.76
housing_inflation = -1.74

household_pressure_index = 44.83
household_pressure_status = "Moderate Pressure"

transport_volatility = 13.24
highest_risk_category = "Transport"

forecast_2026 = 5.25
forecast_2027 = 5.35
forecast_2028 = 5.45
inflation_outlook = "Moderate Inflation Environment"

economic_wellbeing_score = 64.15
economic_wellbeing_status = "Stable but Vulnerable"

national_alert_level = "Level 3 - Moderate Economic Risk"

# =====================================================
# EXECUTIVE INSIGHT TABLE
# =====================================================

insights = pd.DataFrame({
    "Insight_Area": [
        "Inflation Performance",
        "Main Inflation Driver",
        "Household Cost Pressure",
        "Inflation Risk",
        "Growth-Inflation Linkage",
        "Inflation Forecast",
        "Economic Wellbeing",
        "Early Warning Signal"
    ],
    "Key_Finding": [
        f"Latest inflation is {latest_inflation:.2f}%, above the average inflation rate of {average_inflation:.2f}%.",
        f"Transport inflation is the highest inflation driver at {transport_inflation:.2f}%.",
        f"The Household Cost Pressure Index is {household_pressure_index:.2f}/100, indicating {household_pressure_status}.",
        f"Transport is the highest inflation risk category, with volatility of {transport_volatility:.2f}.",
        "External shocks transmit into household costs mainly through fuel, transport and import prices.",
        f"Inflation is forecast to remain moderate between 2026 and 2028, averaging around {forecast_2026:.2f}% to {forecast_2028:.2f}%.",
        f"The Economic Wellbeing Score is {economic_wellbeing_score:.2f}/100, classified as {economic_wellbeing_status}.",
        f"The National Economic Alert Level is {national_alert_level}."
    ],
    "Executive_Interpretation": [
        "Botswana is facing elevated price pressure, although inflation is below the recent peak.",
        "Transport costs are currently the strongest source of household cost pressure.",
        "Households are under pressure, but the situation has not yet reached high or severe pressure levels.",
        "Transport prices are the most unpredictable category and require close monitoring.",
        "Cost of living pressures are not isolated; they are connected to global economic shocks and domestic economic performance.",
        "The medium-term inflation outlook appears stable, but risks remain if transport or food costs rise again.",
        "Botswana is stable, but household affordability and weak growth create vulnerability.",
        "The economy is not in crisis, but key risks require active monitoring."
    ]
})

# =====================================================
# EXECUTIVE RECOMMENDATIONS
# =====================================================

recommendations = pd.DataFrame({
    "Priority_Area": [
        "Transport Cost Stabilisation",
        "Food Affordability Monitoring",
        "Household Pressure Tracking",
        "Economic Diversification",
        "Shock Preparedness",
        "Policy and Business Planning"
    ],
    "Recommendation": [
        "Prioritise monitoring of fuel and transport costs because transport is both the highest inflation driver and the most volatile inflation category.",
        "Continue monitoring food inflation because food remains an essential household expense and can quickly push households into higher pressure levels.",
        "Use the Household Cost Pressure Index as a regular dashboard KPI to track whether households are moving from moderate pressure to high pressure.",
        "Support growth in finance, ICT and professional services to improve household income resilience and reduce dependence on vulnerable traditional sectors.",
        "Strengthen early warning systems for external shocks, especially fuel price shocks, import price shocks and global supply chain disruptions.",
        "Use inflation forecasts and cost pressure simulations to guide business pricing, budgeting, wage planning and policy decisions."
    ],
    "Expected_Value": [
        "Reduces future household affordability shocks.",
        "Protects household welfare and purchasing power.",
        "Improves decision-making for government, banks, retailers and households.",
        "Connects economic growth opportunities to household wellbeing.",
        "Improves national preparedness against imported inflation.",
        "Turns CPI data into practical decision intelligence."
    ]
})

# =====================================================
# EXECUTIVE BRIEFING PARAGRAPH
# =====================================================

briefing_text = f"""
Botswana's cost of living environment shows moderate but important household pressure.
Latest inflation stands at {latest_inflation:.2f}%, above the average inflation rate of
{average_inflation:.2f}%, indicating that households continue to face elevated price conditions.

The strongest pressure point is transport, with inflation of {transport_inflation:.2f}% and
volatility of {transport_volatility:.2f}. This makes transport both the largest current inflation
driver and the highest inflation risk category. Food inflation remains moderate at {food_inflation:.2f}%,
while housing inflation is currently negative at {housing_inflation:.2f}%, helping to reduce the
overall pressure on households.

The Household Cost Pressure Index is {household_pressure_index:.2f}/100, classified as
{household_pressure_status}. This means households are not yet under severe pressure, but they remain
vulnerable to combined shocks in food, transport and housing costs.

The Growth-Inflation Intelligence analysis shows that cost of living pressures are linked to broader
economic shocks. External shocks such as global inflation, fuel price movements and supply chain
disruptions transmit into Botswana through transport and import prices. This connects Economic Growth
Intelligence directly to household affordability.

The medium-term inflation forecast suggests a {inflation_outlook}, with inflation projected at
{forecast_2026:.2f}% in 2026, {forecast_2027:.2f}% in 2027 and {forecast_2028:.2f}% in 2028.
However, transport cost volatility remains the main risk to the outlook.

Overall, Botswana's Economic Wellbeing Score is {economic_wellbeing_score:.2f}/100, classified as
{economic_wellbeing_status}, while the National Economic Alert Level is {national_alert_level}.
This suggests that Botswana is not in crisis, but it remains exposed to weak growth, diamond dependence,
transport inflation and household affordability pressures.
"""

briefing_df = pd.DataFrame({
    "Executive_Briefing": [briefing_text]
})

# =====================================================
# PRINT RESULTS
# =====================================================

print("\n" + "=" * 80)
print("COST OF LIVING INTELLIGENCE INSIGHTS")
print("=" * 80)
print(insights)

print("\n" + "=" * 80)
print("EXECUTIVE RECOMMENDATIONS")
print("=" * 80)
print(recommendations)

print("\n" + "=" * 80)
print("EXECUTIVE BRIEFING")
print("=" * 80)
print(briefing_text)

# =====================================================
# SAVE OUTPUTS
# =====================================================

insights.to_excel(
    "Cost_of_Living_Executive_Insights.xlsx",
    index=False
)

recommendations.to_excel(
    "Cost_of_Living_Executive_Recommendations.xlsx",
    index=False
)

briefing_df.to_excel(
    "Cost_of_Living_Executive_Briefing.xlsx",
    index=False
)

print("\nCost of Living Executive Insights saved successfully.")