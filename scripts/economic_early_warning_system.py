import pandas as pd

warnings = pd.DataFrame({

    "Indicator":[
        "GDP Growth",
        "Inflation",
        "Household Pressure",
        "Economic Resilience",
        "Diversification",
        "Diamond Dependence"
    ],

    "Status":[
        "RED",
        "AMBER",
        "AMBER",
        "GREEN",
        "GREEN",
        "RED"
    ]

})

risk_score = 0

for status in warnings["Status"]:

    if status == "RED":
        risk_score += 3

    elif status == "AMBER":
        risk_score += 2

    else:
        risk_score += 1

if risk_score >= 14:
    alert_level = "Level 4 - High Economic Risk"

elif risk_score >= 10:
    alert_level = "Level 3 - Moderate Economic Risk"

elif risk_score >= 6:
    alert_level = "Level 2 - Low Risk"

else:
    alert_level = "Level 1 - Stable"

print("\n" + "="*80)
print("BOTSWANA ECONOMIC EARLY WARNING SYSTEM")
print("="*80)

print(warnings)

print("\n")
print("National Economic Alert Level:")
print(alert_level)

warnings.to_excel(
    "Botswana_Economic_Early_Warning_System.xlsx",
    index=False
)

print("\nEarly Warning System saved successfully.")