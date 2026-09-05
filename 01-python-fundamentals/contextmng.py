class ManagedFile: # using as a context manager
    def __init__(self,filename,mode):
        print("init")
        self.filename=filename
        self.mode=mode

    def __enter__(self):  # this dunder function opens the file
        print("Enter")
        self.f=open(self.filename,'w')
        return self.f

    def __exit__(self, exc_type, exc_value,exc_traceback): # exc_type,exc_value indicate the exception type, value before closing
        if self.f is not None:
            self.f.close()
        print("Error is :",exc_type,exc_value)
        print("Exit")

with ManagedFile("notes.txt",'w') as file:
    print("Do Something")
    file.write("Some to do...")

        