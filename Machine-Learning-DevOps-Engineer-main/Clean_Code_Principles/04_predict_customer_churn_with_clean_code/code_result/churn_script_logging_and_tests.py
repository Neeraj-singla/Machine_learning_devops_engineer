"""
This module contains functions to test the churn_library functions

author: jazielinho
created: 2024 July
"""


import os
import pytest
import pandas as pd
from churn_library import (
    import_data, perform_eda, encoder_helper,
    perform_feature_engineering, train_models, logging
)

DATA_PATH = './data/bank_data.csv'


@pytest.fixture(scope="module", name="bank_data")
def bank_data_fixture():
    """
    Fixture to import the data
    """
    return import_data(DATA_PATH)


def test_import_data(bank_data: pd.DataFrame):
    """
    Test the import_data function
    input:
            bank_data: the output of the import_data function
    """
    logging.info("Testing the import_data function")
    assert isinstance(bank_data, pd.DataFrame), "Output is not a pandas DataFrame"
    assert 'Attrition_Flag' in bank_data.columns, "Attrition_Flag column is missing"
    assert 'Churn' in bank_data.columns, "Churn column is missing"


def test_perform_eda(bank_data: pd.DataFrame):
    """
    Test the perform_eda function
    input:
            bank_data: the output of the import_data function
    """
    logging.info("Testing the perform_eda function")
    perform_eda(bank_data)
    assert os.path.exists('./images/eda/Churn.png'), "Churn plot was not created"
    assert os.path.exists('./images/eda/Customer_Age.png'), "Customer_Age plot was not created"
    assert os.path.exists('./images/eda/Marital_Status.png'), "Marital_Status plot was not created"
    assert os.path.exists('./images/eda/Total_Trans_Ct.png'), "Total_Trans_Ct plot was not created"
    assert os.path.exists('./images/eda/corr_heatmap.png'), "Correlation heatmap was not created"


def test_encoder_helper(bank_data: pd.DataFrame):
    """
    Test the encoder_helper function
    input:
            bank_data: the output of the import_data function
    """
    logging.info("Testing the encoder_helper function")
    category_lst = [
        'Gender', 'Education_Level',
        'Marital_Status', 'Income_Category',
        'Card_Category'
    ]
    dataframe = encoder_helper(bank_data, category_lst, 'Churn')
    for category in category_lst:
        assert f"{category}_Churn" in dataframe.columns, f"{category}_Churn column is missing"


def test_perform_feature_engineering(bank_data: pd.DataFrame):
    """
    Test the perform_feature_engineering function
    input:
            bank_data: the output of the import_data function
    """
    logging.info("Testing the perform_feature_engineering function")
    train_df, test_df, y_train, y_test = perform_feature_engineering(bank_data, 'Churn')
    assert not train_df.empty, "X_train is empty"
    assert not test_df.empty, "X_test is empty"
    assert not y_train.empty, "y_train is empty"
    assert not y_test.empty, "y_test is empty"


def test_train_models(bank_data: pd.DataFrame):
    """
    Test the train_models function
    input:
            bank_data: the output of the import_data function
    """
    logging.info("Testing the train_models function")
    train_df, test_df, y_train, y_test = perform_feature_engineering(bank_data, 'Churn')
    train_models(train_df, test_df, y_train, y_test)
    assert os.path.exists(
        './models/rf_model.pkl'
    ), "Random forest model was not saved"
    assert os.path.exists(
        './models/logistic_model.pkl'
    ), "Logistic regression model was not saved"
    assert os.path.exists(
        './images/results/rf_classification_report.png'
    ), "Random forest classification report was not created"
    assert os.path.exists(
        './images/results/lr_classification_report.png'
    ), "Logistic regression classification report was not created"
    assert os.path.exists(
        './images/results/rf_feature_importance.png'
    ), "Random forest feature importance plot was not created"
    assert os.path.exists(
        './images/results/lr_feature_importance.png'
    ), "Logistic regression feature importance plot was not created"


if __name__ == "__main__":
    pytest.main()
