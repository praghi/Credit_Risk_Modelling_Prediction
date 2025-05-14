import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked

# Set page configuration
st.set_page_config(page_title="CWC Finance: Credit Risk Modelling", layout="wide", page_icon="📊")

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>CWC Finance: Credit Risk Modelling Prediction</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- INPUT FORM SECTION ---
with st.container():
    st.markdown("### 📝 Customer Financial Details")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('👤 Age', min_value=18, step=1, max_value=100, value=28)
        loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=0, step=1, value=36)
        delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)

    with col2:
        income = st.number_input('💼 Annual Income ($)', min_value=0, value=1200000)
        avg_dpd_per_delinquency = st.number_input('📊 Avg Days Past Due (DPD)', min_value=0, value=20)
        credit_utilization_ratio = st.number_input('📉 Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)

    with col3:
        loan_amount = st.number_input('🏦 Loan Amount ($)', min_value=0, value=2560000)
        num_open_accounts = st.number_input('🔓 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
        
        # Auto-calculated field
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.markdown(f"💡 **Loan to Income Ratio**: `{loan_to_income_ratio:.2f}`")

# --- CATEGORICAL SECTION ---
st.markdown("### 🏠 Loan & Customer Profile")
col4, col5, col6 = st.columns(3)
with col4:
    residence_type = st.selectbox('🏡 Residence Type', ['Owned', 'Rented', 'Mortgage'])
with col5:
    loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with col6:
    loan_type = st.selectbox('🔒 Loan Type', ['Unsecured', 'Secured'])

# --- PREDICTION BUTTON ---
st.markdown("<hr>", unsafe_allow_html=True)

# Regular column layout for the button and predictions
col_button = st.columns([1, 1, 1])[1]
with col_button:
    if st.button('🚀 Calculate Risk'):
        with st.spinner("Predicting..."):
            try:
                # Get prediction results
                probability, credit_score, rating = predict(
                    age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                    delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                    residence_type, loan_purpose, loan_type
                )
                # --- METRICS SECTION (Aligned Like Inputs) ---
                st.markdown("### 📈 Credit Risk Insights")

                   # Display the results
                st.write(f"💣 Deafult Probability: {probability:.2%}")
                st.write(f"💳 Credit Score: {credit_score}")
                st.write(f"🛡️ Rating: {rating}")

                                # --- VISUALIZE THE RISK ---
                st.markdown("#### 📊 Risk Likelihood")
                st.progress(min(probability, 1.0))

                # Optional caption for clarity
                st.caption("Higher default probability means more credit risk. Use with caution.")
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>"
            "<sub>© praghi • Powered by Machine Learning</sub>"
            "</div>", unsafe_allow_html=True)




