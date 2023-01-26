import codecademylib3
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data
cols = ['name','landmass','zone', 'area', 'population', 'language','religion','bars','stripes','colours',
'red','green','blue','gold','white','black','orange','mainhue','circles',
'crosses','saltires','quarters','sunstars','crescent','triangle','icon','animate','text','topleft','botright']
df= pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data", names = cols)

#variable names to use as predictors
var = ['red', 'green', 'blue','gold', 'white', 'black', 'orange', 'mainhue','bars','stripes', 'circles','crosses', 'saltires','quarters','sunstars','triangle','animate']

#Print number of countries by landmass, or continent
#print(df['landmass'].value_counts())

#Create a new dataframe with only flags from Europe and Oceania
df_36 = df["landmass"].isin([3,6])

#Print the average vales of the predictors for Europe and Oceania
#print(df_36.groupby('landmass')[var].mean())

#Create labels for only Europe and Oceania
labels = (df["landmass"].isin([3,6]))*1
#print(labels)
#Print the variable types for the predictors


#Create dummy variables for categorical predictors
data = pd.get_dummies(df[var])
print(data)
#Split data into a train and test set
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=42, test_size=.3)
#Fit a decision tree for max_depth values 1-20; save the accuracy score in acc_depth

depths = [*range(1, 21)]
acc_depth = []
items = []

for item in range(1, 21):
  model = DecisionTreeClassifier(max_depth=item)
  model.fit(train_data, train_labels)
  score = model.score(test_data, test_labels)
  acc_depth.append(score)
  items.append(item)
  

#Plot the accuracy vs depth
plt.plot(depths, acc_depth)
plt.show()
plt.close()
print(depths)
print(acc_depth)
#Find the largest accuracy and the depth this occurs
max_acc = np.max(acc_depth)
max_dep = depths[acc_depth.index(max_acc)]
print(max_acc)
print(max_dep)

#Refit decision tree model with the highest accuracy and plot the decision tree
tree1 = DecisionTreeClassifier(max_depth=3)
tree1.fit(train_data, train_labels)
score1 = model.score(test_data, test_labels)
print(score1)
tree.plot_tree(tree1)
plt.show()
plt.tight_layout()
plt.close()


#Create a new list for the accuracy values of a pruned decision tree.  Loop through
#the values of ccp and append the scores to the list
ccp = [0.0, 0.001, 0.002, 0.003, 0.005, 0.007, 0.01, 0.02]
acc_pruned = []
items_1 = []
for item in ccp:
  model = DecisionTreeClassifier(ccp_alpha=item)
  model.fit(train_data, train_labels)
  score = model.score(test_data, test_labels)
  acc_pruned.append(score)
  items_1.append(item)
#Plot the accuracy vs ccp_alpha
plt.plot(ccp, acc_pruned)
plt.show()
plt.close()
max_acc2 = np.max(acc_pruned)
max_ccp = ccp[acc_pruned.index(max_acc2)]
print(max_acc2)
print(max_ccp)

#Find the largest accuracy and the ccp value this occurs


#Fit a decision tree model with the values for max_depth and ccp_alpha found above


#Plot the final decision tree
tree2 = DecisionTreeClassifier(max_depth=3, ccp_alpha=max_ccp)
tree2.fit(train_data, train_labels)
score2 = model.score(test_data, test_labels)
print(score2)
tree.plot_tree(tree2)
plt.show()
plt.tight_layout()
plt.close()
