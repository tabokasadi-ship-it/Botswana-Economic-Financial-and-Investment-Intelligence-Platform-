import pandas as pd

# =====================================================
# BASE VALUES FROM PREVIOUS ANALYSIS
# =====================================================

headline_inflation = 10.266569
food_inflation = 5.759166
transport_inflation = 28.489633
housing_inflation = -1.735244

# =====================================================
# INDEX FUNCTION
# =====================================================

def calculate_pressure(headline, food, transport, housing):
    headline_score = min(max(headline * 5, 0), 100)
    food_score = min(max(food * 5, 0), 100)
    transport_score = min(max(transport * 3, 0), 100)
    housing_score = min(max(housing * 5, 0), 100)

    pressure_index = (
        headline_score * 0.40
        + food_score * 0.25
        + transport_score * 0.20
        + housing_score * 0.15
    )

    if pressure_index >= 80:
        status = "Severe Pressure"
    elif pressure_index >= 60:
        status = "High Pressure"
    elif pressure_index >= 40:
        status = "Moderate Pressure"
    else:
        status = "Low Pressure"

    return pressure_index, status

# =====================================================
# BASELINE
# =====================================================

baseline_score, baseline_status = calculate_pressure(
    headline_inflation,
    food_inflation,
    transport_inflation,
    housing_inflation
)

# =====================================================
# SCENARIOS
# =====================================================

scenarios = [
    {
        "Scenario": "Food inflation +10%",
        "Headline_Inflation": headline_inflation + 1,
        "Food_Inflation": food_inflation + 10,
        "Transport_Inflation": transport_inflation,
        "Housing_Inflation": housing_inflation
    },
    {
        "Scenario": "Transport inflation +10%",
        "Headline_Inflation": headline_inflation + 1.5,
        "Food_Inflation": food_inflation,
        "Transport_Inflation": transport_inflation + 10,
        "Housing_Inflation": housing_inflation
    },
    {
        "Scenario": "Housing inflation +10%",
        "Headline_Inflation": headline_inflation + 1,
        "Food_Inflation": food_inflation,
        "Transport_Inflation": transport_inflation,
        "Housing_Inflation": housing_inflation + 10
    },
    {
        "Scenario": "Combined household shock",
        "Headline_Inflation": headline_inflation + 2,
        "Food_Inflation": food_inflation + 10,
        "Transport_Inflation": transport_inflation + 10,
        "Housing_Inflation": housing_inflation + 10
    }
]

results = []

for s in scenarios:
    score, status = calculate_pressure(
        s["Headline_Inflation"],
        s["Food_Inflation"],
        s["Transport_Inflation"],
        s["Housing_Inflation"]
    )

    results.append({
        "Scenario": s["Scenario"],
        "Pressure_Index": score,
        "Pressure_Status": status,
        "Change_From_Baseline": score - baseline_score
    })

simulator_df = pd.DataFrame(results)

# =====================================================
# RESULTS
# =====================================================

print("\n" + "=" * 70)
print("COST OF LIVING SIMULATOR")
print("=" * 70)

print(f"Baseline Household Cost Pressure Index: {baseline_score:.2f}/100")
print(f"Baseline Status: {baseline_status}")
print()
print(simulator_df)

# =====================================================
# SAVE OUTPUTS
# =====================================================

simulator_df.to_excel(
    "Cost_of_Living_Simulator_Results.xlsx",
    index=False
)

summary = pd.DataFrame({
    "Metric": [
        "Baseline Household Cost Pressure Index",
        "Baseline Pressure Status"
    ],
    "Value": [
        round(baseline_score, 2),
        baseline_status
    ]
})

summary.to_excel(
    "Cost_of_Living_Simulator_Summary.xlsx",
    index=False
)

print("\nCost of Living Simulator saved successfully.")