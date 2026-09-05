students=[]
def main():
    while True:
        name=input("The student name is : (enter 'exit' to stop)")
        if name.lower()=="exit":
            break
        try:
            marks=float(input(f"\nThe marks of {name}: "))
            students.append({"name":name,"marks":marks})
        except ValueError:
            print("Invalid input for marks. Please enter a number.")
    try:
        if students:
            total_marks=sum(student["marks"] for student in students)
            avg_marks=total_marks/len(students)

            topper=max(students,key=lambda x:x["marks"])
            lowest=min(students,key=lambda x:x["marks"])
            print("\n----Student Report----")
            print(f"Total marks is {total_marks}")
            print(f"Average marks is {avg_marks:.2f}")
            print(f" TOPPER is {topper['name']} with marks {topper['marks']}")
            print(f" LOWEST is {lowest['name']} with marks {lowest['marks']}")
            print("\n----All Students----")
            for student in sorted(students, key=lambda x: x['name']):
                print(f"{student['name']}:{student['marks']}")
        else:
            print("No student data entered.") 
    except Exception as e:
        print(f"AN ERROR HAS OCCURED i.e: {e}")
if __name__=="__main__":
    main()