import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Economic Growth Intelligence",
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

    h1, h2, h3 {
        color: #1f1f1f;
        font-family: 'Segoe UI', sans-serif;
    }

    .executive-card {
        background-color: #ffffff;
        padding: 28px;
        border-radius: 20px;
        border-left: 8px solid #f3a9c9;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 25px;
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

gdp = pd.read_excel("GDP_Analysis.xlsx")
shock_timeline = pd.read_excel("Economic_Shock_Timeline.xlsx")
shock_vulnerability = pd.read_excel("Economic_Shock_Vulnerability_Index.xlsx")
shock_transmission = pd.read_excel("Economic_Shock_Transmission_Summary.xlsx")
shock_summary = pd.read_excel("Economic_Shock_Vulnerability_Summary.xlsx")
health = pd.read_excel("Final_Economic_Health_Score.xlsx")
diversification = pd.read_excel("Diversification_Sector_Shares.xlsx")
transformation = pd.read_excel("Transformation_Tracker_With_Score.xlsx")
opportunity = pd.read_excel("Economic_Opportunity_Score.xlsx")
risk = pd.read_excel("Final_Opportunity_Risk_Assessment.xlsx")
volatility = pd.read_excel("Sector_Volatility_Risk_Analysis.xlsx")
gdp_forecast = pd.read_excel("GDP_Real_Nominal_Forecast_2026_2028.xlsx")
future_growth = pd.read_excel("Future_Growth_Driver_Ranking_2026_2028.xlsx")
confidence = pd.read_excel("Forecast_Confidence_Assessment.xlsx")
full_forecast = pd.read_excel("Full_18_Sector_Forecast_With_Confidence.xlsx")
simulator = pd.read_excel("Economic_Future_Simulator_Results.xlsx")
sector_matrix = pd.read_excel("Sector_Opportunity_Matrix.xlsx")

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("Economic Growth Intelligence")

section = st.sidebar.radio(
    "Go to section",
    [
        "Executive Overview",
        "GDP Performance",
        "Economic Shock Intelligence",   
        "Economic Health",
        "Diversification & Transformation",
        "Sector Opportunity Matrix",
        "Economic Opportunity",
        "Opportunity & Risk",
        "Resilience Index",
        "Forecast Centre",
        "Forecast Confidence",
        "Full Sector Forecast",
        "Future Simulator",
        "Executive Insight"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Botswana Economic, Financial & Investment Intelligence Platform")
st.sidebar.success("Taboka Abaleng Mpatane")

# ======================================================
# HEADER
# ======================================================

st.markdown(
    """
    <div style="
        background-color:white;
        padding:25px;
        border-radius:20px;
        border-left:8px solid #f3a9c9;
        box-shadow:0px 4px 12px rgba(0,0,0,0.05);
        margin-bottom:20px;
    ">

    <h1>🇧🇼 Botswana Economic Growth Intelligence Dashboard</h1>

    <p style="color:gray;">
    Botswana Economic, Financial & Investment Intelligence Platform | 2015–2028
    </p>

    <hr>

    <p>
    <b>Prepared by:</b> Taboka Abaleng Mpatane<br>
    Business Intelligence & Data Analytics<br>
    Economic Intelligence | Forecasting | Risk Analytics | Business Intelligence
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ======================================================
# KPI VALUES
# ======================================================

# ======================================================
# KPI VALUES
# ======================================================

economic_health_score = 60.80
economic_resilience_score = 72.00

latest_growth = gdp.loc[
    gdp["Year"] == 2025,
    "GDP_Growth_Rate"
].iloc[0]

top_priority_sector = risk.loc[
    risk["Verdict"] == "High Priority",
    "Sector"
].iloc[0]

# ======================================================
# EXECUTIVE OVERVIEW
# ======================================================

if section == "Executive Overview":

    st.header("Executive Overview")

    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

    kpi1.metric("Economic Health Score", f"{economic_health_score:.1f}/100", "Vulnerable")
    kpi2.metric("Economic Resilience Index", f"{economic_resilience_score:.0f}/100", "Moderately Resilient")
    kpi3.metric("Shock Vulnerability", "71/100", "Moderately Vulnerable")
    kpi4.metric("2025 Real GDP Growth", f"{latest_growth:.2f}%", "Economic contraction")
    kpi5.metric("Top Opportunity Sector", top_priority_sector)
    kpi6.metric("Highest Risk Sector", "Diamond Traders")

    st.markdown("""
    ### Executive Economic Briefing

    Botswana's economy remains moderately resilient despite recent growth challenges.

    Real GDP growth declined to -0.73% in 2025, reflecting continued weakness in the diamond sector and softer external demand conditions. Economic diversification efforts have improved resilience, with finance, ICT and professional services emerging as important growth areas.

    The Economic Health Score of 60.8/100 indicates a vulnerable but stable economy, while the Economic Resilience Index of 72/100 suggests that Botswana remains capable of recovering from external shocks.

    Forecasts indicate a gradual recovery through 2028, although structural risks related to diamond dependence and global commodity demand remain significant.
    """)

# ======================================================
# GDP PERFORMANCE
# ======================================================

if section == "GDP Performance":

    st.header("GDP Performance Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(
            gdp,
            x="Year",
            y="GDP at Constant Prices",
            markers=True,
            title="Real GDP Trend"
        )
        st.plotly_chart(fig, width="stretch")

    with col2:
        fig = px.bar(
            gdp.dropna(),
            x="Year",
            y="GDP_Growth_Rate",
            title="Real GDP Growth Rate"
        )
        st.plotly_chart(fig, width="stretch")

    st.dataframe(gdp, width="stretch")

    st.info(
        "GDP growth weakened in 2024 and 2025, with 2025 recording negative real growth."
    )

# ======================================================
# ECONOMIC SHOCK INTELLIGENCE
# ======================================================

if section == "Economic Shock Intelligence":

    st.header("Economic Shock & Vulnerability Intelligence")

    shock_index = shock_summary.loc[
        shock_summary["Metric"] == "Shock Vulnerability Index",
        "Value"
    ].iloc[0]

    shock_status = shock_summary.loc[
        shock_summary["Metric"] == "Vulnerability Status",
        "Value"
    ].iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Shock Vulnerability Index",
        f"{float(shock_index):.0f}/100",
        shock_status
    )

    c2.metric(
        "Highest Exposure",
        "Diamond Dependence",
        "Structural risk"
    )

    c3.metric(
        "Key Transmission Channel",
        "Diamond revenue",
        "Fiscal + GDP impact"
    )

    st.info(
        "Botswana's economic growth is exposed to external shocks mainly through diamonds, "
        "exports, fiscal revenue, import prices and global demand conditions."
    )

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(
            shock_timeline,
            x="Year",
            y="GDP_Growth_Rate",
            markers=True,
            title="GDP Growth Through Major Economic Shocks",
            hover_data=[
                "Economic_Shock",
                "Shock_Type",
                "Impact_Level",
                "Transmission_Channel"
            ]
        )

        st.plotly_chart(fig, width="stretch")

    with col2:
        fig = px.bar(
            shock_vulnerability.sort_values("Score", ascending=True),
            x="Score",
            y="Risk_Driver",
            orientation="h",
            title="Economic Shock Vulnerability Drivers"
        )

        st.plotly_chart(fig, width="stretch")

    st.subheader("Economic Shock Timeline")
    st.dataframe(shock_timeline, width="stretch")

    st.subheader("Shock Transmission Summary")
    st.dataframe(shock_transmission, width="stretch")

    st.warning(
        "The strongest vulnerability channel is the diamond value chain. "
        "A diamond market shock can affect export earnings, government revenue, public investment and GDP growth."
    )

# ======================================================
# ECONOMIC HEALTH
# ======================================================

if section == "Economic Health":

    st.header("Final Economic Health Score")

    fig = px.bar(
        health,
        x="Component",
        y="Weighted_Contribution",
        title="Economic Health Score Contributions"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(health, width="stretch")

    st.warning(
        "Botswana's Economic Health Score is 60.8/100. The economy shows strengths in "
        "diversification, opportunity and resilience, but weak recent GDP growth pulls down the score."
    )

# ======================================================
# DIVERSIFICATION & TRANSFORMATION
# ======================================================

if section == "Diversification & Transformation":

    st.header("Diversification and Transformation Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        top10_div = diversification.head(10)

        fig = px.bar(
            top10_div,
            x="Sector_Share",
            y="Sector",
            orientation="h",
            title="Top 10 Sector Shares of GDP"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    with col2:
        trans_summary = pd.concat([
            transformation.sort_values("Change", ascending=False).head(5),
            transformation.sort_values("Change", ascending=True).head(5)
        ])

        fig = px.bar(
            trans_summary,
            x="Change",
            y="Sector",
            orientation="h",
            color="Category",
            title="Top Gainers and Decliners in GDP Share"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    st.dataframe(transformation, width="stretch")

    st.info(
        "Mining lost significant GDP share, while Wholesale & Retail, Finance and Construction gained importance."
    )

# ======================================================
# SECTOR OPPORTUNITY MATRIX
# ======================================================

if section == "Sector Opportunity Matrix":

    st.header("Sector Opportunity Matrix")

    fig = px.scatter(
        sector_matrix,
        x="Growth_Rate",
        y="Size_2025",
        color="Opportunity_Category",
        hover_name="Sector",
        size="Size_2025",
        title="Sector Size vs Growth Rate"
    )

    st.plotly_chart(fig, width="stretch")
    st.dataframe(sector_matrix, width="stretch")

    st.success(
        "This matrix proves that a large sector is not always a growth sector."
    )

# ======================================================
# ECONOMIC OPPORTUNITY
# ======================================================

if section == "Economic Opportunity":

    st.header("Economic Opportunity Score")

    top10_opportunity = opportunity.sort_values(
        by="Economic_Opportunity_Score",
        ascending=False
    ).head(10)

    fig = px.bar(
        top10_opportunity,
        x="Economic_Opportunity_Score",
        y="Sector",
        orientation="h",
        color="Opportunity_Category",
        title="Top 10 Economic Opportunity Sectors"
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, width="stretch")

    st.dataframe(opportunity, width="stretch")

# ======================================================
# OPPORTUNITY & RISK
# ======================================================

if section == "Opportunity & Risk":

    st.header("Opportunity and Risk Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        risk_top = risk.sort_values(
            by="Priority_Index",
            ascending=False
        ).head(10)

        fig = px.bar(
            risk_top,
            x="Priority_Index",
            y="Sector",
            orientation="h",
            color="Verdict",
            title="Top Priority Sectors"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    with col2:
        vol_top = volatility.sort_values(
            by="Volatility_Score",
            ascending=False
        ).head(10)

        fig = px.bar(
            vol_top,
            x="Volatility_Score",
            y="Sector",
            orientation="h",
            color="Risk_Category",
            title="Most Volatile Sectors"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    st.dataframe(risk, width="stretch")

    st.info(
        "Finance emerges as a high-priority sector, while Diamond Traders and Water & Electricity show high-risk characteristics."
    )

# ======================================================
# RESILIENCE INDEX
# ======================================================

if section == "Resilience Index":

    st.header("Botswana Economic Resilience Index")

    resilience_df = pd.DataFrame({
        "Pillar": [
            "Diversification",
            "Transformation",
            "Opportunity Depth",
            "Growth Stability",
            "Risk Structure"
        ],
        "Score": [80, 60, 80, 60, 80]
    })

    fig = px.bar(
        resilience_df,
        x="Pillar",
        y="Score",
        title="Economic Resilience Pillar Scores"
    )

    st.plotly_chart(fig, width="stretch")

    st.metric(
        "Final Economic Resilience Index",
        "72/100",
        "Moderately Resilient"
    )

    st.dataframe(resilience_df, width="stretch")

# ======================================================
# FORECAST CENTRE
# ======================================================

if section == "Forecast Centre":

    st.header("Forecast Centre")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(
            gdp_forecast,
            x="Year",
            y=[
                "Real_GDP_Forecast_Constant_Prices",
                "Nominal_GDP_Forecast_Current_Prices"
            ],
            markers=True,
            title="Real vs Nominal GDP Forecast"
        )

        st.plotly_chart(fig, width="stretch")

    with col2:
        fig = px.bar(
            future_growth,
            x="Average_Forecast_Growth_2026_2028",
            y="Sector",
            orientation="h",
            title="Future Growth Driver Ranking"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    st.dataframe(gdp_forecast, width="stretch")

# ======================================================
# FORECAST CONFIDENCE
# ======================================================

if section == "Forecast Confidence":

    st.header("Forecast Confidence Assessment")

    fig = px.bar(
        confidence,
        x="Average_Forecast_Growth",
        y="Sector",
        orientation="h",
        color="Confidence_Level",
        title="Forecast Growth and Confidence"
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, width="stretch")

    st.dataframe(confidence, width="stretch")

    st.warning(
        "Mining shows high forecast growth but low confidence, suggesting rebound effects rather than stable future growth."
    )

# ======================================================
# FULL SECTOR FORECAST
# ======================================================

if section == "Full Sector Forecast":

    st.header("Full 18-Sector Forecast Engine")

    fig = px.bar(
        full_forecast.sort_values("Growth_2025_2028_%", ascending=False).head(10),
        x="Growth_2025_2028_%",
        y="Sector",
        orientation="h",
        color="Forecast_Confidence",
        title="Top Forecast Growth Sectors by 2028"
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, width="stretch")

    st.dataframe(full_forecast, width="stretch")

# ======================================================
# FUTURE SIMULATOR
# ======================================================

if section == "Future Simulator":

    st.header("Economic Future Simulator")

    fig = px.bar(
        simulator,
        x="GDP_Impact_%",
        y="Scenario",
        orientation="h",
        title="Scenario Impact on 2028 GDP"
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, width="stretch")

    st.dataframe(simulator, width="stretch")

    st.success(
        "A 10% mining shock has a larger GDP impact than a 20% ICT shock because ICT is still relatively small."
    )

# ======================================================
# EXECUTIVE INSIGHT
# ======================================================

if section == "Executive Insight":

    st.header("Executive Insight")

    st.markdown(
        """
        Botswana's economy is **moderately resilient but currently vulnerable**.
        The country has developed a broader sector base, with strong opportunities in
        Finance, Wholesale & Retail, ICT, Education and Professional Services.

        However, real GDP growth weakened in 2024 and 2025, and mining remains an important
        but structurally risky sector. Future growth will depend on whether emerging service
        sectors can expand fast enough to offset weakness in traditional sectors.
        """
    )