import pandas as pd

data = {
"title":["Book","date","Sports pants","bicycle","laptop","pen"],
"amount":[300000,500000,1500000,26000000,155000000,20000],
"category":["Education","Business","Sports","Sports","Programming","Education"],
}
df = pd.DataFrame(data)
while True:
    i = int(input("""
1.Add cost
2.Show all costs
3.View by category
4.Calculate the total of each category  
5.Show total costs  
6.Show the highest cost
7.Eliminate cost
8.Exit  
Enter a number: """))
    #1
    if i == 1:
        i1 = input("Enter title: ")
        i2 = int(input("Enter amount: "))
        i6 = input("Enter category: ")
        dictionary = {"title":i1,"amount":i2,"category":i6}
        df2 = pd.DataFrame([dictionary])
        df = pd.concat([df,df2],ignore_index = True)
    #2
    if i == 2:
        print(df)

    #3
    if i == 3:
        print(df["category"])

    #4
    if i == 4:
        print(df.groupby("category")["amount"].sum())

    #5
    if i == 5:
        print(df["amount"].sum())

    #6
    if i == 6:
        print(df["amount"].max())

    #7
    if i == 7:
        try:
            i3 = int(input("The number you want to delete:"))
            df = df.drop(i3)
            print("The requested member was successfully deleted. Would you like to view the dataframe?(No/Yes)",input())
        except:
            print("de Akhe mashti!")
    #8
    if i == 8:
        print("Hoping to meet you.")
        break