# ======================================================
# BOTSWANA ECONOMIC INTELLIGENCE PLATFORM
# GDP ANALYSIS MODULE
# ======================================================

import pandas as pd

# ======================================================
# LOAD CONSTANT PRICE DATA
# ======================================================

constant_file = r"data\Completed_Value_Added_Constant_Prices_2015_2025_Annual_Quarterly_CORRECT(1)_NoCombined_NoNotes.xlsx"

annual_kp = pd.read_excel(
    constant_file,
    sheet_name="Annual_Constant_Prices"
)

print("GDP dataset loaded successfully.")

# ======================================================
# GDP GROWTH RATE
# ======================================================

annual_kp["GDP_Growth_Rate"] = (
    annual_kp["GDP at Constant Prices"]
    .pct_change()
    * 100
)

# ======================================================
# GDP ANALYSIS TABLE
# ======================================================

gdp_analysis = annual_kp[
    [
        "Year",
        "GDP at Constant Prices",
        "GDP_Growth_Rate"
    ]
]

print("\n")
print("=" * 70)
print("BOTSWANA GDP ANALYSIS")
print("=" * 70)

print(gdp_analysis)

# ======================================================
# HIGHEST GROWTH YEAR
# ======================================================

highest_growth = annual_kp.loc[
    annual_kp["GDP_Growth_Rate"].idxmax()
]

# ======================================================
# LOWEST GROWTH YEAR
# ======================================================

lowest_growth = annual_kp.loc[
    annual_kp["GDP_Growth_Rate"].idxmin()
]

# ======================================================
# AVERAGE GDP GROWTH
# ======================================================

average_growth = annual_kp[
    "GDP_Growth_Rate"
].mean()

# ======================================================
# CURRENT GDP GROWTH
# ======================================================

current_growth = annual_kp.loc[
    annual_kp["Year"] == 2025,
    "GDP_Growth_Rate"
].iloc[0]

# ======================================================
# GDP VOLATILITY
# ======================================================

gdp_volatility = annual_kp[
    "GDP_Growth_Rate"
].std()

# ======================================================
# PRE-COVID VS POST-COVID
# ======================================================

pre_covid = annual_kp.loc[
    annual_kp["Year"].between(2015, 2019),
    "GDP_Growth_Rate"
].mean()

post_covid = annual_kp.loc[
    annual_kp["Year"].between(2020, 2025),
    "GDP_Growth_Rate"
].mean()

# ======================================================
# SUMMARY
# ======================================================

print("\n")
print("=" * 70)
print("GDP PERFORMANCE SUMMARY")
print("=" * 70)

print(
    f"Highest Growth Year: "
    f"{int(highest_growth['Year'])}"
)

print(
    f"Highest Growth Rate: "
    f"{highest_growth['GDP_Growth_Rate']:.2f}%"
)

print()

print(
    f"Lowest Growth Year: "
    f"{int(lowest_growth['Year'])}"
)

print(
    f"Lowest Growth Rate: "
    f"{lowest_growth['GDP_Growth_Rate']:.2f}%"
)

print()

print(
    f"Average GDP Growth: "
    f"{average_growth:.2f}%"
)

print(
    f"Current GDP Growth (2025): "
    f"{current_growth:.2f}%"
)

print()

print(
    f"GDP Growth Volatility: "
    f"{gdp_volatility:.2f}"
)

print()

print(
    f"Average Growth (2015-2019): "
    f"{pre_covid:.2f}%"
)

print(
    f"Average Growth (2020-2025): "
    f"{post_covid:.2f}%"
)

# ======================================================
# CLASSIFICATION
# ======================================================

if current_growth >= 5:
    growth_status = "Strong Growth"

elif current_growth >= 2:
    growth_status = "Healthy Growth"

elif current_growth >= 0:
    growth_status = "Weak Growth"

else:
    growth_status = "Economic Contraction"

print()

print(
    f"Current Economic Status: "
    f"{growth_status}"
)

# ======================================================
# SAVE RESULTS
# ======================================================

gdp_analysis.to_excel(
    "GDP_Analysis.xlsx",
    index=False
)

print("\nGDP Analysis saved successfully.")

# ======================================================
# TOP GDP CONTRIBUTORS 2025
# ======================================================

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

gdp_2025 = annual_kp[
    annual_kp["Year"] == 2025
]

sector_2025 = []

for sector in sector_columns:
    value = gdp_2025[sector].iloc[0]

    sector_2025.append({
        "Sector": sector,
        "GDP_2025": value
    })

sector_2025_df = pd.DataFrame(
    sector_2025
)

sector_2025_df = sector_2025_df.sort_values(
    by="GDP_2025",
    ascending=False
)

print("\nTOP GDP CONTRIBUTORS 2025")
print(
    sector_2025_df.head(10)
)