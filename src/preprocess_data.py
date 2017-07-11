import pandas as pd

train_file = "../data/train.csv"
train_data = pd.read_csv(train_file)

train_data = train_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

train_data = train_data.dropna(how='any')
# train_data['Sex'] = (train_data['Sex'] == 'male').astype(int)

# mapping = {'C': 0, 'Q': 1, 'S': 2}
# train_data = train_data.replace({'Embarked': mapping})

train_data.to_csv("../data/preprocessed_train.csv", index=False)