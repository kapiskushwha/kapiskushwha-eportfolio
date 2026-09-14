import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Kapis Kushwha | Equity Research Portfolio", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

REPO = "https://github.com/kapiskushwha/kapiskushwha-eportfolio"
LOVABLE = "https://kapiskushwha.lovable.app/"
EMAIL = "mailto:motilalkushwaha125@gmail.com"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.block-container { max-width: 1180px; padding-top: 2rem; padding-bottom: 4rem; }
.hero { padding: 3.5rem 0 2.5rem 0; }
.kicker { letter-spacing: .16em; text-transform: uppercase; font-size: .78rem; font-weight: 700; opacity: .68; }
h1, h2, h3 { font-family: 'DM Serif Display', serif !important; }
h1 { font-size: clamp(2.8rem, 6vw, 5.6rem) !important; line-height: .98 !important; margin: .45rem 0 1rem !important; }
h2 { font-size: 2.1rem !important; margin-top: 2.8rem !important; }
h3 { font-size: 1.35rem !important; }
.lead { font-size: 1.08rem; line-height: 1.75; max-width: 780px; opacity: .88; }
.badge { display:inline-block; padding:.42rem .72rem; border:1px solid rgba(127,127,127,.35); border-radius:999px; margin:.2rem .25rem .2rem 0; font-size:.82rem; }
.card { border:1px solid rgba(127,127,127,.25); border-radius:18px; padding:1.25rem; height:100%; background:rgba(127,127,127,.035); }
.metric { font-size:1.9rem; font-weight:700; margin-bottom:.1rem; }
.muted { opacity:.68; font-size:.9rem; }
.timeline { border-left:2px solid rgba(127,127,127,.3); padding-left:1.2rem; margin-left:.35rem; }
.smallcaps { text-transform:uppercase; letter-spacing:.12em; font-size:.72rem; font-weight:700; opacity:.65; }
footer { opacity:.55; padding-top:3rem; font-size:.82rem; }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("<div class='kicker'>KAPIS KUSHWHA · FINANCE · EQUITY RESEARCH</div>", unsafe_allow_html=True)
nav = st.columns(6)
for col, label, anchor in zip(nav, ["About", "Projects", "Experience", "Toolkit", "Education", "Contact"], ["about","projects","experience","toolkit","education","contact"]):
    with col:
        st.markdown(f"[{label}](#{anchor})")

# Hero
st.markdown("<div class='hero'>", unsafe_allow_html=True)
c1, c2 = st.columns([2.1, 1], vertical_alignment="center")
with c1:
    st.markdown("<div class='kicker'>EQUITY RESEARCH ANALYST-IN-TRAINING</div>", unsafe_allow_html=True)
    st.title("I turn financial statements into investment calls.")
    st.markdown("<p class='lead'>PGDM (Financial Management) student at FIIB Delhi with hands-on equity research experience at CSA Advisors. Built valuation models across 9 listed companies and developed AI-assisted research workflows designed to reduce research turnaround while keeping the analytical process evidence-led.</p>", unsafe_allow_html=True)
    st.markdown("**Target role:** Equity Research Analyst  ·  **Location:** Delhi NCR, India")
    st.link_button("View GitHub Repository", REPO)
    st.link_button("Existing Lovable Portfolio", LOVABLE)
with c2:
    img = Path("assets/profile.png")
    if img.exists(): st.image(str(img), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

m = st.columns(4)
for col, value, label in zip(m, ["9", "4", "10+", "70%"], ["Company valuation models", "Valuation frameworks used", "Small-cap funds analysed", "Research turnaround improvement"]):
    with col:
        st.markdown(f"<div class='card'><div class='metric'>{value}</div><div class='muted'>{label}</div></div>", unsafe_allow_html=True)

# About
st.markdown("<a id='about'></a>", unsafe_allow_html=True)
st.header("About")
st.markdown("""
I am pursuing a **PGDM in Financial Management at the Fortune Institute of International Business (FIIB), Delhi**, and building toward a career in equity research and investment analysis.

During my **Equity Research Analyst internship at CSA Advisors, Gurugram**, I worked on end-to-end company valuation, sector research, mutual fund holdings analysis and market-event research. My valuation work covered DCF, Gordon Growth, relative valuation, forecasting, scenario analysis, WACC and beta estimation. I also worked on a metal-sector deep dive and analysed overlapping holdings across leading small-cap mutual funds.

Earlier, as an **Account Trainee at AKKCO Chartered Accountants**, I worked on GST and income-tax returns, TDS, bookkeeping, audit support and compliance work. This combination of accounting foundations and investment analysis shapes how I approach financial research: start with the numbers, make the assumptions explicit, and connect the model to an investable conclusion.
""")

# Projects
st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
st.header("Selected Projects")
projects = [
("01", "Multi-Company Valuation Suite", "Built end-to-end valuation models across 9 listed companies using DCF, Gordon Growth and relative valuation, with supporting forecasting, WACC/beta and scenario analysis.", ["Maruti Suzuki", "HDFC Bank", "Solar Industries", "Ambuja Cements", "DLF", "Exide", "LTIMindtree", "NMDC", "DMart"], "Primary evidence: nine Excel valuation workbooks"),
("02", "Sectoral Analysis · Metal Industry Deep-Dive", "Analysed the Nifty Metal universe through valuation, stock-price, return, FII/DII and sector-outlook lenses, alongside peer benchmarking and event analysis.", ["Nifty Metal Dashboard", "Valuation Scorecard", "Return Analysis", "FII/DII", "Sector Outlook"], "Primary evidence: NiftyMetalAnalysis_Corrected.xlsx"),
("03", "Mutual Fund Holdings & Risk-Return Analysis", "Consolidated holdings across major small-cap fund houses to study overlap, concentration, sector tilt and risk-adjusted performance.", ["Holdings overlap", "Sharpe ratio", "Sortino ratio", "Drawdown", "Concentration"], "Primary evidence: SMALL_CAP_MUTUAL_FUNDS (1).xlsx"),
("04", "AI-Assisted Research Workflow", "Developed an AI-assisted research workflow concept around rule-based financial red-flag screening and research-memo generation, using Python/Streamlit and research tools.", ["Python", "Pandas", "Streamlit", "Rule-based screening", "Investment memo workflow"], "Portfolio description based on the supplied professional portfolio materials"),
]
for num, title, desc, tags, evidence in projects:
    with st.container(border=True):
        a,b = st.columns([.08,.92])
        with a: st.markdown(f"### {num}")
        with b:
            st.subheader(title)
            st.write(desc)
            st.markdown(" ".join([f"<span class='badge'>{x}</span>" for x in tags]), unsafe_allow_html=True)
            st.caption(evidence)

st.subheader("Valuation Evidence Library")
files = [
("Maruti Suzuki", "maruti_public_final_filled.xlsx"), ("HDFC Bank", "info edge final.xlsx"), ("Solar Industries", "L_T_Forecasting_v3_public (1).xlsx"),
("Ambuja Cements", "Ambuja_GGM_filled.xlsx"), ("DLF", "DLF_Equity_Research.xlsx"), ("Exide Industries", "exide_quarterly_filled (1).xlsx"),
("LTIMindtree", "ltim_final_1.xlsx"), ("NMDC", "nmdc_valuation_formatted (1).xlsx"), ("DMart", "dmart_final (1).xlsx"),
]
cols = st.columns(3)
for i,(name,fname) in enumerate(files):
    url = f"{REPO}/blob/main/{fname.replace(' ','%20')}"
    with cols[i%3]:
        st.link_button(f"{name} valuation workbook", url, use_container_width=True)

metal_url=f"{REPO}/blob/main/NiftyMetalAnalysis_Corrected.xlsx"
fund_url=f"{REPO}/blob/main/SMALL_CAP_MUTUAL_FUNDS%20(1).xlsx"
st.link_button("Open Nifty Metal analysis workbook", metal_url)
st.link_button("Open Small-Cap Mutual Fund analysis", fund_url)

# Experience
st.markdown("<a id='experience'></a>", unsafe_allow_html=True)
st.header("Experience")
exp = [
("Apr 2026 – Jun 2026", "Equity Research Analyst Intern", "CSA Advisors · Gurugram", "Built 9 end-to-end company valuation models; contributed to metal-sector analysis, small-cap mutual-fund overlap analysis, MSCI index-event research and AI-assisted research workflows."),
("May 2024 – Dec 2024", "Account Trainee", "AKKCO Chartered Accountants · Delhi", "Worked on GST and income-tax returns, TDS, bookkeeping, audit support and compliance activities across multiple clients."),
("Jan 2026", "Social Internship Program", "GiftAbled Foundation", "Supported data validation and impact assessment for employability profiles of persons with disabilities."),
("Aug 2022 – Oct 2022", "Marketing Intern", "UAS International", "Supported social-media and outreach activities across travel, career and wealth-service offerings."),
]
for date, role, org, desc in exp:
    st.markdown(f"<div class='timeline'><div class='smallcaps'>{date}</div><h3>{role}</h3><b>{org}</b><p>{desc}</p></div>", unsafe_allow_html=True)

# Toolkit
st.markdown("<a id='toolkit'></a>", unsafe_allow_html=True)
st.header("Toolkit")
left,right = st.columns(2)
with left:
    st.markdown("### Valuation & Modelling")
    st.write("DCF · Relative Valuation · Gordon Growth · LBO · M&A Modelling · Scenario Analysis · WACC · Beta Estimation · Ratio Analysis")
    st.markdown("### Research")
    st.write("Equity Research · Sectoral Analysis · Mutual Fund Analysis · Due Diligence · Investment Memo Writing")
with right:
    st.markdown("### Tools")
    st.write("Advanced Excel · Python · Pandas · Streamlit · Power BI · NotebookLM · Tally Prime · CompuTax")
    st.markdown("### Certifications & Coursework")
    st.write("CFA Level I Candidate · Financial Econometrics (VAR-GARCH) · Financial Modelling (NPTEL) · Henry Harvin Tax Practitioner · Certified Tally Accountant")

# Education
st.markdown("<a id='education'></a>", unsafe_allow_html=True)
st.header("Education")
e1,e2=st.columns(2)
with e1:
    st.markdown("### PGDM · Financial Management")
    st.write("Fortune Institute of International Business (FIIB), Delhi")
    st.caption("2025 – 2027 · Term IV")
with e2:
    st.markdown("### B.Com (Hons.)")
    st.write("GGSIPU · KIHEAT")
    st.caption("2021 – 2024")

# Resume/contact
st.markdown("<a id='contact'></a>", unsafe_allow_html=True)
st.header("Contact")
c1,c2=st.columns([1,1])
with c1:
    st.markdown("### Kapis Kushwha")
    st.write("Equity Research Analyst-in-Training · Delhi NCR, India")
    st.link_button("Email Kapis", EMAIL)
    st.link_button("GitHub", REPO)
    st.link_button("Lovable Portfolio", LOVABLE)
with c2:
    resume=Path("assets/resume.pdf")
    if resume.exists():
        st.download_button("Download Resume", data=resume.read_bytes(), file_name="Kapis_Kushwha_Resume.pdf", mime="application/pdf")

st.markdown("""
<footer>
Built as a professional e-portfolio microsite for academic and recruiter review. Project evidence and factual claims are based on the materials supplied for this portfolio.
</footer>
""", unsafe_allow_html=True)
