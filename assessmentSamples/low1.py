# This script will import a markbook and allow you to estimate a mark
# Written by Bruce Banner - 5/11/2024
# Version 0.4
import numpy
import csv
from sklearn.linear_model import LinearRegression

# Import the data from a csv file.
# Assumes that the file is marks only.
def importData (dataFile) :
    marks = []
    marksFile = open(dataFile)
    marksRaw = csv.reader(marksFile)
    
    # iterate over each row in the file
    for student in marksRaw :
        studentMarksInt = []
        
        # iterate over each task converting the mark from a string to an integer
        for mark in student :
            studentMarksInt.append(int(mark))
            
        marks.append(studentMarksInt)
        
    return marks


# Ask the user which Student and Task to estimate mark for
def getWhichTask () :
    student = int(input("Which student to estimate the mark for : "))
    task = int(input("Which task to estimate the mark for : "))
    return student, task


# Generate an estimated mark
def processEstimate (data, student, task) :
    # Create base data with the task to estimate omitted
    tasksBase = []  # this needs to be an array of arrays with a single item which is the task number
    marksBase = []  # this is a 1 dimensional array or marks in other tasks 
    
    counter = 1
    for taskNumber in data[0] :
        if counter != task : # So that we omit the task that are estimating
            taskTitle = [counter]
            tasksBase.append(taskTitle)
            marksBase.append(data[student-1][counter - 1]) # -1 as zero indexing
        counter = counter + 1
    
    # Create the model
    model = LinearRegression()
    model.fit(tasksBase, marksBase)
    
    mark_prediction = model.predict([[task]])
    
    return mark_prediction[0]


# Simple output of the results
def showResult (student, task, estimate) :
    print(f"Student {student} has en estimated mark of {estimate} for task {task}")


# Manage the overall processing
def main () :
    dataFile = 'marksSimple.csv'
    marks = importData (dataFile)
    #print (marks)
    student, task = getWhichTask ()
    estimate = processEstimate (marks, student, task)
    showResult (student, task, estimate)
    
main ()