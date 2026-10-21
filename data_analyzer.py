import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_name):    
    df = pd.read_excel(f"{file_name}")
    return df

df = load_data("dataset.xlsx")

def show_basic_info(df):
    print(df.head())
    df.info()
    print(df.describe())
    print(df.isnull().sum())

def show_values_counts(df,column):
    return df[column].value_counts()

def plot_bar(df,column,title):
    counts = df[column].value_counts()
    plt.bar(counts.index,counts.values)
    plt.title(title)
    plt.show()

def plot_hist(df,column,title):
    plt.hist(df[column])
    plt.title(title)
    plt.show()

while True:
    num = int(input(
"""
0.Exit
1.Show basic info
2.Show values counts
3.Plot bar
4.Plot histogram
Enter an number: """))
    if num == 0:
        break

    elif num == 1:
        show_basic_info(df)

    elif num == 2:
        print(show_values_counts(df,"نام کالا"))

    elif num == 3:
        for col in df.columns:
            if df[col].dtype == "object":
                plot_bar(df, col, f"نمودار {col}")
                
    elif num == 4:
        for col in df.columns:
            if df[col].dtype in ["int64", "float64"]:
                plot_hist(df, col, f"نمودار {col}")

    else:
        print("Invalid Input!")