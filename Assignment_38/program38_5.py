#-----------------------------------------------------------------
#
#  File name   : Assigment38 program38_5.py
#  Descreption : Based on the dataset values, analyze whether
#  Author      : Omkar Balasaheb Deshmukh
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Higher StudyHours increase the chance of passing.
#   Higher Attendance improves FinalResult.
#   Write your observations in 4–5 lines.



import pandas as pd

def main():
    border = "-"*90
    print(border)
    print(border)

    DatasetPath = "student_performance_ml.csv"

#   Csv Loading
    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Succeesfully. ")

    pass_data = df[df["FinalResult"] == 1]
    fail_data = df[df["FinalResult"] == 0]
    
    Average_pass = pass_data["StudyHours"].mean()
    Average_fail = fail_data["StudyHours"].mean()

    Attendance_pass = pass_data["Attendance"].mean()
    Attendance_fail = fail_data["Attendance"].mean()
        
    print("Average studyHours of pass : ",Average_pass)
    print("Average studyHours of fail : ",Average_fail)

    print("Average Attendance Pass:",Attendance_pass)
    print("Average Attendance Fail:",Attendance_fail)


    counts = df["FinalResult"].value_counts()

    if counts[1] == counts[0]:
        print("Dataset is Balanced")
    else:
        print("Dataset is Not Balanced")


# 1.Those who pass are having higher studyhour compared to who fail
# 2.Similarly,student  with higher Attendance percentage tend to have better result
# 3.Regular attendance appears to improve understanding and performance in exams.
# 4.Both studyHours and attendance show a positive correlation with passing results.


if __name__ =="__main__":
    main()