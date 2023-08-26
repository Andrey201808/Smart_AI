import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization
import warnings
import category_encoders as ce
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
data = 'prefix_20230808.csv'
df = pd.read_csv(data)


print('Вхождение search_index-name')
df = pd.read_csv(data)
#df.shape
#df.head()
df.isnull().sum()
X = df['search_index']

y = df['name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
X_train.shape, X_test.shape
X_train.dtypes
X_train.head()

encoder = ce.OrdinalEncoder(cols=['search_index'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)
X_train.head()
X_test.head()

# import Random Forest classifier

from sklearn.ensemble import RandomForestClassifier



# instantiate the classifier 

rfc = RandomForestClassifier(random_state=0)



# fit the model

rfc.fit(X_train, y_train)



# Predict the Test set results

y_pred = rfc.predict(X_test)



# Check accuracy score 

from sklearn.metrics import accuracy_score

print('Точность модели для 10-и деревьев: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# instantiate the classifier with n_estimators = 100

rfc_100 = RandomForestClassifier(n_estimators=100, random_state=0)



# fit the model to the training set

rfc_100.fit(X_train, y_train)



# Predict on the test set results

y_pred_100 = rfc_100.predict(X_test)



# Check accuracy score 

print('Точность модели для 100-и деревьев : {0:0.4f}'. format(accuracy_score(y_test, y_pred_100)))

# create the classifier with n_estimators = 100

clf = RandomForestClassifier(n_estimators=100, random_state=0)



# fit the model to the training set

clf.fit(X_train, y_train)

# view the feature scores

feature_scores = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

# Creating a seaborn bar plot

sns.barplot(x=feature_scores, y=feature_scores.index)



# Add labels to the graph

plt.xlabel('Шкала признаков')

plt.ylabel('Признаки')



# Add title to the graph

plt.title("Визуализация признаков")



# Visualize the graph

plt.show()




