import pandas as pd

briefing = pd.DataFrame({

    "Area":[
        "Economic Growth",
        "Inflation",
        "Household Pressure",
        "Economic Resilience",
        "Diversification",
        "Future Outlook"
    ],

    "Current_Status":[
        "Weak",
        "Moderate",
        "Moderate",
        "Strong",
        "Improving",
        "Positive"
    ],

    "Outlook":[
        "Recovery Expected",
        "Stable",
        "Stable",
        "Stable",
        "Positive",
        "Moderately Positive"
    ],

    "Priority":[
        "High",
        "High",
        "High",
        "Medium",
        "Medium",
        "Medium"
    ]

})

print("\n" + "="*80)
print("BOTSWANA ECONOMIC EXECUTIVE BRIEFING")
print("="*80)

print(briefing)

briefing.to_excel(
    "Botswana_Economic_Executive_Briefing.xlsx",
    index=False
)

print("\nExecutive Briefing saved successfully.")