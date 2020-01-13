import os


def get_var():
    # Ask the user to enter string to search
    Search_path = input("Enter Directory Path To search: ")
    Search_str = input("Enter Your File Name: ")
    program = input("Name Of Progam to Open File with: ")
    return Search_path, Search_str, program


def check_folder(Search_str, Search_path):
    try:
        in_it = os.listdir(Search_path)
    except:
        print("File Path Does not exist. Make Sure you typed the name correctly, then try again.: " + Search_path)
        return 0
    all_file = []
    for file in in_it:
        if Search_str in file:
            #print(file)
            all_file.append(file)
    #print(all_file)
    if len(all_file) > 1:
        print("Select only one file, there are " + str(len(all_file)) + " files with a similar name")
        print("Select one of the following: " + str(all_file))
        Search_str = input("Enter Your File Name: ")
        return Search_str
    else:
        return file

def run_prog():
    Search_path, Search_str, program = get_var()
    wild = check_folder(Search_str, Search_path)
    file = str(wild)
    try:
        give = os.system("start"+ " " + program + " " + Search_path +"\\"+ file)
    except:
        Print("file Cannot Open")
    return give
run_prog()


