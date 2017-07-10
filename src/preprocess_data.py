import pandas as pd

train_file = "../data/train.csv"
train_data = pd.read_csv(train_file)

del train_data['Name']
del train_data['Ticket']
del train_data['Cabin']

train_data = train_data.dropna(how='any')
train_data['Sex'] = (train_data['Sex'] == 'male').astype(int)

mapping = {'C': 0, 'Q': 1, 'S': 2}
train_data = train_data.replace({'Embarked': mapping})

train_data.to_csv("../data/preprocessed_train.csv", index=False)