"""
Home.py — Customer Satisfaction Intelligence & Analytics Platform
Premium, SaaS-grade landing page for the platform's Streamlit app.

Drop this in as your app's entry point (or pages/0_Home.py in a
multipage app). It only renders the Home page — no architecture,
routing, or business-logic decisions are made here.
"""

import streamlit as st

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Customer Satisfaction Intelligence & Analytics Platform",
    page_icon="◍",

    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — minimal inline stroke-SVGs (no external requests, no emoji)
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
        "github": '<path d="M12 3a9 9 0 0 0-2.85 17.54c.45.08.6-.2.6-.43v-1.7c-2.45.53-2.97-1.13-2.97-1.13-.4-1.02-.98-1.29-.98-1.29-.8-.55.06-.54.06-.54.88.06 1.35.9 1.35.9.79 1.34 2.06.96 2.56.73.08-.57.31-.96.56-1.18-1.96-.22-4.02-.98-4.02-4.34 0-.96.34-1.74.9-2.36-.09-.22-.39-1.11.09-2.31 0 0 .74-.24 2.42.9a8.4 8.4 0 0 1 4.4 0c1.68-1.14 2.42-.9 2.42-.9.48 1.2.18 2.09.09 2.31.56.62.9 1.4.9 2.36 0 3.37-2.06 4.11-4.03 4.33.32.28.6.82.6 1.66v2.46c0 .24.15.51.61.43A9 9 0 0 0 12 3Z"/>',
    }
    p = paths.get(name, "")
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        f'stroke-linejoin="round" class="icn">{p}</svg>'
    )


# ----------------------------------------------------------------------
# GLOBAL STYLE
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
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# NAVIGATION HELPER
# Attempts to route to a companion page if it's registered in the app.
# This component only owns the Home page — target pages are wired by
# the app's own page architecture.
# ----------------------------------------------------------------------
def go_to(candidates):
    for path in candidates:
        try:
            st.switch_page(path)
            return
        except Exception:
            continue
    st.toast("This section isn't wired up yet — connect it in your app's pages/ folder.",icon="✅")


# ----------------------------------------------------------------------
# SECTION 1 — HERO
# ----------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
hero_l, hero_r = st.columns([1.15, 0.85], gap="large")

with hero_l:
    st.markdown(
        """
        <div class="eyebrow">Customer Intelligence Platform</div>
        <div class="hero-title">Customer Satisfaction<br><span class="grad">Intelligence &amp; Analytics</span></div>
        <div class="hero-tagline">Transforming Customer Experience Into Business Intelligence.</div>
        <div>
          <span class="badge"><span class="badge-dot"></span>ML Powered</span>
          <span class="badge"><span class="badge-dot"></span>Random Forest</span>
          <span class="badge"><span class="badge-dot"></span>SMOTE Enabled</span>
          <span class="badge"><span class="badge-dot"></span>Cross Validated</span>
          <span class="badge"><span class="badge-dot"></span>Deployment Ready</span>
        </div>
        <div class="hero-desc">
          A machine-learning platform that predicts satisfaction scores, surfaces
          business insights, and turns customer experience data into decisions
          your team can act on.
        </div>
        """,
        unsafe_allow_html=True,
    )
    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
        if st.button("Explore Prediction", use_container_width=True):
            go_to(["pages/Prediction.py"])
        st.markdown("</div>", unsafe_allow_html=True)
    with b2:
        if st.button("Explore Analytics", use_container_width=True):
            go_to(["pages/Analytics.py"])
    with b3:
        if st.button("Explore Insights", use_container_width=True):
            go_to(["pages/Business_Insights.py"])

with hero_r:
    st.markdown(
        """
        <svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="arcGrad" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#4338CA"/>
              <stop offset="100%" stop-color="#9B8CFB"/>
            </linearGradient>
          </defs>
          <path d="M40 190 A120 120 0 0 1 280 190" fill="none" stroke="#E9E8F2" stroke-width="14" stroke-linecap="round"/>
          <path d="M40 190 A120 120 0 0 1 225 76" fill="none" stroke="url(#arcGrad)" stroke-width="14" stroke-linecap="round"/>
          <circle cx="160" cy="190" r="4" fill="#14161C"/>
          <line x1="160" y1="190" x2="215" y2="95" stroke="#14161C" stroke-width="3" stroke-linecap="round"/>
          <text x="160" y="150" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="34" font-weight="600" fill="#14161C">CSAT</text>
          <text x="160" y="176" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="2" fill="#9296A4">LIVE SIGNAL</text>
        </svg>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — PLATFORM FEATURES
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Platform</div>
    <div class="section-title">Everything the experience runs on</div>
    <div class="section-sub">Eight capabilities working together, from raw customer signal to a recommendation your team can execute on.</div>
    """,
    unsafe_allow_html=True,
)

features = [
    ("target", "Customer Satisfaction Prediction", "Predicts satisfaction outcomes from customer and interaction data using a trained ML model."),
    ("chart", "Business Analytics", "Breaks down performance across categories, channels, and time to reveal what's driving experience."),
    ("bulb", "Customer Insights", "Surfaces the patterns and drivers behind satisfaction, not just the score itself."),
    ("layers", "Interactive Visualizations", "Explore the data directly through responsive, drill-down charts and views."),
    ("compass", "Business Recommendations", "Translates analytics into concrete, prioritized actions for the business."),
    ("cloud", "Public Deployment", "Built to run in production on Streamlit Cloud — accessible from anywhere."),
    ("case", "Portfolio Ready", "Structured and styled to stand on its own in a professional portfolio."),
    ("building", "Industry Ready", "Modeled on real business analytics workflows, not a classroom exercise."),
]
cols = st.columns(4, gap="medium")
for i, (ic, title, desc) in enumerate(features):
    with cols[i % 4]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 4 == 3 and i != len(features) - 1:
        cols = st.columns(4, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 3 — QUICK OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="overview-panel">
      <p>The platform predicts customer satisfaction scores, generates business
      insights, visualizes customer experience analytics and supports
      data-driven business decisions using Machine Learning and Business
      Analytics.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 4 — MODEL HIGHLIGHTS
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Under the Hood</div>
    <div class="section-title">Model highlights</div>
    <div class="section-sub">The modeling approach behind every prediction the platform makes.</div>
    """,
    unsafe_allow_html=True,
)
models = [
    ("tree", "Random Forest", "Ensemble of decision trees for robust, high-accuracy classification."),
    ("scale", "SMOTE", "Balances the training set so minority satisfaction classes are represented fairly."),
    ("grid", "Cross Validation", "Validates performance across multiple folds to avoid overfitting."),
    ("sliders", "Hyperparameter Tuning", "Systematically searched to get the best-performing model configuration."),
    ("cpu", "Machine Learning Powered", "Every prediction is generated by a trained, evaluated ML pipeline."),
    ("bolt", "Real-Time Predictions", "Scores are generated on demand as new inputs come in."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(models):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(models) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5 — QUICK INSIGHTS (placeholders only, no fabricated values)
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">At a Glance</div>
    <div class="section-title">Quick insights</div>
    <div class="section-sub">Populated automatically once the platform is connected to live data.</div>
    """,
    unsafe_allow_html=True,
)
insights = [
    ("award", "Live Business Insights", "Available after dataset integration."),
    ("radio", "Real-Time Analytics", "Generated after prediction execution."),
    ("star", "Customer Intelligence", "Business patterns will be displayed here."),
    ("gauge", "Deployment Ready", "Ready for analytics integration."),
]
cols = st.columns(4, gap="medium")
for i, (ic, title, desc) in enumerate(insights):
    with cols[i]:
        st.markdown(
            f"""<div class="insight-card card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4>
            <p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5B — PROJECT SNAPSHOT
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">By the Numbers</div>
    <div class="section-title">Project snapshot</div>
    <div class="section-sub">Where the model stands today.</div>
    """,
    unsafe_allow_html=True,
)
snapshot = [
    ("grid", "10", "Input Features"),
    ("layers", "5", "Satisfaction Classes"),
    ("gauge", "74.15%", "Cross Validation Accuracy"),
    ("chart", "67.31%", "Test Accuracy"),
    ("tree", "Random Forest", "ML Model"),
    ("cloud", "Deployment Ready", "Public Cloud Support"),
]
cols = st.columns(3, gap="medium")
for i, (ic, value, label) in enumerate(snapshot):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="insight-card"><div class="icon-box">{icon(ic)}</div>
            <div class="placeholder-value">{value}</div>
            <div class="label">{label}</div></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(snapshot) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5C — PROJECT WORKFLOW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Pipeline</div>
    <div class="section-title">Project workflow</div>
    <div class="section-sub">How a record moves from raw data to a business decision.</div>
    """,
    unsafe_allow_html=True,
)
workflow_steps = [
    "Dataset", "Preprocessing", "Feature Engineering", "SMOTE",
    "Random Forest", "Prediction", "Analytics", "Business Insights", "Deployment",
]
workflow_html = f'<span style="color:var(--ink-faint);margin:0 4px 10px 0;">&#8594;</span>'.join(
    f'<span class="badge"><span class="badge-dot"></span>{step}</span>' for step in workflow_steps
)
st.markdown(f'<div style="display:flex;flex-wrap:wrap;align-items:center;">{workflow_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — TECH STACK
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Built With</div>
    <div class="section-title">Tech stack</div>
    """,
    unsafe_allow_html=True,
)
stack = ["Python", "Streamlit", "Pandas", "NumPy", "Scikit-Learn", "Plotly", "Joblib", "GitHub", "Streamlit Cloud"]
badges_html = "".join(f'<span class="badge"><span class="badge-dot"></span>{s}</span>' for s in stack)
st.markdown(f'<div>{badges_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — EXPLORE THE PLATFORM
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Navigate</div>
    <div class="section-title">Explore the platform</div>
    <div class="section-sub">Jump straight into any part of the experience.</div>
    """,
    unsafe_allow_html=True,
)
nav_items = [
("target","Prediction",
"Score new customer records in real time.",
["pages/Prediction.py"]),

("chart","Analytics",
"Explore performance across categories and channels.",
["pages/Analytics.py"]),

("message","Business Insights",
"See the drivers behind customer satisfaction.",
["pages/Business_Insights.py"]),

("box","Model Center",
"Inspect model performance and configuration.",
["pages/Model_Center.py"]),

("code","Developer Hub",
"Docs, source and integration details.",
["pages/Developer_Hub.py"])
]
cols = st.columns(5, gap="medium")
for i, (ic, title, desc, targets) in enumerate(nav_items):
    with cols[i]:
        st.markdown(
            f"""<div class="nav-card"><div class="row">
            <div class="icon-box">{icon(ic, 20)}</div><span class="arrow">&#8594;</span></div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
        if st.button(f"Launch {title}", key=f"nav_{title}", use_container_width=True):
            go_to(targets)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 8 — FOOTER
# ----------------------------------------------------------------------
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="footer-badges">
      <span class="footer-pill">Portfolio Ready</span>
      <span class="footer-pill">Industry Ready</span>
      <span class="footer-pill">GitHub Ready</span>
      <span class="footer-pill">Public Deployment Ready</span>
      <span class="footer-pill">Streamlit Cloud Ready</span>
    </div>
    <div class="built-with">
      Built with <b>Machine Learning</b>, <b>Business Analytics</b>,
      <b>Customer Analytics</b> and <b>Data Science</b>.
    </div>
    <div class="footer-brand">Customer Satisfaction Intelligence &amp; Analytics Platform</div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
