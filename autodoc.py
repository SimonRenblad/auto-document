import os
import sys
import getopt

print_dot = False

def print_folder(working_dir, relative_dir, previous_relative_dir, current_depth, recursive_depth):
    # recursive function to print the contents of the folders

    if current_depth == recursive_depth:
        return

    directory = os.path.join(working_dir, relative_dir)

    # determine if there shld be a back
    if previous_relative_dir != 0:
        back_link = u" (<a href=\"#" + str(previous_relative_dir) + u"\">back</a>)"
    else:
        back_link = u""

    # complete link
    title_complete = u"<a name=\"" + str(relative_dir) + u"\">" + str(relative_dir) + u"</a>" + back_link + u"</br>"

    print("__________________________</br>".encode("utf-8"))
    print("</br>".encode("utf-8"))
    print(title_complete.encode("utf-8"))
    print("__________________________</br>".encode("utf-8"))
    print("</br>".encode("utf-8"))

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        rd = os.path.join(relative_dir, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                s = u"<a href=\"#" + str(rd) + u"\">" + str(f) + u"</a></br>"
                print(s.encode("utf-8"))
        else:
            s = str(f) + u"</br>"
            print(s.encode("utf-8"))

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        rd = os.path.join(relative_dir, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                print_folder(working_dir, rd, relative_dir, current_depth + 1, recursive_depth)

def main(argv):
    # get cli arguments
    try:
        opts, args = getopt.getopt(argv, "d:p")
    except getopt.GetoptError:
        print("invalid option")
        sys.exit(2)
    recursive_depth = 3
    for opt, arg in opts:
        if opt == '-d':
            recursive_depth = int(arg)
        elif opt == '-p':
            print_dot = True

    print_folder(os.getcwd(), '.', 0, 0, recursive_depth)

if __name__ == "__main__":
    main(sys.argv[1:])
