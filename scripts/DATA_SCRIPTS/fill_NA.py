import pandas as pd

df_test = pd.read_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/new_test.csv')
df_train = pd.read_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/new_train.csv')


# Заполняем возраст медианным значением
df_train['Age'] = df_train['Age'].fillna(df_train['Age'].median())
df_test['Age'] = df_test['Age'].fillna(df_test['Age'].median())


# Заполняем пропуски в Cabin
df_test['Cabin'] = df_test['Cabin'].fillna(0)
df_train['Cabin'] = df_train['Cabin'].fillna(0)
df_test.Cabin[df_test.Cabin != 0] = 1
df_train.Cabin[df_train.Cabin != 0] = 1


# Переводим в числовые значения пол и другие фичи
df_test.Sex = df_test.Sex.astype('category').cat.codes
df_test.Embarked = df_test.Embarked.astype('category').cat.codes
df_train.Sex = df_train.Sex.astype('category').cat.codes
df_train.Embarked = df_train.Embarked.astype('category').cat.codes


# В финале прогоняем циклом чтобы заполнить оставшиеся пропуски медианой
for column in df_train.columns:
    df_train[column] = df_train[column].fillna(df_train[column].median())
    
for column in df_test.columns:
    df_test[column] = df_test[column].fillna(df_test[column].median())


# Всё сохраняем для благодарных потомков
df_test.to_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/ed_test.csv', index=False)
df_train.to_csv('/home/data_srv_admin/projects/2_MLOPS/data/RAW/ed_train.csv', index=False)