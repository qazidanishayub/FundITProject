import streamlit as st
from datetime import datetime

st.title('Mortgage Application Form')

# Dictionary to hold the form inputs
input_data = {}

# Define the fields with the 'Date' in their names as date input fields
# Other fields will be considered as text input fields
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

for field in fields:
    if "Date" in field:
        # Use date input for fields containing 'Date'
        input_data[field] = st.date_input(field, datetime.today())
    else:
        # Use text input for all other fields
        input_data[field] = st.text_input(field)

# Button to submit the form
if st.button('Submit'):
    st.success('Application Submitted Successfully!')
    # Here you can handle the form submission, like saving the data to a database
    # For demonstration, the input data is printed on the screen
    st.json(input_data)

# To run this app, save the above code to a file and run it with: streamlit run your_script.py
