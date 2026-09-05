import os
class recursion:
    def display_content(path,indent=0):
        if not os.path.exists(path):
            print("path does-not exists")

        for item in os.listdir(path):
            item_path=os.path.join(path,item)
            if os.path.isdir(item_path):
                print(" " * indent + f"[DIR] {item}")
                recursion.display_content(item_path, indent + 4)  # RECURSION: Call the method again for the sub-folder
            else:
                print(" " * indent + f"[FILE] {item}")

folder_path=input("The path is:")
print(f"\nThe contents Of The {folder_path} present is:")
recursion.display_content(folder_path)





# class FolderScanner:
#     def __init__(self, starting_path):
#         """
#         This is the constructor. It initializes the scanner with 
#         the base path you want to search.
#         """
#         self.starting_path = starting_path

#     def display_content(self, path=None, indent=0):
#         """
#         This method handles the recursive scanning.
#         """
#         # If no path is provided, use the starting path defined when the object was made
#         if path is None:
#             path = self.starting_path

#         # Check if the path actually exists
#         if not os.path.exists(path):
#             print("Path does not exist")
#             return

#         # Loop through everything inside the directory
#         for item in os.listdir(path):
#             # Combine folder path and item name
#             item_path = os.path.join(path, item)
            
#             # Check if the item is a folder (directory)
#             if os.path.isdir(item_path):
#                 print(" " * indent + f"[DIR] {item}")
#                 # RECURSION: We call the method again using 'self' for the sub-folder
#                 self.display_content(item_path, indent + 4)
#             else:
#                 # If it's a file, just print it
#                 print(" " * indent + f"[FILE] {item}")

# def main():
#     folder_path = input("The path is: ")
#     print(f"\nThe contents of {folder_path} present are:")
    
#     # 1. Create an 'instance' (a real object) of our class
#     scanner = FolderScanner(folder_path)
    
#     # 2. Trigger the recursive scanning method
#     scanner.display_content()

# if __name__ == "__main__":
#     main()


