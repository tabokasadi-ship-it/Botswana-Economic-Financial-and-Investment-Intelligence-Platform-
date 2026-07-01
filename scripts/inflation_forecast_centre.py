import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# =====================================================
# LOAD CPI DATA
# =====================================================

df = pd.read_excel("Botswana_CPI_Master.xlsx")

# =====================================================
# HEADLINE CPI
# =====================================================

headline = df[df["Indicator"] == "PCPI_IX"].copy()

headline["Date"] = pd.to_datetime(headline["Date"])

headline = headline.sort_values("Date")

# =====================================================
# ANNUAL INFLATION
# =====================================================

headline["Inflation_Rate"] = (
    headline["Value"].pct_change(12) * 100
)

headline = headline.dropna()

# =====================================================
# ANNUAL AVERAGES
# =====================================================

headline["Year"] = headline["Date"].dt.year

annual = (
    headline
    .groupby("Year")["Inflation_Rate"]
    .mean()
    .reset_index()
)

# =====================================================
# FORECAST MODEL
# =====================================================

X = annual[["Year"]]

y = annual["Inflation_Rate"]

model = LinearRegression()

model.fit(X, y)

# =====================================================
# FUTURE YEARS
# =====================================================

future_years = pd.DataFrame({
    "Year": [2026, 2027, 2028]
})

future_years["Forecast_Inflation_%"] = (
    model.predict(future_years[["Year"]])
)

# =====================================================
# OUTLOOK CLASSIFICATION
# =====================================================

def classify(x):

    if x >= 8:
        return "High Inflation"

    elif x >= 4:
        return "Moderate Inflation"

    else:
        return "Low Inflation"

future_years["Inflation_Outlook"] = (
    future_years["Forecast_Inflation_%"]
    .apply(classify)
)

# =====================================================
# RESULTS
# =====================================================

print("\n")
print("=" * 80)
print("INFLATION FORECAST CENTRE")
print("=" * 80)

print(future_years)

# =====================================================
# EXECUTIVE OUTLOOK
# =====================================================

avg_forecast = future_years[
    "Forecast_Inflation_%"
].mean()

if avg_forecast >= 8:
    outlook = "Persistent High Inflation"

elif avg_forecast >= 4:
    outlook = "Moderate Inflation Environment"

else:
    outlook = "Low Inflation Environment"

print("\n")
print("Overall Inflation Outlook:")
print(outlook)

# =====================================================
# SAVE OUTPUTS
# =====================================================

future_years.to_excel(
    "Inflation_Forecast_2026_2028.xlsx",
    index=False
)

summary = pd.DataFrame({
    "Metric": [
        "Average Forecast Inflation",
        "Inflation Outlook"
    ],
    "Value": [
        round(avg_forecast, 2),
        outlook
    ]
})

summary.to_excel(
    "Inflation_Outlook_Summary.xlsx",
    index=False
)

print("\nInflation Forecast Centre saved successfully.")