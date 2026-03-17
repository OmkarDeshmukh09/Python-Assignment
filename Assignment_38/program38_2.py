#-----------------------------------------------------------------
#
#  File name   : Assigment38 progam38_2.py
#  Descreption : Write a program to
#  Author      : Omkar Balasaheb Deshmukh
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Display total number of students in the dataset
#   Count how many students Passed (FinalResult = 1)
#   Count how many students Failed (FinalResult = 0)

import pandas as pd

def main():
    border = "-"*90
    print(border)
    print(border)

    DatasetPath = "student_performance_ml.csv"

#   Csv Loading
    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Succeesfully. ")

#   Total number of students in dataset

    print("Total number of Students in DataSet : ",df.shape[0])

#   Count how many students have passed (Passed = 1)
    Students_Passed = (df["FinalResult"] == 1).sum()
    print("Total number of students have passed : ",Students_Passed)


#   Count how many students have passed (Failed = 0)
    Students_Failed = (df["FinalResult"] == 0).sum()
    print("Total number of students have failed : ",Students_Failed)
    
    
if __name__ =="__main__":
    main()