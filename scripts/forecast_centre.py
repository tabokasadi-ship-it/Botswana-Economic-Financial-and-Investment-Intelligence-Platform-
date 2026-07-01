# ======================================================
# BOTSWANA ECONOMIC INTELLIGENCE PLATFORM
# FORECAST CENTRE
# REAL GDP + NOMINAL GDP FORECAST
# ======================================================

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# ======================================================
# PART 1: LOAD BOTH DATASETS
# ======================================================

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

print("Current and constant price datasets loaded successfully.")

# ======================================================
# PART 2: PREPARE REAL AND NOMINAL GDP SERIES
# ======================================================

real_gdp = annual_kp[["Year", "GDP at Constant Prices"]].copy()
nominal_gdp = annual_cp[["Year", "GDP at Current Prices"]].copy()

real_gdp = real_gdp.sort_values(by="Year")
nominal_gdp = nominal_gdp.sort_values(by="Year")

print("\nREAL GDP DATA")
print(real_gdp)

print("\nNOMINAL GDP DATA")
print(nominal_gdp)

# ======================================================
# PART 3: CREATE TIME SERIES
# ======================================================

real_gdp_ts = pd.Series(
    data=real_gdp["GDP at Constant Prices"].values,
    index=real_gdp["Year"]
)

nominal_gdp_ts = pd.Series(
    data=nominal_gdp["GDP at Current Prices"].values,
    index=nominal_gdp["Year"]
)

# ======================================================
# PART 4: BUILD FORECAST MODELS
# ======================================================

real_model = ExponentialSmoothing(
    real_gdp_ts,
    trend="add",
    seasonal=None
).fit()

nominal_model = ExponentialSmoothing(
    nominal_gdp_ts,
    trend="add",
    seasonal=None
).fit()

# ======================================================
# PART 5: FORECAST 2026-2028
# ======================================================

forecast_years = [2026, 2027, 2028]

real_forecast = real_model.forecast(steps=3)
nominal_forecast = nominal_model.forecast(steps=3)

forecast_df = pd.DataFrame({
    "Year": forecast_years,
    "Real_GDP_Forecast_Constant_Prices": real_forecast.values,
    "Nominal_GDP_Forecast_Current_Prices": nominal_forecast.values
})

print("\n")
print("=" * 70)
print("GDP FORECAST CENTRE")
print("=" * 70)

print(forecast_df)

forecast_df.to_excel(
    "GDP_Real_Nominal_Forecast_2026_2028.xlsx",
    index=False
)

print("\nGDP Real and Nominal Forecast saved successfully.")

# ======================================================
# PART 6: FORECAST GROWTH RATES
# ======================================================

last_real_gdp = real_gdp["GDP at Constant Prices"].iloc[-1]
last_nominal_gdp = nominal_gdp["GDP at Current Prices"].iloc[-1]

forecast_df["Real_GDP_Growth_Forecast_%"] = (
    forecast_df["Real_GDP_Forecast_Constant_Prices"]
    .pct_change()
    * 100
)

forecast_df["Nominal_GDP_Growth_Forecast_%"] = (
    forecast_df["Nominal_GDP_Forecast_Current_Prices"]
    .pct_change()
    * 100
)

# Fix first forecast growth rate using 2025 as base year
forecast_df.loc[0, "Real_GDP_Growth_Forecast_%"] = (
    (
        forecast_df.loc[0, "Real_GDP_Forecast_Constant_Prices"]
        - last_real_gdp
    )
    / last_real_gdp
) * 100

forecast_df.loc[0, "Nominal_GDP_Growth_Forecast_%"] = (
    (
        forecast_df.loc[0, "Nominal_GDP_Forecast_Current_Prices"]
        - last_nominal_gdp
    )
    / last_nominal_gdp
) * 100

print("\n")
print("=" * 70)
print("GDP FORECAST CENTRE")
print("=" * 70)

print(forecast_df)

# ======================================================
# PART 7: STRATEGIC SECTOR FORECASTS
# ======================================================

strategic_sectors = [
    "Mining & Quarrying",
    "Wholesale & Retail",
    "Finance, Insurance & Pension Funding",
    "Construction",
    "Information & Communication Technology",
    "Education"
]

sector_forecast_results = []

for sector in strategic_sectors:

    sector_data = annual_kp[
        [
            "Year",
            sector
        ]
    ].copy()

    sector_data = sector_data.sort_values(
        by="Year"
    )

    sector_ts = pd.Series(
        data=sector_data[sector].values,
        index=sector_data["Year"]
    )

    sector_model = ExponentialSmoothing(
        sector_ts,
        trend="add",
        seasonal=None
    ).fit()

    sector_forecast = sector_model.forecast(
        steps=3
    )

    last_value = sector_data[sector].iloc[-1]

    for i, year in enumerate(forecast_years):

        forecast_value = sector_forecast.values[i]

        if i == 0:
            growth_rate = (
                (forecast_value - last_value)
                / last_value
            ) * 100
        else:
            previous_value = sector_forecast.values[i - 1]
            growth_rate = (
                (forecast_value - previous_value)
                / previous_value
            ) * 100

        sector_forecast_results.append({
            "Sector": sector,
            "Year": year,
            "Forecast_Value_Constant_Prices": forecast_value,
            "Forecast_Growth_Rate_%": growth_rate
        })

sector_forecast_df = pd.DataFrame(
    sector_forecast_results
)

print("\n")
print("=" * 70)
print("STRATEGIC SECTOR FORECASTS")
print("=" * 70)

print(sector_forecast_df)

sector_forecast_df.to_excel(
    "Strategic_Sector_Forecasts_2026_2028.xlsx",
    index=False
)

print("\nStrategic Sector Forecasts saved successfully.")

# ======================================================
# PART 8: FUTURE GROWTH DRIVER RANKING
# ======================================================

future_growth_summary = (
    sector_forecast_df
    .groupby("Sector")["Forecast_Growth_Rate_%"]
    .mean()
    .reset_index()
)

future_growth_summary = future_growth_summary.rename(
    columns={
        "Forecast_Growth_Rate_%": "Average_Forecast_Growth_2026_2028"
    }
)

future_growth_summary = future_growth_summary.sort_values(
    by="Average_Forecast_Growth_2026_2028",
    ascending=False
)

print("\n")
print("=" * 70)
print("FUTURE GROWTH DRIVER RANKING")
print("=" * 70)

print(future_growth_summary)

print("\n")
print("=" * 70)
print("TOP FUTURE GROWTH SECTORS")
print("=" * 70)

print(future_growth_summary.head(5))

print("\n")
print("=" * 70)
print("FUTURE RISK SECTORS")
print("=" * 70)

print(future_growth_summary.tail(5))

future_growth_summary.to_excel(
    "Future_Growth_Driver_Ranking_2026_2028.xlsx",
    index=False
)

print("\nFuture Growth Driver Ranking saved successfully.")

# ======================================================
# PART 9: FORECAST CONFIDENCE ASSESSMENT
# ======================================================

confidence_results = []

for sector in strategic_sectors:

    sector_forecasts = sector_forecast_df[
        sector_forecast_df["Sector"] == sector
    ]["Forecast_Growth_Rate_%"]

    growth_volatility = sector_forecasts.std()

    average_growth = sector_forecasts.mean()

    if growth_volatility <= 2:
        confidence = "High"

    elif growth_volatility <= 5:
        confidence = "Moderate"

    else:
        confidence = "Low"

    confidence_results.append({
        "Sector": sector,
        "Average_Forecast_Growth": average_growth,
        "Forecast_Volatility": growth_volatility,
        "Confidence_Level": confidence
    })

confidence_df = pd.DataFrame(
    confidence_results
)

confidence_df = confidence_df.sort_values(
    by="Average_Forecast_Growth",
    ascending=False
)

print("\n")
print("=" * 70)
print("FORECAST CONFIDENCE ASSESSMENT")
print("=" * 70)

print(confidence_df)

print("\n")
print("=" * 70)
print("HIGH CONFIDENCE FORECASTS")
print("=" * 70)

print(
    confidence_df[
        confidence_df["Confidence_Level"] == "High"
    ]
)

print("\n")
print("=" * 70)
print("LOW CONFIDENCE FORECASTS")
print("=" * 70)

print(
    confidence_df[
        confidence_df["Confidence_Level"] == "Low"
    ]
)

confidence_df.to_excel(
    "Forecast_Confidence_Assessment.xlsx",
    index=False
)

print("\nForecast Confidence Assessment saved successfully.")

# ======================================================
# PART 10: FULL 18-SECTOR FORECAST ENGINE
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

all_sector_forecasts = []

for sector in sector_columns:

    sector_data = annual_kp[
        [
            "Year",
            sector
        ]
    ].copy()

    sector_data = sector_data.sort_values(
        by="Year"
    )

    sector_ts = pd.Series(
        data=sector_data[sector].values,
        index=sector_data["Year"]
    )

    model = ExponentialSmoothing(
        sector_ts,
        trend="add",
        seasonal=None
    ).fit()

    forecasts = model.forecast(
        steps=3
    )

    last_value = sector_data[sector].iloc[-1]

    forecast_2028 = forecasts.iloc[-1]

    growth_rate = (
        (
            forecast_2028
            - last_value
        )
        /
        last_value
    ) * 100

    all_sector_forecasts.append({

        "Sector": sector,

        "Value_2025": last_value,

        "Forecast_2028": forecast_2028,

        "Growth_2025_2028_%": growth_rate

    })

full_forecast_df = pd.DataFrame(
    all_sector_forecasts
)

full_forecast_df = full_forecast_df.sort_values(
    by="Growth_2025_2028_%",
    ascending=False
)

print("\n")
print("=" * 80)
print("FULL 18-SECTOR FORECAST ENGINE")
print("=" * 80)

print(full_forecast_df)

full_forecast_df.to_excel(
    "Full_18_Sector_Forecast_Engine.xlsx",
    index=False
)

print("\nFull 18-Sector Forecast Engine saved successfully.")

# ======================================================
# FUTURE GROWTH LEADERS
# ======================================================

print("\n")
print("=" * 80)
print("TOP 10 FUTURE GROWTH LEADERS")
print("=" * 80)

print(
    full_forecast_df.head(10)
)

print("\n")
print("=" * 80)
print("TOP 10 FUTURE DECLINING SECTORS")
print("=" * 80)

print(
    full_forecast_df.tail(10)
)

# ======================================================
# FULL SECTOR FORECAST CONFIDENCE ASSESSMENT
# ======================================================

forecast_confidence_results = []

for sector in sector_columns:

    sector_forecasts = full_forecast_df[
        full_forecast_df["Sector"] == sector
    ]

    growth_2025_2028 = sector_forecasts[
        "Growth_2025_2028_%"
    ].iloc[0]

    # Use historical quarterly volatility from earlier logic if available later.
    # For now, classify based on forecast growth extremity.
    if abs(growth_2025_2028) >= 25:
        confidence = "Low"

    elif abs(growth_2025_2028) >= 15:
        confidence = "Moderate"

    else:
        confidence = "High"

    forecast_confidence_results.append({
        "Sector": sector,
        "Growth_2025_2028_%": growth_2025_2028,
        "Forecast_Confidence": confidence
    })

forecast_confidence_df = pd.DataFrame(
    forecast_confidence_results
)

full_forecast_df = pd.merge(
    full_forecast_df,
    forecast_confidence_df,
    on=[
        "Sector",
        "Growth_2025_2028_%"
    ],
    how="left"
)

print("\n")
print("=" * 80)
print("FULL SECTOR FORECAST WITH CONFIDENCE")
print("=" * 80)

print(full_forecast_df)

print("\n")
print("=" * 80)
print("LOW CONFIDENCE FORECASTS")
print("=" * 80)

print(
    full_forecast_df[
        full_forecast_df["Forecast_Confidence"] == "Low"
    ]
)

full_forecast_df.to_excel(
    "Full_18_Sector_Forecast_With_Confidence.xlsx",
    index=False
)

print("\nFull 18-Sector Forecast with Confidence saved successfully.")