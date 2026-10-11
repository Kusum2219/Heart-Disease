
import requests
import streamlit as st

API_URL = "http://127.0.0.1:5000/predict"

st.set_page_config(
    page_title="Heart Health | History Classifier",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Styling --------------------

st.markdown("""
<style>
    .block-container {
        max-width: 1100px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 1.5rem 1.7rem;
        border: 1px solid #dce5e8;
        border-radius: 16px;
        background: linear-gradient(120deg, #f2f7f8, #ffffff);
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        color: #173b46;
        margin-bottom: 0.5rem;
    }

    .muted {
        color: #52636b;
        font-size: 0.96rem;
    }

    div.stButton > button,
    div.stFormSubmitButton > button {
        background: #174b57;
        color: white;
        border: 0;
        border-radius: 9px;
        min-height: 46px;
        font-weight: 600;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        background: #236675;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# -------------------- Sidebar --------------------

st.sidebar.title("Heart Health")
st.sidebar.caption("Reported heart disease history classifier")
st.sidebar.divider()

st.sidebar.markdown(
    "This educational application uses a CatBoost model "
    "trained on BRFSS survey data."
)

st.sidebar.info(
    "The model score is not a clinical risk estimate. "
    "This application is not a medical diagnostic tool."
)


# -------------------- Page Header --------------------

st.markdown("""
<div class="hero">
    <h1>Heart Health Classifier</h1>
    <p class="muted">
        Enter health survey information to classify whether the
        model predicts a reported history of heart attack or
        coronary heart disease.
    </p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "For educational and project demonstration only. "
    "Do not use this result to make medical decisions."
)


# -------------------- Helpers --------------------

def coded_select(label, options, key):
    """Show readable options and return their model input codes."""
    selected = st.selectbox(
        label,
        list(options.keys()),
        key=key,
    )
    return options[selected]


def days_options():
    """BRFSS: 88 means zero unhealthy days."""
    options = {"0 days": "88"}

    options.update({
        f"{n} day(s)": str(n)
        for n in range(1, 31)
    })

    options["Unknown / don't know / refused"] = "Unknown"
    return options


UNKNOWN = "Unknown"


# -------------------- Survey Form --------------------

with st.form("heart_health_form"):

    # Demographics
    st.subheader("1. Demographic information")

    col1, col2 = st.columns(2)

    with col1:
        sex = coded_select(
            "Sex recorded in survey",
            {
                "Male": "1",
                "Female": "2",
            },
            "sex",
        )

    with col2:
        age = coded_select(
            "Age group",
            {
                "18–24 years": "1",
                "25–29 years": "2",
                "30–34 years": "3",
                "35–39 years": "4",
                "40–44 years": "5",
                "45–49 years": "6",
                "50–54 years": "7",
                "55–59 years": "8",
                "60–64 years": "9",
                "65–69 years": "10",
                "70–74 years": "11",
                "75–79 years": "12",
                "80 years or older": "13",
                "Unknown / unavailable": "14",
            },
            "age",
        )

    st.divider()

    # Health history
    st.subheader("2. Health history")

    col1, col2 = st.columns(2)

    with col1:
        bp = coded_select(
            "Ever told you have high blood pressure?",
            {
                "Yes": "1",
                "Yes, during pregnancy only": "2",
                "No": "3",
                "Borderline / pre-hypertension": "4",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "bp",
        )

        cholesterol = coded_select(
            "Ever told you have high cholesterol?",
            {
                "Yes": "1",
                "No": "2",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "cholesterol",
        )

        diabetes = coded_select(
            "Diabetes status",
            {
                "Yes": "1",
                "Yes, during pregnancy only": "2",
                "No": "3",
                "Prediabetes / borderline diabetes": "4",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "diabetes",
        )

        bmi = coded_select(
            "BMI category",
            {
                "Underweight": "1",
                "Normal weight": "2",
                "Overweight": "3",
                "Obesity": "4",
                "Unknown / unavailable": UNKNOWN,
            },
            "bmi",
        )

        kidney = coded_select(
            "Ever told you have kidney disease?",
            {
                "Yes": "1",
                "No": "2",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "kidney",
        )

    with col2:
        general_health = coded_select(
            "General health",
            {
                "Excellent": "1",
                "Very good": "2",
                "Good": "3",
                "Fair": "4",
                "Poor": "5",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "general_health",
        )

        walking = coded_select(
            "Have serious difficulty walking or climbing stairs?",
            {
                "Yes": "1",
                "No": "2",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "walking",
        )

        physical = coded_select(
            "Days physical health was not good (past 30 days)",
            days_options(),
            "physical",
        )

        mental = coded_select(
            "Days mental health was not good (past 30 days)",
            days_options(),
            "mental",
        )

    st.divider()

    # Lifestyle
    st.subheader("3. Lifestyle information")

    col1, col2 = st.columns(2)

    with col1:
        smoke100 = coded_select(
            "Smoked at least 100 cigarettes in your life?",
            {
                "Yes": "1",
                "No": "2",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "smoke100",
        )

        smoke_days = coded_select(
            "Current smoking frequency",
            {
                "Every day": "1",
                "Some days": "2",
                "Not at all": "3",
                "Unknown / not applicable": UNKNOWN,
            },
            "smoke_days",
        )

    with col2:
        exercise = coded_select(
            "Any physical activity outside your regular job "
            "in the past 30 days?",
            {
                "Yes": "1",
                "No": "2",
                "Unknown / don't know / refused": UNKNOWN,
            },
            "exercise",
        )

    submitted = st.form_submit_button(
        "Run Classification",
        use_container_width=True,
    )


# -------------------- Prediction --------------------

if submitted:

    payload = {
        "SEXVAR": sex,
        "_AGEG5YR": age,
        "BPHIGH6": bp,
        "TOLDHI3": cholesterol,
        "DIABETE4": diabetes,
        "_BMI5CAT": bmi,
        "PHYSHLTH": physical,
        "MENTHLTH": mental,
        "GENHLTH": general_health,
        "DIFFWALK": walking,
        "SMOKE100": smoke100,
        "SMOKDAY2": smoke_days,
        "EXERANY2": exercise,
        "CHCKDNY2": kidney,
    }

    with st.spinner("Running model classification..."):

        try:
            response = requests.post(
                API_URL,
                json=payload,
                timeout=20,
            )

            if response.ok:
                result = response.json()

                score = float(result["model_score_percent"])
                prediction = result["prediction"]
                threshold = float(result["threshold_percent"])

                st.divider()
                st.subheader("Classification result")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Model score (not clinical risk)",
                        f"{score:.2f}%",
                    )

                with col2:
                    st.metric(
                        "Model prediction",
                        prediction,
                    )

                st.progress(
                    min(max(score / 100, 0.0), 1.0)
                )

                st.caption(
                    f"Classification threshold: {threshold:.0f}%"
                )

                st.info(
                    result.get(
                        "disclaimer",
                        "Educational model output only; "
                        "not a medical diagnosis or validated "
                        "estimate of clinical risk.",
                    )
                )

                with st.expander("View submitted feature codes"):
                    st.json(payload)

            else:
                try:
                    error_data = response.json()
                    message = error_data.get(
                        "error",
                        response.text,
                    )
                except ValueError:
                    message = response.text

                st.error(
                    f"API error ({response.status_code}): {message}"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                "Flask API se connection nahi ho paaya. "
                "Backend ko alag terminal mein chalu karo, "
                "phir dobara try karo."
            )

        except requests.exceptions.Timeout:
            st.error(
                "API request timed out. Check whether the "
                "backend is running and try again."
            )

        except (requests.exceptions.RequestException, ValueError, KeyError) as exc:
            st.error(f"Request or response error: {exc}")
