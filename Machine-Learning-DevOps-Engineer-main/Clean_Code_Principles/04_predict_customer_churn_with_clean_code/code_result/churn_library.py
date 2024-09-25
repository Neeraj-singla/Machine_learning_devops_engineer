"""
This module contains functions to:
* import data
* perform eda
* feature engineering
* train models
* store results

author: jazielinho
created: 2024 July
"""

from typing import List, Tuple, Union
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib


logging.basicConfig(
    filename='./logs/churn_library.log',
    level = logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)


def import_data(pth: str) -> pd.DataFrame:
    """
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            dataframe: pandas dataframe
    """
    try:
        logging.info('Importing data from %s', pth)
        dataframe = pd.read_csv(pth)
        dataframe['Churn'] = (dataframe['Attrition_Flag'] != "Attrited Customer").astype(int)
        return dataframe
    except FileNotFoundError as err:
        logging.error('File not found at %s', pth)
        raise err
    except Exception as err:
        logging.error('An error occurred while importing data from %s, %s', pth, err)
        raise err


def _plot_categorical(dataframe: pd.DataFrame, category: str):
    """
    helper function to plot categorical data
    input:
            dataframe: pandas dataframe
            category: string of category column
    output:
            None
    """
    plt.figure(figsize=(20, 10))
    dataframe[category].value_counts(normalize=True).plot(kind='bar')
    plt.savefig(f'./images/eda/{category}.png')
    plt.close()


def _plot_numerical(dataframe: pd.DataFrame, category: str, add_density: bool):
    """
    helper function to plot numerical data
    input:
            dataframe: pandas dataframe
            category: string of category column
    output:
            None
    """
    plt.figure(figsize=(20, 10))
    sns.histplot(dataframe[category], stat='density', kde=add_density)
    plt.savefig(f'./images/eda/{category}.png')
    plt.close()


def _plot_correlation(dataframe: pd.DataFrame):
    """
    helper function to plot correlation
    input:
            dataframe: pandas dataframe
    output:
            None
    """
    plt.figure(figsize=(20, 10))
    sns.heatmap(dataframe.corr(numeric_only=True), annot=False, cmap='Dark2_r', linewidths=2)
    plt.savefig('./images/eda/corr_heatmap.png')
    plt.close()


def perform_eda(dataframe: pd.DataFrame):
    """
    perform eda on dataframe and save figures to images folder
    input:
            dataframe: pandas dataframe

    output:
            None
    """
    try:
        logging.info('Performing EDA')
        logging.info('Plotting Churn')
        _plot_categorical(dataframe, 'Churn')
        logging.info('Plotting Customer_Age')
        _plot_numerical(dataframe, 'Customer_Age', False)
        logging.info('Plotting Marital_Status')
        _plot_categorical(dataframe, 'Marital_Status')
        logging.info('Plotting Total_Trans_Ct')
        _plot_numerical(dataframe, 'Total_Trans_Ct', True)
        logging.info('Plotting correlation')
        _plot_correlation(dataframe)
    except Exception as err:
        logging.error('An error occurred during EDA, %s', err)
        raise err


def encoder_helper(dataframe: pd.DataFrame, category_lst: List[str], response: str) -> pd.DataFrame:
    """
    helper function to turn each categorical column into a new column with
    proportion of churn for each category - associated with cell 15 from the notebook

    input:
            dataframe: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name

    output:
            dataframe: pandas dataframe with new columns for
    """
    category = None
    try:
        logging.info('Encoding categorical features')
        for category in category_lst:
            logging.info('Encoding %s', category)
            groups = dataframe.groupby(category)[response].mean().to_dict()
            dataframe[f'{category}_Churn'] = dataframe[category].map(groups)
        return dataframe
    except Exception as err:
        if category is not None:
            logging.error('An error occurred while encoding %s', category)
        else:
            logging.error('An error occurred while encoding')
        raise err


def _select_features(dataframe: pd.DataFrame, response: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    select features for the model
    input:
              dataframe: pandas dataframe
              response: string of response name

    output:
              X: X data
              y: y data
    """
    try:
        logging.info('Selecting features')
        keep_cols = [
            'Customer_Age', 'Dependent_count', 'Months_on_book',
            'Total_Relationship_Count', 'Months_Inactive_12_mon',
            'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
            'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
            'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
            'Gender_Churn', 'Education_Level_Churn', 'Marital_Status_Churn',
            'Income_Category_Churn', 'Card_Category_Churn'
        ]
        logging.info('Selecting columns %s', keep_cols)
        dataframe_selected = dataframe[keep_cols]
        target = dataframe[response]
        return dataframe_selected, target
    except Exception as err:
        logging.error('An error occurred during feature selection, %s', err)
        raise err


def _split_data(
        dataframe_selected: pd.DataFrame,
        target: pd.Series
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    split data into training and testing
    input:
                dataframe_selected: pandas dataframe
                target: pandas series
    output:
                X_train: X training data
    """
    try:
        logging.info('Splitting data')
        train_df, test_df, y_train, y_test = train_test_split(
            dataframe_selected,
            target,
            test_size=0.3,
            random_state=42
        )
        return train_df, test_df, y_train, y_test
    except Exception as err:
        logging.error('An error occurred during data splitting, %s', err)
        raise err


def perform_feature_engineering(
        dataframe: pd.DataFrame,
        response: str
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    perform feature engineering
    input:
              dataframe: pandas dataframe
              response: string of response name

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    """
    try:
        logging.info('Performing feature engineering')
        dataframe, target = _select_features(dataframe, response)
        train_df, test_df, y_train, y_test = _split_data(dataframe, target)
        return train_df, test_df, y_train, y_test
    except Exception as err:
        logging.error('An error occurred during feature engineering, %s', err)
        raise err


def classification_report_image(
        y_train: pd.Series,
        y_test: pd.Series,
        y_train_preds: pd.Series,
        y_test_preds: pd.Series,
        title: str
):
    """
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds: training predictions
            y_test_preds: test predictions
            title: title for the plot

    output:
             None
    """
    try:
        logging.info('Creating classification report')
        plt.figure(figsize=(10, 10))

        # Ajustar el tamaño de fuente para las diferentes secciones
        plt.text(0.01, 1.05, f'{title} Train', {'fontsize': 14}, fontproperties='monospace')
        plt.text(
            0.01, 0.6,
            str(classification_report(y_train, y_train_preds)), {'fontsize': 12},
            fontproperties='monospace'
        )
        plt.text(0.01, 0.5, f'{title} Test', {'fontsize': 14}, fontproperties='monospace')
        plt.text(
            0.01, 0.0,
            str(classification_report(y_test, y_test_preds)), {'fontsize': 12},
            fontproperties='monospace'
        )

        plt.axis('off')
        plt.tight_layout()

        plt.savefig(f'./images/results/{title}_classification_report.png', bbox_inches='tight')
        plt.close()
    except Exception as err:
        logging.error('An error occurred while creating classification report, %s', err)
        raise err


def feature_importance_plot(
        model: Union[RandomForestClassifier, LogisticRegression],
        train_df: pd.DataFrame,
        output_pth: str
):
    """
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            train_df: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    """

    try:
        logging.info('Plotting feature importance')

        if not hasattr(model, 'feature_importances_') and not hasattr(model, 'coef_'):
            raise ValueError('Model does not have feature_importances_ or coef_ attribute')

        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
        else:
            importances = model.coef_[0]

        indices = np.argsort(importances)[::-1]
        names = [train_df.columns[i] for i in indices]
        plt.figure(figsize=(20, 10))
        plt.title("Feature Importance")
        plt.bar(range(train_df.shape[1]), importances[indices])
        plt.xticks(range(train_df.shape[1]), names, rotation=90)
        plt.savefig(output_pth)
        plt.close()
    except Exception as err:
        logging.error('An error occurred while plotting feature importance, %s', err)
        raise err


def _select_best_random_forest_model(
        train_df: pd.DataFrame,
        y_train: pd.Series
) -> RandomForestClassifier:
    """
    trains random forest model and returns the model
    input:
            X_train: X training data
            X_test: X testing data
            y_train: y training data
            y_test: y testing data

    output:
            rf: trained random forest model
    """
    try:
        logging.info('Training Random Forest')
        rf_model = RandomForestClassifier(random_state=42)
        param_grid = {
            'n_estimators': [200, 500],
            'max_features': ['auto', 'sqrt'],
            'max_depth': [4, 5, 100],
            'criterion': ['gini', 'entropy']
        }
        cv_rfc = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5)
        cv_rfc.fit(train_df, y_train)
        rf_model = cv_rfc.best_estimator_
        return rf_model
    except Exception as err:
        logging.error('An error occurred while training random forest, %s', err)
        raise err


def _get_logistic_regression_model(
        train_df: pd.DataFrame,
        y_train: pd.Series
) -> LogisticRegression:
    """
    trains logistic regression model and returns the model
    input:
            X_train: X training data
            X_test: X testing data
            y_train: y training data
            y_test: y testing data

    output:
            lr: trained logistic regression model
    """
    try:
        logging.info('Training Logistic Regression')
        lr_model = LogisticRegression(solver='lbfgs', max_iter=3000)
        lr_model.fit(train_df, y_train)
        return lr_model
    except Exception as err:
        logging.error('An error occurred while training logistic regression, %s', err)
        raise err


def _get_predictions(
        model: Union[RandomForestClassifier, LogisticRegression],
        train_df: pd.DataFrame,
        test_df: pd.DataFrame
):
    """
    get predictions from model
    input:
            model: model object
            train_df: training data
            test_df: testing data
    output:
            y_train_preds: training predictions
            y_test_preds: testing predictions
    """
    try:
        logging.info('Getting predictions')
        y_train_preds = model.predict(train_df)
        y_test_preds = model.predict(test_df)
        return y_train_preds, y_test_preds
    except Exception as err:
        logging.error('An error occurred while getting predictions, %s', err)
        raise err


def _save_models(model: Union[RandomForestClassifier, LogisticRegression], path: str):
    """
    save model to path
    input:
            model: model object
            path: path to save model
    output:
            None
    """
    try:
        logging.info('Saving model to %s', path)
        joblib.dump(model, path)
    except Exception as err:
        logging.error('An error occurred while saving model to %s, %s', path, err)
        raise err


def _train_rf_model(
        train_df: pd.DataFrame,
        test_df: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series
):
    """
    train random forest model
    input:
            X_train: X training data
            X_test: X testing data
            y_train: y training data
            y_test: y testing data
    output:
            rf_model: trained random forest model
            y_train_preds_rf: training predictions
            y_test_preds_rf: testing predictions
    """
    try:
        rf_model = _select_best_random_forest_model(train_df, y_train)
        y_train_preds_rf, y_test_preds_rf = _get_predictions(rf_model, train_df, test_df)
        feature_importance_plot(rf_model, train_df, './images/results/rf_feature_importance.png')
        classification_report_image(y_train, y_test, y_train_preds_rf, y_test_preds_rf, 'rf')
        _save_models(rf_model, './models/rf_model.pkl')
    except Exception as err:
        logging.error('An error occurred while training random forest model, %s', err)
        raise err


def _train_lr_model(
        train_df: pd.DataFrame,
        test_df: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series
):
    """
    train logistic regression model
    input:
            X_train: X training data
            X_test: X testing data
            y_train: y training data
            y_test: y testing data
    output:
            lr_model: trained logistic regression model
            y_train_preds_lr: training predictions
            y_test_preds_lr: testing predictions
    """
    try:
        lr_model = _get_logistic_regression_model(train_df, y_train)
        y_train_preds_lr, y_test_preds_lr = _get_predictions(lr_model, train_df, test_df)
        feature_importance_plot(lr_model, train_df, './images/results/lr_feature_importance.png')
        classification_report_image(y_train, y_test, y_train_preds_lr, y_test_preds_lr, 'lr')
        _save_models(lr_model, './models/logistic_model.pkl')
    except Exception as err:
        logging.error('An error occurred while training logistic regression model, %s', err)
        raise err


def train_models(
        train_df: pd.DataFrame,
        test_df: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series
):
    """
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    """
    try:
        logging.info('Training models')
        _train_rf_model(train_df, test_df, y_train, y_test)
        _train_lr_model(train_df, test_df, y_train, y_test)
    except Exception as err:
        logging.error('An error occurred while training models, %s', err)
        raise err


def main():
    """
    main function to run the entire module
    """
    dataframe = import_data('./data/bank_data.csv')
    perform_eda(dataframe)
    dataframe = encoder_helper(
        dataframe,
        [
            'Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category'
        ],
        'Churn'
    )
    train_df, test_df, y_train, y_test = perform_feature_engineering(dataframe, 'Churn')
    train_models(train_df, test_df, y_train, y_test)


if __name__ == '__main__':
    main()
