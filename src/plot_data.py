import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train_file = "../data/preprocessed_train.csv"
train_data = pd.read_csv(train_file)


# plot PClass and Sex
# sns.countplot(x="Pclass", hue="Sex", data=df_survived)

# plot Embarked
# fig, (axis1, axis2, axis3) = plt.subplots(1, 3, figsize=(15, 5))
# sns.countplot(x="Embarked", data=train_data, order=['S', 'C', 'Q'], ax=axis1)
# sns.countplot(x="Survived", hue="Embarked", data=train_data, ax=axis2)
#
# embark_mean = train_data[["Embarked", "Survived"]].groupby(["Embarked"], as_index=False).mean()
# sns.barplot(x="Embarked", y="Survived", data=embark_mean, order=['S', 'C', 'Q'], ax=axis3)

# plot Age
# train_data["Age"].astype(int).hist(bins=70)

# plot Fare
# df_fare_survived = train_data["Fare"][train_data["Survived"] == 1]
# df_fare_not_survived = train_data["Fare"][train_data["Survived"] == 0]
# avg_fare = DataFrame([df_fare_not_survived.mean(), df_fare_survived.mean()])
# std_fare = DataFrame([df_fare_not_survived.std(), df_fare_survived.std()])
# train_data["Fare"].plot(kind="hist", figsize=(15, 3), bins=100, xlim=(0, 600))
# avg_fare.plot(yerr=std_fare, kind="bar", legend=False)

def plot_bar(label, data):
    sns.set_color_codes("pastel")
    total = data[[label, "Survived"]]
    total["Survived"] = 1
    total = total.groupby([label], as_index=False).sum()
    sns.barplot(x=label, y="Survived", data=data, label="Total", color="b")
    sns.set_color_codes("muted")
    survived = data[[label, "Survived"]].groupby([label], as_index=False).sum()
    sns.barplot(x=label, y="Survived", data=survived, label="Survived", color="b")


# plot SibSp
#plot_bar("SibSp", train_data)

# plot Parch
#plot_bar("Parch", train_data)

family = pd.DataFrame({'Survived': train_data["Survived"], 'Family': train_data["Parch"] + train_data["SibSp"]})
family["Family"][family["Family"] > 0] = 1

plt.show()
