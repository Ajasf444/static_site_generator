import os
import shutil


def main():
    root = "static/"
    dest = "public/"
    recursive_copy(root, dest)


def recursive_copy(root, dest, first_pass=True):
    if first_pass:
        if not os.path.exists(dest):
            print(f"Making directory: {dest}")
            os.mkdir(dest)
        else:
            recursive_rm(dest)
    for item in os.listdir(root):
        src_path = os.path.join(root, item)
        if os.path.isfile(src_path):
            print(f"Copying {item} to {dest}")
            shutil.copy(src_path, dest)
        else:
            dest_path = os.path.join(dest, item)
            print(f"Making directory: {dest_path}")
            os.mkdir(dest_path)
            recursive_copy(src_path, dest_path, False)


def recursive_rm(dest):
    print(f"Removing contents of: {dest}")
    for item in os.listdir(dest):
        path = os.path.join(dest, item)
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


if __name__ == "__main__":
    main()
