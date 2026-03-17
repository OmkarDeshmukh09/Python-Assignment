import pandas as pd

def main():
    border = "-"*90
    print(border)
    print(border)

#           Csv Loading
    Data = pd.read_csv("student_performance_ml.csv")

#       First 5 records
    print("First 5 records :")
    print(Data.head())
    print(border)

#       Last 5 records
    print("Last 5 records : ")
    print(Data.tail())
    print(border)


#   Total number of row and coloumns
    print("Total number of row and coloumns :")
    print(Data.shape)
    print(border)

    
#   List of the coloumn names
    print("List of the coloumn names :")
    print(Data.columns.tolist())
    print(border)

#   List of the datatype of each coloumn
    print("List of the datatype of each coloumn :")
    print(Data.dtypes)
    print(border)


if __name__ =="__main__":
    main()