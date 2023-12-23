import streamlit as st
from datetime import datetime

# Custom CSS to inject into Streamlit's HTML
st.markdown(
    """
    <style>
    .stTextInput, .stDateInput {
        margin-bottom: 10px;
    }
    /* You can add more styles to make it colorful and visually appealing */
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Mortgage Application Form for Predicting the PurchaseByInvesterDT')

# Input validation functions based on the field name
def validate_input(field_name, value):
    if 'Zip' in field_name and not value.isnumeric():
        return f"{field_name} should contain only numbers."
    if 'Rate' in field_name or 'Ratio' in field_name or 'APR' in field_name:
        try:
            float(value)
        except ValueError:
            return f"{field_name} should be a number."
    if 'Date' in field_name:
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return f"{field_name} should be a valid date in YYYY-MM-DD format."
    # Add more validations as needed
    return None

# Responsive layout for input fields
num_cols = 3  # You can adjust this based on the layout you want
cols = st.beta_columns(num_cols)
cols_iter = iter(cols)

for index, field in enumerate(fields):
    col = next(cols_iter)
    with col:
        if "Date" in field:
            # Use date input for fields containing 'Date'
            input_value = st.date_input(field, datetime.today())
        else:
            # Use text input for all other fields
            input_value = st.text_input(field)

        # Perform validation and show error if needed
        error_message = validate_input(field, input_value)
        if error_message:
            st.error(error_message)

# Button to submit the form
if st.button('Predict Purchase Date'):
    # Assume all data is valid for demonstration purposes
    st.success('Application Submitted Successfully!')
    # For demonstration, the input data is printed on the screen
    # Replace with actual form handling logic
    st.json({field: col for field, col in zip(fields, cols)})

# To run this app, save the above code to a file and run it with: streamlit run your_script.py
