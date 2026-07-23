"""
Analytics.py — Customer Satisfaction Intelligence & Analytics Platform
Analytics Center — frontend-only UI. No charts, ML logic, backend logic,
analytics calculations, feature engineering, or prediction logic is
implemented here; every metric and chart area is a static, styled
placeholder.

Uses the exact same design system (colors, type, cards, gradients,
navigation style) established in Home.py and Prediction.py.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


DATA_PATH = "data/Customer_support_data.csv"

df = pd.read_csv(DATA_PATH)

# converting datatypes
df["CSAT Score"] = pd.to_numeric(
    df["CSAT Score"],
    errors="coerce"
)

df["connected_handling_time"] = pd.to_numeric(
    df["connected_handling_time"],
    errors="coerce"
)

df["Survey_response_Date"] = pd.to_datetime(
    df["Survey_response_Date"],
    errors="coerce"
)

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Analytics Center — Customer Satisfaction Intelligence",
    page_icon="◍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — minimal inline stroke-SVGs (no external requests, no emoji)
# Same icon set as Home.py / Prediction.py, extended with a couple of
# analytics-specific glyphs.
# ----------------------------------------------------------------------
def icon(name: str, size: int = 22) -> str:
    paths = {
        "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.6" fill="currentColor"/>',
        "chart": '<path d="M4 19V9"/><path d="M11 19V5"/><path d="M18 19v-7"/><path d="M3 19h18"/>',
        "bulb": '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.4 1 2.5h6c0-1.1.4-1.9 1-2.5A6 6 0 0 0 12 3Z"/>',
        "layers": '<path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="M3 13l9 5 9-5"/>',
        "compass": '<circle cx="12" cy="12" r="9"/><path d="m14.5 9.5-2 5-5 2 2-5 5-2Z"/>',
        "cloud": '<path d="M7 18a4.5 4.5 0 0 1-1-8.9A5.5 5.5 0 0 1 16.6 8 4 4 0 0 1 17 16H7Z"/>',
        "case": '<rect x="3" y="8" width="18" height="12" rx="1.5"/><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>',
        "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 8h1M14 8h1M9 12h1M14 12h1M9 16h1M14 16h1"/>',
        "tree": '<path d="M12 3v18"/><path d="M12 3 7 9h10L12 3Z"/><path d="M12 9 6 15h12L12 9Z"/>',
        "scale": '<path d="M12 3v18"/><path d="M5 8h4M15 8h4"/><path d="M3 8l2 5a2 2 0 0 0 4 0l-2-5"/><path d="M15 8l2 5a2 2 0 0 0 4 0l-2-5"/>',
        "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><path d="m5.5 5.5 2 2M17.5 5.5l-2 2M5.5 18.5l2-2M17.5 18.5l-2-2"/>',
        "sliders": '<path d="M4 6h9M17 6h3M4 18h3M11 18h9M4 12h13M20 12h0"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="18" r="2"/><circle cx="17" cy="12" r="2"/>',
        "cpu": '<rect x="7" y="7" width="10" height="10" rx="1"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M7.5 3v0M7 20v0"/>',
        "bolt": '<path d="M13 3 5 14h6l-1 7 8-11h-6l1-7Z"/>',
        "award": '<circle cx="12" cy="8" r="5"/><path d="m8.5 12.5-1.5 8 5-3 5 3-1.5-8"/>',
        "radio": '<circle cx="12" cy="12" r="2"/><path d="M8 8a5.5 5.5 0 0 0 0 8M16 8a5.5 5.5 0 0 1 0 8M5 5a10 10 0 0 0 0 14M19 5a10 10 0 0 1 0 14"/>',
        "star": '<path d="m12 3 2.6 5.9 6.4.6-4.8 4.3 1.4 6.3L12 17l-5.6 3.1 1.4-6.3L3 9.5l6.4-.6L12 3Z"/>',
        "gauge": '<path d="M4 15a8 8 0 1 1 16 0"/><path d="M12 15 15.5 9"/><circle cx="12" cy="15" r="1"/>',
        "message": '<path d="M4 5h16v11H8l-4 4V5Z"/>',
        "box": '<path d="M12 3 3 7.5 12 12l9-4.5L12 3Z"/><path d="M3 7.5V16l9 4.5 9-4.5V7.5"/><path d="M12 12v8.5"/>',
        "code": '<path d="m9 8-4 4 4 4"/><path d="m15 8 4 4-4 4"/>',
        "user": '<circle cx="12" cy="8" r="4"/><path d="M4 20c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
        "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c1-3.2 3.2-5 6-5s5 1.8 6 5"/><path d="M16 5.5a3 3 0 0 1 0 5.9"/><path d="M20 20c-.4-2-1.4-3.6-2.8-4.5"/>',
        "map-pin": '<path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z"/><circle cx="12" cy="10" r="2.4"/>',
        "tag": '<path d="M4 4h7l9 9-7 7-9-9V4Z"/><circle cx="8" cy="8" r="1.2" fill="currentColor" stroke="none"/>',
        "dollar": '<path d="M12 3v18"/><path d="M16.5 7.5c0-1.8-2-2.7-4.5-2.7S7.5 5.7 7.5 7.5s2 2.4 4.5 2.9 4.5 1.1 4.5 2.9-2 2.9-4.5 2.9-4.5-1-4.5-2.9"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
        "calendar": '<rect x="3.5" y="5" width="17" height="16" rx="1.5"/><path d="M8 3v4M16 3v4M3.5 10h17"/>',
        "clipboard": '<rect x="6" y="4" width="12" height="17" rx="1.5"/><rect x="9" y="2.5" width="6" height="3.5" rx="1"/>',
        "download": '<path d="M12 4v11"/><path d="m7.5 11 4.5 4.5 4.5-4.5"/><path d="M5 19.5h14"/>',
        "trend": '<path d="M4 17 10 11l4 4 6-8"/><path d="M14 7h6v6"/>',
        "table": '<rect x="3.5" y="4.5" width="17" height="15" rx="1.5"/><path d="M3.5 9.5h17M9 9.5V19.5"/>',
    }
    p = paths.get(name, "")
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        f'stroke-linejoin="round" class="icn">{p}</svg>'
    )


# ----------------------------------------------------------------------
# GLOBAL STYLE — identical design system to Home.py / Prediction.py
# ----------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root{
  --bg:#FAFAF8;
  --surface:#FFFFFF;
  --surface-2:rgba(255,255,255,0.6);
  --ink:#14161C;
  --ink-soft:#5B5F70;
  --ink-faint:#9296A4;
  --line:rgba(20,22,28,0.09);
  --accent:#4338CA;
  --accent-2:#6D5DF6;
  --accent-soft:rgba(67,56,202,0.08);
  --positive:#0F9D68;
  --positive-soft:rgba(15,157,104,0.09);
  --radius:16px;
  --shadow-sm:0 1px 2px rgba(20,22,28,0.04), 0 1px 1px rgba(20,22,28,0.03);
  --shadow-md:0 12px 32px -14px rgba(20,22,28,0.16);
}

html, body, [class*="css"]{ font-family:'Inter',-apple-system,sans-serif; }
.stApp{ background:var(--bg); }
#MainMenu, footer, header{ visibility:hidden; }
.block-container{ padding-top:2.2rem; padding-bottom:0; max-width:1180px; }
.icn{ display:block; }

/* ---------- shared type ---------- */
.eyebrow{
  font-family:'IBM Plex Mono',monospace; font-size:0.72rem; font-weight:500;
  letter-spacing:0.14em; text-transform:uppercase; color:var(--accent);
  display:flex; align-items:center; gap:8px; margin-bottom:14px;
}
.eyebrow::before{ content:""; width:14px; height:1px; background:var(--accent); display:inline-block; }
.section-title{ font-size:2rem; font-weight:700; letter-spacing:-0.02em; color:var(--ink); margin:0 0 10px 0; }
.section-sub{ font-size:1.02rem; color:var(--ink-soft); max-width:640px; margin:0 0 2.6rem 0; line-height:1.6; }
.section{ padding:4.4rem 0; }
.section + .section{ border-top:1px solid var(--line); }
.arc-divider{ width:100%; display:flex; justify-content:center; margin-bottom:0; opacity:0.5; }

/* ---------- hero ---------- */
.hero-wrap{ padding:1.5rem 0 3.4rem 0; }
.hero-title{
  font-size:3.4rem; line-height:1.06; font-weight:800; letter-spacing:-0.03em;
  color:var(--ink); margin:0 0 20px 0;
}
.hero-title .grad{
  background:linear-gradient(100deg,var(--accent) 0%,var(--accent-2) 60%,#9B8CFB 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.hero-tagline{ font-size:1.18rem; font-weight:500; color:var(--ink); margin:0 0 12px 0; }
.hero-desc{ font-size:1rem; color:var(--ink-soft); max-width:520px; line-height:1.65; margin:0 0 2.1rem 0; }

/* ---------- CTA buttons rendered by streamlit ---------- */
div[data-testid="stButton"] > button{
  font-family:'Inter',sans-serif; font-weight:600; font-size:0.92rem;
  border-radius:11px; padding:0.62rem 1.15rem; border:1px solid var(--line);
  background:var(--surface); color:var(--ink); box-shadow:var(--shadow-sm);
  transition:transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
}
div[data-testid="stButton"] > button:hover{
  transform:translateY(-1px); box-shadow:var(--shadow-md); border-color:rgba(67,56,202,0.25);
}
div[data-testid="stButton"] > button:focus:not(:active){
  outline:2px solid var(--accent); outline-offset:2px;
}
.cta-primary button{
  background:linear-gradient(100deg,var(--accent),var(--accent-2)) !important;
  color:#fff !important; border:none !important;
}

/* ---------- generic card ---------- */
.card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.5rem 1.4rem; height:100%; box-shadow:var(--shadow-sm);
  transition:transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
}
.card:hover{ transform:translateY(-3px); box-shadow:var(--shadow-md); border-color:rgba(67,56,202,0.18); }
.card .icon-box{
  width:42px; height:42px; border-radius:10px; background:var(--accent-soft);
  color:var(--accent); display:flex; align-items:center; justify-content:center; margin-bottom:14px;
}
.card h4{ font-size:1rem; font-weight:600; color:var(--ink); margin:0 0 6px 0; letter-spacing:-0.01em; }
.card p{ font-size:0.87rem; color:var(--ink-soft); margin:0; line-height:1.55; }

/* ---------- insight placeholder cards ---------- */
.insight-card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.4rem; text-align:left; box-shadow:var(--shadow-sm); position:relative; overflow:hidden;
}
.insight-card .icon-box{ background:var(--positive-soft); color:var(--positive); }
.insight-card .placeholder-value{
  font-family:'IBM Plex Mono',monospace; font-size:1.6rem; font-weight:600; color:var(--ink-faint);
  margin:2px 0 4px 0; letter-spacing:0.01em;
}
.insight-card .label{ font-size:0.83rem; color:var(--ink-soft); font-weight:500; }
.insight-card .status{
  font-family:'IBM Plex Mono',monospace; font-size:0.66rem; color:var(--ink-faint);
  letter-spacing:0.06em; text-transform:uppercase; margin-top:10px; display:block;
}

/* ---------- quick overview ---------- */
.overview-panel{
  background:linear-gradient(180deg,rgba(67,56,202,0.04),rgba(109,93,246,0.02));
  border:1px solid var(--line); border-radius:20px; padding:3rem 3rem; text-align:center;
}
.overview-panel p{
  font-size:1.28rem; line-height:1.6; color:var(--ink); font-weight:500;
  max-width:820px; margin:0 auto; letter-spacing:-0.01em;
}

/* ---------- tech / badges ---------- */
.badge{
  display:inline-flex; align-items:center; gap:8px; font-family:'IBM Plex Mono',monospace;
  font-size:0.82rem; font-weight:500; color:var(--ink-soft); background:var(--surface);
  border:1px solid var(--line); border-radius:999px; padding:0.5rem 1rem; margin:0 10px 10px 0;
}
.badge-dot{ width:6px; height:6px; border-radius:50%; background:var(--accent); }

/* ---------- explore nav cards ---------- */
.nav-card{
  display:block; background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.5rem; height:100%; box-shadow:var(--shadow-sm);
  transition:transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
}
.nav-card:hover{ transform:translateY(-3px); box-shadow:var(--shadow-md); border-color:rgba(67,56,202,0.2); }
.nav-card .row{ display:flex; align-items:center; justify-content:space-between; }
.nav-card .icon-box{ width:38px; height:38px; }
.nav-card h4{ margin-top:14px; }
.nav-card .arrow{ color:var(--ink-faint); font-size:1.1rem; transition:transform 160ms ease, color 160ms ease; }
.nav-card:hover .arrow{ transform:translateX(3px); color:var(--accent); }

/* ---------- footer ---------- */
.footer{ padding:3rem 0 3.2rem 0; }
.footer-badges{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:1.8rem; }
.footer-pill{
  font-family:'IBM Plex Mono',monospace; font-size:0.72rem; font-weight:600; letter-spacing:0.05em;
  text-transform:uppercase; color:var(--positive); background:var(--positive-soft);
  border-radius:999px; padding:0.4rem 0.85rem;
}
.built-with{ font-size:0.86rem; color:var(--ink-soft); }
.built-with b{ color:var(--ink); font-weight:600; }
.footer-brand{ font-size:0.86rem; color:var(--ink-faint); margin-top:1.4rem; }

@media (max-width: 900px){
  .hero-title{ font-size:2.3rem; }
  .overview-panel{ padding:2rem 1.4rem; }
}

/* =========================================================
   ADDITIVE ONLY — carried forward from Prediction.py, reused
   here unchanged so both pages share the exact same form/panel
   and result-card language. No existing rule is modified.
   ========================================================= */
div[data-testid="stVerticalBlockBorderWrapper"]{
  border-radius:var(--radius) !important;
  border:1px solid var(--line) !important;
  background:var(--surface) !important;
  box-shadow:var(--shadow-sm) !important;
}
.panel-header{ display:flex; align-items:center; gap:12px; margin:0 0 1.2rem 0; }
.panel-header .icon-box{
  width:38px; height:38px; border-radius:10px; background:var(--accent-soft);
  color:var(--accent); display:flex; align-items:center; justify-content:center; flex-shrink:0;
}
.panel-header h4{ font-size:1.02rem; font-weight:600; color:var(--ink); margin:0; letter-spacing:-0.01em; }
.panel-header span{ font-size:0.82rem; color:var(--ink-soft); }

.result-card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.6rem; text-align:center; box-shadow:var(--shadow-sm);
}
.result-card .icon-box{
  width:44px; height:44px; border-radius:12px; background:var(--accent-soft); color:var(--accent);
  display:flex; align-items:center; justify-content:center; margin:0 auto 14px auto;
}
.result-card .result-value{
  font-family:'IBM Plex Mono',monospace; font-size:1.5rem; font-weight:600;
  color:var(--ink-faint); margin:0 0 6px 0;
}
.result-card .result-label{ font-size:0.86rem; font-weight:600; color:var(--ink); margin-bottom:4px; }
.result-card .result-note{ font-size:0.78rem; color:var(--ink-soft); line-height:1.5; }

.summary-row{
  display:flex; justify-content:space-between; align-items:center;
  padding:0.85rem 0; border-bottom:1px solid var(--line);
}
.summary-row:last-child{ border-bottom:none; }
.summary-row .k{ font-size:0.86rem; color:var(--ink-soft); font-weight:500; }
.summary-row .v{ font-family:'IBM Plex Mono',monospace; font-size:0.86rem; color:var(--ink-faint); }

/* =========================================================
   ADDITIVE ONLY — new for Analytics.py: empty chart canvas.
   Built entirely from tokens already defined above.
   ========================================================= */
.chart-placeholder{
  background:var(--bg); border:1px solid var(--line); border-radius:var(--radius);
  min-height:230px; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:2.2rem; gap:6px;
}
.chart-placeholder .icon-box{
  width:48px; height:48px; border-radius:12px; background:var(--accent-soft); color:var(--accent);
  display:flex; align-items:center; justify-content:center; margin-bottom:8px;
}
.chart-placeholder h4{ font-size:0.98rem; font-weight:600; color:var(--ink); margin:0; }
.chart-placeholder p{ font-size:0.83rem; color:var(--ink-soft); max-width:440px; margin:0; line-height:1.55; }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# NAVIGATION HELPER — same pattern as Home.py / Prediction.py
# ----------------------------------------------------------------------
def go_to(candidates):
    for path in candidates:
        try:
            st.switch_page(path)
            return
        except Exception:
            continue
    st.toast("This section isn't wired up yet — connect it in your app's pages/ folder.", icon="✅")


def chart_placeholder(icon_name, title, note):
    st.markdown(
        f"""<div class="chart-placeholder"><div class="icon-box">{icon(icon_name, 22)}</div>
        <h4>{title}</h4><p>{note}</p></div>""",
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------
# SECTION 1 — ANALYTICS CENTER HERO
# ----------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Analytics Center</div>
    <div class="hero-title">Customer Experience,<br><span class="grad">Measured and Explained</span></div>
    <div class="hero-desc">
      A single place to read satisfaction distribution, feature drivers,
      category performance, and manager performance across the business.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — CSAT SCORE DISTRIBUTION
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Score Spread</div>
    <div class="section-title">CSAT score distribution</div>
    <div class="section-sub">How satisfaction scores are spread across all recorded interactions.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("chart", 18)}</div>
        <div><h4>Score Distribution</h4><span>Count of interactions per CSAT score</span></div></div>""",
        unsafe_allow_html=True,
    )


    fig = px.histogram(
        df,
        x="CSAT Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.markdown(
    """
    <div class="eyebrow">Model Drivers</div>
    <div class="section-title">Feature importance analysis</div>
    <div class="section-sub">Which inputs influence the model's predictions most.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):

    st.markdown(
        f"""
        <div class="panel-header">
        <div class="icon-box">{icon("sliders",18)}</div>
        <div>
        <h4>Feature Importance</h4>
        <span>Ranked by contribution to the prediction</span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    model = joblib.load(
    "models/customer_satisfaction_model_backup.pkl"
)
    feature_names = [

        "Channel Name",
        "Category",
        "Sub Category",
        "Customer City",
        "Product Category",
        "Item Price",
        "Handling Time",
        "Agent Name",
        "Tenure Bucket",
        "Agent Shift"

    ]

    importance_values = (

        model.feature_importances_

        if hasattr(
            model,
            "feature_importances_"
        )

        else [0]*10

    )


    importance_df = pd.DataFrame(

        {

            "Feature":feature_names,
            "Importance":importance_values

        }

    )


    importance_df = importance_df.sort_values(

        by="Importance",
        ascending=False

    )


    fig = px.bar(

        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"

    )


    st.plotly_chart(

        fig,
        use_container_width=True

    )


    chips_html = "".join(

        f'<span class="badge"><span class="badge-dot"></span>{f}</span>'

        for f in feature_names

    )


    st.markdown(

        f'<div style="margin-top:1.1rem;">{chips_html}</div>',

        unsafe_allow_html=True

    )


# ----------------------------------------------------------------------
# SECTION 4 — CATEGORY ANALYSIS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">By Category</div>
    <div class="section-title">Category analysis</div>
    <div class="section-sub">Satisfaction performance broken down by interaction category.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("tag", 18)}</div>
        <div><h4>Category Breakdown</h4><span>Average CSAT per category</span></div></div>""",
        unsafe_allow_html=True,
    )

    category_df = (
        df.groupby("category")["CSAT Score"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig = px.bar(
        category_df,
        x="category",
        y="CSAT Score",
        title="Average CSAT by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    cols = st.columns(5)

    for i, row in category_df.iterrows():
        with cols[i]:
            st.metric(
                row["category"],
                round(
                    row["CSAT Score"],
                    2
                )
            )

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5 — PRODUCT CATEGORY ANALYSIS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">By Product</div>
    <div class="section-title">Product category analysis</div>
    <div class="section-sub">Satisfaction performance broken down by product category.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):

    st.markdown(
        f"""<div class="panel-header">
        <div class="icon-box">{icon("box",18)}</div>
        <div>
        <h4>Product Breakdown</h4>
        <span>Average CSAT per product category</span>
        </div>
        </div>""",
        unsafe_allow_html=True,
    )

    product_df = (

        df.groupby("Product_category")["CSAT Score"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()

    )

    fig = px.bar(

        product_df,
        x="Product_category",
        y="CSAT Score",
        title="Average CSAT by Product Category"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    cols = st.columns(5)

    for i, row in product_df.iterrows():

        with cols[i]:

            st.metric(

                row["Product_category"],
                round(row["CSAT Score"],2)

            )

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — CUSTOMER SATISFACTION TRENDS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Over Time</div>
    <div class="section-title">Customer satisfaction trends</div>
    <div class="section-sub">How satisfaction has moved over the selected period.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):

    st.markdown(
        f"""
        <div class="panel-header">
        <div class="icon-box">{icon("trend",18)}</div>

        <div>
        <h4>Satisfaction Trend</h4>

        <span>
        CSAT Score over time
        </span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    trend_df = (

        df.groupby("Survey_response_Date")
        ["CSAT Score"]
        .mean()
        .reset_index()

    )

    fig = px.line(

        trend_df,
        x="Survey_response_Date",
        y="CSAT Score",
        title="Customer Satisfaction Trend"

    )

    st.plotly_chart(

        fig,
        use_container_width=True

    )

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — MANAGER PERFORMANCE ANALYSIS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">By Manager</div>
    <div class="section-title">Manager performance analysis</div>
    <div class="section-sub">How teams under each manager are performing on satisfaction.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("users", 18)}</div>
        <div><h4>Manager Leaderboard</h4><span>Ranked by team average CSAT</span></div></div>""",
        unsafe_allow_html=True,
    )
    manager_df = (

    df.groupby("Agent_name")
    .agg(
        {
            "CSAT Score":"mean",
            "connected_handling_time":"mean"
        }
    )
    .reset_index()

)

top_manager = (

    manager_df
    .sort_values(
        by="CSAT Score",
        ascending=False
    )
    .iloc[0]

)


fig = px.bar(

    manager_df.sort_values(
        by="CSAT Score",
        ascending=False
    ).head(10),

    x="Agent_name",
    y="CSAT Score",

    title="Top Performing Agents by Average CSAT"

)

st.plotly_chart(

    fig,
    use_container_width=True

)


manager_metrics=[

    (

        "award",
        "Top Performing Agent",
        str(
            top_manager["Agent_name"]
        )

    ),

    (

        "clock",
        "Avg. Handling Time",

        round(
            df["connected_handling_time"]
            .mean(),
            2
        )

    ),

    (

        "users",
        "Total Agents",

        df["Agent_name"]
        .nunique()

    ),

    (

        "gauge",
        "Overall Avg. CSAT",

        round(
            df["CSAT Score"]
            .mean(),
            2
        )

    ),

]


cols = st.columns(4,gap="medium")


for i,(ic,label,value) in enumerate(manager_metrics):

    with cols[i]:

        st.markdown(

            f"""
            <div class="result-card">

            <div class="icon-box">
            {icon(ic,20)}
            </div>

            <div class="result-value">
            {value}
            </div>

            <div class="result-label">
            {label}
            </div>

            </div>
            """,

            unsafe_allow_html=True

        )

# ----------------------------------------------------------------------
# SECTION 8 — ANALYTICS SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Recap</div>
    <div class="section-title">Analytics summary</div>
    <div class="section-sub">A single-glance recap of everything on this page.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("clipboard", 18)}</div>
        <div><h4>Summary</h4><span>Populated once analytics are connected</span></div></div>""",
        unsafe_allow_html=True,
    )
    summary_rows = [

    (
        "Total Interactions Analyzed",
        len(df)
    ),

    (
        "Overall Average CSAT",
        round(
            df["CSAT Score"].mean(),
            2
        )
    ),

    (
        "Top Performing Category",
        df.groupby("category")
        ["CSAT Score"]
        .mean()
        .idxmax()
    ),

    (
        "Top Performing Product Category",
        df.groupby("Product_category")
        ["CSAT Score"]
        .mean()
        .idxmax()
    ),

   (
    "Top Performing Agent",

    df.groupby("Agent_name")
    ["CSAT Score"]
    .mean()
    .idxmax()

),

    (
        "Data Last Updated",
        str(
            df["Survey_response_Date"]
            .max()
            .date()
        )
    ),

]
    rows_html = "".join(
        f'<div class="summary-row"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in summary_rows
    )
    st.markdown(f'<div style="padding:0.4rem 0.6rem;">{rows_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
