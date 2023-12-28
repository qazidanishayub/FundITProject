import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin

class CustomLabelEncode(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        transformed_data = np.empty_like(X, dtype=int)
        for i in range(X.shape[1]):
            encoded_column = LabelEncoder().fit_transform(X[:, i])
            transformed_data[:, i] = encoded_column
        return transformed_data

class DateTimeScaler(BaseEstimator, TransformerMixin):
    def __init__(self, min_value):
        self.min_value = min_value

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for column in X.columns:
            X[column] = (X[column] - self.min_value[column]).dt.days
        return X

def preprocess_input(input_data):
    # Extract numerical, categorical, and datetime columns
    numerical_cols = ['APR', 'CashoutToBorrower', 'DTI', 'FICO', 'QualifyingHousingRatio',
                      'PropertyZip', 'TotalPrice', 'TotalLoanAmount', 'PrimaryBorrowerZip',
                      'AppraisalValue', 'TotalPayment', 'CLTV', 'InterestRate', 'LTV', 'Points']

    datetime_cols = ['SubmittedToInvestorDate', 'FundingDate', 'ModifiedTimestamp',
                     'LockExpirationDate', 'CreateDate', 'PlannedClosingDate', 'LockDate']

    categorical_cols = ['Investor', 'propertyCounty', 'PrimaryBorrowerCity', 'PropertyCity',
                        'CostCenter', 'Branch', 'Region', 'LoanProgram']

    # Create DataFrame from input data
    input_df = pd.DataFrame({key: [input_data[key]] for key in input_data})

    # Separate columns based on data type
    numerical_data = input_df[numerical_cols]
    datetime_data = input_df[datetime_cols]
    categorical_data = input_df[categorical_cols]

    # Load the preprocessor pipeline
    # Replace 'preprocessor.pkl' with the actual filename you saved your preprocessor as
    preprocessor = joblib.load('preprocessor_pipeline_purchase.pkl')

    # Apply the preprocessor pipeline to the input data
    numerical_transformed = preprocessor.named_transformers_['num'].transform(numerical_data)
    categorical_transformed = preprocessor.named_transformers_['cat'].transform(categorical_data)
    datetime_transformed = preprocessor.named_transformers_['datetime'].transform(datetime_data)

    # Combine the transformed data
    processed_input = np.concatenate([numerical_transformed, categorical_transformed, datetime_transformed], axis=1)

    return processed_input
