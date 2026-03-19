import requests
import streamlit as st

API_URL = "https://ai-cv-job-matcher-api.onrender.com/analyze-resume-match"

st.set_page_config(
    page_title="AI CV Job Matcher",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0, 194, 255, 0.12), transparent 28%),
            radial-gradient(circle at top right, rgba(124, 58, 237, 0.14), transparent 30%),
            linear-gradient(180deg, #050816 0%, #081120 45%, #0a1426 100%);
        color: white;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero-title {
        text-align: center;
        font-size: 3.8rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #ffffff 0%, #c4d8ff 45%, #7dd3fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 24px rgba(0, 194, 255, 0.10);
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1rem;
        color: #b7c6db;
        margin-bottom: 2rem;
    }

    .input-title {
        font-size: 1.45rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.8rem;
    }

    .metric-box {
        background: rgba(11, 20, 38, 0.92);
        border: 1px solid rgba(93, 122, 163, 0.22);
        border-radius: 18px;
        padding: 1.2rem;
        text-align: center;
        margin-bottom: 1rem;
        min-height: 120px;
    }

    .metric-label {
        color: #9fb4cc;
        font-size: 0.95rem;
        margin-bottom: 0.45rem;
        font-weight: 600;
    }

    .metric-value {
        color: white;
        font-size: 2rem;
        font-weight: 800;
    }

    .section-title {
        font-size: 1.18rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }

    .section-desc {
        font-size: 0.92rem;
        color: #9fb4cc;
        margin-bottom: 0.8rem;
        line-height: 1.45;
    }

    .section-group {
        margin-bottom: 1.6rem;
        padding: 0.2rem 0 0.2rem 0;
    }

    .badge {
        display: inline-block;
        padding: 0.48rem 0.85rem;
        margin: 0.24rem;
        border-radius: 999px;
        font-size: 0.9rem;
        font-weight: 700;
    }

    .badge-cv {
        background: rgba(96, 165, 250, 0.12);
        color: #93c5fd;
        border: 1px solid rgba(96, 165, 250, 0.35);
    }

    .badge-job {
        background: rgba(56, 189, 248, 0.12);
        color: #7dd3fc;
        border: 1px solid rgba(56, 189, 248, 0.35);
    }

    .badge-matched {
        background: rgba(34, 197, 94, 0.12);
        color: #86efac;
        border: 1px solid rgba(34, 197, 94, 0.32);
    }

    .badge-missing {
        background: rgba(239, 68, 68, 0.12);
        color: #fca5a5;
        border: 1px solid rgba(239, 68, 68, 0.30);
    }

    .empty-text {
        color: #8ea3bb;
        font-size: 0.95rem;
    }

    .recommendation-strong {
        color: #22c55e;
        font-size: 1.3rem;
        font-weight: 800;
    }

    .recommendation-partial {
        color: #facc15;
        font-size: 1.3rem;
        font-weight: 800;
    }

    .recommendation-weak {
        color: #ef4444;
        font-size: 1.3rem;
        font-weight: 800;
    }

    .helper-text {
        color: #9db0c7;
        font-size: 0.92rem;
        margin-top: 0.45rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #0b1629 !important;
        color: white !important;
        border: 1px solid rgba(93, 122, 163, 0.25) !important;
        border-radius: 16px !important;
        min-height: 235px !important;
    }

    div.stButton > button {
        width: 240px;
        display: block;
        margin: 1rem auto 1.4rem auto;
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 14px;
        font-weight: 800;
        padding: 0.85rem 1rem;
        font-size: 1rem;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.22);
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
        color: white;
    }

    .footer-note {
        text-align: center;
        color: #7f94ad;
        font-size: 0.9rem;
        margin-top: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height: 10vh'></div>", unsafe_allow_html=True)
st.markdown('<div class="hero-title">AI CV Job Matcher</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Compare your CV with a job description and instantly see the missing skills.</div>',
    unsafe_allow_html=True
)

left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown('<div class="input-title">Upload Resume</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF only)",
        type=["pdf"],
        label_visibility="collapsed"
    )
    st.markdown('<div class="helper-text">Accepted format: PDF only</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="input-title">Job Description</div>', unsafe_allow_html=True)
    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the full job description here...",
        label_visibility="collapsed"
    )
    st.markdown(
        '<div class="helper-text">Paste the role requirements, responsibilities, or full job description.</div>',
        unsafe_allow_html=True
    )

col_btn1, col_btn2, col_btn3 = st.columns([1,1,1])
with col_btn2:
    analyze_button = st.button("Analyze Match")


def render_badges(skills: list[str], badge_class: str) -> None:
    if not skills:
        st.markdown('<div class="empty-text">No skills detected.</div>', unsafe_allow_html=True)
        return

    html = "".join(
        [f'<span class="badge {badge_class}">{skill}</span>' for skill in skills]
    )
    st.markdown(html, unsafe_allow_html=True)

def recommendation_class(value: str) -> str:
    lowered = value.lower()
    if "strong" in lowered:
        return "recommendation-strong"
    if "partial" in lowered:
        return "recommendation-partial"
    return "recommendation-weak"

def generate_fallback_message(result: dict) -> str:
    if not result["job_skills"]:
        return (
            "No clear job skills were detected from the job description. "
            "Try pasting a cleaner version of the requirements or add more explicit technologies."
        )
    if not result["cv_skills"]:
        return (
            "No clear CV skills were detected from the uploaded file. "
            "Check whether the PDF contains selectable text and a clear skills section."
        )
    return ""

if analyze_button:
    if uploaded_file is None:
        st.error("Please upload a PDF resume.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        with st.spinner("Analyzing your CV and matching skills..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
            }
            data = {
                "job_description": job_description
            }

            try:
                response = requests.post(API_URL, files=files, data=data, timeout=120)

                if response.status_code == 200:
                    result = response.json()
                    fallback_message = generate_fallback_message(result)

                    if fallback_message:
                        st.warning(fallback_message)
                    else:
                        st.success("Analysis completed successfully.")

                    top1, top2 = st.columns(2, gap="large")

                    with top1:
                        st.markdown(
                            f"""
                            <div class="metric-box">
                                <div class="metric-label">Match Score</div>
                                <div class="metric-value">{result["match_score"]}%</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with top2:
                        rec_class = recommendation_class(result["recommendation"])
                        st.markdown(
                            f"""
                            <div class="metric-box">
                                <div class="metric-label">Recommendation</div>
                                <div class="{rec_class}">{result["recommendation"]}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    row1_col1, row1_col2 = st.columns(2, gap="large")

                    with row1_col1:
                        st.markdown('<div class="section-group">', unsafe_allow_html=True)
                        st.markdown('<div class="section-title">CV Skills</div>', unsafe_allow_html=True)
                        st.markdown(
                            '<div class="section-desc">This section shows the skills detected from the uploaded CV.</div>',
                            unsafe_allow_html=True
                        )
                        render_badges(result["cv_skills"], "badge-cv")
                        st.markdown('</div>', unsafe_allow_html=True)

                    with row1_col2:
                        st.markdown('<div class="section-group">', unsafe_allow_html=True)
                        st.markdown('<div class="section-title">Job Skills</div>', unsafe_allow_html=True)
                        st.markdown(
                            '<div class="section-desc">This section shows the skills extracted from the job description.</div>',
                            unsafe_allow_html=True
                        )
                        render_badges(result["job_skills"], "badge-job")
                        st.markdown('</div>', unsafe_allow_html=True)

                    row2_col1, row2_col2 = st.columns(2, gap="large")

                    with row2_col1:
                        st.markdown('<div class="section-group">', unsafe_allow_html=True)
                        st.markdown('<div class="section-title">Matched Skills</div>', unsafe_allow_html=True)
                        st.markdown(
                            '<div class="section-desc">These skills appear in both the CV and the job description.</div>',
                            unsafe_allow_html=True
                        )
                        render_badges(result["matched_skills"], "badge-matched")
                        st.markdown('</div>', unsafe_allow_html=True)

                    with row2_col2:
                        st.markdown('<div class="section-group">', unsafe_allow_html=True)
                        st.markdown('<div class="section-title">Missing Skills</div>', unsafe_allow_html=True)
                        st.markdown(
                            '<div class="section-desc">These skills are required by the job but are not found in the CV.</div>',
                            unsafe_allow_html=True
                        )
                        render_badges(result["missing_skills"], "badge-missing")
                        st.markdown('</div>', unsafe_allow_html=True)

                else:
                    st.error(f"API error: {response.status_code}")
                    st.json(response.json())

            except requests.exceptions.RequestException as e:
                st.error("Could not connect to the FastAPI server.")
                st.exception(e)

st.markdown(
    '<div class="footer-note">Built with FastAPI, Streamlit, and skill-based matching logic.</div>',
    unsafe_allow_html=True
)
