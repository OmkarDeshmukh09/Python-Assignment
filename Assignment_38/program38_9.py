#-----------------------------------------------------------------
#
#  File name   : Assigment38 program38_8.py
#  Descreption : Create the Boxplot of Attandance & check outliers 
#  Author      : Omkar Balasaheb Deshmukh
#  Date        : 24/2/26
#
#-----------------------------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt

def main():
    border = "-"*90
    print(border)
    print(border)

    DatasetPath = "student_performance_ml.csv"

#   Csv Loading
    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Succeesfully. ")
    
    pass_students = df[df["FinalResult"] == 1]
    fail_students = df[df["FinalResult"] == 0]


    plt.boxplot([fail_students["AssignmentsCompleted"],
                    pass_students["AssignmentsCompleted"]],
                    labels=["Fail", "Pass"])

    plt.ylabel("Assignments Completed")
    plt.title("Assignments Completed vs Final Result")
    plt.show()


# It is showed generally who passed as completed it more assignment that who failed

if __name__ =="__main__":
    main()