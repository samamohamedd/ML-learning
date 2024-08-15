import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#This function is used to split a dataset into two subsets: a training set and a testing set
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
#This function is used to compute the accuracy of a classification model
from sklearn.metrics import accuracy_score