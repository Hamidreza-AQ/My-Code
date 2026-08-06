students = [{"name":"Hamid","score":99},
            {"name":"Niloofar","score":95},
            {"name":"Nila","score":83},
            {"name":"Shahrbanoo","score":89},
            {"name":"Sara","score":85},
            {"name":"Mohammad","score":90}]
while True:
    a = int(input("""
1.Add a student
2.Register points
3.Show all students
4.Show rankings
5.Student search
6.Delete student
7.Show statistics
8.Exit
Enter a num : """))
    if a > 8 or a < 1:
        print("invalid input")
        
    if a == 1:
        i1 = input("Enter the student's name: ")
        new_student = {"name": i1 ,"score":0}
        students.append(new_student)
        print("Student added successfully.")
        
    if a == 2:
        i2 = input("Enter the student's name: ")
        found = False
        for k in students:
            if k["name"] == i2:
                found = True
                score = int(input("Enter the score: "))
                k["score"] = k["score"] + score
        if found == False:
            print("Student not found!")
        
    if a == 3:
        for tmp in students:
            print(tmp)
    
    if a == 4:
        rank = 1
        students_sorted = sorted(students,key= lambda i:i["score"],reverse = True)
        for i in students_sorted:
                print(f'{rank}_{i["name"]} : {i["score"]}')
                rank = rank + 1
                
    if a == 5:
        search = False
        i5 = input("Enter the student's name: ")
        for m in students:
            if m["name"] == i5:
                search = True
                print(f'{m["name"]} : {m["score"]}')
        if search == False:
            print("Student not found!")
    if a == 6:
        keke = False
        i6 = input("Enter the student's name: ")
        for l in students:
            if l["name"] == i6:
                students.remove(l)
                keke = True
        if keke == False:
            print("Student not found!")
            
    if a == 7:
        l1 = []
        avarage = 0
        for n in students:
            avarage = avarage + n["score"]
            l1.append(n["score"])
            
        print(f"Number of students :{len(students)}\n")
        
        print(f"Average scores : {avarage / len(students):.2f}")
        
        print(f"Highest score : {max(l1)}")
        
        print(f"Lowest score : {min(l1)}")
        
    if a == 8:
        print("Hoping to meet you.")
        break