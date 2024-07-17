from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit.components.v1 as components


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"

# AWS_ML_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "aws_ml.jpg"
# ML_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "ml_stanford.png"
# NN_DL_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "nn_dl.png"
# DL_TUNE_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "dl_tuning.png"
# AWS_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "aws_pract.png"
# NLP_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "nlp.png"
SAP_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "SF_EC.png"  # Add the new image path

# ------------ CONSTANTS ----------
PAGE_TITLE = "Certifications | CJ Chew"
PAGE_ICON = "📜"

#-------- Certifications CONTENT----------
SAP_CERTIFICATION_TITLE = "SAP Certified Associate - Implementation Consultant - SAP SuccessFactors Employee Central Core"
SAP_CERTIFICATION_LINK = "https://www.credly.com/badges/a2464039-6ef2-4d9e-8421-7041b1580736/public_url"
SAP_CERTIFICATION_DESCRIPTION = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Employee Central Core.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for SAP SuccessFactors Employee Central, including implmentation, and system administration.
    """ 

# AWS_ML_CERTIFICATION_TITLE = "AWS Certified Machine Learning Specialty 2023 - Hands On!"
# AWS_ML_CERTIFICATION_PIC = Image.open(AWS_ML_CERTIFICATION_PIC_PATH)
# AWS_ML_CERTIFICATION_LINK = "https://www.udemy.com/certificate/UC-c0613ef8-6d5c-49aa-8429-c384dfec8d36/"
# AWS_ML_CERTIFICATION_DESCRIPTION = """
#     - ✔  <span style="color:#f50057; font-size: 15;">**AWS Certified Machine Learning Specialty 2023 - Hands On!**</span> is an depth hands on course training for the machine learning specialty certification by aws.
#     - ✔  This certification teaches a wide set of high level ML aws services, their use cases and how to implement them in large scale solutions inside a bigger aws architecture.
#     - ✔  Some of the services include SageMaker, canvas, Comprehend, Forecast, Kinesis, Glue and more. 

#     """ 

# ML_CERTIFICATION_TITLE = "Machine Learning : Stanford University "
# ML_CERTIFICATION_PIC = Image.open(ML_CERTIFICATION_PIC_PATH)
# ML_CERTIFICATION_LINK = "https://www.coursera.org/account/accomplishments/verify/K52NAQ2FB8Z7"
# ML_CERTIFICATION_DESCRIPTION = """
#     - ✔  <span style="color:#f50057; font-size: 15;">**The Machine Learning Specialization**</span> is a foundational online program created in collaboration between <span style="color:#19A7CE; font-size: 15;">**DeepLearning.AI and Stanford Online.**</span>
#     - ✔  This certification teaches the fundamentals of machine learning and how to use these techniques to build real-world AI applications. 

#     """ 

# NN_DL_CERTIFICATION_TITLE = "Neural Networks and Deep Learning"
# NN_DL_CERTIFICATION_PIC = Image.open(NN_DL_CERTIFICATION_PIC_PATH)
# NN_DL_CERTIFICATION_LINK = "https://www.coursera.org/account/accomplishments/verify/M5SRBK44NKX3"
# NN_DL_CERTIFICATION_DESCRIPTION = """
#     - ✔ The Deep Learning Specialization is a foundational program created by <span style="color:#19A7CE; font-size: 15;">**DeepLearning.AI**</span> that will helped me understand the capabilities, challenges, and consequences of deep learning
#     - ✔ It prepared me to participate in the development of leading-edge AI technology. 
#     - ✔ It provided a pathway for me to gain the knowledge and skills to apply Deep learning to my work, and level up my technical career.
#     """ 

# DL_TUNE_CERTIFICATION_TITLE = "Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization"
# DL_TUNE_CERTIFICATION_PIC = Image.open(DL_TUNE_CERTIFICATION_PIC_PATH)
# DL_TUNE_CERTIFICATION_LINK = "https://www.coursera.org/account/accomplishments/verify/3XZ4UJ2CLZD5"
# DL_TUNE_CERTIFICATION_DESCRIPTION = """
#     - ✔  <span style="color:#f50057; font-size: 15;">**The Machine Learning Specialization**</span> is a foundational online program created in collaboration between <span style="color:#19A7CE; font-size: 15;">**DeepLearning.AI and Stanford Online.**</span>
#     - ✔  This certification teaches the fundamentals of machine learning and how to use these techniques to build real-world AI applications. 
#     """ 

# AWS_CERTIFICATION_TITLE = "AWS Certified Cloud Practitioner"
# AWS_CERTIFICATION_PIC = Image.open(AWS_CERTIFICATION_PIC_PATH)
# AWS_CERTIFICATION_LINK = "https://www.credly.com/badges/354d559c-4d1e-463c-8852-5dad79e75d13"
# AWS_CERTIFICATION_DESCRIPTION = """
# - ✔ <span style="color:#f50057; font-size: 15;">**The AWS Certified Cloud Practitioner**</span>  offers a foundational understanding of <span style="color:#19A7CE; font-size: 15;">**AWS Cloud concepts, services, and terminology.**</span>
# - ✔ This was a good starting point for me as I was interested in deploying <span style="color:#19A7CE; font-size: 15;">**ML systems on the cloud.**</span>
# - ✔ A potiential next step is to get the <span style="color:#19A7CE; font-size: 15;">**Machine learning Specialty certification**</span> if I need it for a job opportunity.
#     """ 

# NLP_CERTIFICATION_TITLE = "NLP - Natural Language Processing with Python"
# NLP_CERTIFICATION_PIC = Image.open(NLP_CERTIFICATION_PIC_PATH)
# NLP_CERTIFICATION_LINK = "https://www.udemy.com/certificate/UC-a13d1b17-6863-4209-8980-25f32ba51815/"
# NLP_CERTIFICATION_DESCRIPTION = """
# - ✔ This Certification helped me :
#     - 💠 Master Python-based text file manipulation and processing.
#     - 💠 Gain expertise in handling PDF files and extracting information using Python.
#     - 💠 Acquire skills in pattern searching using <span style="color:#19A7CE; font-size: 15;">**regular expressions**</span> and employ <span style="color:#19A7CE; font-size: 15;">**Spacy**</span> for efficient tokenization and vocabulary matching.
#     """ 
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Certifications")
# --------------- HELPER FUNCTIONS -----------------------

# def certification_section(CERTIFICATION_TITLE,CERTIFICATION_LINK,CERTIFICATION_DESCRIPTION,CERTIFICATION_PIC):

#     st.subheader(f"[{CERTIFICATION_TITLE}]({CERTIFICATION_LINK})")
#     st.write(CERTIFICATION_DESCRIPTION, unsafe_allow_html=True)
#     with st.expander("Check Certification"):
#         st.image(CERTIFICATION_PIC,width=800)
#     st.write('----')
def certification_section(CERTIFICATION_TITLE,CERTIFICATION_LINK,CERTIFICATION_DESCRIPTION,CERTIFICATION_PIC=None, embed_code=None):
    st.subheader(f"[{CERTIFICATION_TITLE}]({CERTIFICATION_LINK})")
    st.write(CERTIFICATION_DESCRIPTION, unsafe_allow_html=True)
    if CERTIFICATION_PIC:
        with st.expander("Check Certification"):
            st.image(CERTIFICATION_PIC, width=800)
    if embed_code:
        components.html(embed_code, height=270)
    st.write('----')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ CERTIFICATION AWS ML SECTION ---------
# certification_section(AWS_ML_CERTIFICATION_TITLE,AWS_ML_CERTIFICATION_LINK,AWS_ML_CERTIFICATION_DESCRIPTION,AWS_ML_CERTIFICATION_PIC)

# # ------ CERTIFICATION ML SECTION ---------
# certification_section(ML_CERTIFICATION_TITLE,ML_CERTIFICATION_LINK,ML_CERTIFICATION_DESCRIPTION,ML_CERTIFICATION_PIC)

# # ------ CERTIFICATION NN DL SECTION ---------
# certification_section(NN_DL_CERTIFICATION_TITLE,NN_DL_CERTIFICATION_LINK,NN_DL_CERTIFICATION_DESCRIPTION,NN_DL_CERTIFICATION_PIC)

# # ------ CERTIFICATION DL SECTION ---------
# certification_section(DL_TUNE_CERTIFICATION_TITLE,DL_TUNE_CERTIFICATION_LINK,DL_TUNE_CERTIFICATION_DESCRIPTION,DL_TUNE_CERTIFICATION_PIC)

# # ------ CERTIFICATION AWS SECTION ---------
# certification_section(AWS_CERTIFICATION_TITLE,AWS_CERTIFICATION_LINK,AWS_CERTIFICATION_DESCRIPTION,AWS_CERTIFICATION_PIC)

# # ------ CERTIFICATION NLP SECTION ---------
# certification_section(NLP_CERTIFICATION_TITLE,NLP_CERTIFICATION_LINK,NLP_CERTIFICATION_DESCRIPTION,NLP_CERTIFICATION_PIC)

# ------ CERTIFICATION SAP SECTION ---------
credly_embed_code = '''
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="a2464039-6ef2-4d9e-8421-7041b1580736" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''
certification_section(SAP_CERTIFICATION_TITLE, SAP_CERTIFICATION_LINK, SAP_CERTIFICATION_DESCRIPTION, embed_code=credly_embed_code)