# coding=utf-8
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from models import *

df = pd.read_csv('data/online_shoppers_intention.csv', header=0)
print(df.columns)
print(df.head(5))
attributes = np.array(df.columns[:-1])
raw_data = df.to_numpy()
print(raw_data)
enc = LabelEncoder()
for i in [10, 15, 16, 17]:
    a = raw_data[:, i].reshape(-1, 1)
    # print(a.shape)
    raw_data[:, i] = enc.fit_transform(raw_data[:, i])

vectors = raw_data[:, :-1]
targets = raw_data[:, -1]
targets = targets.astype('int')
print(vectors.shape)
print(targets.shape)
print(vectors)
print(targets)

x_train, x_test, y_train, y_test = train_test_split(vectors, targets,
                                                    test_size=0.2,
                                                    random_state=0)

# naive_bay(x_train, y_train, x_test, y_test)
# linear_svm(x_train, y_train, x_test, y_test)
# logic_reg(x_train, y_train, x_test, y_test)
# knn(x_train, y_train, x_test, y_test)
# decision_tree(x_train, y_train, x_test, y_test)
random_forest(x_train, y_train, x_test, y_test)
