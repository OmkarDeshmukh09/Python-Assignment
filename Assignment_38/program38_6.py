#-----------------------------------------------------------------
#
#  File name   : Assigment38 program38_6.py
#  Descreption : Plot the histogram of StudyHours
#  Author      : Omkar Balasaheb Deshmukh
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Explain the distribution tells you


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

    plt.hist(df["StudyHours"])
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.title("Histogram of Study Hours")
    plt.grid(True)
    plt.show()


if __name__ =="__main__":
    main()

# 1. If most bars are concentrated in the middle range,
# it means most students study moderate hours.
# 2. If the graph is right side more students with lower hours,
# fewer students study very long hours.
# 3 .If the graph is left side more students with higher hours,
# most students are studying regularly.