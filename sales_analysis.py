import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
data = {
"months" : ["farvardin", "ordibehsht", "khordad", "tir", "mordad", "shahrivar", "mehr", "aban", "azar", "dey", "bahman", "esfand"],
"sale" :[12, 15, 18, 22, 28, 45, 52, 48, 40, 35, 25, 20],
"number_of_customers":[200, 220, 250, 300, 400, 600, 750, 680, 550, 480, 350, 300],
"profit":[5, 6, 8, 10, 12, 20, 25, 22, 18, 15, 10, 8]
}

#1
df = pd.DataFrame(data)
df = df.set_index("months")

while True:

    i = int(input("""
1.View DataFrame
2.View statistics
3.View the chart
4.Exit
Enter a number: """))
    
    if i > 3 or i < 1:
        print("invalid input!")
    if i == 1:
        print(df)
    if i == 2:

        print("Total annual sales: ",sum(df["sale"]))

        print("_" * 25)

        print("Average monthly sales:",np.mean(df["sale"]))

        print("_" * 25)

        print("Best Sellers:",df["sale"].idxmax(),max(df["sale"]))

        print("_" * 25)

        print("Lowest sales:",df["sale"].idxmin(),min(df["sale"]))

        print("_" * 25)

        print("Total annual profit:",sum(df["profit"]))

        #3
        df["nesbat profit be sale"] = round(df["profit"] / df["sale"] * 100,2)
        print("nesbat profit be sale",df["nesbat profit be sale"])

        print("_" * 25)

        print("Month with the most customers:",df["number_of_customers"].idxmax(),max(df["number_of_customers"]))

        print("_" * 25)

        print("Month with the fewest customers:",df["number_of_customers"].idxmin(),min(df["number_of_customers"]))

        print("_" * 25)

        print("Average number of customers per month:",round(df["number_of_customers"].mean(),2))

        print("_" * 25)

    if i == 3:
        plt.plot(df.index, df["sale"],marker = "o",color = "blue",linewidth = 2)
        plt.grid()
        plt.xlabel("Months")
        plt.ylabel("Sales(Billion Tomans)")
        plt.title("Sales analysis")
        plt.show()
        
    if i == 4:
        print("Goodbye.")
        break