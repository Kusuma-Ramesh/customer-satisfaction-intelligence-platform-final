"""
Developer_Hub.py — Customer Satisfaction Intelligence & Analytics Platform
Developer Hub — frontend-only UI. No backend logic, APIs, databases,
deployment logic or business logic is implemented here; every technical
detail is a static, styled placeholder.

Uses the exact same design system (colors, type, cards, gradients,
navigation style) established in Home.py, Prediction.py, Analytics.py,
Business_Insights.py and Model_Center.py.
"""

import streamlit as st

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Developer Hub — Customer Satisfaction Intelligence",
    page_icon="◍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — identical set
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

.badge{
  display:inline-flex; align-items:center; gap:8px; font-family:'IBM Plex Mono',monospace;
  font-size:0.82rem; font-weight:500; color:var(--ink-soft); background:var(--surface);
  border:1px solid var(--line); border-radius:999px; padding:0.5rem 1rem; margin:0 10px 10px 0;
}
.badge-dot{ width:6px; height:6px; border-radius:50%; background:var(--accent); }

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

.dev-card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:1.6rem 1.5rem; box-shadow:var(--shadow-sm); text-align:center;
}
.dev-card .avatar{
  width:64px; height:64px; margin:0 auto 14px auto; border-radius:50%;
  background:linear-gradient(135deg,var(--accent),var(--accent-2));
  display:flex; align-items:center; justify-content:center; color:#fff;
  font-family:'IBM Plex Mono',monospace; font-size:1.4rem; font-weight:600;
}
.dev-card h4{ font-size:1.1rem; font-weight:600; color:var(--ink); margin:0 0 4px 0; }
.dev-card .role{
  font-family:'IBM Plex Mono',monospace; font-size:0.72rem; letter-spacing:0.14em;
  text-transform:uppercase; color:var(--accent); margin-bottom:10px;
}
.dev-card p{ font-size:0.88rem; color:var(--ink-soft); margin:0 0 14px 0; line-height:1.55; }

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
        <div class="eyebrow">Developer Hub</div>
        <div class="hero-title">Built for<br><span class="grad">Developers &amp; Engineers</span></div>
        <div class="hero-tagline">The architecture, stack, and source behind the platform.</div>
        <div>
          <span class="badge"><span class="badge-dot"></span>Python</span>
          <span class="badge"><span class="badge-dot"></span>Streamlit</span>
          <span class="badge"><span class="badge-dot"></span>Scikit-Learn</span>
          <span class="badge"><span class="badge-dot"></span>GitHub</span>
          <span class="badge"><span class="badge-dot"></span>Streamlit Cloud</span>
        </div>
        <div class="hero-desc">
          Everything a developer needs to understand, extend, and deploy the
          Customer Satisfaction Intelligence &amp; Analytics Platform — the
          architecture, the pipeline, the stack and the source.
        </div>
        """,
        unsafe_allow_html=True,
    )
    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
        if st.button("View Model Center", use_container_width=True):
            go_to(["pages/4_Model_Center.py", "pages/Model_Center.py"])
        st.markdown("</div>", unsafe_allow_html=True)
    with b2:
        if st.button("Back to Home", use_container_width=True):
            go_to(["Home.py", "pages/0_Home.py"])
    with b3:
        if st.button("Business Insights", use_container_width=True):
            go_to(["pages/3_Insights.py", "pages/Business_Insights.py"])

with hero_r:
    st.markdown(
        """
        <svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="dhGrad" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#4338CA"/>
              <stop offset="100%" stop-color="#9B8CFB"/>
            </linearGradient>
          </defs>
          <rect x="60" y="60" width="200" height="140" rx="14" fill="none" stroke="#E9E8F2" stroke-width="2"/>
          <path d="M100 110 L80 130 L100 150" fill="none" stroke="url(#dhGrad)" stroke-width="3" stroke-linecap="round"/>
          <path d="M220 110 L240 130 L220 150" fill="none" stroke="url(#dhGrad)" stroke-width="3" stroke-linecap="round"/>
          <path d="M180 100 L140 160" stroke="url(#dhGrad)" stroke-width="3" stroke-linecap="round"/>
          <text x="160" y="230" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="2" fill="#9296A4">SOURCE READY</text>
        </svg>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — PROJECT ARCHITECTURE
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Architecture</div>
    <div class="section-title">Project architecture</div>
    <div class="section-sub">A modular, multi-page Streamlit application organized by responsibility.</div>
    """,
    unsafe_allow_html=True,
)
arch = [
    ("target", "Prediction Layer", "Interactive form that scores new customer records in real time."),
    ("chart", "Analytics Layer", "Breakdowns of performance across categories, channels and time."),
    ("bulb", "Insights Layer", "Business recommendations distilled from analytics output."),
    ("box", "Model Layer", "Trained pipeline, evaluation metrics and deployment metadata."),
    ("code", "Developer Layer", "Codebase, documentation and integration surface."),
    ("cloud", "Deployment Layer", "Public hosting through Streamlit Cloud."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(arch):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(arch) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 3 — DATASET OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Dataset</div>
    <div class="section-title">Dataset overview</div>
    <div class="section-sub">The customer experience dataset the model is trained on.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="summary-panel">
      <div class="summary-row"><span class="k">Domain</span><span class="v">Customer Experience</span></div>
      <div class="summary-row"><span class="k">Format</span><span class="v">Structured Tabular</span></div>
      <div class="summary-row"><span class="k">Input Features</span><span class="v">10</span></div>
      <div class="summary-row"><span class="k">Target</span><span class="v">Satisfaction Class</span></div>
      <div class="summary-row"><span class="k">Target Classes</span><span class="v">5</span></div>
      <div class="summary-row"><span class="k">Class Balancing</span><span class="v">SMOTE</span></div>
      <div class="summary-row"><span class="k">Preprocessing</span><span class="v">Automated</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 4 — ML PIPELINE OVERVIEW
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">ML Pipeline</div>
    <div class="section-title">ML pipeline overview</div>
    <div class="section-sub">A single repeatable path from raw data to a live prediction.</div>
    """,
    unsafe_allow_html=True,
)
pipeline = [
    ("01", "Dataset", "Structured customer records loaded from source."),
    ("02", "Preprocessing", "Cleaning, encoding and normalization."),
    ("03", "Feature Engineering", "Modeling features assembled from raw signals."),
    ("04", "SMOTE", "Balanced training set for fair class representation."),
    ("05", "Training", "Random Forest fit with tuned hyperparameters."),
    ("06", "Evaluation", "Cross validation and test-set metrics."),
    ("07", "Serialization", "Trained pipeline persisted through Joblib."),
    ("08", "Prediction", "Live inference served through Streamlit."),
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
# SECTION 5 — TECHNOLOGY STACK
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Stack</div>
    <div class="section-title">Technology stack</div>
    <div class="section-sub">The libraries and services that make the platform run.</div>
    """,
    unsafe_allow_html=True,
)
stack_groups = [
    ("Language", ["Python"]),
    ("Application", ["Streamlit"]),
    ("Data", ["Pandas", "NumPy"]),
    ("Machine Learning", ["Scikit-Learn", "Imbalanced-Learn", "Joblib"]),
    ("Visualization", ["Plotly"]),
    ("Source & Deploy", ["GitHub", "Streamlit Cloud"]),
]
for group, items in stack_groups:
    st.markdown(
        f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.72rem;'
        f'letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-faint);'
        f'margin:0 0 10px 2px;">{group}</div>',
        unsafe_allow_html=True,
    )
    badges_html = "".join(
        f'<span class="badge"><span class="badge-dot"></span>{it}</span>' for it in items
    )
    st.markdown(f'<div style="margin-bottom:1.2rem;">{badges_html}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — DEPLOYMENT INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Deployment</div>
    <div class="section-title">Deployment information</div>
    <div class="section-sub">How the platform reaches production.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="summary-panel">
      <div class="summary-row"><span class="k">Hosting</span><span class="v">Streamlit Cloud</span></div>
      <div class="summary-row"><span class="k">Access</span><span class="v">Public URL</span></div>
      <div class="summary-row"><span class="k">Source Control</span><span class="v">GitHub</span></div>
      <div class="summary-row"><span class="k">Runtime</span><span class="v">Python 3</span></div>
      <div class="summary-row"><span class="k">Model Artifact</span><span class="v">Joblib</span></div>
      <div class="summary-row"><span class="k">Cold Start</span><span class="v">Cached</span></div>
      <div class="summary-row"><span class="k">Status</span><span class="v">Deployment Ready</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — GITHUB INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">GitHub</div>
    <div class="section-title">GitHub information</div>
    <div class="section-sub">The full codebase is versioned and shipped through GitHub.</div>
    """,
    unsafe_allow_html=True,
)
github_cards = [
    ("github", "Repository", "Complete source of the platform lives on GitHub."),
    ("code", "Open Source Ready", "Structured to be readable, forkable and extendable."),
    ("layers", "Multi-Page Layout", "Each page of the app maps to a dedicated source file."),
    ("case", "Portfolio Ready", "Repository presented as a professional showcase project."),
]
cols = st.columns(4, gap="medium")
for i, (ic, title, desc) in enumerate(github_cards):
    with cols[i % 4]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 8 — PROJECT DOCUMENTATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Documentation</div>
    <div class="section-title">Project documentation</div>
    <div class="section-sub">Everything needed to understand and extend the platform.</div>
    """,
    unsafe_allow_html=True,
)
docs = [
    ("compass", "Product Overview", "Purpose, audience and scope of the platform."),
    ("tree", "Architecture Guide", "How the multi-page app and ML pipeline fit together."),
    ("sliders", "Model Card", "Algorithm, dataset, features and evaluation details."),
    ("chart", "Analytics Guide", "How performance is broken down across the business."),
    ("bulb", "Insights Guide", "How recommendations are surfaced from analytics."),
    ("cloud", "Deployment Guide", "Steps to run the project locally or on Streamlit Cloud."),
]
cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(docs):
    with cols[i % 3]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
    if i % 3 == 2 and i != len(docs) - 1:
        cols = st.columns(3, gap="medium")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 9 — DEVELOPER INFORMATION
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Developer</div>
    <div class="section-title">Developer information</div>
    <div class="section-sub">The person behind the platform.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="dev-card" style="max-width:520px;margin:0 auto;">
      <div class="avatar">◍</div>
      <h4>Project Developer</h4>
      <div class="role">Machine Learning &middot; Data Science</div>
      <p>Designed, trained and deployed the Customer Satisfaction Intelligence
      &amp; Analytics Platform end-to-end — from dataset preparation through
      to public deployment.</p>
      <div>
        <span class="badge"><span class="badge-dot"></span>Machine Learning</span>
        <span class="badge"><span class="badge-dot"></span>Business Analytics</span>
        <span class="badge"><span class="badge-dot"></span>Data Science</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 10 — PROJECT SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Summary</div>
    <div class="section-title">Project summary</div>
    <div class="section-sub">The platform at a glance for anyone reading the codebase.</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="summary-panel">
      <div class="summary-row"><span class="k">Project</span><span class="v">Customer Satisfaction Intelligence &amp; Analytics</span></div>
      <div class="summary-row"><span class="k">Type</span><span class="v">Machine Learning Web Application</span></div>
      <div class="summary-row"><span class="k">Language</span><span class="v">Python</span></div>
      <div class="summary-row"><span class="k">Framework</span><span class="v">Streamlit</span></div>
      <div class="summary-row"><span class="k">Model</span><span class="v">Random Forest Classifier</span></div>
      <div class="summary-row"><span class="k">Features</span><span class="v">10 Inputs / 5 Classes</span></div>
      <div class="summary-row"><span class="k">Balancing</span><span class="v">SMOTE</span></div>
      <div class="summary-row"><span class="k">Validation</span><span class="v">Cross Validation</span></div>
      <div class="summary-row"><span class="k">Cross Validation Accuracy</span><span class="v">74.15%</span></div>
      <div class="summary-row"><span class="k">Test Accuracy</span><span class="v">67.31%</span></div>
      <div class="summary-row"><span class="k">Source</span><span class="v">GitHub</span></div>
      <div class="summary-row"><span class="k">Deployment</span><span class="v">Streamlit Cloud</span></div>
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