import os 
import random
import argparse
import sys

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

# Function to rename multiple files 
def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("dest", help="dest folder to random renaming")
    args = parser.parse_args()
    print("Target folder:", args.dest)
    print("Files:", os.listdir(args.dest))
    if query_yes_no('Rename all files in this folder?'):
        for count, filename in enumerate(os.listdir(args.dest)):
            dst =str(random.randint(100,999)) + "_" + filename
            dst =args.dest + "/" + dst
            src =args.dest + "/" + filename
            if os.path.isfile(src):
                # rename() function will 
                # rename all the files 
                os.rename(src, dst) 
                print(src, "->", dst)

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 