import os
import sys
import getopt

recursive_depth = 3
print_dot = False

def print_folder(directory, current_depth):
    # recursive function to print the contents of the folders

    if current_depth == recursive_depth:
        print("depth reached")
        return

    for f in os.listdir(directory):
        print(f)

    print("__________________________")

    for f in os.listdir(directory):
        d = os.path.join(directory, f)
        if os.path.isdir(d):
            if(f[0] != '.' or print_dot):
                print_folder(d, current_depth + 1)

def main(argv):
    # get cli arguments
    try:
        opts, args = getopt.getopt(argv, "d:")
    except getopt.GetoptError:
        print("invalid option")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-d':
            recursive_depth = int(arg)

    print_folder(os.getcwd(), 0)

if __name__ == "__main__":
    main(sys.argv[1:])
