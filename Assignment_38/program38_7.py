#-----------------------------------------------------------------
#
#  File name   : Assigment38 program38_7.py
#  Descreption : Create the scatterplot of Studyhours and PreviouScore 
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

    pass_student = df[df["FinalResult"] == 1]
    fail_student = df[df["FinalResult"] == 0]

    plt.scatter(pass_student["StudyHours"],
                pass_student["PreviousScore"],
                color="yellow",
                label="Pass")

    plt.scatter(fail_student["StudyHours"],
                fail_student["PreviousScore"],
                color="red",
                label="Fail")

    plt.xlabel("Study Hours")
    plt.ylabel("Previos Score")
    plt.title("StudyHours vs PreviosScore")
    plt.legend()
    
    plt.show()


if __name__ =="__main__":
    main()

# 1. If most bars are concentrated in the middle range,
# it means most students study moderate hours.
# 2. If the graph is right side more students with lower hours,
# fewer students study very long hours.
# 3 .If the graph is left side more students with higher hours,
# most students are studying regularly.