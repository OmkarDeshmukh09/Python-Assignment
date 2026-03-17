#-----------------------------------------------------------------
#
#  File name   : Assigment38 program38_3.py
#  Descreption : Using pandas functions, calculate and display
#  Author      : Omkar Balasaheb Deshmukh
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Average StudyHours
#   Average Attendance
#   Maximum PreviousScore
#   Minimum SleepHours


import pandas as pd

def main():
    border = "-"*90
    print(border)
    print(border)

    DatasetPath = "student_performance_ml.csv"

#   Csv Loading
    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Succeesfully. ")


#   Average StudyHours
    StudyHrs = round(df["StudyHours"].mean(),2)
    print("The Average number of Study Hours is : ",StudyHrs)


#   Average Attendance
    AvgAttandance = round(df["Attendance"].mean(),2)
    print("The Average number of Attendance is : ",AvgAttandance)


#   Maximum PreviousScore
    MaxPreviousScore = df["PreviousScore"].max()
    print("The Maximum number of PreviousScore is : ",MaxPreviousScore)

#   Minimum SleepHours
    MinSleepHours = df["SleepHours"].min()
    print("The Minimum number of SleepHours is : ",MinSleepHours)

    
if __name__ =="__main__":
    main()