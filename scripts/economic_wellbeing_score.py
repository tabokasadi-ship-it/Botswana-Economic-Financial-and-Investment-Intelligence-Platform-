import pandas as pd

# =====================================================
# INPUTS FROM PREVIOUS INTELLIGENCE MODULES
# =====================================================

economic_health_score = 60.8
economic_resilience_index = 72.0
household_cost_pressure_index = 44.83

# =====================================================
# ECONOMIC WELLBEING SCORE
# =====================================================

wellbeing_score = (
    economic_health_score * 0.40
    + economic_resilience_index * 0.40
    + (100 - household_cost_pressure_index) * 0.20
)

# =====================================================
# STATUS
# =====================================================

if wellbeing_score >= 80:
    status = "Strong Wellbeing"

elif wellbeing_score >= 60:
    status = "Stable but Vulnerable"

elif wellbeing_score >= 40:
    status = "Moderate Wellbeing"

else:
    status = "Weak Wellbeing"

# =====================================================
# RESULTS
# =====================================================

print("\n" + "="*80)
print("BOTSWANA ECONOMIC WELLBEING SCORE")
print("="*80)

print(f"Economic Health Score: {economic_health_score}")
print(f"Economic Resilience Index: {economic_resilience_index}")
print(f"Household Cost Pressure Index: {household_cost_pressure_index}")

print("\n")
print(f"Economic Wellbeing Score: {wellbeing_score:.2f}/100")
print(f"Status: {status}")

# =====================================================
# SAVE
# =====================================================

summary = pd.DataFrame({
    "Metric":[
        "Economic Health Score",
        "Economic Resilience Index",
        "Household Cost Pressure Index",
        "Economic Wellbeing Score",
        "Status"
    ],
    "Value":[
        economic_health_score,
        economic_resilience_index,
        household_cost_pressure_index,
        round(wellbeing_score,2),
        status
    ]
})

summary.to_excel(
    "Economic_Wellbeing_Score.xlsx",
    index=False
)

print("\nEconomic Wellbeing Score saved successfully.")