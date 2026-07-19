import streamlit as st
import pandas as pd
import joblib
import time

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Autism Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load("models/autism_app_model.pkl")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* ================= BACKGROUND ================= */

.stApp{
    background:#1E1E1E;
    color:#F1F1F1;
}

/* Hide Streamlit Menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"]{
    background:#181818;
    border-right:1px solid #333333;
}

section[data-testid="stSidebar"] *{
    color:#F1F1F1;
}

/* ================= HEADINGS ================= */

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    color:#F1F1F1;
    margin-bottom:15px;
    letter-spacing:1px;
}

.section-title{
    font-size:28px;
    font-weight:700;
    color:#F1F1F1;
    margin-top:10px;
    margin-bottom:15px;
}

.sub-heading{
    font-size:18px;
    font-weight:600;
    color:#14B8A6;
    margin-top:20px;
}

/* ================= CARDS ================= */

div[data-testid="stVerticalBlock"] div:has(> div[data-testid="stRadio"]){

    background:#2A2A2A;

    border:1px solid #3A3A3A;

    border-radius:14px;

    padding:18px;

    margin-bottom:15px;

}

/* ================= BUTTON ================= */

.stButton>button{

    background:#0D9488;

    color:white;

    border:none;

    border-radius:12px;

    height:55px;

    width:100%;

    font-size:18px;

    font-weight:bold;

}

.stButton>button:hover{

    background:#0F766E;

}

/* ================= INPUTS ================= */

div[data-baseweb="select"]{

    background:#2A2A2A;

}

input{

    background:#2A2A2A !important;

    color:#F1F1F1 !important;

}

/* ================= METRIC ================= */

div[data-testid="stMetric"]{

    background:#2A2A2A;

    border:1px solid #3A3A3A;

    padding:15px;

    border-radius:12px;

}

/* ================= EXPANDER ================= */

details{

    background:#2A2A2A;

    border:1px solid #3A3A3A;

    border-radius:10px;

}

</style>

""",unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("AUTISM PREDICTION")

    st.write("""

This application estimates the likelihood of Autism Spectrum Disorder (ASD) using a trained Machine Learning model based on questionnaire responses and patient information.

### HOW TO USE

• Fill in the patient information.

• Answer all screening questions.

• Click **PREDICT AUTISM RISK**.

• View the prediction and confidence score.

""")

# ==========================================================
# HOME PAGE
# ==========================================================

st.markdown(
"""
<div class="main-title">
AUTISM PREDICTION SYSTEM
</div>
""",
unsafe_allow_html=True
)

st.markdown("""
### Early Screening Through Machine Learning

This application assists in the early screening of **Autism Spectrum Disorder (ASD)** by analyzing responses to a behavioural questionnaire along with basic demographic information.
The Machine Learning model identifies behavioural patterns associated with ASD and provides a prediction that may support early awareness and encourage timely professional consultation.

""")

st.markdown("## OUR MISSION")

st.write("""

Our mission is to leverage Artificial Intelligence to make autism screening more accessible, efficient and user-friendly.
By providing an easy-to-use digital assessment tool, we aim to promote early identification, increase awareness and support informed decision-making.

""")

st.markdown("---")

st.markdown(
"""
<div class="section-title">
PATIENT INFORMATION
</div>
""",
unsafe_allow_html=True
)

col1,col2=st.columns(2)

with col1:

    age=st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

with col2:

    gender=st.selectbox(
        "Gender",
        ["Female","Male"]
    )

col3,col4=st.columns(2)

with col3:

    jundice=st.selectbox(
        "Jaundice at Birth",
        ["No","Yes"]
    )

with col4:

    austim=st.selectbox(
        "Family History of Autism",
        ["No","Yes"]
    )

used_app_before=st.selectbox(

    "Used Autism Screening App Before",

    ["No","Yes"]

)

st.progress(35,text="Assessment Progress")

# ==========================================================
# QUESTIONNAIRE
# ==========================================================

st.markdown(
"""
<div class="section-title">
SCREENING QUESTIONNAIRE
</div>
""",
unsafe_allow_html=True
)

st.write(
"Answer the following questions based on the individual's usual behaviour."
)

aq_questions = [

"I notice small sounds or details that others often miss.",

"I usually find it easy to focus on the overall picture.",

"I can comfortably switch between different activities.",

"If interrupted, I can quickly return to what I was doing.",

"I find it easy to understand what someone else is thinking or feeling.",

"I can usually predict how another person might react.",

"I enjoy social conversations.",

"People often say I notice small details.",

"I can usually understand another person's intentions.",

"I enjoy imaginative or creative activities."

]

questions=[]

for i, question in enumerate(aq_questions):

    with st.container(border=True):

        st.markdown(
            f"""
            <span style="
            color:#A3A3A3;
            font-size:15px;
            font-weight:600;
            ">
            Question {i+1}
            </span>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
            font-size:20px;
            font-weight:600;
            color:#F1F1F1;
            margin-top:8px;
            margin-bottom:18px;
            ">
            {question}
            </div>
            """,
            unsafe_allow_html=True
        )

        answer = st.radio(

            label="",

            options=["No","Yes"],

            horizontal=True,

            key=f"question_{i}",

            label_visibility="collapsed"

        )

        questions.append(
            1 if answer=="Yes" else 0
        )

st.progress(
    75,
    text="Assessment Progress"
)

st.write("")

predict = st.button(

    "PREDICT AUTISM RISK",

    use_container_width=True

)

# ==========================================================
# PREDICTION
# ==========================================================
# NOTE: prediction/confidence/probability are stored in
# st.session_state so they survive Streamlit reruns (e.g. when
# the user opens the expander below after clicking predict).
# Referencing a plain local variable like `prediction` outside
# this block would raise a NameError on first load / rerun.

if predict:

    with st.spinner("Analyzing responses..."):

        time.sleep(1.5)

        gender_value = 1 if gender == "Male" else 0
        jundice_value = 1 if jundice == "Yes" else 0
        austim_value = 1 if austim == "Yes" else 0
        used_app_value = 1 if used_app_before == "Yes" else 0

        input_data = pd.DataFrame(
            [[
                questions[0],
                questions[1],
                questions[2],
                questions[3],
                questions[4],
                questions[5],
                questions[6],
                questions[7],
                questions[8],
                questions[9],
                age,
                gender_value,
                jundice_value,
                austim_value,
                used_app_value
            ]],
            columns=[
                "A1_Score",
                "A2_Score",
                "A3_Score",
                "A4_Score",
                "A5_Score",
                "A6_Score",
                "A7_Score",
                "A8_Score",
                "A9_Score",
                "A10_Score",
                "age",
                "gender",
                "jundice",
                "austim",
                "used_app_before"
            ]
        )

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        confidence = (
            probability[1]
            if prediction == 1
            else probability[0]
        )

    # persist results so they survive future reruns
    st.session_state["prediction"] = prediction
    st.session_state["confidence"] = confidence
    st.session_state["probability"] = probability

# ==========================================================
# RESULTS (only render once a prediction exists)
# ==========================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    confidence = st.session_state["confidence"]
    probability = st.session_state["probability"]

    st.progress(
        100,
        text="Assessment Complete"
    )

    st.write("")

    st.markdown(
        """
        <div style="
        background:#2A2A2A;
        padding:18px;
        border-radius:18px;
        border:2px solid #0D9488;
        text-align:center;
        ">
            <h2 style="color:#F1F1F1; font-size:20px; margin:0; letter-spacing:1px;">
                PREDICTION RESULT
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if prediction == 1:

        st.markdown(
            """
            <div style="
            background:#7F1D1D;
            padding:16px;
            border-radius:15px;
            text-align:center;
            ">
                <h2 style="color:white; font-size:17px; margin:0; font-weight:700;">
                HIGHER RISK OF AUTISM SPECTRUM DISORDER
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div style="
            background:#14532D;
            padding:16px;
            border-radius:15px;
            text-align:center;
            ">
                <h2 style="color:white; font-size:17px; margin:0; font-weight:700;">
                LOWER RISK OF AUTISM SPECTRUM DISORDER
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.metric(
            "Confidence Score",
            f"{confidence*100:.2f}%"
        )

    with col2:

        st.metric(
            "Prediction",
            "Higher Risk"
            if prediction == 1
            else "Lower Risk"
        )

    st.progress(float(confidence))

    st.write("")

    st.markdown("### Recommendation")

    if prediction == 1:

        st.warning(
            """
The model indicates a higher likelihood of Autism Spectrum Disorder.

A comprehensive assessment by a qualified healthcare professional is recommended.
            """
        )

    else:

        st.success(
            """
The model indicates a lower likelihood of Autism Spectrum Disorder.

If behavioural concerns persist, seeking professional evaluation is still recommended.
            """
        )

    # ==========================================================
    # MODEL PROBABILITIES
    # ==========================================================

    st.write("")

    st.markdown("### Probability Distribution")

    probability_df = pd.DataFrame({

        "Category": [
            "Lower Risk",
            "Higher Risk"
        ],

        "Probability": [
            probability[0] * 100,
            probability[1] * 100
        ]

    })

    st.bar_chart(
        probability_df.set_index("Category")
    )

    # ==========================================================
    # NEXT STEPS
    # ==========================================================

    st.write("")

    st.markdown("### Next Steps")

    if prediction == 1:

        st.info("""

• Schedule an appointment with a qualified healthcare professional.

• Share the screening responses during the consultation.

• Remember that this result is only an initial screening and not a diagnosis.

""")

    else:

        st.info("""

• Continue monitoring behavioural development.

• If any concerns arise in the future, consult a healthcare professional.

• Regular developmental assessments are always beneficial.

""")

# ==========================================================
# INPUT SUMMARY
# ==========================================================

st.write("")

with st.expander("View Assessment Summary"):

    patient_summary = pd.DataFrame({

        "Field":[
            "Age",
            "Gender",
            "Jaundice at Birth",
            "Family History",
            "Used Screening App Before"
        ],

        "Value":[
            age,
            gender,
            jundice,
            austim,
            used_app_before
        ]

    })

    st.subheader("Patient Information")

    st.table(patient_summary)

    st.subheader("Questionnaire Responses")

    response_summary = pd.DataFrame({

        "Question":[
            f"Question {i+1}"
            for i in range(10)
        ],

        "Response":[
            "Yes" if x==1 else "No"
            for x in questions
        ]

    })

    st.dataframe(
        response_summary,
        use_container_width=True,
        hide_index=True
    )

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.write("")

st.markdown(
"""
<div style="text-align:center;
color:#A3A3A3;
font-size:14px;
line-height:1.6;">

Autism Prediction System<br>
Machine Learning Based Screening Application<br><br>

<span style="font-size:12px;">
This tool does not provide a medical diagnosis. Please consult a
qualified healthcare professional for clinical evaluation.
</span>

</div>
""",
unsafe_allow_html=True
)