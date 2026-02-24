#ES 1 file handler
#make a funtion for viewing files 
def view_file(path):
    #open the file and read it 
    try:
        file = open(path, "r")
        #print the document content and close it
        print("\nDocument content:")
        print(file.read())
        file.close()
    #except print file not found 
    except:
        print("File not found.")

#make a funtion for adding file 
def add_to_file(path):
    #print the enter text and press enter twice to stop
    print("Enter text (press enter twice to stop):")
    #make the lines a empty list
    lines = []
    #make a while loop 
    while True:
        #make line equlas input 
        line = input()
        #if the line is two spaces break 
        if line == "":
            break
        #append lines to line 
        lines.append(line)
    #open the file and append 
    try:
        file = open(path, "a")
        #make a loop in lines 
        for line in lines:
            #write line plus enter
            file.write(line + "\n")
        #close the file and print content added 
        file.close()
        print("Content added.")
    #excep print the file not found 
    except:
        print("File not found.")

# make a funtion for update file 
def update_file(path):
    #open the file and read it, then close it 
    try:
        file = open(path, "r")
        text = file.read()
        file.close()
        #make a string for word counter and make the length text split
        word_count = len(text.split())
        #print that the word count is wordcount
        print("word count:", word_count)
    #except print file not found
    except:
        print("File not found.")