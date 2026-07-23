"""
Business_Insights.py — Customer Satisfaction Intelligence & Analytics Platform
Business Insights — frontend-only UI. No ML logic, analytics calculations,
backend logic, recommendation logic, prediction logic, graphs, or charts
are implemented here; every insight, recommendation, and indicator is a
static, styled placeholder.

Uses the exact same design system (colors, type, cards, gradients,
navigation style) established in Home.py, Prediction.py and Analytics.py.
"""

import streamlit as st
import pandas as pd

DATA_PATH="data/Customer_support_data.csv"

df=pd.read_csv(DATA_PATH)

df["CSAT Score"]=pd.to_numeric(
    df["CSAT Score"],
    errors="coerce"
)

df["connected_handling_time"]=pd.to_numeric(
    df["connected_handling_time"],
    errors="coerce"
)
# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Business Insights — Customer Satisfaction Intelligence",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — minimal inline stroke-SVGs (no external requests, no emoji)
# Same icon set as Home.py / Prediction.py / Analytics.py, extended with
# a couple of insight-specific glyphs.
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
        "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6l-7-3Z"/>',
        "alert": '<path d="M12 4 3 20h18L12 4Z"/><path d="M12 10v4"/><circle cx="12" cy="17" r="0.6" fill="currentColor"/>',
        "flag": '<path d="M6 21V4"/><path d="M6 4h12l-3 4 3 4H6"/>',
        "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Z"/><path d="M9 4v14M15 6v14"/>',
    }
    p = paths.get(name, "")
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        f'stroke-linejoin="round" class="icn">{p}</svg>'
    )


# ----------------------------------------------------------------------
# GLOBAL STYLE — identical design system to Home.py / Prediction.py / Analytics.py
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
   ADDITIVE ONLY — carried forward from Prediction.py /
   Analytics.py, reused unchanged so every page shares the
   same panel and result-card language. No existing rule
   is modified.
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
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# NAVIGATION HELPER — same pattern as previous pages
# ----------------------------------------------------------------------
def go_to(candidates):
    for path in candidates:
        try:
            st.switch_page(path)
            return
        except Exception:
            continue
    st.toast("This section isn't wired up yet — connect it in your app's pages/ folder.", icon="◍")


# ----------------------------------------------------------------------
# SECTION 1 — BUSINESS INSIGHTS HERO
# ----------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Business Insights</div>
    <div class="hero-title">From Customer Signal<br>to <span class="grad">Business Decisions</span></div>
    <div class="hero-desc">
      A curated view of what the platform's data means for the business —
      satisfaction insights, recommendations, risks, and the decisions
      they should inform.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — CUSTOMER SATISFACTION INSIGHTS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Understanding the Customer</div>
    <div class="section-title">Customer satisfaction insights</div>
    <div class="section-sub">What the data says about how customers are experiencing the business.</div>
    """,
    unsafe_allow_html=True,
)
highest_category = (
    df.groupby("category")["CSAT Score"]
    .mean()
    .idxmax()
)

lowest_category = (
    df.groupby("category")["CSAT Score"]
    .mean()
    .idxmin()
)

top_manager = (
    df.groupby("Manager")["CSAT Score"]
    .mean()
    .idxmax()
)

avg_handling_time = round(
    df["connected_handling_time"].mean(),
    2
)


csat_insights = [

    (
        "bulb",
        "Satisfaction Drivers",
        f"Highest satisfaction category : {highest_category}"
    ),

    (
        "message",
        "Customer Sentiment",
        f"Average handling time : {avg_handling_time} minutes"
    ),

    (
        "star",
        "Experience Highlights",
        f"Top performing manager : {top_manager}"
    ),

    (
        "alert",
        "Areas for Improvement",
        f"Lowest satisfaction category : {lowest_category}"
    ),

]
cols = st.columns(4, gap="medium")

for i, (ic, title, desc) in enumerate(csat_insights):

    with cols[i]:

        st.markdown(

            f"""
            <div class="card">
            <div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4>
            <p>{desc}</p>
            </div>
            """,

            unsafe_allow_html=True,

        )


st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 3 — BUSINESS RECOMMENDATIONS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Next Best Action</div>
    <div class="section-title">Business recommendations</div>
    <div class="section-sub">Actions the business can take based on the platform's findings.</div>
    """,
    unsafe_allow_html=True,
)
recommendations = [

    (
        "compass",
        "Prioritized Actions",
        "Improve low performing customer support categories."
    ),

    (
        "bolt",
        "Quick Wins",
        "Reduce customer handling time whenever possible."
    ),

    (
        "map",
        "Long-Term Initiatives",
        "Invest in service quality improvements and agent training."
    ),

]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(recommendations):
    with cols[i]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 4 — OPERATIONAL INSIGHTS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">How the Business Runs</div>
    <div class="section-title">Operational insights</div>
    <div class="section-sub">Where operations are helping or hurting the customer experience.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("cpu", 18)}</div>
        <div><h4>Operational Signals</h4><span>Service delivery patterns across the business</span></div></div>""",
        unsafe_allow_html=True,
    )
    ops = [

    (
        "radio",
        "Channel Efficiency",
        df["channel_name"].mode()[0]
    ),

    (
        "users",
        "Agent Workload",
        df["Agent_name"].nunique()
    ),

    (
        "clock",
        "Handling Time Patterns",
        f"{avg_handling_time} min"
    ),

    (
        "alert",
        "Service Bottlenecks",
        lowest_category
    ),

]
    cols = st.columns(4, gap="medium")
    for i, (ic, label, value) in enumerate(ops):
        with cols[i]:
            st.markdown(
                f"""<div class="result-card"><div class="icon-box">{icon(ic, 20)}</div>
                <div class="result-value">{value}</div>
                <div class="result-label">{label}</div></div>""",
                unsafe_allow_html=True,
            )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5 — STRATEGIC DECISION SUPPORT
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">For Leadership</div>
    <div class="section-title">Strategic decision support</div>
    <div class="section-sub">Higher-level context to inform business strategy.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="overview-panel">
      <p>This section will translate customer satisfaction data into strategic
      context — where to invest, where to hold steady, and where the
      business is exposed — once insights are connected.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")
strategy_cards = [
    ("dollar", "Investment Priorities", "Where investment would most improve satisfaction outcomes."),
    ("sliders", "Resource Allocation", "How staffing and resources could be better balanced."),
    ("trend", "Growth Opportunities", "Segments or channels with the greatest upside."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(strategy_cards):
    with cols[i]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — POTENTIAL RISK INDICATORS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Watch List</div>
    <div class="section-title">Potential risk indicators</div>
    <div class="section-sub">Early signals worth keeping an eye on.</div>
    """,
    unsafe_allow_html=True,
)
risks = [
    ("shield", "Satisfaction Decline Risk", "Flags a sustained drop in satisfaction scores."),
    ("flag", "Churn Risk Signals", "Flags interactions associated with customer attrition."),
    ("alert", "Service Escalation Risk", "Flags categories prone to repeated escalation."),
    ("gauge", "Operational Strain Risk", "Flags teams or channels showing signs of overload."),
]
cols = st.columns(4, gap="medium")
for i, (ic, title, desc) in enumerate(risks):
    with cols[i]:
        st.markdown(
            f"""<div class="insight-card"><div class="icon-box">{icon(ic)}</div>
            <div class="placeholder-value">—</div>
            <div class="label">{title}</div>
            <span class="status">{desc}</span></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — CUSTOMER EXPERIENCE SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">The Whole Picture</div>
    <div class="section-title">Customer experience summary</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="overview-panel">
      <p>A narrative summary of the customer experience — pulling together
      satisfaction, sentiment, and service quality into a single view —
      will appear here once the platform's insights are connected.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 8 — BUSINESS INSIGHTS SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Recap</div>
    <div class="section-title">Business insights summary</div>
    <div class="section-sub">A single-glance recap of everything on this page.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("clipboard", 18)}</div>
        <div><h4>Summary</h4><span>Populated once business insights are connected</span></div></div>""",
        unsafe_allow_html=True,
    )
    summary_rows = [

    (
        "Top Insight",
        highest_category
    ),

    (
        "Top Recommendation",
        "Improve service efficiency"
    ),

    (
        "Highest Risk Area",
        lowest_category
    ),

    (
        "Strategic Priority",
        "Customer Satisfaction"
    ),

    (
        "Overall Business Impact",
        "High"
    ),

    (
        "Data Last Updated",
        "Current Dataset"
    ),

]
    rows_html = "".join(
        f'<div class="summary-row"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in summary_rows
    )
    st.markdown(f'<div style="padding:0.4rem 0.6rem;">{rows_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
