# ======================================================
# BOTSWANA FINAL ECONOMIC HEALTH SCORE
# WITH DATA SOURCES EXPLAINED
# ======================================================

# ======================================================
# INPUT SCORES FROM PREVIOUS ANALYSIS OUTPUTS
# ======================================================

# From GDP Analysis:
# 2025 GDP Growth Rate = -0.73%
# Negative growth = weak growth score
gdp_growth_score = 20

# From Diversification Analysis:
# Top 5 sectors share = 58.38%
# This gives diversification score = 80
diversification_score = 80

# From Transformation Tracker:
# Average structural change = 1.39 percentage points
# This gives transformation score = 60
transformation_score = 60

# From Opportunity Matrix:
# 14 out of 18 sectors are Strategic Leaders or Emerging Opportunities
# This gives opportunity score = 80
opportunity_score = 80

# From Botswana Economic Resilience Index:
# Final resilience score = 72
resilience_score = 72

# From Risk Structure Analysis:
# Risk structure score = 80
risk_score = 80

# ======================================================
# WEIGHTS
# ======================================================

weights = {
    "GDP Growth": 0.25,
    "Diversification": 0.20,
    "Transformation": 0.15,
    "Opportunity": 0.15,
    "Resilience": 0.15,
    "Risk": 0.10
}

economic_health_score = (
    (gdp_growth_score * weights["GDP Growth"])
    + (diversification_score * weights["Diversification"])
    + (transformation_score * weights["Transformation"])
    + (opportunity_score * weights["Opportunity"])
    + (resilience_score * weights["Resilience"])
    + (risk_score * weights["Risk"])
)

# ======================================================
# STATUS
# ======================================================

if economic_health_score >= 80:
    status = "Strong"
elif economic_health_score >= 65:
    status = "Moderately Healthy"
elif economic_health_score >= 50:
    status = "Vulnerable"
else:
    status = "Weak"

# ======================================================
# OUTPUT TABLE
# ======================================================

import pandas as pd

health_components = pd.DataFrame({
    "Component": [
        "GDP Growth",
        "Diversification",
        "Transformation",
        "Opportunity",
        "Resilience",
        "Risk"
    ],
    "Data_Source": [
        "GDP Analysis: 2025 real GDP growth rate",
        "Diversification Analysis: top 5 sector GDP concentration",
        "Transformation Tracker: 2015 vs 2025 sector share change",
        "Opportunity Matrix: strategic leaders + emerging opportunities",
        "Botswana Economic Resilience Index",
        "Risk Structure Analysis: volatility risk categories"
    ],
    "Actual_Evidence": [
        "2025 real GDP growth = -0.73%",
        "Top 5 sectors = 58.38% of GDP",
        "Average structural change = 1.39 percentage points",
        "14 out of 18 sectors are positive opportunity sectors",
        "Resilience score = 72/100",
        "Risk structure score = 80/100"
    ],
    "Score": [
        gdp_growth_score,
        diversification_score,
        transformation_score,
        opportunity_score,
        resilience_score,
        risk_score
    ],
    "Weight": [
        weights["GDP Growth"],
        weights["Diversification"],
        weights["Transformation"],
        weights["Opportunity"],
        weights["Resilience"],
        weights["Risk"]
    ]
})

health_components["Weighted_Contribution"] = (
    health_components["Score"] * health_components["Weight"]
)

print("\n")
print("=" * 80)
print("BOTSWANA FINAL ECONOMIC HEALTH SCORE")
print("=" * 80)

print(health_components)

print("\n")
print(f"Final Economic Health Score: {economic_health_score:.2f}/100")
print(f"Economic Health Status: {status}")

health_components.to_excel(
    "Final_Economic_Health_Score.xlsx",
    index=False
)

print("\nFinal Economic Health Score saved successfully.")