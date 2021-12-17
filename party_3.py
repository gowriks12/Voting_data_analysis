# Code to run the decision tree on the Party dataset ##

# Implemented by Stephen Marsland
# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.
type = int(input("Press 1 for info_gain and 2 for gini_index \n"))
print(type)
import dtree1
tree = dtree1.dtree1()
if type == 2:
    import dtree2
    tree = dtree2.dtree2()
    print("Using Gini_index")
else:
    print("Using Information gain")

train_data, test_data, train_class, test_class, features = tree.read_data('voting_data_cleaned.csv')
t = tree.make_tree(train_data, train_class, features)
tree.printTree(t, ' ')

print('train classes', train_class[:5])
print("Train classification")
train_classi=tree.classifyAll(t, train_data)
print(train_classi[:5])

for i in range(len(test_data)):
    tree.classify(t, test_data[i])


test_classi = tree.classifyAll(t, test_data)
print("test classes", test_class[:5])
print("Test classified", test_classi[:5])
wrong = 0

for i in range(len(test_class)):
    if test_class[i] != test_classi[i]:
        wrong += 1

print("Test error = ", (wrong / len(test_data)))
