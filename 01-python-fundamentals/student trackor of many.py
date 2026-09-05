student=[]
SUBJECT=['SANSKRIT','HINDI','KANNADA','PYTHON']
while True:
    name=input("\nThe name of the student (enter 'done' to finish) is:")
    if name.lower()=='done':
        break
    rollno=input("\nThe rollnumber of the student:")
    try:
        marks={}
        for sub in SUBJECT:
            mark=int(input(f"Enter the marks for {sub}:"))
            marks[sub]=mark
        total=sum(marks.values())
        average=total/len(SUBJECT)
        student.append({"name":name,"roll_no":rollno,"marks":marks,"total":total,"average":average})
    except ValueError:
        print("Invalid input for marks. Please enter a number.")
    
try:
    topper=max(student,key=lambda x:x['total'])
    lowest=min(student,key=lambda x:x['total'])
    print("\n----Student Report----")
    print(f"\nTOPPER is {topper['name']} with total marks {topper['total']}")
    print(f"\nLOWEST is {lowest['name']} with total marks {lowest['total']}")
    print("\n----All Students----")
    for student in sorted(student,key=lambda x:x['total'],reverse=True):
        print(f"\n Name:{student['name']} | Roll No:{student['roll_no']} | Total Marks:{student['total']} | Average:{student['average']:.2f}")
except Exception as e:
    print(f"An Error has occured i.e:{e}")



