import streamlit as st
from datetime import datetime

st.title('Mortgage Application Form')

# Input fields as specified
fields = [
    "Investor",
    "SubmittedToInvestorDate",
    "propertyCounty",
    "APR",
    "CashoutToBorrower",
    "FundingDate",
    "DTI",
    "ModifiedTimestamp",
    "FICO",
    "QualifyingHousingRatio",
    "PropertyZip",
    "PrimaryBorrowerCity",
    "TotalPrice",
    "PropertyCity",
    "TotalLoanAmount",
    "PrimaryBorrowerZip",
    "AppraisalValue",
    "CostCenter",
    "TotalPayment",
    "CLTV",
    "Branch",
    "InterestRate",
    "LockExpirationDate",
    "CreateDate",
    "LTV",
    "PlannedClosingDate",
    "Points",
    "Region",
    "LockDate",
    "LoanProgram"
]

# Function to validate input based on field name
def validate_input(field_name, value):
    errors = []
    if 'Zip' in field_name and not value.isnumeric():
        errors.append(f"{field_name} should contain only numbers.")
    if 'Rate' in field_name or 'Ratio' in field_name or 'APR' in field_name:
        try:
            value = float(value)
            if value <= 0:
                errors.append(f"{field_name} should be a positive number.")
        except ValueError:
            errors.append(f"{field_name} should be a number.")
    # You can add more specific validations for each field as needed.
    return errors

# Create a responsive layout with 2-3 columns based on the width of the screen
num_cols = 3
cols = st.columns(num_cols)

# Dictionary to hold the form inputs
input_data = {}
errors = {}

# Create input fields with validation
for index, field in enumerate(fields):
    col_index = index % num_cols
    with cols[col_index]:
        if "Date" in field:
            # Use date input for fields containing 'Date'
            input_data[field] = st.date_input(field, datetime.today())
        else:
            # Use text input for all other fields
            input_data[field] = st.text_input(field)

        # Perform validation and show error if needed
        field_errors = validate_input(field, input_data[field])
        if field_errors:
            errors[field] = field_errors
            for err in field_errors:
                st.error(err)

# Button to submit the form
if st.button('Submit'):
    if not errors:
        st.success('Application Submitted Successfully!')
        # For demonstration, the input data is printed on the screen
        st.json(input_data)
    else:
        st.error('Please correct the errors before submitting.')

# To run this app, save the above code to a file and run it with: streamlit run your_script.py
