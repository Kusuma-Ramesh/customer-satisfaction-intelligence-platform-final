"""
Model_Center.py — Customer Satisfaction Intelligence & Analytics Platform
Model Center — frontend-only UI. No ML logic, training, prediction,
deployment, backend logic, or graphs are implemented here; every
metric, pipeline step and indicator is a static, styled placeholder.

Uses the exact same design system (colors, type, cards, gradients,
navigation style) established in Home.py, Prediction.py, Analytics.py
and Business_Insights.py.
"""

import streamlit as st

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Model Center — Customer Satisfaction Intelligence",
    page_icon="◍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — minimal inline stroke-SVGs (no external requests, no emoji)
# Same icon set as Home.py / Prediction.py / Analytics.py / Business_Insights.py.
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
# GLOBAL STYLE — identical design system
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

div[data-testid="stButton"] > button{
  font-family:'Inter',sans-serif; font-weight:600; font-size:0.92rem;
  border-radius:11px; padding:0.62rem 1.15rem; border:1px solid var(--line);
  background:var(--surface); color:var(--ink); box-shadow:var(--shadow-sm);
  transition:transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
}
div[data-testid="stButton"] > button:hover{
  transform:translateY(-1px); box-shadow:var(--shadow-md); border-color:rgba(67,56,202,0.25);
}
.cta-primary button{
  background:linear-gradient(100deg,var(--accent),var(--accent-2)) !important;
  color:#fff !important; border:none !important;
}

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

.insight-card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.4rem; text-align:left; box-shadow:var(--shadow-sm); position:relative; overflow:hidden;
}
.insight-card .icon-box{ background:var(--positive-soft); color:var(--positive); width:42px; height:42px; border-radius:10px; display:flex; align-items:center; justify-content:center; margin-bottom:14px; }
.insight-card .placeholder-value{
  font-family:'IBM Plex Mono',monospace; font-size:1.6rem; font-weight:600; color:var(--ink-faint);
  margin:2px 0 4px 0; letter-spacing:0.01em;
}
.insight-card h4{ font-size:1rem; font-weight:600; color:var(--ink); margin:0 0 6px 0; letter-spacing:-0.01em; }
.insight-card p{ font-size:0.87rem; color:var(--ink-soft); margin:0; line-height:1.55; }
.insight-card .label{ font-size:0.83rem; color:var(--ink-soft); font-weight:500; }

.overview-panel{
  background:linear-gradient(180deg,rgba(67,56,202,0.04),rgba(109,93,246,0.02));
  border:1px solid var(--line); border-radius:20px; padding:3rem 3rem; text-align:center;
}
.overview-panel p{
  font-size:1.28rem; line-height:1.6; color:var(--ink); font-weight:500;
  max-width:820px; margin:0 auto; letter-spacing:-0.01em;
}

.badge{
  display:inline-flex; align-items:center; gap:8px; font-family:'IBM Plex Mono',monospace;
  font-size:0.82rem; font-weight:500; color:var(--ink-soft); background:var(--surface);
  border:1px solid var(--line); border-radius:999px; padding:0.5rem 1rem; margin:0 10px 10px 0;
}
.badge-dot{ width:6px; height:6px; border-radius:50%; background:var(--accent); }

/* pipeline step */
.pipe-step{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.2rem 1.2rem; height:100%; box-shadow:var(--shadow-sm); position:relative;
}
.pipe-step .num{
  font-family:'IBM Plex Mono',monospace; font-size:0.7rem; letter-spacing:0.14em;
  color:var(--accent); text-transform:uppercase; margin-bottom:8px;
}
.pipe-step h4{ font-size:0.98rem; font-weight:600; color:var(--ink); margin:0 0 4px 0; }
.pipe-step p{ font-size:0.85rem; color:var(--ink-soft); margin:0; line-height:1.55; }

/* summary row */
.summary-row{
  display:flex; justify-content:space-between; align-items:center;
  padding:0.95rem 1.3rem; border-bottom:1px solid var(--line);
}
.summary-row:last-child{ border-bottom:none; }
.summary-row .k{ font-size:0.9rem; color:var(--ink-soft); }
.summary-row .v{ font-family:'IBM Plex Mono',monospace; font-size:0.9rem; color:var(--ink); font-weight:600; }
.summary-panel{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  box-shadow:var(--shadow-sm); overflow:hidden;
}

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
# NAV HELPER
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
        <div class="eyebrow">Model Center</div>
        <div class="hero-title">Inside the <span class="grad">Machine Learning</span><br>engine</div>
        <div class="hero-tagline">The model, the pipeline, and everything behind every prediction.</div>
        <div>
          <span class="badge"><span class="badge-dot"></span>Random Forest</span>
          <span class="badge"><span class="badge-dot"></span>SMOTE Balanced</span>
          <span class="badge"><span class="badge-dot"></span>Cross Validated</span>
          <span class="badge"><span class="badge-dot"></span>Hyperparameter Tuned</span>
          <span class="badge"><span class="badge-dot"></span>Deployment Ready</span>
        </div>
        <div class="hero-desc">
          A transparent view into how the platform learns from customer data —
          from raw dataset, through feature engineering and training, all the
          way to production-ready predictions.
        </div>
        """,
        unsafe_allow_html=True,
    )
    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
        if st.button("Explore Prediction", use_container_width=True):
            go_to(["pages/1_Prediction.py", "pages/Prediction.py"])
        st.markdown("</div>", unsafe_allow_html=True)
    with b2:
        if st.button("Explore Analytics", use_container_width=True):
            go_to(["pages/2_Analytics.py", "pages/Analytics.py"])
    with b3:
        if st.button("Developer Hub", use_container_width=True):
            go_to(["pages/5_Developer_Hub.py", "pages/Developer_Hub.py"])

with hero_r:
    st.markdown(
        """
        <svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="mcGrad" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#4338CA"/>
              <stop offset="100%" stop-color="#9B8CFB"/>
            </linearGradient>
          </defs>
          <rect x="40" y="40" width="240" height="180" rx="18" fill="none" stroke="#E9E8F2" stroke-width="2"/>
          <path d="M160 60 L110 120 L160 120 L160 200" fill="none" stroke="url(#mcGrad)" stroke-width="3"/>
          <path d="M160 60 L210 120 L160 120" fill="none" stroke="url(#mcGrad)" stroke-width="3"/>
          <circle cx="160" cy="60" r="6" fill="#14161C"/>
          <circle cx="110" cy="120" r="6" fill="url(#mcGrad)"/>
          <circle cx="210" cy="120" r="6" fill="url(#mcGrad)"/>
          <circle cx="160" cy="200" r="6" fill="#14161C"/>
          <text x="160" y="240" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="2" fill="#9296A4">RANDOM FOREST</text>
        </svg>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — MODEL OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Model Overview</div>
    <div class="section-title">The model at a glance</div>
    <div class="section-sub">A concise look at the algorithm powering every prediction the platform makes.</div>
    """,
    unsafe_allow_html=True,
)
overview = [
    ("tree", "Random Forest Classifier", "Ensemble of decision trees producing robust, high-accuracy classifications."),
    ("scale", "Balanced Training", "SMOTE oversampling ensures minority satisfaction classes are represented fairly."),
    ("grid", "Cross Validated", "K-fold cross validation used to check the model generalizes beyond the training set."),
    ("sliders", "Hyperparameter Tuned", "Configuration was systematically searched to lock in the best performance."),
]
cols = st.columns(4, gap="medium")
for i, (ic, title, desc) in enumerate(overview):
    with cols[i % 4]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 3 — ML PIPELINE OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">ML Pipeline</div>
    <div class="section-title">From raw data to a prediction</div>
    <div class="section-sub">Every record flows through the same repeatable pipeline before a satisfaction score is produced.</div>
    """,
    unsafe_allow_html=True,
)
pipeline = [
    ("01", "Dataset Ingestion", "Raw customer interaction records are loaded from the source dataset."),
    ("02", "Preprocessing", "Missing values handled, types normalized, categorical variables encoded."),
    ("03", "Feature Engineering", "Behavioral signals and interaction attributes assembled into modeling features."),
    ("04", "SMOTE Balancing", "Minority satisfaction classes upsampled so the model sees a balanced training set."),
    ("05", "Model Training", "Random Forest trained across the balanced dataset with tuned hyperparameters."),
    ("06", "Evaluation", "Cross validation and test-set metrics confirm the model generalizes well."),
    ("07", "Prediction", "New customer records scored in real time through the trained pipeline."),
    ("08", "Deployment", "Pipeline packaged and served through Streamlit Cloud."),
]
cols = st.columns(4, gap="medium")
for i, (num, title, desc) in enumerate(pipeline):
    with cols[i % 4]:
        st.markdown(
            f"""<div class="pipe-step"><div class="num">Step {num}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 4 == 3 and i != len(pipeline) - 1:
        cols = st.columns(4, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 4 — DATASET INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Dataset</div>
    <div class="section-title">Dataset information</div>
    <div class="section-sub">The customer experience data the model learns from.</div>
    """,
    unsafe_allow_html=True,
)
dataset = [
    ("layers", "Customer Records", "The full population of customer interactions used across training and evaluation."),
    ("grid", "10  Input Features", "Behavioral, transactional and demographic attributes describing each record."),
    ("star", "5 Satisfaction Classes", "Ordinal target ranging across the full satisfaction spectrum."),
    ("scale", "Class Balanced", "SMOTE applied at training time so no class is starved of examples."),
    ("case", "Structured Source", "Cleaned tabular dataset — one row per customer interaction."),
    ("cloud", "Portable Format", "Loadable directly by the training and prediction pipelines."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(dataset):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(dataset) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5 — FEATURE INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Features</div>
    <div class="section-title">Feature information</div>
    <div class="section-sub">The ten inputs the model considers for every prediction.</div>
    """,
    unsafe_allow_html=True,
)
features=[

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
badges_html = "".join(f'<span class="badge"><span class="badge-dot"></span>{f}</span>' for f in features)
st.markdown(f'<div>{badges_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — MODEL PERFORMANCE OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Performance</div>
    <div class="section-title">Model performance overview</div>
    <div class="section-sub">Headline evaluation metrics captured during model validation.</div>
    """,
    unsafe_allow_html=True,
)
perf = [
    ("gauge", "74.15%", "Cross Validation Accuracy"),
    ("chart", "67.31%", "Test Accuracy"),
    ("target", "Balanced", "Class Distribution"),
    ("award", "Validated", "Generalization Check"),
    ("radio", "Stable", "Fold-to-Fold Variance"),
    ("bolt", "Real-Time", "Inference Latency"),
]
cols = st.columns(3, gap="medium")
for i, (ic, value, label) in enumerate(perf):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="insight-card"><div class="icon-box">{icon(ic)}</div>
            <div class="placeholder-value">{value}</div>
            <div class="label">{label}</div></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(perf) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — TRAINING SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Training</div>
    <div class="section-title">Training summary</div>
    <div class="section-sub">How the model was fit against the prepared dataset.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="summary-panel">
      <div class="summary-row"><span class="k">Algorithm</span><span class="v">Random Forest Classifier</span></div>
      <div class="summary-row"><span class="k">Class Balancing</span><span class="v">SMOTE</span></div>
      <div class="summary-row"><span class="k">Validation Strategy</span><span class="v">K-Fold Cross Validation</span></div>
      <div class="summary-row"><span class="k">Hyperparameter Search</span><span class="v">Enabled</span></div>
      <div class="summary-row"><span class="k">Feature Count</span><span class="v">10</span></div>
      <div class="summary-row"><span class="k">Target Classes</span><span class="v">5</span></div>
      <div class="summary-row"><span class="k">Training Status</span><span class="v">Completed</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 8 — PREDICTION PIPELINE SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Prediction Pipeline</div>
    <div class="section-title">How a new record is scored</div>
    <div class="section-sub">The path a single input takes at inference time.</div>
    """,
    unsafe_allow_html=True,
)
pred_pipeline = [
    ("01", "Input Capture", "New customer record collected from the Prediction Center."),
    ("02", "Preprocessing", "Same transformations used during training are re-applied."),
    ("03", "Feature Assembly","Ten modeling features constructed from the input."),
    ("04", "Model Inference", "Trained Random Forest scores the record in real time."),
    ("05", "Score Output", "Predicted satisfaction class returned to the interface."),
    ("06", "Insight Handoff", "Score feeds Analytics and Business Insights views."),
]
cols = st.columns(3, gap="medium")
for i, (num, title, desc) in enumerate(pred_pipeline):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="pipe-step"><div class="num">Step {num}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(pred_pipeline) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 9 — DEPLOYMENT INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Deployment</div>
    <div class="section-title">Deployment information</div>
    <div class="section-sub">How the trained model reaches production.</div>
    """,
    unsafe_allow_html=True,
)
deploy = [
    ("cloud", "Streamlit Cloud", "The application is designed to run publicly on Streamlit Cloud."),
    ("box", "Packaged Model", "Trained model serialized with Joblib for portable loading."),
    ("github", "Source Controlled", "Complete codebase versioned and shipped through GitHub."),
    ("cpu", "Real-Time Inference", "Predictions generated on demand as users interact with the app."),
    ("compass", "Public Access", "Reachable from anywhere once deployed to a public URL."),
    ("bolt", "Zero Cold Path", "Model and pipeline load once, then serve requests instantly."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(deploy):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(deploy) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 10 — MODEL SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="summary-panel">
      <div class="summary-row"><span class="k">Model</span><span class="v">Random Forest Classifier</span></div>
      <div class="summary-row"><span class="k">Task</span><span class="v">Customer Satisfaction Classification</span></div>
      <div class="summary-row"><span class="k">Input Features</span><span class="v">10</span></div>
      <div class="summary-row"><span class="k">Target Classes</span><span class="v">5</span></div>
      <div class="summary-row"><span class="k">Class Balancing</span><span class="v">SMOTE</span></div>
      <div class="summary-row"><span class="k">Validation</span><span class="v">Cross Validation</span></div>
      <div class="summary-row"><span class="k">Cross Validation Accuracy</span><span class="v">74.15%</span></div>
      <div class="summary-row"><span class="k">Test Accuracy</span><span class="v">67.31%</span></div>
      <div class="summary-row"><span class="k">Serialization</span><span class="v">Joblib</span></div>
      <div class="summary-row"><span class="k">Deployment Target</span><span class="v">Streamlit Cloud</span></div>
      <div class="summary-row"><span class="k">Status</span><span class="v">Deployment Ready</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# FOOTER
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