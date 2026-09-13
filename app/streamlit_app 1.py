
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "customer_risk_analytics.csv"
CASES = ROOT / "data" / "raw" / "kyc_review_cases.csv"

st.set_page_config(page_title="Financial Crime Customer Risk & KYC/EDD Analytics", layout="wide")
st.title("Financial Crime Customer Risk & KYC/EDD Analytics")
st.caption("Synthetic portfolio project | SQL + Python + Tableau + Streamlit")

df = pd.read_csv(DATA)
cases = pd.read_csv(CASES)

with st.sidebar:
    st.header("Filters")
    risk_filter = st.multiselect("Risk level", sorted(df["risk_level"].unique()), default=sorted(df["risk_level"].unique()))
    type_filter = st.multiselect("Customer type", sorted(df["customer_type"].unique()), default=sorted(df["customer_type"].unique()))
    country_filter = st.multiselect("Country", sorted(df["country"].unique()), default=sorted(df["country"].unique()))

f = df[
    df["risk_level"].isin(risk_filter) &
    df["customer_type"].isin(type_filter) &
    df["country"].isin(country_filter)
]

k1,k2,k3,k4,k5,k6 = st.columns(6)
k1.metric("Customers", f"{len(f):,}")
k2.metric("High/Critical", f"{f['risk_level'].isin(['High','Critical']).sum():,}")
k3.metric("EDD Required", f"{f['edd_required'].sum():,}")
k4.metric("KYC Complete", f"{(f['kyc_complete_pct']==100).sum():,}")
k5.metric("PEP", f"{f['pep_flag'].sum():,}")
k6.metric("Sanctions Hits", f"{f['sanctions_hit'].sum():,}")

tabs = st.tabs(["Customer Risk Queue","Customer 360","KYC/EDD Cases","Portfolio Analytics","Tableau Gallery"])

with tabs[0]:
    st.subheader("Risk-Ranked Customer Queue")
    queue = f[["customer_id","customer_type","country","risk_score","risk_level","kyc_complete_pct",
               "edd_required","primary_risk_driver","customer_status"]].sort_values(
                   ["risk_score","kyc_complete_pct"], ascending=[False,True])
    st.dataframe(queue, use_container_width=True, hide_index=True)

with tabs[1]:
    st.subheader("Customer 360")
    cid = st.selectbox("Select customer", f.sort_values("risk_score",ascending=False)["customer_id"].tolist())
    row = f[f.customer_id==cid].iloc[0]
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Risk Score", int(row.risk_score))
    c2.metric("Risk Level", row.risk_level)
    c3.metric("KYC Complete", f"{row.kyc_complete_pct:.0f}%")
    c4.metric("EDD Required", "Yes" if row.edd_required else "No")
    st.write("**Primary risk driver:**", row.primary_risk_driver)
    st.write("**Customer status:**", row.customer_status)
    st.dataframe(pd.DataFrame({
        "Control":["ID verified","Address verified","Tax verified","UBO complete","Source of wealth verified",
                   "PEP","Sanctions hit","Adverse media"],
        "Value":[row.id_verified,row.address_verified,row.tax_verified,row.ubo_complete,row.source_of_wealth_verified,
                 row.pep_flag,row.sanctions_hit,row.adverse_media_flag]
    }), use_container_width=True, hide_index=True)

with tabs[2]:
    st.subheader("KYC / EDD Review Cases")
    st.dataframe(cases.sort_values(["risk_score","age_days"],ascending=[False,False]), use_container_width=True, hide_index=True)

with tabs[3]:
    st.subheader("Portfolio Analytics")
    c1,c2 = st.columns(2)
    with c1:
        st.bar_chart(f["risk_level"].value_counts())
    with c2:
        st.bar_chart(f[f.edd_required==1]["primary_risk_driver"].value_counts())

with tabs[4]:
    st.subheader("Tableau Analytics Gallery")
    st.image(str(ROOT/"images"/"01_kpi_scorecard.png"), caption="KPI Scorecard", use_container_width=True)
    st.image(str(ROOT/"images"/"02_executive_dashboard.png"), caption="Executive Dashboard", use_container_width=True)
    c1,c2=st.columns(2)
    with c1:
        st.image(str(ROOT/"images"/"03_risk_score_distribution.png"), caption="Risk Score Distribution", use_container_width=True)
    with c2:
        st.image(str(ROOT/"images"/"04_edd_drivers.png"), caption="EDD Drivers", use_container_width=True)
    c3,c4=st.columns(2)
    with c3:
        st.image(str(ROOT/"images"/"05_review_case_aging.png"), caption="Review Case Aging", use_container_width=True)
    with c4:
        st.image(str(ROOT/"images"/"06_top_high_risk_countries.png"), caption="High-Risk Countries", use_container_width=True)

st.caption("Synthetic educational portfolio project. No real customer or bank data.")
