# convert_cpi_to_excel.py

import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse("CPI_STATS.xml")
root = tree.getroot()

records = []

for series in root.iter():
    if series.tag.endswith("Series"):

        indicator = series.attrib.get("INDICATOR")

        for obs in series:

            if obs.tag.endswith("Obs"):

                records.append({
                    "Indicator": indicator,
                    "Date": obs.attrib.get("TIME_PERIOD"),
                    "Value": obs.attrib.get("OBS_VALUE")
                })

df = pd.DataFrame(records)

df["Value"] = pd.to_numeric(df["Value"])

df.to_excel(
    "Botswana_CPI_Master.xlsx",
    index=False
)

print(df.head())
print()
print("Botswana_CPI_Master.xlsx created successfully")

import pandas as pd

# ==========================================
# LOAD CPI DATA
# ==========================================

df = pd.read_excel("Botswana_CPI_Master.xlsx")

print("CPI data loaded successfully.")

print(df.head())

# ==========================================
# HEADLINE CPI ONLY
# ==========================================

headline = df[df["Indicator"] == "PCPI_IX"].copy()

headline["Date"] = pd.to_datetime(headline["Date"])

headline = headline.sort_values("Date")

# ==========================================
# ANNUAL INFLATION
# ==========================================

headline["Inflation_Rate"] = (
    headline["Value"].pct_change(12) * 100
)

latest_inflation = headline["Inflation_Rate"].iloc[-1]

average_inflation = headline["Inflation_Rate"].mean()

peak_inflation = headline["Inflation_Rate"].max()

# ==========================================
# SUMMARY
# ==========================================

summary = pd.DataFrame({
    "Metric":[
        "Latest Inflation",
        "Average Inflation",
        "Peak Inflation"
    ],
    "Value":[
        latest_inflation,
        average_inflation,
        peak_inflation
    ]
})

print()
print("="*70)
print("BOTSWANA INFLATION PERFORMANCE")
print("="*70)

print(summary)

summary.to_excel(
    "Inflation_Performance_Summary.xlsx",
    index=False
)

headline.to_excel(
    "Inflation_Time_Series.xlsx",
    index=False
)

print()
print("Inflation files saved successfully.")