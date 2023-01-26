import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("tennis_stats.csv")
plt.scatter(df["Wins"], df["Aces"], alpha=0.4)
plt.show()
plt.close()


# perform exploratory analysis here:
#One feature model
features = df[['DoubleFaults']]
outcome = df[["Wins"]]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
model = LinearRegression()
model.fit(features_train, outcome_train)
prediction = model.predict(features_test)
print("Test_Score:")
print(model.score(features_test,outcome_test))
print("Train_Score:")
print(model.score(features_train,outcome_train))
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()
plt.close()

#Two feature model
features = df[['DoubleFaults', "TotalServicePointsWon"]]
outcome = df[["Wins"]]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
model = LinearRegression()
model.fit(features_train, outcome_train)
prediction = model.predict(features_test)
print("Test_Score:")
print(model.score(features_test,outcome_test))
print("Train_Score:")
print(model.score(features_train,outcome_train))
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()
plt.close()


#Two feature model winnigs
features = df[['DoubleFaults', "TotalServicePointsWon"]]
outcome = df[["Winnings"]]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
model = LinearRegression()
model.fit(features_train, outcome_train)
prediction = model.predict(features_test)
print("Test_Score:")
print(model.score(features_test,outcome_test))
print("Train_Score:")
print(model.score(features_train,outcome_train))
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()
plt.close()

