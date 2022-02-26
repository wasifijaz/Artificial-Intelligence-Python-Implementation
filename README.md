# Artificial-Intelligence-Python-Implementation
## Lab 1
Introduction to Python
### Task 1
If A =5, B = 7 and C = 3, find which number is greatest and which is smallest using IF ELSE conditions. 
### Task 2
Design a calculator which can perform following operations: 
* Take 2 numbers from user. 
* Take choice of operation from user. 
* Perform addition, subtraction, multiplication and division. 
* Display the result. 
## Lab 2
Loops, Function, Tuples, Lists and Dictionary in Python
### Task 1
Write a program of simple calculator program. Follow the steps below, 
* Declare and define a function name Menu which displays a list of choices for user such as addition, subtraction, multiplication etc. It takes the choice from user as an input and return. 
* Define and declare a separate function for each choice. 
* In the main body of the program call respective function depending on user’s choice. 
* Program should not terminate till user chooses last option that is “Quit".
### Task 2
Write a method to calculate Fibonacci Series up to ‘n’ points. 
### Task 3
Write a program to calculate factorial of a number entered by user. 
### Task 4
Make a dictionary in python which should contain following “keys” and their values: “Name” “Reg. No” “Class” “D.O.B” “Gender”
### Home Task 1
Perform all the functions of list mentioned in this lab manual with atleast one example.
### Home Task 2
Write a program that lets the user enter in some English text, then convert the text to Pig-latin.

*To review, Pig-latin takes the first letter of a word, put it at the end, and appends "ay". The only exception is if the first letter is vowel, in which case we keep it as it is and append "hay" to the end. e.g. "hello" -> "ellohay", and "image" -> "imagehay"*
## Lab 3
Classes and Inheritance in Python
### Task 1
Create a class name basic_calc with following attributes and methods; Two integers (values are passed with instance creation) Different methods such as addition, subtraction, division, multiplication Create another class inherited from basic_calc named s_calc which should have the following additional methods; Factorial, x_power_y,log, ln etc class child_class(parent_class): def __init__(self,x):

#it will modify the _init_ function from parent class
#additional methods can be defined
## Lab 4
Arrays, Matrices and Vector Programming in Python
### Task 1
Generate two vectors ranges from 0 to 50. One vector contains first 20 odd numbers and the other should contain first 20 even numbers. Find the sum of both vectors. Find the maximum and minimum numbers and their indices from the resultant vector.
### Task 2
Let A = [[1,2,3],[4,5,6],[7,8,9]] and B = [[5,8,9],[1,3,1],[6,2,4]], find the following: 
* A+B, A-B, A*B, A/B 
* Find the max, min and mean value of A+B and A-B
* Find determinant and transpose of A*B 
* Find trace of A/B
### Task 3
Let A = [ 1 2 3 4 ] and B = [ 1 2 3 4 ] . Find the following and explain the difference: 
* A*B 
* numpy.dot(A,B)
* numpy.matmul(A,B)
### Task 4
Generate array A and B of size 2 x 2, where A should contain all ones and B should contain 
all zeros. Also perform the following: 
* Concatenate both arrays horizontally and find its shape. 
* Concatenate both arrays vertically and find its shape 
* Concatenate both arrays using “np.dstack()” and find its shape.
* Flatten the resultant array of part c (previous step) and find its shape.
## Lab 5
Graph Theory and Path Searches in Python
### Task 1
Write a method to output degree of each node within the graph. Implement the given Graph in Python.

![image](https://user-images.githubusercontent.com/62423571/155850615-3ae6659d-bd0d-47eb-a478-d696281eae2f.png)
### Task 2
Write a method to find any path from node 6 to node 1 in given Graph. Implement the given Graph in Python.

![image](https://user-images.githubusercontent.com/62423571/155850615-3ae6659d-bd0d-47eb-a478-d696281eae2f.png)
## Lab 6
Implementation of Breath First Search and Depth First Search
### Task 1
Apply BFS algorithm to solve the graph shown and display the output. Also display the adjacency list, vertex list and edge list.

![image](https://user-images.githubusercontent.com/62423571/155851604-6a52c25d-689d-4645-a5b8-b365e79a2c5c.png)
### Task 2
Apply DFS algorithm to solve the graph shown and display the output. Also display the adjacency list, vertex list and edge list.

![image](https://user-images.githubusercontent.com/62423571/155851604-6a52c25d-689d-4645-a5b8-b365e79a2c5c.png)
## Lab 7
Implementation of Greedy Best First Search & A*  Search Algorithm
### Task 1
Implement Greedy Best First Search Algorithm for the given example, if starting node is Arad and goal node is Bucharest.
### Task 2
Implement A* Algorithm for the graph given in Task1, if starting node is Arad and goal node is Bucharest.
## Lab 9
Implementation of K-nearest Neighbor Classification Model
### Task 1
Write a program to implement KNN classifier and classify given vector. (for k = 3)
| Age | Loan   | Class (Defaulter) |
|-----|--------|-------------------|
| 25  | 40000  | N                 |
| 35  | 60000  | N                 |
| 45  | 80000  | N                 |
| 20  | 20000  | N                 |
| 35  | 120000 | N                 |
| 52  | 18000  | N                 |
| 23  | 95000  | Y                 |
| 40  | 62000  | Y                 |
| 60  | 100000 | Y                 |
| 48  | 220000 | Y                 |
| 33  | 150000 | Y                 |
| 48  | 142000 | ?                 |
### Task 2
Modify Task 1 and perform it for all odd values of k from 1 to 10. 
* Find accuracy for each value of k and display. 
* Find the best k which gives highest value of accuracy 
* Also compute confusion matrix for the best value of k.
### Task 3
Implement KNN algorithm yourself in python for Iris Dataset without using built-in KNN classifier library. 
* Load dataset 
* Split dataset into test and train sets 
* Perform KNN algorithm to make predictions for k=5 
* Compute accuracy and confusion matrix
## Lab 10
Naïve Bayes Classification Model
### Task 1 
Develop a python program to implement Bayesian classification model for the following dataset and classify the given test vector:
| Age | Loan   | Class (Defaulter) |
|-----|--------|-------------------|
| 25  | 40000  | 0                 |
| 35  | 60000  | 0                 |
| 45  | 80000  | 0                 |
| 20  | 20000  | 0                 |
| 35  | 120000 | 0                 |
| 52  | 18000  | 0                 |
| 23  | 95000  | 1                 |
| 40  | 62000  | 1                 |
| 60  | 100000 | 1                 |
| 48  | 220000 | 1                 |
| 33  | 150000 | 1                 |
| 48  | 142000 | ?                 |
### Task 2
Use the given cancer dataset and classify it using Bayesian classification model: 
* First create a python script and load ‘breast_cancer’ file. 
* Identify features and classes from the loaded dataset.
* Perform 2-fold cross validation on the dataset by splitting it into testing and training parts.
* Implement a Bayesian classifier using the above algorithm and use training dataset to classify each of the sample within testing dataset. 
* Compute the accuracy from the predicted test samples.
## Lab 11
Implementation of Support Vector Machine Classification Model
### Task 1
* Import “breast cancer”data, split the data into a test and train dataset, train a SVM, and predict with the SVM using 10-fold cross validation. 
* Implement for linear svm.
* Compute accuracy and confusion matrix.
### Task 2
Perform SVM for blobs dataset by taking 400 samples and 2 features. 
* Compute accuracy
* Plot the decision boundary
## Lab 12
K-means Clustering
### Task 1
Implement k-means algorithm on iris dataset. 
* Take 70% training data and 30% testing data using train-test split. 
* Compute Accuracy and time taken by algorithm. 
### Task 2
Take blobs dataset and cluster it using K-means 
* Take 400 samples and 4 features. 
* Plot result for K=3,4,5 
## Lab 13
Implementation of Agglomerative Clustering
### Task
Implement Single Linkage and Complete Linkage agglomerative clustering for blobs dataset with 500 samples and 5 features. Plot results for N = 5,6,7. Compute the time taken by both algorithms and also compare the results.
## Lab 14
Single Layered Feed Forward Neural Network (Perceptron)
### Task 1
Develop a python application to implement perceptron for the following dataset. Use learning rate of 0.1 with zero biasing factor and initialize all the weights with 0:
| x0 | x1 | x2 | class |
|----|----|----|-------|
| 1  | 0  | 0  | 1     |
| 1  | 0  | 1  | 1     |
| 1  | 1  | 0  | 1     |
| 1  | 1  | 1  | 0     |
### Task 2
Use the given cancer dataset and classify it using perceptron:
* First create a python script and load ‘cancer’ file.
* Identify features and classes from the loaded dataset.
* Perform 2-fold cross validation on the dataset by splitting it into testing and training parts.
* Implement the perceptron using the above algorithm and use training dataset to classify each of the sample within testing dataset. Use learning rate of 0.1 and 0 biasing factor with 0 initial weights.
* Repeat the above process until the accuracy of 80% or above is not achieved.
