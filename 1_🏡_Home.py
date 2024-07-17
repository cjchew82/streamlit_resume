from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "cv_mouad.pdf"

profile_pic = current_dir / "assets" / "home" /"profile-pic.png"

my_zone_pic = current_dir / "assets" / "home" / "my_zone.png"

# ------------ CONSTANTS ----------
PAGE_TITLE = "Digital Resume | CJ Chew"
PAGE_ICON = "💼"
NAME = "Chuan Juen (CJ) Chew"
GENDER = "MALE"
DESCRIPTION = """
SAP SuccessFactors Senior Consultant @ Tenthpin Malaysia, specializing in HXM project rollouts, 
passionate about programming and data-driven machine learning.
"""
EMAIL = "ccjuen@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/chuan-juen-cj-chew-99012462/",
    "GitHub": "https://github.com/cjchew82",
    "X": "",
    "Facebook": "",
    "Instagram": ""
}

SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055",
    "GitHub": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
    "X": "https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
    "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
}
PROJECTS = {
    "📋 Digital resume streamlit ": "https://github.com/MouadEttali/streamlit_resume",
    "📊 Quantatitive Backtest App streamlit ": "",
    "📈 Crypto Algorithm Trading Bot (Bybit)": ""
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Function to generate social media icons
def social_media_icon(link, icon_url, name):
    return f'''
    <a href="{link}" target="_blank" style="text-decoration:none;">
        <img src="{icon_url}" alt="{name}" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;">
    </a>
    <p style="text-align:center;font-size:16px;margin-top:10px;">{name}</p>
    '''

st.title("Hi / 您好 / Apa Kahbar")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)


# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

my_zone_pic = Image.open(my_zone_pic)
# ------ HERO SECTION -----------

cols = st.columns(2, gap='small')

with cols[0]:
    st.image(profile_pic)
    # st.image(profile_pic, width=230)

with cols[1]:
    st.title(NAME)
    st.write("♀️♂️",GENDER)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧",EMAIL)


# -------- SOCIALS ---------

V_SPACE(1)

# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# Social media icons display
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        st.markdown(social_media_icon(link, SOCIAL_MEDIA_ICONS[platform], platform), unsafe_allow_html=True)

# ------- EXPERIENCE AND QUALIFS --------

V_SPACE(1)
st.subheader('About me 🧑‍🦱')
# st.write(
#     """
#     - ✔️ **8 years of experience** in SAP SuccessFactors consulting firms for clients like <span style="color:#f50057; font-size: 15;">Total Energies , ONCF , Nexans, Allegro Musique </span> (Details in Professional Experiences)
#     - ✔️ Built multiple ML based web applications (Python, Javascript, D3js, Streamlit) with deployment in AWS **(Sagemaker, API Gateway, Lambda).**
#     - ✔️ Expertise in statistical principles and classical ML models
#     - ✔️ Product and value oriented mindset ( my dream is to build valuable ML tools, my nightmare is models dying in notebooks )
#     - ✔️ Work feels best when it's **challenging enough to push me and not easy enough to make me bored**
#     """
# ,unsafe_allow_html=True)

st.write(
    """
    - ✔️ **8 years of experience** in SAP SuccessFactors Consulting across various industries, including <span style="color:#f50057; font-size: 15;">manufacturing, shared services, pharmaceutical, refinery & cracker, Life Science, </span> with involvement in multi-country implementations.
    - ✔️ Certified Associate Consultant in **Employee Central, Recruiting (Candidate & Recruiter), Learning Management, and Onboarding.**
    - ✔️ Project lead with comprehensive experience in the full HXM implementation project cycle and system maintenance, covering requirement workshops, iteration reviews, configuration, end-user training, user acceptance testing, and Go-Live hypercare support.
    - ✔️ Solution Architect providing end-to-end HXM architecture flow and workaround solutions.
    - ✔️ Expertise in the SuccessFactors platform, including Reporting Canvas, Integration Center, Job Profile Builder, and API endpoint scripting. Strong knowledge of HR data analysis.
    - ✔️ **2 years of experience** in Python programming, with a passion for exploring data statistics and machine learning.
    """
,unsafe_allow_html=True)

# st.image(my_zone_pic)
# st.write(""" ⚠️ Warning : if you hand me a boring task <span style="color:#f50057; font-size: 15;">I will try to automate it.</span>""",unsafe_allow_html=True)
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills 🔬")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, Microsoft Office, HTML
- 🧪 Data science : Machine Learning, Deep Learning, Optimisation
- 🗄️ Databases: Microsoft SQL Server
- 🚀 Deployment : Github, Steamlit
"""
)
go_to_full_page("See my certifications and trainings" , "Certifications")

# --------- work history ---------
V_SPACE(1)
st.subheader("Recent Job Experience 🧑‍💻")
st.write('---')

st.write('\n')
st.write("🚧", "**SAP SuccessFactors Senior Consultant | Tenthpin Management Consultants Sdn Bhd**")
st.write("12/2021 - Present")
# st.write(
#     """
# **Project Implementation**
# My experience in the full project implementation cycle
# - Includes facilitating workshops to gather requirements,
# - Conducting system reviews and iterations, performing configuration testing,
# - Delivering train-the-trainer sessions, conducting user acceptance tests,
# - Providing go-live project support.
# - Also partially involved in Project Managing such as kick-off meeting.
# - Additionally, I guide and collaborate closely with team members to ensure successful project delivery.
#
# **Business Development**
# - Work closely with the Business Development on any opportunity pipeline bidding presentation.
# - Pre-sales demo to client, and discussion with client on project architecture framework.
# - Workout on the project timeline and propose the project methodology to client during the bidding presentation.
#
# **Client Support**
# ✅Project: Clover Biopharmaceuticals (EC, RCM, and ONB 2.0 Oversea UK and US implementation)
# ✅Project: Mindray (EC Integration and SF full suite system support)
# ✅Project: Clover Biopharmaceuticals (Compensation new worksheet implementation)
# ✅Project Fapon Biotech EC and Onboarding Rollout and support
# ✅Project: ND Paper SAP HCM Malaysia Payroll (Project Manager)
# """ , unsafe_allow_html=True
# )

col1, col2, col3 = st.columns(3)

with st.expander("Project Implementation"):
    st.write(
        """
        My experience in the full project implementation cycle:
        - Facilitating workshops to gather requirements
        - Conducting system reviews and iterations, performing configuration testing
        - Delivering train-the-trainer sessions, conducting user acceptance tests
        - Providing go-live project support
        - Partially involved in Project Managing such as kick-off meeting
        - Additionally, I guide and collaborate closely with team members to ensure successful project delivery
        """
    )

with st.expander("Business Development"):
    st.write(
        """
        - Work closely with the Business Development on any opportunity pipeline bidding presentation
        - Pre-sales demo to client, and discussion with client on project architecture framework
        - Workout on the project timeline and propose the project methodology to client during the bidding presentation
        """
    )

with st.expander("Client Support"):
    st.write(
        """
        ✅Project: Clover Biopharmaceuticals (EC, RCM, and ONB 2.0 Oversea UK and US implementation)
        ✅Project: Mindray (EC Integration and SF full suite system support)
        ✅Project: Clover Biopharmaceuticals (Compensation new worksheet implementation)
        ✅Project Fapon Biotech EC and Onboarding Rollout and support
        ✅Project: ND Paper SAP HCM Malaysia Payroll (Project Manager)
        """
    )

go_to_full_page("Check out all my experiences" , "Professional Experiences")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Personal Projects 🧙‍♂️")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

go_to_full_page("More Personal Projects" , "Personal Projects")

# Add footer
st.write('---')
st.write('© Chew Chuan Juen  |  Last updated: July 2024')