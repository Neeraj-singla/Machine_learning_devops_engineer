
import ast
import numpy as np

newr2 = 0.3625

with open('previousscores.txt', 'r') as f:
    r2list = ast.literal_eval(f.read())


firstest = newr2 < np.min(r2list)
print(firstest)

secondtest = newr2 < np.mean(r2list) - 2 * np.std(r2list)
print(secondtest)

iqr = np.percentile(r2list, 75) - np.percentile(r2list, 25)
thirdtest = newr2 < np.percentile(r2list, 25) - 1.5 * iqr
print(thirdtest)


import pandas as pd
import pickle
from sklearn import metrics
import ast
import numpy as np

model = pickle.load(open('l3final.pkl', 'rb'))

testdata = pd.read_csv('testdatafinal.csv')

X = testdata['timeperiod'].values.reshape(-1, 1)
y = testdata['sales'].values.reshape(-1, 1)

predicted = model.predict(X)
print(predicted)

mse = metrics.mean_squared_error(y, predicted)
print(mse)

mselist = ast.literal_eval(open('l3finalscores.txt', 'r').read())

iqr = np.quantile(mselist, 0.75) - np.quantile(mselist, 0.25)
driftest = mse > np.quantile(mselist, 0.75) + 1.5 * iqr
print(driftest)
