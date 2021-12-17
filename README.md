# Voting_data_analysis
Voting data analysis using decision tree and distance metrics like information gain and gini index

In this project, the voting data is analysed and a prediction is made for a test set as to whom the person with the given characterictics is more probable to vote.

The file dtree1.py has the decision tree algorithm with information gain as the metric for split. The file dtree2.py has the decision tree algorithm with gini index as the split metric.
Party_3.py is the main file where the voting data is taken and either information gain or gini index is used for the decision tree and predictions are made on the test set of information.

The voting data is preprocessed to remove the unknown values from the voting data. For the missing values, the minimum value for that attribute is chosen and the missing value is replaced with this value.
