import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Cost of Living Intelligence",
    layout="wide"
)

# ======================================================
# CUSTOM STYLE
# ======================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff7fb;
    }

    .executive-card {
        background-color: white;
        padding: 28px;
        border-radius: 20px;
        border-left: 8px solid #f3a9c9;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 25px;
    }

    h1, h2, h3 {
        color: #1f1f1f;
    }

    .small-note {
        color: #555555;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================================================
# LOAD DATA
# ======================================================

inflation_summary = pd.read_excel("Inflation_Performance_Summary.xlsx")
inflation_series = pd.read_excel("Inflation_Time_Series.xlsx")
drivers = pd.read_excel("Inflation_Driver_Analysis.xlsx")
pressure_index = pd.read_excel("Household_Cost_Pressure_Index.xlsx")
pressure_components = pd.read_excel("Household_Cost_Pressure_Components.xlsx")
risk = pd.read_excel("Inflation_Risk_Analysis.xlsx")
forecast = pd.read_excel("Inflation_Forecast_2026_2028.xlsx")
simulator = pd.read_excel("Cost_of_Living_Simulator_Results.xlsx")
linkage = pd.read_excel("Growth_Inflation_Linkage_Analysis.xlsx")
linkage_summary = pd.read_excel("Growth_Inflation_Intelligence_Summary.xlsx")
insights = pd.read_excel("Cost_of_Living_Executive_Insights.xlsx")
recommendations = pd.read_excel("Cost_of_Living_Executive_Recommendations.xlsx")
briefing = pd.read_excel("Cost_of_Living_Executive_Briefing.xlsx")
wellbeing = pd.read_excel("Economic_Wellbeing_Score.xlsx")
early_warning = pd.read_excel("Botswana_Economic_Early_Warning_System.xlsx")
executive_briefing = pd.read_excel("Botswana_Economic_Executive_Briefing.xlsx")

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("Cost of Living Intelligence")

section = st.sidebar.radio(
    "Go to section",
    [
        "Executive Overview",
        "Inflation Performance",
        "Inflation Drivers",
        "Household Cost Pressure",
        "Inflation Risk Analysis",
        "Growth–Inflation Intelligence",
        "Forecast Centre",
        "Cost of Living Simulator",
        "Executive Recommendations",
        "Executive Insight"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Botswana Economic, Financial & Investment Intelligence Platform")
st.sidebar.success("Prepared by Taboka Abaleng Mpatane")

# ======================================================
# HEADER
# ======================================================

st.markdown(
    """
    <div class="executive-card">
        <h1>💰 Botswana Cost of Living Intelligence Dashboard</h1>
        <p class="small-note">
        Botswana Economic, Financial & Investment Intelligence Platform | CPI & Household Pressure Analytics
        </p>
        <hr>
        <p>
        <b>Prepared by:</b> Taboka Abaleng Mpatane<br>
        Business Intelligence & Data Analytics<br>
        Inflation Intelligence | Household Pressure | Forecasting | Decision Intelligence
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================================================
# KPI VALUES
# ======================================================

latest_inflation = float(
    inflation_summary.loc[
        inflation_summary["Metric"] == "Latest Inflation",
        "Value"
    ].iloc[0]
)

average_inflation = float(
    inflation_summary.loc[
        inflation_summary["Metric"] == "Average Inflation",
        "Value"
    ].iloc[0]
)

peak_inflation = float(
    inflation_summary.loc[
        inflation_summary["Metric"] == "Peak Inflation",
        "Value"
    ].iloc[0]
)

household_pressure_score = float(
    pressure_index.loc[
        pressure_index["Metric"] == "Household Cost Pressure Index",
        "Value"
    ].iloc[0]
)

household_pressure_status = pressure_index.loc[
    pressure_index["Metric"] == "Pressure Status",
    "Value"
].iloc[0]

top_driver = drivers.iloc[0]["Category"]
top_driver_value = float(drivers.iloc[0]["Latest_Inflation_%"])

highest_risk = risk.iloc[0]["Category"]

wellbeing_score = wellbeing.loc[
    wellbeing["Metric"] == "Economic Wellbeing Score",
    "Value"
].iloc[0]

alert_level = "Level 3 - Moderate Economic Risk"

# ======================================================
# EXECUTIVE OVERVIEW
# ======================================================

if section == "Executive Overview":

    st.header("Executive Overview")

    k1, k2, k3 = st.columns(3)
    k4, k5, k6 = st.columns(3)

    k1.metric("Latest Inflation", f"{latest_inflation:.2f}%", "Elevated")
    k2.metric("Household Cost Pressure", f"{household_pressure_score:.2f}/100", household_pressure_status)
    k3.metric("Main Inflation Driver", top_driver, f"{top_driver_value:.2f}%")

    k4.metric("Highest Inflation Risk", highest_risk, "Most volatile")
    k5.metric("Economic Wellbeing Score", f"{float(wellbeing_score):.2f}/100", "Stable but Vulnerable")
    k6.metric("Economic Alert Level", "Level 3", "Moderate Economic Risk")

    st.markdown("### Executive Economic Briefing")
    st.write(briefing["Executive_Briefing"].iloc[0])

    st.subheader("Economic Executive Snapshot")
    st.dataframe(executive_briefing, width="stretch")

# ======================================================
# INFLATION PERFORMANCE
# ======================================================

if section == "Inflation Performance":

    st.header("Inflation Performance Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(
            inflation_series,
            x="Date",
            y="Value",
            title="Headline CPI Trend",
            markers=True
        )
        st.plotly_chart(fig, width="stretch")

    with col2:
        fig = px.line(
            inflation_series,
            x="Date",
            y="Inflation_Rate",
            title="Year-on-Year Inflation Rate",
            markers=True
        )
        st.plotly_chart(fig, width="stretch")

    st.dataframe(inflation_summary, width="stretch")
    st.info(
        "Inflation remains above the historical average, indicating continued pressure on households."
    )

# ======================================================
# INFLATION DRIVERS
# ======================================================

if section == "Inflation Drivers":

    st.header("Inflation Driver Intelligence")

    fig = px.bar(
        drivers.sort_values("Latest_Inflation_%", ascending=True),
        x="Latest_Inflation_%",
        y="Category",
        orientation="h",
        color="Pressure_Level",
        title="Latest Inflation by CPI Category"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(drivers, width="stretch")

    st.warning(
        "Transport is the dominant inflation driver, showing that household pressure is strongly linked to mobility and fuel-related costs."
    )

# ======================================================
# HOUSEHOLD COST PRESSURE
# ======================================================

if section == "Household Cost Pressure":

    st.header("Household Cost Pressure Index")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Household Cost Pressure Index",
            f"{household_pressure_score:.2f}/100",
            household_pressure_status
        )

    with c2:
        fig = px.bar(
            pressure_components,
            x="Component",
            y="Inflation_%",
            title="Cost Pressure Components"
        )
        st.plotly_chart(fig, width="stretch")

    st.dataframe(pressure_components, width="stretch")

    st.info(
        "The index shows moderate household pressure. Transport inflation is high, but housing inflation is currently reducing overall pressure."
    )

# ======================================================
# INFLATION RISK ANALYSIS
# ======================================================

if section == "Inflation Risk Analysis":

    st.header("Inflation Risk Analysis")

    fig = px.bar(
        risk.sort_values("Inflation_Volatility", ascending=True),
        x="Inflation_Volatility",
        y="Category",
        orientation="h",
        color="Risk_Level",
        title="Inflation Volatility by Category"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(risk, width="stretch")

    st.warning(
        "Transport is the highest inflation risk category because it has the highest volatility."
    )

# ======================================================
# GROWTH–INFLATION INTELLIGENCE
# ======================================================

if section == "Growth–Inflation Intelligence":

    st.header("Growth–Inflation Intelligence")
    st.subheader("Economic Shocks → Inflation Transmission")

    c1, c2, c3 = st.columns(3)

    c1.metric("Transport Inflation", "28.49%", "Highest driver")
    c2.metric("Transport Volatility", "13.24", "Highest risk")
    c3.metric("Household Pressure", "44.83/100", "Moderate")

    st.markdown(
        """
        Economic Growth Intelligence and Cost of Living Intelligence are connected through
        external shocks, fuel prices, transport costs and household affordability.
        """
    )

    st.dataframe(linkage, width="stretch")
    st.dataframe(linkage_summary, width="stretch")

    st.warning(
        "Strategic Insight: External economic shocks are ultimately felt by households through higher transport costs, imported inflation and reduced purchasing power."
    )

# ======================================================
# FORECAST CENTRE
# ======================================================

if section == "Forecast Centre":

    st.header("Inflation Forecast Centre")

    fig = px.line(
        forecast,
        x="Year",
        y="Forecast_Inflation_%",
        markers=True,
        title="Forecast Inflation 2026–2028"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(forecast, width="stretch")

    st.info(
        "Inflation is forecast to remain in a moderate inflation environment between 2026 and 2028."
    )

# ======================================================
# COST OF LIVING SIMULATOR
# ======================================================

if section == "Cost of Living Simulator":

    st.header("Cost of Living Simulator")

    fig = px.bar(
        simulator.sort_values("Pressure_Index", ascending=True),
        x="Pressure_Index",
        y="Scenario",
        orientation="h",
        color="Pressure_Status",
        title="Scenario Impact on Household Cost Pressure"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(simulator, width="stretch")

    st.success(
        "The combined household shock scenario pushes household pressure into high pressure territory."
    )

# ======================================================
# EXECUTIVE RECOMMENDATIONS
# ======================================================

if section == "Executive Recommendations":

    st.header("Executive Recommendations")

    st.dataframe(recommendations, width="stretch")

    st.success(
        "The strongest recommendation is to monitor transport costs because transport is both the largest inflation driver and the highest inflation risk category."
    )

# ======================================================
# EXECUTIVE INSIGHT
# ======================================================

if section == "Executive Insight":

    st.header("Executive Insight")

    st.dataframe(insights, width="stretch")

    st.markdown("### Final Interpretation")

    st.write(
        """
        Botswana's cost-of-living environment is under moderate pressure. Inflation remains elevated,
        with transport standing out as the main inflation driver and the highest inflation risk category.
        Food inflation remains important because of its direct effect on households, while housing inflation
        currently provides some relief.

        The platform shows that household affordability cannot be understood separately from economic growth.
        Global shocks, weak growth, transport costs and import price pressures all connect to household welfare.
        Botswana is stable, but vulnerable to future transport and food price shocks.
        """
    )