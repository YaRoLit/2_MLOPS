import pandas as pd

df_test = pd.read_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/test.csv', index_col='PassengerId')
df_train = pd.read_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/train.csv', index_col='PassengerId')


new_df_test = df_test[['Pclass', 
                       'Sex', 
                       'Age', 
                       'SibSp', 
                       'Parch', 
                       'Fare', 
                       'Cabin', 
                       'Embarked']]

new_df_train = df_train[['Pclass', 
                         'Sex', 
                         'Age', 
                         'SibSp', 
                         'Parch', 
                         'Fare', 
                         'Cabin', 
                         'Embarked',
                         'Survived']]


new_df_test.to_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/new_test.csv', index=False)
new_df_train.to_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/new_train.csv', index=False)