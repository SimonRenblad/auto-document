import os
import sys
import getopt

recursive_depth = 3
print_dot = False

def print_folder(working_dir, relative_dir, previous_relative_dir, current_depth):
    # recursive function to print the contents of the folders

    if current_depth == recursive_depth:
        return

    directory = os.path.join(working_dir, relative_dir)
    
    # determine if there shld be a back
    if previous_relative_dir != 0:
        back_link = " (<a href=\"#" + str(previous_relative_dir) + "\">back</a>)"
    else:
        back_link = ""

    # complete link
    title_complete = "<a name=\"" + str(relative_dir) + "\">" + str(relative_dir) + "</a>" + back_link + "</br>"

    print("__________________________</br>")
    print("</br>")
    print(title_complete)
    print("__________________________</br>")
    print("</br>")

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                print("<a href=\"#" + str(f) + "\">" + str(f) + "</a></br>")
        else:
            print(str(f) + "</br>")

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        rd = os.path.join(relative_dir, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                print_folder(working_dir, rd, relative_dir, current_depth + 1)

def main(argv):
    # get cli arguments
    try:
        opts, args = getopt.getopt(argv, "d:p")
    except getopt.GetoptError:
        print("invalid option")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-d':
            recursive_depth = int(arg)
        elif opt == '-p':
            print_dot = True

    print_folder(os.getcwd(), '.', 0, 0)

if __name__ == "__main__":
    main(sys.argv[1:])
