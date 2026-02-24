#ES main 

#import all of the files
from file_handler import view_file, add_to_file, update_file

#make a funtion for main 
def main():
    #make file path be an input to enter the relative path 
    file_path = input("Enter the relative file path: ")
    #make a while loop 
    while True:
        #print the options to select 
        print("1. Update document info\n2. View document\n3. Add content\n4. Exit")
        #make choice input to enter the choice 
        choice = input("Enter choice (1-4): ")
        #if choice is 1 call the update file file
        if choice == "1":
            update_file(file_path)
        #elif choice is 2 call the view file 
        elif choice == "2":
            view_file(file_path)
        #elif choice is 3 call the add to file 
        elif choice == "3":
            add_to_file(file_path)
        #elif choice is 4 print bye and break 
        elif choice == "4":
            print("BYE")
            break
        #else print invalid choice 
            print("Invalid choice.")

# call main in the way the notes tought us 
if __name__ == "__main__":
    main()