import os
import shutil


def main():
    root = "Baconator"
    dest = "Fries"
    r_copy(root, dest, True)


def r_copy(root, dest, first_pass=False):
    if first_pass:
        if not os.path.exists(dest):
            os.mkdir(dest)
        else:
            for item in os.listdir(dest):
                path = os.path.join(dest, item)
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isfile(path):
            print(f"Copying {item} to {dest}")
            shutil.copy(path, dest)
        else:
            dest_path = os.path.join(dest, item)
            print(f"Making directory: {dest_path}")
            os.mkdir(dest_path)
            r_copy(path, dest_path)


if __name__ == "__main__":
    main()
