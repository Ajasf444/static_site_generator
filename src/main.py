import os
import shutil


def main():
    root = "blah"
    dest = "Baconator_Fries"
    r_copy(root, dest, True)


def r_copy(root, dest, first_pass=False):
    if first_pass:
        if not os.path.exists(dest):
            print(f"Creating directory: {dest}")
            os.mkdir(dest)
        else:
            for item in os.listdir(dest):
                path = os.path.join(dest, item)
                if os.path.isfile(path):
                    print(f"Removing file: {path}")
                    os.remove(path)
                else:
                    print(f"Removing directory: {path}")
                    shutil.rmtree(path)


if __name__ == "__main__":
    main()
