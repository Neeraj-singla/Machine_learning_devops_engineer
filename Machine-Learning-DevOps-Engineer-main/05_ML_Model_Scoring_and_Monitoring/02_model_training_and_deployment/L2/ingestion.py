
import pandas as pd
import os


PATH = r'C:\Users\jahaz\OneDrive\Escritorio\Test\mlops_specialization\mlops\05_ML_Model_Scoring_and_Monitoring\02_model_training_and_deployment\L2'

DIRECTORIES = ['data1', 'data2', 'data3']

dfs = []

for directory in DIRECTORIES:
    final_directory = os.path.join(PATH, directory)
    for file in os.listdir(final_directory):
        df = None
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(final_directory, file))
        if file.endswith('.json'):
            df = pd.read_json(os.path.join(final_directory, file))
        if df is None:
            continue
        dfs.append(df)

final_df = pd.concat(dfs, axis=0).reset_index(drop=True)
final_df = final_df.drop_duplicates().reset_index(drop=True)
final_df.to_csv(os.path.join(PATH, 'result.csv'), index=False)
