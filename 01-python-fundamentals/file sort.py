# with open("Untitled.txt","r") as f:
#     print(f.readlines()) #this reads whole document and return a list of strings 
#     print(f.read()) #this reads only whole document but in string format
#     print(f.readline()) #this reads only one line of the document and return a string

with open("marks.txt","r") as f:# we can also do x=open("marks.txt","r") 
                                # but we have to  close the file after manually x.close()
    marks=f.readlines()
    marks.sort()
    for line in marks:
        print(line,end="")
print("\n")
with open("updated","w") as output: #in write mode the file is over-writted by earsing previous  
    for line in marks:
        output.write(line)
    output.write("\nmarks(student5)=60,70,80")
with open("updated","at") as output:
    output.write("\nmarks(student6)=60,70,80")
    output.write("\nmarks(student7)=60,70,100")
with open("updated","rt") as f:
    print("\nReading the updated file")
    for line_no,line in enumerate(f,1):
        if "100" in line:
            print(f"student scored 100 marks is {line_no}")
        elif "80" in line:
            print(f"student scored 80 marks is {line_no}")
    f.seek(0)#readlien method moves the pointer/stream to end of file after reading the file
    for line_no,line in enumerate(f,1):
       part=line[14:] #seek method does not apply for in strings
       digit=[i for i in part if i.isdigit()]
       print(digit)
           


        

