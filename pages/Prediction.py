"""
Prediction.py — Customer Satisfaction Intelligence & Analytics Platform
Prediction Center — frontend-only UI. No ML, prediction, or backend logic
is implemented here; all results are static, beautifully styled placeholders.

Uses the exact same design system (colors, type, cards, gradients,
navigation style) established in Home.py.
"""

import streamlit as st
from engines.prediction_engine import prediction_engine

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Prediction Center — Customer Satisfaction Intelligence",
    page_icon="◍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# ICONS — minimal inline stroke-SVGs (no external requests, no emoji)
# Same icon set as Home.py, extended with a few form-related glyphs.
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
    }
    p = paths.get(name, "")
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        f'stroke-linejoin="round" class="icn">{p}</svg>'
    )


# ----------------------------------------------------------------------
# GLOBAL STYLE — identical design system to Home.py
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
   ADDITIVE ONLY — Prediction Center form + result elements.
   These rules do not exist on Home.py; they reuse the exact
   same tokens (colors, radius, shadows, fonts) defined above
   so the page reads as the same product, not a new theme.
   ========================================================= */

/* form section panels: real Streamlit widgets grouped in a card-like frame */
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

/* widget labels */
div[data-testid="stWidgetLabel"] p{
  font-family:'Inter',sans-serif; font-size:0.82rem; font-weight:600;
  color:var(--ink-soft); letter-spacing:0.01em;
}

/* text / number inputs */
div[data-baseweb="input"] > div, div[data-baseweb="base-input"]{
  border-radius:10px !important; border:1px solid var(--line) !important;
  background:var(--surface) !important; box-shadow:none !important;
}
div[data-baseweb="input"] input{ color:var(--ink) !important; font-family:'Inter',sans-serif !important; }
div[data-baseweb="input"]:focus-within, div[data-baseweb="base-input"]:focus-within{
  border-color:var(--accent) !important; box-shadow:0 0 0 3px var(--accent-soft) !important;
}

/* select boxes */
div[data-baseweb="select"] > div{
  border-radius:10px !important; border:1px solid var(--line) !important;
  background:var(--surface) !important; box-shadow:none !important;
}
div[data-baseweb="select"]:focus-within > div{
  border-color:var(--accent) !important; box-shadow:0 0 0 3px var(--accent-soft) !important;
}

/* result / interpretation / recommendation panels */
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
# NAVIGATION HELPER — same pattern as Home.py
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
# SECTION 1 — PREDICTION CENTER HERO
# ----------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Prediction Center</div>
    <div class="hero-title">Predict <span class="grad">Customer Satisfaction</span><br>Before It's Reported</div>
    <div class="hero-desc">
      Enter the details of a customer interaction below to generate a
      satisfaction prediction. Fill in the customer, product, and service
      details, then run the model.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 2 — CUSTOMER DETAILS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">New Prediction</div>
    <div class="section-title">Interaction details</div>
    <div class="section-sub">The more complete the record, the more reliable the prediction.</div>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("user", 18)}</div>
        <div><h4>Customer Details</h4><span>Who the interaction was with</span></div></div>""",
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox(
            "Channel Name",
            [
                "Inbound",
                "Outcall",
                "Email"
                ],
                index=None,
                placeholder="Select Channel Name",
                key="channel_name"
                )
    with c2:
        st.selectbox(
            "Category",
            [
                "App/website",
                "Cancellation",
                "Feedback",
                "Offers & Cashback",
                "Onboarding related",
                "Order Related",
                "Others",
                "Payments related",
                "Product Queries",
                "Refund Related",
                "Returns",
                "Shopzilla Related",
            ],
            key="category",
        )
        with c3:
            st.text_input(
                "Customer City",
                placeholder="e.g. MUMBAI",
                key="customer_city"
                )

st.write("")

with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("box", 18)}</div>
        <div><h4>Product Details</h4><span>What the interaction was about</span></div></div>""",
        unsafe_allow_html=True,
    )
    p1, p2 = st.columns(2)
    with p1:
        st.selectbox(
            "Product Category",
            [
                "Affiliates",
                "Books & General merchandise",
                "Electronics",
                "Furniture",
                "GiftCard",
                "Home",
                "Home Appliences",
                "LifeStyle",
                "Mobile",
                "Unknown",
            ],
           index=None,
           placeholder="Select Product Category",
           key="product_category",
           )
    with p2:
        st.number_input(
            "Item Price",
            min_value=0.0,
            step=1.0,
            format="%.2f",
            key="item_price",
        )

st.write("")

with st.container(border=True):
    st.markdown(
        f"""<div class="panel-header"><div class="icon-box">{icon("users", 18)}</div>
        <div><h4>Service Details</h4><span>Who handled it, and how</span></div></div>""",
        unsafe_allow_html=True,
    )
    s1, s2 = st.columns(2)
    with s1:
        st.text_input(
            "Agent Name",
            placeholder="e.g. Wendy Taylor",
            key="agent_name"
            )
    with s2:
        st.empty()

    s4, s5, s6 = st.columns(3)
    with s4:
        st.selectbox(
            "Agent Shift",
            [
                "Afternoon",
                "Evening",
                "Morning",
                "Night",
                "Split",
            ],
            index=None,
            placeholder="Select Agent Shift",
            key="agent_shift",
)
    with s5:
        st.selectbox(
            "Tenure Bucket",
            [
                "0-30",
                "31-60",
                "61-90",
                ">90",
                "On Job Training",
            ],
            index=None,
            placeholder="Select Tenure Bucket",key="tenure_bucket",
        )
    with s6:
        st.number_input(
            "Connected Handling Time (min)",
            min_value=0.0,
            step=1.0,
            key="handling_time",
        )

    s7, _s8 = st.columns(2)
    with s7:
        st.selectbox(
            "Sub Category",
            [
                "Account updation",
                "Affiliate Offers",
                "App/website Related",
                "Billing Related",
                "COD Refund Details",
                "Call back request",
                "Call disconnected",
                "Card/EMI",
                "Commission related",
                "Customer Requested Modifications",
                "Damaged",
                "Delayed",
                "Exchange / Replacement",
                "Fraudulent User",
                "General Enquiry",
                "Installation/demo",
                "Instant discount",
                "Invoice request",
                "Issues with Shopzilla App",
                "Life Insurance",
                "Missing",
                "Non Order related",
                "Not Needed",
                "Online Payment Issues",
                "Order Verification",
                "Order status enquiry",
                "Other Account Related Issues",
                "Other Cashback",
                "Others",
                "PayLater related",
                "Payment pending",
                "Payment related Queries",
                "Priority delivery",
                "Product Specific Information",
                "Product related Issues",
                "Refund Enquiry",
                "Refund Related Issues",
                "Return cancellation",
                "Return request",
                "Reverse Pickup Enquiry",
                "Self-Help",
                "Seller Cancelled Order",
                "Seller onboarding",
                "Service Center - Service Denial",
                "Service Centres Related",
                "Shopzila Premium Related",
                "Shopzilla Rewards",
                "Signup Issues",
                "Technician Visit",
                "UnProfessional Behaviour",
                "Unable to Login",
                "Unable to track",
                "Wallet related",
                "Warranty related",
                "Wrong",
                "e-Gift Voucher",
            ],
            index=None,
            placeholder="Select Sub Category",
            key="sub_category",
        )

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 5 — RUN PREDICTION
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;text-align:center;">', unsafe_allow_html=True)
run_l, run_c, run_r = st.columns([1, 1, 1])
with run_c:
    st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
    run_clicked = st.button("Run Prediction", use_container_width=True, key="run_prediction")
    st.markdown("</div>", unsafe_allow_html=True)

if run_clicked:
    user_inputs = {
        "channel_name": st.session_state.channel_name,
        "category": st.session_state.category,
        "Sub-category": st.session_state.sub_category,
        "Customer_City": st.session_state.customer_city,
        "Product_category": st.session_state.product_category,
        "Item_price": st.session_state.item_price,
        "connected_handling_time": st.session_state.handling_time,
        "Agent_name": st.session_state.agent_name,
        "Tenure Bucket": st.session_state.tenure_bucket,
        "Agent Shift": st.session_state.agent_shift,
    }

    prediction_results = prediction_engine(user_inputs)

    st.session_state["prediction_results"] = prediction_results

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 6 — PREDICTION RESULTS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Output</div>
    <div class="section-title">Prediction results</div>
    <div class="section-sub">Real-time customer satisfaction predictions powered by the trained Random Forest model.</div>
    """,
    unsafe_allow_html=True,
)
prediction_results = st.session_state.get(
    "prediction_results",
    None
)

prediction = "Awaiting Prediction"
confidence = 0.0
risk_level = "Not Available"
confidence_display = "Not Generated"

if (
    prediction_results
    and prediction_results.get("status") == "SUCCESS"
):

    prediction = prediction_results.get(
        "prediction",
        prediction
    )

    confidence = prediction_results.get(
        "confidence_score",
        confidence
    )

    risk_level = prediction_results.get(
        "risk_level",
        risk_level
    )

    confidence_display = (
        f"{confidence:.2f}%"
    )
    confidence_display=f"{confidence:.2f}%"

else:
    prediction="Awaiting Prediction"
    confidence=0.0
    risk_level="Not Available"
    confidence_display="Not Generated"


risk_display_map={

    "HIGH":"High Risk",

    "MEDIUM":"Medium Risk",

    "LOW":"Low Risk",

    "Not Available":"Not Available"

}


risk_display=risk_display_map.get(

    risk_level,
    risk_level

)
cards = [
(
"gauge",
prediction,
"Customer Satisfaction",
"Predicted satisfaction level."
),
(
"star",
confidence_display,
"Confidence Score",
"Model confidence score."
),
(
"target",
risk_display,
"Risk Level",
"Business risk assessment."
)
]
cols = st.columns(3, gap="medium")
for i, (ic, value, label, note) in enumerate(cards):
    with cols[i]:
        st.markdown(
            f"""<div class="result-card"><div class="icon-box">{icon(ic, 20)}</div>
            <div class="result-value">{value}</div>
            <div class="result-label">{label}</div>
            <div class="result-note">{note}</div></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 7 — BUSINESS INTERPRETATION
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">In Plain Terms</div>
    <div class="section-title">Business interpretation</div>
    """,
    unsafe_allow_html=True,
)
interpretation_map = {
    "HIGH": "This customer interaction indicates a high risk of dissatisfaction. Immediate service recovery and escalation are recommended to improve customer experience and reduce churn.",
    "MEDIUM": "This interaction requires attention. The customer experience is acceptable but improvements in response quality and service handling may significantly increase satisfaction.",
    "LOW": "This customer interaction reflects a positive experience. Maintaining current service standards and proactive engagement is recommended.",
}
interpretation_text = interpretation_map.get(
    str(risk_level).upper(),
    "Once a prediction is generated, this section will explain what the score means for the business — in plain, non-technical language.",
)
st.markdown(
    f"""
    <div class="overview-panel">
      <p>{interpretation_text}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 8 — RECOMMENDATIONS
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Next Best Action</div>
    <div class="section-title">Recommendations</div>
    <div class="section-sub">Actionable steps will appear here once a prediction is run.</div>
    """,
    unsafe_allow_html=True,
)
if prediction_results:

    prediction_label = prediction_results.get(
        "prediction",
        "UNKNOWN"
    )

else:

    prediction_label = "UNKNOWN"


recommendations_map = {

    "Highly Unsatisfied":[

        ("compass",
         "Immediate Escalation",
         "Escalate this case immediately to senior customer support."),

        ("bulb",
         "Priority Resolution",
         "Resolve the customer's issue on priority to avoid churn."),

        ("award",
         "Retention Strategy",
         "Provide compensation or special assistance if necessary.")

    ],


    "Unsatisfied":[

        ("compass",
         "Improve Service Quality",
         "Review service handling practices for this interaction."),

        ("bulb",
         "Follow Up Quickly",
         "Perform a timely follow-up with the customer."),

        ("award",
         "Collect Feedback",
         "Gather additional feedback to improve satisfaction.")

    ],


    "Neutral":[

        ("compass",
         "Monitor Experience",
         "Monitor future customer interactions closely."),

        ("bulb",
         "Improve Engagement",
         "Provide proactive customer assistance."),

        ("award",
         "Increase Satisfaction",
         "Identify opportunities to improve service quality.")

    ],


    "Satisfied":[

        ("compass",
         "Maintain Standards",
         "Maintain good customer service standards."),

        ("bulb",
         "Improve Engagement",
         "Provide proactive customer support whenever possible."),

        ("award",
         "Build Loyalty",
         "Encourage repeat purchases and engagement.")

    ],


    "Highly Satisfied":[

        ("compass",
         "Reward Loyalty",
         "Offer exclusive loyalty benefits whenever appropriate."),

        ("bulb",
         "Promote Advocacy",
         "Encourage customers to share positive experiences."),

        ("award",
         "Maintain Excellence",
         "Continue delivering exceptional customer experiences.")

    ]

}


recs = recommendations_map.get(

    prediction_label,

    [

        ("compass","Recommendation 1","No recommendation available."),

        ("bulb","Recommendation 2","No recommendation available."),

        ("award","Recommendation 3","No recommendation available.")

    ]

)

cols = st.columns(3, gap="medium")
for i, (ic, title, desc) in enumerate(recs):
    with cols[i]:
        st.markdown(
            f"""<div class="card"><div class="icon-box">{icon(ic)}</div>
            <h4>{title}</h4><p>{desc}</p></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SECTION 9 — PREDICTION SUMMARY
# ----------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="eyebrow">Record</div>
    <div class="section-title">Prediction summary</div>
    <div class="section-sub">A structured recap of this prediction — inputs, score, and confidence — once generated.</div>
    """,
    unsafe_allow_html=True,
)
with st.container(border=True):
    channel_val = st.session_state.get("channel_name") or "—"
    category_val = st.session_state.get("category") or "—"
    product_category_val = st.session_state.get("product_category") or "—"
    CLASS_SCORE_MAPPING = {
        "Highly Unsatisfied": 1,
        "Unsatisfied": 2,
        "Neutral": 3,
        "Satisfied": 4,
        "Highly Satisfied": 5,
    }

    if (
        prediction_results
        and prediction_results.get("status") == "SUCCESS"
    ):

        satisfaction_level_val = prediction

        csat_score_val = CLASS_SCORE_MAPPING.get(
            prediction,
            "-"
        )

        confidence_val = f"{confidence:.2f}%"

    else:

        csat_score_val = "—"

        satisfaction_level_val = "—"

        confidence_val = "—"

    summary_rows = [

        ("Channel Name", channel_val),

        ("Category", category_val),

        ("Product Category", product_category_val),

        ("Predicted CSAT Score", csat_score_val),

        ("Satisfaction Level", satisfaction_level_val),

        ("Confidence Score", confidence_val),

        ("Risk Level", risk_display),

    ]
    rows_html = "".join(
        f'<div class="summary-row"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in summary_rows
    )
    st.markdown(f'<div style="padding:0.4rem 0.6rem;">{rows_html}</div>', unsafe_allow_html=True)

st.write("")
dl_l, dl_c, dl_r = st.columns([1,1,1])

recommendation_text = "\n\n".join(
    [
        f"{i+1}. {r[1]}\n{r[2]}"
        for i, r in enumerate(recs)
    ]
)

report = f"""
================================================

      CUSTOMER SATISFACTION REPORT

================================================

Prediction :
{prediction}

Predicted CSAT Score :
{csat_score_val}

Confidence Score :
{confidence_val}

Risk Level :
{risk_display}

Satisfaction Level :
{satisfaction_level_val}

Channel Name :
{channel_val}

Category :
{category_val}

Product Category :
{product_category_val}

Recommendations :

{recommendation_text}

================================================

THANK YOU FOR USING

CUSTOMER SATISFACTION
INTELLIGENCE PLATFORM

================================================
"""
if (
    prediction_results
    and prediction_results.get("status") == "SUCCESS"
):

    with dl_c:
        st.download_button(
            label="Download Prediction Report",
            data=report,
            file_name="prediction_report.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_report"
        )

else:

    with dl_c:
        st.info(
            "Run a prediction to download the report."
        )
st.markdown("</div>", unsafe_allow_html=True)