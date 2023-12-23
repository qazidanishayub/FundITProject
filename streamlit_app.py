import streamlit as st
from datetime import datetime

st.title('Mortgage Application Form')

# Use columns for a responsive layout
num_cols = 3  # Adjust the number of columns based on device responsiveness

# Dictionary to hold the form inputs
input_data = {}

# Function to validate input based on field name
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

# Iterate over fields and create inputs with validation
for index, field in enumerate(fields):
    # Create columns dynamically
    col = st.columns(num_cols)[index % num_cols]
    with col:
        if "Date" in field:
            # Use date input for fields containing 'Date'
            input_data[field] = st.date_input(field, datetime.today())
        else:
            # Use text input for all other fields
            input_data[field] = st.text_input(field)

        # Perform validation and show error if needed
        error_message = validate_input(field, input_data[field])
        if error_message:
            st.error(error_message)

# Button to submit the form
if st.button('Submit'):
    # Here you can handle the form submission, like saving the data to a database
    # For demonstration, the input data is printed on the screen
    st.json(input_data)

# To run this app, save the above code to a file and run it with: streamlit run your_script.py
