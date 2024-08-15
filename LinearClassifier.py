import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#This function splits a dataset into two subsets: a training set and a testing set
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
#This function computes the accuracy of a classification model
from sklearn.metrics import classification_report

#loading the dataset
iris = load_iris()
x = iris.data 
y = iris.target #labels

#visualizing it
plt.scatter(x[:, 0], x[:, 1], c = y,cmap='viridis')
#x[:, 0]: This selects the first column of the x array. It represents the x-coordinates of the data points for the scatter plot
#By setting c=y, the color of each point will correspond to its category in the y array
#This argument sets the colormap used for coloring the data points. The viridis colormap is a popular choice that transitions from 
# green (low values) to yellow and red (high values)
plt.show()

#splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
#test_size=0.2:specifies that 20% of the data will be for testing, and the remaining 80% will be for training
#random_state=42: This argument sets a random seed for splitting the data. This ensures that we get the same random elements splited 
# every time we run the code

#creating the perceptors model
per = Perceptron(tol=1e-3, random_state=0)
#tol=1e-3: This argument specifies the tolerance level for the model. It essentially sets a threshold for how close the model's predictions
#  need to be to the actual labels before it stops training

#training the model
per.fit(x_train, y_train)

#make predictions
y_pred = per.predict(x_test)

print(classification_report(y_test, y_pred))

