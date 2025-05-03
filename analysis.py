import pandas as pd
#from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
#import joblib

df = pd.read_csv('Financial_inclusion_dataset.csv')
df = df.drop('uniqueid', axis=1)
#transforming binary features to numerical
#df['bank_account'] = df['bank_account'].map({'True': 1, 'False': 0})
df['location_type'] = df['location_type'].map({'Urban':1,'Rural':0})
df['cellphone_access'] = df['cellphone_access'].map({'Yes': 1, 'No': 0})
df['gender_of_respondent'] = df['gender_of_respondent'].map({'Male': 1, 'Female': 0})

#encode the remaining categorical non binary features
df_encoded = pd.get_dummies(df, columns=['country', 'marital_status','relationship_with_head', 'education_level', 'job_type'])

X = df_encoded.drop('bank_account', axis=1)
y = df_encoded['bank_account']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print('Accuracy: {:.2f}'.format(logreg.score(X_test, y_test)))
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
feature_names = X_train.columns


# After training
#joblib.dump(logreg, 'model.pkl')