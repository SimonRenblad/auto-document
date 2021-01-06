import os
import sys
import getopt

def check_tmp():
    # check for a .autodoc directory
    ad = os.path.join(os.getcwd(), ".autodoc")
    try:
        os.mkdir(ad)
    except FileExistsError:
        pass
        
    return ad

def prepare_file(tmp_dir):
    # refresh the file to put documentation
    name = str(os.path.join(tmp_dir, "index.html"))
    f = open(name, "w")
    f.close()
    return
    
def add_folder_to_file(folder):
    # append to file
    name = os.path.join(os.getcwd(), ".autodoc\\index.html")
    with open(name, "a", encoding="utf-8") as f:
        f.write(folder)
        f.close()
    return

def print_folder(relative_dir, previous_relative_dir, current_depth, recursive_depth, print_dot):
    # recursive function to print the contents of the folders
    
    folder = ""

    if current_depth == recursive_depth:
        return

    directory = os.path.join(os.getcwd(), relative_dir)

    # determine if there shld be a back
    if previous_relative_dir != 0:
        back_link = u" (<a href=\"#" + str(previous_relative_dir) + u"\">back</a>)"
    else:
        back_link = u""

    # complete link
    title_complete = u"<a name=\"" + str(relative_dir) + u"\">" + str(relative_dir) + u"</a>" + back_link + u"</br>\n"

    folder += "__________________________</br>\n"
    folder += "</br>\n"
    folder += title_complete
    folder += "__________________________</br>\n"
    folder += "</br>\n"

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        rd = os.path.join(relative_dir, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                folder += u"<a href=\"#" + str(rd) + u"\">" + str(f) + u"</a></br>\n"
        else:
            folder += str(f) + u"</br>\n"
            
    # save to file
    add_folder_to_file(folder)

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        rd = os.path.join(relative_dir, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                print_folder(rd, relative_dir, current_depth + 1, recursive_depth, print_dot)

def main(argv):
    # get cli arguments
    try:
        opts, args = getopt.getopt(argv, "d:p")
    except getopt.GetoptError:
        print("invalid option")
        sys.exit(2)
    recursive_depth = 3
    print_dot = False
    for opt, arg in opts:
        if opt == '-d':
            recursive_depth = int(arg)
        elif opt == '-p':
            print_dot = True
            
    tmp_dir = check_tmp()
    prepare_file(tmp_dir)

    print_folder('.', 0, 0, recursive_depth, print_dot)

if __name__ == "__main__":
    main(sys.argv[1:])
