import pandas as pd
from sklearn import datasets


iris_data = datasets.load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df['target'] = iris_data.target


def slice_iris(df, feature):
    """ Function for calculating descriptive stats on slices of the Iris dataset."""
    for cls in df['target'].unique():
        df_temp = df[df['target'] == cls]
        mean = df_temp[feature].mean()
        stddev = df_temp[feature].std()
        print(f'Class: {cls}, Mean: {mean:.2f}, Std Dev: {stddev:.2f}')
    print('\n')


slice_iris(df, 'sepal length (cm)')
slice_iris(df, 'sepal width (cm)')
slice_iris(df, 'petal length (cm)')
slice_iris(df, 'petal width (cm)')



