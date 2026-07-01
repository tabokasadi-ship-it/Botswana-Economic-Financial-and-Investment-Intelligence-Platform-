import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

print("All packages loaded successfully!")

# ==========================================
# BOTSWANA ECONOMIC INTELLIGENCE PLATFORM
# ==========================================

import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

current_file = r"data\Completed_Value_Added_Current_Prices_2015_2025_Annual_Quarterly(2)_NoCombined_NoNotes.xlsx"

constant_file = r"data\Completed_Value_Added_Constant_Prices_2015_2025_Annual_Quarterly_CORRECT(1)_NoCombined_NoNotes.xlsx"

annual_cp = pd.read_excel(
    current_file,
    sheet_name="Annual_Current_Prices"
)

annual_kp = pd.read_excel(
    constant_file,
    sheet_name="Annual_Constant_Prices"
)

print("Datasets Loaded Successfully!")

print("\nANNUAL CURRENT PRICE COLUMNS")
print(annual_cp.columns.tolist())

print("\nANNUAL CONSTANT PRICE COLUMNS")
print(annual_kp.columns.tolist())

sector_columns = [
    'Agriculture,Forestry & Fishing',
    'Mining & Quarrying',
    'Manufacturing',
    'Water & Electricity',
    'Construction',
    'Wholesale & Retail',
    'Diamond Traders',
    'Transport & Storage',
    'Accomodation & Food Services',
    'Information & Communication Technology',
    'Finance, Insurance & Pension Funding',
    'Real Estate Activities',
    'Professional, Scientific & Technical Activities',
    ' Administrative & Support Activities',
    'Public Administration & Defence',
    'Education',
    'Human Health & Social Work',
    'Other Services'
]

transformation_results = []

gdp_2015 = annual_cp.loc[
    annual_cp["Year"] == 2015,
    "GDP at Current Prices"
].iloc[0]

gdp_2025 = annual_cp.loc[
    annual_cp["Year"] == 2025,
    "GDP at Current Prices"
].iloc[0]

for sector in sector_columns:

    value_2015 = annual_cp.loc[
        annual_cp["Year"] == 2015,
        sector
    ].iloc[0]

    value_2025 = annual_cp.loc[
        annual_cp["Year"] == 2025,
        sector
    ].iloc[0]

    share_2015 = (
        value_2015 / gdp_2015
    ) * 100

    share_2025 = (
        value_2025 / gdp_2025
    ) * 100

    change = share_2025 - share_2015

    transformation_results.append([
        sector,
        share_2015,
        share_2025,
        change
    ])
    transformation_df = pd.DataFrame(
    transformation_results,
    columns=[
        "Sector",
        "Share_2015",
        "Share_2025",
        "Change"
    ]
)

transformation_df = transformation_df.sort_values(
    by="Change",
    ascending=False
)
print("\nTOP GAINING SECTORS")
print(
    transformation_df.head(5)
)

print("\nTOP DECLINING SECTORS")
print(
    transformation_df.tail(5)
)
# ==========================================
# TRANSFORMATION TRACKER TABLE - ALL SECTORS
# ==========================================

sector_columns = [
    'Agriculture,Forestry & Fishing',
    'Mining & Quarrying',
    'Manufacturing',
    'Water & Electricity',
    'Construction',
    'Wholesale & Retail',
    'Diamond Traders',
    'Transport & Storage',
    'Accomodation & Food Services',
    'Information & Communication Technology',
    'Finance, Insurance & Pension Funding',
    'Real Estate Activities',
    'Professional, Scientific & Technical Activities',
    ' Administrative & Support Activities',
    'Public Administration & Defence',
    'Education',
    'Human Health & Social Work',
    'Other Services'
]

gdp_2015 = annual_cp.loc[annual_cp["Year"] == 2015, "GDP at Current Prices"].iloc[0]
gdp_2025 = annual_cp.loc[annual_cp["Year"] == 2025, "GDP at Current Prices"].iloc[0]

transformation_results = []

for sector in sector_columns:
    value_2015 = annual_cp.loc[annual_cp["Year"] == 2015, sector].iloc[0]
    value_2025 = annual_cp.loc[annual_cp["Year"] == 2025, sector].iloc[0]

    share_2015 = (value_2015 / gdp_2015) * 100
    share_2025 = (value_2025 / gdp_2025) * 100
    change = share_2025 - share_2015

    transformation_results.append({
        "Sector": sector,
        "Value_2015": value_2015,
        "Value_2025": value_2025,
        "Share_2015": share_2015,
        "Share_2025": share_2025,
        "Change": change
    })

transformation_df = pd.DataFrame(transformation_results)

transformation_df = transformation_df.sort_values(
    by="Change",
    ascending=False
)

print("\nFULL TRANSFORMATION TRACKER TABLE")
print(transformation_df)

transformation_df.to_excel(
    "Transformation_Tracker_All_Sectors.xlsx",
    index=False
)

print("\nTransformation Tracker table saved successfully.")

# ==========================================
# TRANSFORMATION CATEGORIES
# ==========================================

def transformation_category(change):
    if change >= 2:
        return "Major Gainer"
    elif change >= 0.5:
        return "Moderate Gainer"
    elif change > -0.5:
        return "Stable"
    elif change > -2:
        return "Moderate Decliner"
    else:
        return "Major Decliner"

transformation_df["Category"] = transformation_df["Change"].apply(transformation_category)

print("\nTRANSFORMATION TRACKER WITH CATEGORIES")
print(transformation_df)

print("\nTRANSFORMATION CATEGORY SUMMARY")
print(transformation_df["Category"].value_counts())

transformation_df.to_excel(
    "Transformation_Tracker_With_Categories.xlsx",
    index=False
)

print("\nTransformation Tracker with categories saved successfully.")

# ======================================================
# PART 5: BOTSWANA TRANSFORMATION SCORE
# ======================================================

transformation_df["Absolute_Change"] = transformation_df["Change"].abs()

total_structural_change = transformation_df["Absolute_Change"].sum()

average_structural_change = transformation_df["Absolute_Change"].mean()

if average_structural_change >= 3:
    transformation_status = "Very High Transformation"
elif average_structural_change >= 2:
    transformation_status = "High Transformation"
elif average_structural_change >= 1:
    transformation_status = "Moderate Transformation"
elif average_structural_change >= 0.5:
    transformation_status = "Low Transformation"
else:
    transformation_status = "Minimal Transformation"

print("\n" + "=" * 60)
print("BOTSWANA TRANSFORMATION SCORE")
print("=" * 60)

print(f"Total Structural Change: {total_structural_change:.2f} percentage points")
print(f"Average Structural Change: {average_structural_change:.2f} percentage points")
print(f"Transformation Status: {transformation_status}")

# ======================================================
# PART 6: TOP GAINERS AND DECLINERS
# ======================================================

top_gainers = transformation_df.head(5)
top_decliners = transformation_df.tail(5)

print("\nTOP 5 GAINING SECTORS")
print(top_gainers[["Sector", "Share_2015", "Share_2025", "Change", "Category"]])

print("\nTOP 5 DECLINING SECTORS")
print(top_decliners[["Sector", "Share_2015", "Share_2025", "Change", "Category"]])

# ======================================================
# PART 7: SAVE OUTPUTS
# ======================================================

transformation_df.to_excel(
    "Transformation_Tracker_With_Score.xlsx",
    index=False
)

top_gainers.to_excel(
    "Top_5_Gaining_Sectors.xlsx",
    index=False
)

top_decliners.to_excel(
    "Top_5_Declining_Sectors.xlsx",
    index=False
)

print("\nFiles saved successfully:")
print("Transformation_Tracker_With_Score.xlsx")
print("Top_5_Gaining_Sectors.xlsx")
print("Top_5_Declining_Sectors.xlsx")

# ======================================================
# GROWTH DRIVER ANALYSIS
# ======================================================

growth_results = []
for sector in sector_columns:

    value_2024 = annual_kp.loc[
        annual_kp["Year"] == 2024,
        sector
    ].iloc[0]

    value_2025 = annual_kp.loc[
        annual_kp["Year"] == 2025,
        sector
    ].iloc[0]

    growth = value_2025 - value_2024

    growth_results.append({
        "Sector": sector,
        "Value_2024": value_2024,
        "Value_2025": value_2025,
        "Growth_Contribution": growth
    })
    growth_driver_df = pd.DataFrame(
    growth_results
)

growth_driver_df = growth_driver_df.sort_values(
    by="Growth_Contribution",
    ascending=False
)
print("\n")
print("=" * 60)
print("GROWTH DRIVER ANALYSIS")
print("=" * 60)

print(growth_driver_df)
print("\nTOP 5 GROWTH DRIVERS")

print(
    growth_driver_df.head(5)
)
print("\nTOP 5 GROWTH DRAGS")

print(
    growth_driver_df.tail(5)
)

sector_columns = [
    "Agriculture,Forestry & Fishing",
    "Mining & Quarrying",
    "Manufacturing",
    "Water & Electricity",
    "Construction",
    "Wholesale & Retail",
    "Diamond Traders",
    "Transport & Storage",
    "Accomodation & Food Services",
    "Information & Communication Technology",
    "Finance, Insurance & Pension Funding",
    "Real Estate Activities",
    "Professional, Scientific & Technical Activities",
    " Administrative & Support Activities",
    "Public Administration & Defence",
    "Education",
    "Human Health & Social Work",
    "Other Services"
]

results = []

for sector in sector_columns:

    size_2025 = annual_cp.loc[
        annual_cp["Year"] == 2025,
        sector
    ].iloc[0]

    value_2024 = annual_kp.loc[
        annual_kp["Year"] == 2024,
        sector
    ].iloc[0]

    value_2025 = annual_kp.loc[
        annual_kp["Year"] == 2025,
        sector
    ].iloc[0]

    growth_rate = (
        (value_2025 - value_2024)
        / value_2024
    ) * 100

    results.append({
        "Sector": sector,
        "Size_2025": size_2025,
        "Growth_Rate": growth_rate
    })

opportunity_df = pd.DataFrame(results)

print(opportunity_df)

# ======================================================
# MATRIX THRESHOLDS
# ======================================================

average_size = opportunity_df["Size_2025"].mean()

average_growth = opportunity_df["Growth_Rate"].mean()

print("\nAVERAGE SIZE")
print(average_size)

print("\nAVERAGE GROWTH")
print(average_growth)

# ======================================================
# SECTOR OPPORTUNITY MATRIX
# ======================================================

def opportunity_matrix(row):

    size = row["Size_2025"]
    growth = row["Growth_Rate"]

    if size > average_size and growth > average_growth:
        return "Strategic Leader"

    elif size <= average_size and growth > average_growth:
        return "Emerging Opportunity"

    elif size > average_size and growth <= average_growth:
        return "Mature Risk Sector"

    else:
        return "Weak Sector"

opportunity_df["Opportunity_Category"] = (
    opportunity_df.apply(
        opportunity_matrix,
        axis=1
    )
)

print("\n")
print("=" * 70)
print("SECTOR OPPORTUNITY MATRIX")
print("=" * 70)

print(
    opportunity_df.sort_values(
        by=["Opportunity_Category", "Size_2025"],
        ascending=False
    )
)

print("\n")
print("=" * 70)
print("OPPORTUNITY MATRIX SUMMARY")
print("=" * 70)

print(
    opportunity_df[
        "Opportunity_Category"
    ].value_counts()
)
opportunity_df.to_excel(
    "Sector_Opportunity_Matrix.xlsx",
    index=False
)

print("\nSector Opportunity Matrix saved successfully.")

# ======================================================
# ECONOMIC OPPORTUNITY SCORE
# ======================================================

# Normalize Size

opportunity_df["Size_Score"] = (
    opportunity_df["Size_2025"]
    /
    opportunity_df["Size_2025"].max()
) * 100

# Normalize Growth

growth_min = opportunity_df["Growth_Rate"].min()
growth_max = opportunity_df["Growth_Rate"].max()

opportunity_df["Growth_Score"] = (
    (
        opportunity_df["Growth_Rate"]
        - growth_min
    )
    /
    (
        growth_max
        - growth_min
    )
) * 100

# Matrix Points

matrix_points = {
    "Strategic Leader": 100,
    "Emerging Opportunity": 75,
    "Mature Risk Sector": 40,
    "Weak Sector": 20
}

opportunity_df["Matrix_Score"] = (
    opportunity_df["Opportunity_Category"]
    .map(matrix_points)
)

opportunity_df["Economic_Opportunity_Score"] = (

    opportunity_df["Size_Score"] * 0.40

    +

    opportunity_df["Growth_Score"] * 0.40

    +

    opportunity_df["Matrix_Score"] * 0.20

)

opportunity_df = opportunity_df.sort_values(
    by="Economic_Opportunity_Score",
    ascending=False
)

print("\n")
print("=" * 70)
print("ECONOMIC OPPORTUNITY SCORE")
print("=" * 70)

print(
    opportunity_df[
        [
            "Sector",
            "Opportunity_Category",
            "Economic_Opportunity_Score"
        ]
    ]
)

print("\n")
print("=" * 70)
print("TOP 10 OPPORTUNITY SECTORS")
print("=" * 70)

print(
    opportunity_df[
        [
            "Sector",
            "Economic_Opportunity_Score"
        ]
    ].head(10)
)

opportunity_df.to_excel(
    "Economic_Opportunity_Score.xlsx",
    index=False
)

print("\nEconomic Opportunity Score saved successfully.")

constant_file = r"data\Completed_Value_Added_Constant_Prices_2015_2025_Annual_Quarterly_CORRECT(1)_NoCombined_NoNotes.xlsx"

quarterly_kp = pd.read_excel(
    constant_file,
    sheet_name="Quarterly_Constant_Prices"
)

print("Quarterly dataset loaded successfully.")

# ======================================================
# SECTOR COLUMNS
# ======================================================

sector_columns = [
    "Agriculture,Forestry & Fishing",
    "Mining & Quarrying",
    "Manufacturing",
    "Water & Electricity",
    "Construction",
    "Wholesale & Retail",
    "Diamond Traders",
    "Transport & Storage",
    "Accomodation & Food Services",
    "Information & Communication Technology",
    "Finance, Insurance & Pension Funding",
    "Real Estate Activities",
    "Professional, Scientific & Technical Activities",
    " Administrative & Support Activities",
    "Public Administration & Defence",
    "Education",
    "Human Health & Social Work",
    "Other Services"
]

# ======================================================
# CALCULATE VOLATILITY
# ======================================================

volatility_results = []

for sector in sector_columns:

    volatility = quarterly_kp[sector].std()

    mean_value = quarterly_kp[sector].mean()

    coefficient_variation = (
        volatility / mean_value
    ) * 100

    volatility_results.append({
        "Sector": sector,
        "Standard_Deviation": volatility,
        "Mean_Value": mean_value,
        "Volatility_Score": coefficient_variation
    })

volatility_df = pd.DataFrame(
    volatility_results
)

volatility_df = volatility_df.sort_values(
    by="Volatility_Score",
    ascending=False
)

# ======================================================
# RISK CATEGORY
# ======================================================

def volatility_category(score):

    if score >= 50:
        return "Very High Risk"

    elif score >= 30:
        return "High Risk"

    elif score >= 20:
        return "Moderate Risk"

    elif score >= 10:
        return "Low Risk"

    else:
        return "Very Low Risk"

volatility_df["Risk_Category"] = (
    volatility_df["Volatility_Score"]
    .apply(volatility_category)
)

# ======================================================
# RESULTS
# ======================================================

print("\n")
print("=" * 70)
print("SECTOR VOLATILITY RISK ANALYSIS")
print("=" * 70)

print(volatility_df)

print("\n")
print("=" * 70)
print("TOP 10 MOST VOLATILE SECTORS")
print("=" * 70)

print(
    volatility_df.head(10)
)

print("\n")
print("=" * 70)
print("TOP 10 MOST STABLE SECTORS")
print("=" * 70)

print(
    volatility_df.tail(10)
)

# ======================================================
# SUMMARY
# ======================================================

print("\n")
print("=" * 70)
print("VOLATILITY RISK SUMMARY")
print("=" * 70)

print(
    volatility_df["Risk_Category"]
    .value_counts()
)

# ======================================================
# SAVE
# ======================================================

volatility_df.to_excel(
    "Sector_Volatility_Risk_Analysis.xlsx",
    index=False
)

print("\nSector Volatility Risk Analysis saved successfully.")

# ======================================================
# OPPORTUNITY & RISK ASSESSMENT
# ======================================================

# ======================================================
# LOAD FILES
# ======================================================

opportunity_df = pd.read_excel(
    "Economic_Opportunity_Score.xlsx"
)

risk_df = pd.read_excel(
    "Sector_Volatility_Risk_Analysis.xlsx"
)

# ======================================================
# MERGE DATA
# ======================================================

assessment_df = pd.merge(
    opportunity_df,
    risk_df[
        [
            "Sector",
            "Volatility_Score",
            "Risk_Category"
        ]
    ],
    on="Sector",
    how="left"
)

# ======================================================
# VERDICT LOGIC
# ======================================================

def verdict(row):

    opportunity = row["Economic_Opportunity_Score"]
    risk = row["Volatility_Score"]

    if opportunity >= 70 and risk < 15:
        return "High Priority"

    elif opportunity >= 60 and risk < 20:
        return "Attractive"

    elif opportunity >= 50 and risk < 25:
        return "Monitor"

    elif opportunity < 40 and risk >= 20:
        return "High Risk"

    else:
        return "Neutral"

assessment_df["Verdict"] = (
    assessment_df.apply(
        verdict,
        axis=1
    )
)

# ======================================================
# DISPLAY RESULTS
# ======================================================

print("\n")
print("=" * 80)
print("OPPORTUNITY & RISK ASSESSMENT")
print("=" * 80)

print(
    assessment_df[
        [
            "Sector",
            "Economic_Opportunity_Score",
            "Volatility_Score",
            "Risk_Category",
            "Verdict"
        ]
    ]
)

# ======================================================
# TOP SECTORS
# ======================================================

print("\n")
print("=" * 80)
print("TOP PRIORITY SECTORS")
print("=" * 80)

print(
    assessment_df[
        assessment_df["Verdict"]
        == "High Priority"
    ][
        [
            "Sector",
            "Economic_Opportunity_Score",
            "Volatility_Score"
        ]
    ]
)

# ======================================================
# HIGH RISK SECTORS
# ======================================================

print("\n")
print("=" * 80)
print("HIGH RISK SECTORS")
print("=" * 80)

print(
    assessment_df[
        assessment_df["Verdict"]
        == "High Risk"
    ][
        [
            "Sector",
            "Economic_Opportunity_Score",
            "Volatility_Score"
        ]
    ]
)

# ======================================================
# SUMMARY
# ======================================================

print("\n")
print("=" * 80)
print("VERDICT SUMMARY")
print("=" * 80)

print(
    assessment_df["Verdict"]
    .value_counts()
)

# ======================================================
# SAVE
# ======================================================

assessment_df.to_excel(
    "Opportunity_Risk_Assessment.xlsx",
    index=False
)

print(
    "\nOpportunity & Risk Assessment saved successfully."
)

# ======================================================
# SAVE
# ======================================================

assessment_df.to_excel(
    "Opportunity_Risk_Assessment.xlsx",
    index=False
)

print(
    "\nOpportunity & Risk Assessment saved successfully."
)
# ======================================================
# FINAL PRIORITY INDEX
# ======================================================

assessment_df["Priority_Index"] = (
    assessment_df["Economic_Opportunity_Score"]
    - (assessment_df["Volatility_Score"] * 0.75)
)

assessment_df = assessment_df.sort_values(
    by="Priority_Index",
    ascending=False
)

print("\n")
print("=" * 80)
print("FINAL OPPORTUNITY & RISK PRIORITY RANKING")
print("=" * 80)

print(
    assessment_df[
        [
            "Sector",
            "Economic_Opportunity_Score",
            "Volatility_Score",
            "Risk_Category",
            "Priority_Index",
            "Verdict"
        ]
    ]
)

assessment_df.to_excel(
    "Final_Opportunity_Risk_Assessment.xlsx",
    index=False
)

print("\nFinal Opportunity & Risk Assessment saved successfully.")

current_file = r"data\Completed_Value_Added_Current_Prices_2015_2025_Annual_Quarterly(2)_NoCombined_NoNotes.xlsx"

annual_cp = pd.read_excel(
    current_file,
    sheet_name="Annual_Current_Prices"
)

print("Annual current prices data loaded successfully.")

# ======================================================
# SECTOR COLUMNS
# ======================================================

sector_columns = [
    "Agriculture,Forestry & Fishing",
    "Mining & Quarrying",
    "Manufacturing",
    "Water & Electricity",
    "Construction",
    "Wholesale & Retail",
    "Diamond Traders",
    "Transport & Storage",
    "Accomodation & Food Services",
    "Information & Communication Technology",
    "Finance, Insurance & Pension Funding",
    "Real Estate Activities",
    "Professional, Scientific & Technical Activities",
    " Administrative & Support Activities",
    "Public Administration & Defence",
    "Education",
    "Human Health & Social Work",
    "Other Services"
]

# ======================================================
# GET LATEST YEAR
# ======================================================

latest_year = annual_cp["Year"].max()

latest_data = annual_cp[
    annual_cp["Year"] == latest_year
]

total_gdp = latest_data[
    "GDP at Current Prices"
].iloc[0]

# ======================================================
# CALCULATE SECTOR SHARES
# ======================================================

sector_shares = []

for sector in sector_columns:

    sector_value = latest_data[
        sector
    ].iloc[0]

    sector_share = (
        sector_value / total_gdp
    ) * 100

    sector_shares.append({
        "Sector": sector,
        "Sector_Value": sector_value,
        "Sector_Share": sector_share
    })

sector_share_df = pd.DataFrame(
    sector_shares
)

sector_share_df = sector_share_df.sort_values(
    by="Sector_Share",
    ascending=False
)

print("\n")
print("=" * 70)
print("SECTOR SHARES FOR DIVERSIFICATION ANALYSIS")
print("=" * 70)

print(sector_share_df)

# ======================================================
# CONCENTRATION MEASURE
# ======================================================

top_3_share = sector_share_df.head(3)["Sector_Share"].sum()
top_5_share = sector_share_df.head(5)["Sector_Share"].sum()

largest_sector_share = sector_share_df.iloc[0]["Sector_Share"]

print("\n")
print("=" * 70)
print("ECONOMIC CONCENTRATION SUMMARY")
print("=" * 70)

print(f"Latest Year: {latest_year}")
print(f"Largest Sector Share: {largest_sector_share:.2f}%")
print(f"Top 3 Sectors Share: {top_3_share:.2f}%")
print(f"Top 5 Sectors Share: {top_5_share:.2f}%")

# ======================================================
# DIVERSIFICATION SCORE
# ======================================================

# The lower the Top 5 concentration, the more diversified the economy.
# Score interpretation:
# Top 5 <= 50%  -> Very diversified
# Top 5 50-60%  -> Diversified
# Top 5 60-70%  -> Moderately diversified
# Top 5 70-80%  -> Concentrated
# Top 5 > 80%   -> Highly concentrated

def diversification_score(top_5_share):

    if top_5_share <= 50:
        return 100

    elif top_5_share <= 60:
        return 80

    elif top_5_share <= 70:
        return 60

    elif top_5_share <= 80:
        return 40

    else:
        return 20

div_score = diversification_score(
    top_5_share
)

print("\n")
print("=" * 70)
print("DIVERSIFICATION SCORE")
print("=" * 70)

print(f"Diversification Score: {div_score}/100")

# ======================================================
# SAVE OUTPUT
# ======================================================

sector_share_df.to_excel(
    "Diversification_Sector_Shares.xlsx",
    index=False
)

print("\nDiversification sector shares saved successfully.")

# ======================================================
# PILLAR 2: TRANSFORMATION SCORE
# ======================================================

# This measures how much Botswana's sector structure changed
# between 2015 and 2025.

gdp_2015 = annual_cp.loc[
    annual_cp["Year"] == 2015,
    "GDP at Current Prices"
].iloc[0]

gdp_2025 = annual_cp.loc[
    annual_cp["Year"] == 2025,
    "GDP at Current Prices"
].iloc[0]

transformation_results = []

for sector in sector_columns:

    value_2015 = annual_cp.loc[
        annual_cp["Year"] == 2015,
        sector
    ].iloc[0]

    value_2025 = annual_cp.loc[
        annual_cp["Year"] == 2025,
        sector
    ].iloc[0]

    share_2015 = (value_2015 / gdp_2015) * 100
    share_2025 = (value_2025 / gdp_2025) * 100

    change = share_2025 - share_2015

    transformation_results.append({
        "Sector": sector,
        "Share_2015": share_2015,
        "Share_2025": share_2025,
        "Change": change,
        "Absolute_Change": abs(change)
    })

transformation_df = pd.DataFrame(transformation_results)

total_structural_change = transformation_df["Absolute_Change"].sum()
average_structural_change = transformation_df["Absolute_Change"].mean()

# Convert average structural change into a 0-100 score
if average_structural_change >= 3:
    transformation_score = 100
elif average_structural_change >= 2:
    transformation_score = 80
elif average_structural_change >= 1:
    transformation_score = 60
elif average_structural_change >= 0.5:
    transformation_score = 40
else:
    transformation_score = 20

print("\n")
print("=" * 70)
print("TRANSFORMATION SCORE")
print("=" * 70)

print(f"Total Structural Change: {total_structural_change:.2f} percentage points")
print(f"Average Structural Change: {average_structural_change:.2f} percentage points")
print(f"Transformation Score: {transformation_score}/100")

transformation_df.to_excel(
    "Resilience_Transformation_Analysis.xlsx",
    index=False
)

print("\nTransformation analysis saved successfully.")

# ======================================================
# PILLAR 3: OPPORTUNITY DEPTH SCORE
# ======================================================

strategic_leaders = 4
emerging_opportunities = 10

total_positive_sectors = (
    strategic_leaders
    + emerging_opportunities
)

total_sectors = 18

opportunity_depth = (
    total_positive_sectors
    / total_sectors
) * 100

if opportunity_depth >= 80:
    opportunity_score = 100

elif opportunity_depth >= 70:
    opportunity_score = 80

elif opportunity_depth >= 60:
    opportunity_score = 60

elif opportunity_depth >= 50:
    opportunity_score = 40

else:
    opportunity_score = 20

print("\n")
print("=" * 70)
print("OPPORTUNITY DEPTH SCORE")
print("=" * 70)

print(f"Strategic Leaders: {strategic_leaders}")
print(f"Emerging Opportunities: {emerging_opportunities}")
print(f"Positive Sectors: {total_positive_sectors}")
print(f"Opportunity Depth: {opportunity_depth:.2f}%")
print(f"Opportunity Depth Score: {opportunity_score}/100")

# ======================================================
# PILLAR 4: GROWTH STABILITY SCORE
# ======================================================

gdp_volatility = 5.68

if gdp_volatility <= 2:
    stability_score = 100

elif gdp_volatility <= 4:
    stability_score = 80

elif gdp_volatility <= 6:
    stability_score = 60

elif gdp_volatility <= 8:
    stability_score = 40

else:
    stability_score = 20

print("\n")
print("=" * 70)
print("GROWTH STABILITY SCORE")
print("=" * 70)

print(f"GDP Growth Volatility: {gdp_volatility:.2f}")
print(f"Growth Stability Score: {stability_score}/100")

# ======================================================
# PILLAR 5: RISK STRUCTURE SCORE
# ======================================================

high_risk = 1
moderate_risk = 2
low_risk = 9
very_low_risk = 6

total_sectors = (
    high_risk
    + moderate_risk
    + low_risk
    + very_low_risk
)

risk_weighted_score = (

    (very_low_risk * 100)

    +

    (low_risk * 80)

    +

    (moderate_risk * 50)

    +

    (high_risk * 20)

) / total_sectors

risk_structure_score = round(
    risk_weighted_score,
    2
)

print("\n")
print("=" * 70)
print("RISK STRUCTURE SCORE")
print("=" * 70)

print(f"Very Low Risk Sectors: {very_low_risk}")
print(f"Low Risk Sectors: {low_risk}")
print(f"Moderate Risk Sectors: {moderate_risk}")
print(f"High Risk Sectors: {high_risk}")

print(
    f"Risk Structure Score: "
    f"{risk_structure_score}/100"
)

# ======================================================
# BOTSWANA ECONOMIC RESILIENCE INDEX
# ======================================================

final_resilience_score = (

    (80 * 0.25)

    +

    (60 * 0.20)

    +

    (80 * 0.20)

    +

    (60 * 0.20)

    +

    (risk_structure_score * 0.15)

)

if final_resilience_score >= 80:
    resilience_status = "Highly Resilient"

elif final_resilience_score >= 65:
    resilience_status = "Moderately Resilient"

elif final_resilience_score >= 50:
    resilience_status = "Vulnerable"

else:
    resilience_status = "Highly Vulnerable"

print("\n")
print("=" * 70)
print("BOTSWANA ECONOMIC RESILIENCE INDEX")
print("=" * 70)

print(
    f"Diversification Score: 80"
)

print(
    f"Transformation Score: 60"
)

print(
    f"Opportunity Depth Score: 80"
)

print(
    f"Growth Stability Score: 60"
)

print(
    f"Risk Structure Score: "
    f"{risk_structure_score}"
)

print()

print(
    f"Final Resilience Score: "
    f"{final_resilience_score:.2f}/100"
)

print(
    f"Resilience Status: "
    f"{resilience_status}"
)