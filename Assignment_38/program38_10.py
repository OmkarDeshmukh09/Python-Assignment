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

    plt.scatter(pass_students["FinalResult"],
                pass_students["SleepHours"],
                label="Pass")

    plt.scatter(fail_students["FinalResult"],
                fail_students["SleepHours"],
                label="Fail")

    plt.xlabel("Final Result")
    plt.ylabel("Sleep Hours")
    plt.title("Sleep Hours vs Final Result")
    plt.legend()
    plt.show()


# It is show how sleep more has pass the exam and who sleep less fails it


if __name__ =="__main__":
    main()