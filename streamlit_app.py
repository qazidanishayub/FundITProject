import streamlit as st
from datetime import datetime

st.title('Mortgage Application Form for PurchaseByInvesterDT Prediction')

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

cost_center_options= ['083', '124', '452', '419', '523', '360', '053', '408', '212', '540', '060', '348', '551', '126', '418', '303', '517', '336', '205', '326', '522', '402', '570', '401', '322', '043', '580', '528', '310', '416', '544', '073', '535', '573', '112', '542', '131', '406', '301', '521', '330', '519', '585', '314', '560', '541', '407', '304', '128', '932', '575', '571', '526', '064', '545', '046', '467', None, '120', '332', '351', '568', '579', '422', '317', '311', '572', '505', '577', '595', '578', '410', '515', '510', '482', '594', '321', '415', '446', '421', '316', '795', '235', '933', '312', '525', '093', '420', '516', '023', '063', '082', '589', '597', '520', '409', '331', '309', '586', '404', '362', '699', '048', '561', '492', '564', '476', '569', '118', '349', '493', '139', '495', '315', '230', '590', '425', '130', '454', '494', '055', '365', '361', '132', '491', '698', '218', '013', '574', '530', '213', '313', '533', '543', '527', '364', '215', '324', '217', '592', '302', '343', '453', '700', '509', '375', '136', '470', '403', '591', '518', '566', '305', '587', '133', '327', '536', '137', '338', '236', '531', '507', '514', '141', '529', '342', '532', '058', '538', '231', '140', '142', '508', '582', '546', '596', '138', '363', '576', '382', '371', '373', '503', '547', '548', '075', '567', '581', '552', '411', '374', '378', '241', '121', '599', '379', '583', '372', '598', '225', '588', '553', '339', '549', '385', '384', '555']

branch_options = ['Keene II', 'Kirkland', 'Santa Barbara', 'Campbell', 'Greenville', 'Del Mar', 'Auburn', 'RPM Mortgage Danville', 'Danvers', 'Amherst', 'North Fort Myers', 'The Logemann Group', 'Lexington', 'Seattle', 'Carmel', 'Los Angeles', 'AEM Lutz', 'San Diego', 'Tewksbury', 'Manhattan Beach', 'Orinda - 408', 'Alamo', 'Worthington | Columbus', 'Vista', 'Bedford', 'Kennesaw', 'Greenville II', 'Newport Beach - Dove Street', 'Benicia ', 'Portsmouth', 'Columbus', 'Lancaster', 'RPM Portland', 'Rocky River', 'Scottsdale', 'Tahoe City', 'Tampa', 'Newport Beach', 'Cape Coral', 'Miami 585', 'West LA', 'West Chester', 'Huron', 'Roseville', 'Gig Harbor', 'Ontario-OH - 575', 'Grove City - 571', 'Mt. Pleasant', 'Brunswick', 'Independence', 'Concord', 'Berkeley', 'Nashua', 'Lake Oswego', 'Keene', 'Huntington Beach', 'Heath', 'Zephyr Cove', 'RPM Mortgage San Rafael', 'Rancho Santa Fe', 'Irvine - 311', 'Walnut Creek - Shadelands', 'Naples Golden Gate', 'Zanesville', 'Norcross II', 'Washington Court House', None, 'Walnut Creek', 'Naples - Galleria Court', 'Cartersville', 'Temecula', 'Denver', 'Ontario-CA', 'Capitola', 'Napa', 'San Luis Obispo', 'Bakersfield-RPM', 'LendUS Loyalty', 'MFI - Fort Lauderdale', 'Torrance', 'Costa Mesa', 'Charlotte', 'Naples', 'South Burlington', 'Sonoma/Wine Country', 'El Paso 516', 'Bangor', 'Portland', 'Regency- Greenfield, MA', 'San Antonio', 'Orinda-Suite 8', 'Daphne', 'Naples - 520', 'Petaluma', 'San Juan Capistrano', 'Jacksonville', 'Pleasanton West Neal', 'Beverly', 'Conway', 'Billings', 'Middletown', 'Mill Valley', 'Chattanooga', 'RPM Mortgage Tempe', 'Fort Myers', 'Missoula', 'Corona', 'Seattle II', 'Kalispell', 'Victorville', 'Colchester', 'Southlake', 'Buford - Disabled', 'Park City', 'Encinitas', 'Whitefish', 'Newport', 'The Del Mar Group at Huntington Beach', 'Tahoe Vista', 'Boca Raton', 'Alamo II', 'South Jordan', 'Mason', 'Bigfork', 'Vista AZ', 'Atkinson', 'Newport Beach II', 'Hookset', 'Marion', 'Brentwood', 'Norcross', 'Irvine II', 'Chadds Ford', 'Florence', 'Madison (503)', 'Huntersville', 'Polizzi Branch', 'Lynnfield', 'Buford II', 'Conyers', 'Whitehall(343)', 'Los Angeles - 301', 'Calabasas', 'Miami - Disabled 2', 'Atascadero', 'Hilliard', 'Vancouver', 'RPM Mortgage San Francisco Letterman PUI', 'Suwanee', 'Franklin', 'Polizzi Alamo 401', 'Englewood', 'Spartanburg', 'Portland II', 'Willard', 'MFI - North Fort Myers', 'Greenville IV', 'Fort Lauderdale II', 'Gilbert', 'Tucker', 'Louisville', 'El Paso', 'Regency- Naples, FL', 'Stowe', 'Spokane', 'Gilford, NH', 'Fort Lauderdale', 'Plantation', 'Santa Rosa', 'Westford', 'Mt. Vernon', 'Columbus Steren', 'The Del Mar Group at Manhattan Beach', 'Crandall', 'Bradenton', 'Reno (373)', 'Bakersfield', 'Alpharetta', 'Nashville', 'Palos Verdes Estates', 'Chesapeake', 'Regency - York, ME', 'West Hills for Cost Center Only', 'Hickory', 'Whitehall', 'San Rafael', 'Murray', 'Condado', 'Mobile', 'Nashville HLO', 'Oakland', 'Knoxville', 'Cocoa', 'West Linn', 'Lake Wylie', 'Macon', 'New Braunfels', 'Nokomis', 'Northridge', 'Lake Oswego LendUS', 'Blaine', 'Poulsbo', 'Rancho Cucamonga', 'Norwalk']
region_options = ['REG', 'PNW-WA', 'NORCAL', 'SC', 'Independent', None, 'NEOH', 'SOCAL', 'TAFL', 'CEOH', 'KEGA', 'PNW-AZ/OR', 'SWFL', 'CORP', 'PA', 'CAGA', 'HLO', 'MT', 'N/A', 'BUGA', 'SCA2', 'MSP', 'PR']
loan_program_options = ['VA30FIX', 'C30FIX', 'J7/1INTARM', 'J30FIX', 'CHENOAFHA', 'OHOFHA', 'C10FIX', 'CJ30FIX', 'C30HOME', 'JFHA30 FIX', 'FHA30FIX', 'J7/1LIBOR', 'J5/1LIBOR', 'USDA30FIX', 'FLFHFCHFAPREF', 'BOND', 'C7/1LIBOR', 'C15FIX', 'J10/1 LIB', 'CJ20FIX', 'OHCOMMFIRS', 'C20FIX', 'CJ15FIX', 'SEC30/30', 'NHHFAHMPREF', 'FHA15 FIX', 'J5/1INTARM', 'JVA30FIX', 'MEFHAADV', 'J40INT', 'C5/1 LIB', 'NHHFA+FHA', 'J15FIX', 'NHHFA+FHAMCC', 'MAHMPREF', 'FLFHFCFIRST', 'NHHFA203K', 'J20FIX', 'MEADVMOBILE', 'CAFIXGSFAPLAT', 'AZFXHOME+', 'MEFIXADV', 'VA5/1ARM', 'C15HOME', 'NHHFAFHA', 'PISCATAQUA5/1ARM', 'C20HOME', 'NHHFAUSDAMCC', 'C10/1 LIB', 'C30REFI+', 'VA15FIX', 'NHHFA+203KMCC', 'FHA30203K', 'BONDSEC', 'NHHFA203KMCC', 'AZFHAHOME5DAP', 'NHHFAFHAMCC', 'CJ30HOME', 'CJ10/1 LIB', 'C25FIX', 'MEVAADV', 'AZFXPATHPUR', 'VA25FIX', 'NHHFA+USDAMCC', 'FHA30203SL', 'CAFHAGSFAPLAT', 'Home Possible 30 Yr Fixed (II8/JJ6)', 'FHA30 SL', 'CJ7/1 LIB', 'SCHFHA1st', 'MEADVUSDA', 'J30INT', 'C7/1I/OLIB', 'FHA20FIX', 'MEUGPMI', 'MEUSDA', 'J7/1LIBREX', 'J10/1IOLIB', 'NHHFA+203K', 'VTHFAMOVCONV', 'VA20FIX', 'FLFHFCSEC', 'PISCATAQUA10/1ARM', 'C40INT', 'VA30 NHF', 'NHHFAUSDA', 'J3/1LIBOR', 'MEVA', 'J5/1LIBREX', 'MEADV203K', 'SEC20/20', 'AZFHAHOME+', 'MEFIX', 'J5/5ARM', 'OHOHFA203K', 'FHA 5/1 ARM  1.75 Margin (1605)', 'MAHM100', 'NHHFA+USDA', 'C15REFI+', 'J10/1IOL40', 'AZFXHOME5DAP', 'C20REFI+', 'SEC15/15', None, 'MEFHA', 'MEMOBILE', 'J7/6SOFR', 'J5/6SOFR', 'AZFXPATHPURDAP', 'HELOC 30', 'ME203K', 'BRIDGE LOAN', 'J10/6SOFR', 'J5/1ARM', 'JFHA5/1ARM', 'Home Possible Advantage 30 Yr Fixed DISCONTINUED 7', 'C25HOME', 'J5/1INT40', 'CJ5/1 LIB', 'CJ25FIX', 'J15ARM', 'FHA25 SL', 'J40FIX', 'VTHFACONV', 'LEL', 'VA10FIX', 'FHA15 SL', 'JFHA30SL', 'J7/1INT40', 'FHA25FIX', 'CJ10FIX', 'J10FIX', 'J25FIX', 'C7/6SOFR', 'FHA20 SL', 'C10/6SOFR', 'SEC30INT', 'C5/6SOFR']


# Create a responsive layout with 2-3 columns based on the width of the screen
num_cols = 3
cols = st.columns(num_cols)

# Dictionary to hold the form inputs
input_data = {}

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

# Create input fields with dropdowns for specified fields and text inputs for others
for index, field in enumerate(fields):
    col_index = index % num_cols
    with cols[col_index]:
        if field == 'CostCenter':
            input_data[field] = st.selectbox(field, cost_center_options)
        elif field == 'Branch':
            input_data[field] = st.selectbox(field, branch_options)
        elif field == 'Region':
            input_data[field] = st.selectbox(field, region_options)
        elif field == 'LoanProgram':
            input_data[field] = st.selectbox(field, loan_program_options)
        elif "Date" or "ModifiedTimestamp" in field:
            # Use date input for fields containing 'Date'
            input_data[field] = st.date_input(field, datetime.today())
        else:
            # Use text input for all other fields
            input_data[field] = st.text_input(field)

        # Perform validation and show error if needed
        field_errors = validate_input(field, input_data[field])
        if field_errors:
            for err in field_errors:
                st.error(err)

# Button to submit the form
if st.button('Submit'):
    # Here you can handle the form submission, like saving the data to a database
    # For demonstration, the input data is printed on the screen
    st.json(input_data)

# To run this app, save the above code to a file and run it with: streamlit run your_script.py
