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

    StudentAttandance = df["Attendance"]
    plt.boxplot(StudentAttandance)
    plt.title("Attandance")
    plt.legend()
    plt.grid(True)
    
    plt.show()


if __name__ =="__main__":
    main()