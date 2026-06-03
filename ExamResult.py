students = { "Asha": [78, 82, 69], 
            "Rahul": [35, 60, 38], 
            "Meena": [90, 92, 88], 
            "Kiran": [25, 30, 28] } 


passCount = 0
failCount = 0
topper = ""
top_avg = 0
failed = []

for name , marks in students.items():
    avg = int(sum(marks)/len(marks))
    
    if avg >= 75:
        result = "Distinction"
        passCount += 1
    elif avg >= 50:
        result = "Pass"
        passCount += 1
    else:
        result = "Failed"
        failCount += 1
        failed.append(name)

    if avg > top_avg:
        top_avg = avg
        topper = name

    print(f"{name} : {avg}% - {result}")

print(f"No of passed : {passCount}")
print(f"No of failed: {failCount}")
print(f"The Class Topper : {topper}")
print(f"Those Who failed : {failed}")
    
