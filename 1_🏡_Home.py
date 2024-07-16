
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
NAME = "Chew Chuan Juen (CJ)"
DESCRIPTION = """
SAP SuccessFactors Senior Consultant @ Tenthpin Malaysia, specializing in HXM project rollouts, passionate about programming and data-driven machine learning.
"""
# EMAIL = "ccjuen@gmail.com"
# SOCIAL_MEDIA = {
#     "LinkedIn": "https://www.linkedin.com/in/chuan-juen-cj-chew-99012462/",
#     "GitHub": "https://github.com/cjchew82"
# }
# Create columns for each social media link
col1, col2, col3, col4 = st.columns(4)

# Add LinkedIn link
with col1:
    st.markdown('<a href="https://www.linkedin.com/in/chuan-juen-cj-chew-99012462/" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col2:
    st.markdown('<a href="https://github.com/cjchew82" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

# Add WhatsApp link
# with col3:
#     st.markdown('<a href="https://wa.me/917710020979?text=Hello%20there,%20thanks%20for%20connecting!" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1200px-WhatsApp.svg.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
#     st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">WhatsApp</p>', unsafe_allow_html=True)

# Add X link    
with col3:
    st.markdown('<a href="https://x.com/cj7chew" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">X</p>', unsafe_allow_html=True)

# Add Email link
with col4:
    st.markdown('<a href="mailto:ccjuen@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

PROJECTS = {
    "🏆 Dimensionality reduction/clustering of data from scientific articles/ wikipedia summaries/news headlines": "https://github.com/MouadEttali/NLP-and-Text_Mining",
    "🏆 Implementation of a neural network for semi-supervised learning to predict MNIST data": "https://github.com/MouadEttali/ComputerVision_DeepLearning/tree/main/PseudoLabelingProject",
    "🏆 Implementation of multiple regression and logistic regression algorithms from the mathematical foundations. ": "https://github.com/MouadEttali/From-scratch-machine-learning---From-mathematical-formulas-to-functioning-algorithms",
    "🏆 This resume streamlit ": "https://github.com/MouadEttali/streamlit_resume",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


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
    st.image(profile_pic, width=230)


with cols[1]:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button( 
        label="📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫",EMAIL)


# -------- SOCIALS ---------

# V_SPACE(1)

# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")



# ------- EXPERIENCE AND QUALIFS --------

V_SPACE(1)
st.subheader('About me 🛝')
st.write(
    """
    - ✔️ **3 years of experience** in data science consulting firms for clients like <span style="color:#f50057; font-size: 15;">Total Energies , ONCF , Nexans, Allegro Musique </span> (Details in Professional Experiences)
    - ✔️ Built multiple ML based web applications (Python, Javascript, D3js, Streamlit) with deployment in AWS **(Sagemaker, API Gateway, Lambda).** 
    - ✔️ Expertise in statistical principles and classical ML models
    - ✔️ Product and value oriented mindset ( my dream is to build valuable ML tools, my nightmare is models dying in notebooks )  
    - ✔️ Work feels best when it's **challenging enough to push me and not easy enough to make me bored**
    """
,unsafe_allow_html=True)
# st.image(my_zone_pic)
# st.write(""" ⚠️ Warning : if you hand me a boring task <span style="color:#f50057; font-size: 15;">I will try to automate it.</span>""",unsafe_allow_html=True)
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills 🔬")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, pySpark
- 🧪 Data science : Machine Learning, Ensemble methods (Bagging, Boosting) / kernel methods (SVM, SPCA), Deep Learning, Natural Language Processing, Optimisation
- 📊 Data Visulization: PowerBi, Qlicksense, D3js
- 📚 Transfer Learning: LLMS, CNNs, Transformers ...
- 🗄️ Databases: Postgres, MongoDB, MySQL (on Premise and Cloud)
- ☁️ Cloud : AWS (Certified Cloud Practitioner (CLF)), Palantir Foundry
- 🚀 Deployment : Docker, Heroku, AWS 
"""
)
go_to_full_page("See my certifications and trainings" , "Certifications")

# --------- work history ---------
V_SPACE(1)
st.subheader("Recent Job Experience 🧑‍💻")
st.write('---')

st.write('\n')
st.write("🚧", "**Data Scientist | Aqsone**")
st.write("09/2022 - Present")
st.write(
    """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
- ► Commercial work : Participation in the <span style="color:#f50057; font-size: 15;">the developement of multiple proofs of concept</span> to demonstrate to prospects and clients for biz dev purposes
- ► Internal work : Along 2 other data scientist and an Agile coach, we handle the management of different courses and certifications for the rest of the company.
- ► Internal work : organization monthly presentations about the state of the art in the fields of data, AI and ML. As well as introduce new tools to our collaborators
""" , unsafe_allow_html=True
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
