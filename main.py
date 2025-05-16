# This script will import a markbook and allow you to estimate a mark
# Written by Bruce Banner - 16/05/2025
# Version 0.4
import numpy
import csv
from sklearn.linear_model import LinearRegression

# Input
# Import the data from a csv file.
# Assumes that the file is marks only.
# datafile is a string which is the name of the csv file to open

def importData (dataFile): 
    return True # Ask the user which Student and Task to estimate mark for
def getWhichTask (): 
    return True #Process # Generate an estimated mark # data is a two dimensional array of the marks and tasks # student is an integer which is which student to estimate the mark for # task is an integer which is which task to estimate the mark for
def processEstimate (data, student, task): 
    return True # Output # Simple output of the results # student is an integer which is the student to estimate the mark for # task is an integer which is which task to estimate the mark for

# estimate is an integer which is the estimated mark
# Simple output of the results # student is an integer which is which student to estimate the mark for # task is an integer which is which task to estimate the mark for
# estimate is an integer which is the estimated mark

def showResult (student, task, estimate): 
    print(f"Student {student} has an estimated mark of {estimate} for task {task}")


def main (): 
    dataFile = 'marksSimple.csv'

    #marks = importData (dataFile)
    #print (marks)
    #student, task = getWhichTask () #print (f’Student: {student}, Task: {task}’)
    #estimate = processEstimate (marks, student, task)
    #showResult (student, task, estimate)
    student = 4 
    task = 3 
    estimate = 81

    showResult (student, task, estimate)

main()

