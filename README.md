## Document_Classifier

This program classifies text document using Naive-Bayes machine learning model. 

On high level, the program for a given document D, calculates the posterior probability that a document belongs to certain topic given the features in that document.

There are two directories - train and test with containing document files. 
  The train directory is further divided based on topics. Each file inside the topic directory belongs to that particular topic.

In test directory, files can belong to any topic. Our program based on the model it got trained on, predicts the mostly likely topic a file can belong to.

## To run the program - 
```
python doc_classification.py
```
*** Make sure you're using python 2.7

 The program runs by first training/creating the model for each file in train dataset. Once it has trained itself on the files, the program starts predicting topic for each file in test dataset.
