
import pickle
import pandas as pd
from sklearn.metrics import f1_score

model = pickle.load(open('samplemodel.pkl', 'rb'))

test_data_df = pd.read_csv('testdata.csv')

predictions = model.predict(test_data_df[['col1', 'col2']])

print(predictions)

f1_metric = f1_score(test_data_df['col3'], predictions)

print(f1_metric)