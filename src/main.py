import os
import shutil


def main():
    root = "static/"
    dest = "public/"
    # TODO: delete contents of public/
    r_copy(root, dest, True)


def r_copy(root, dest, first_pass=False):
    if first_pass:
        if not os.path.exists(dest):
            print(f"Making directory: {dest}")
            os.mkdir(dest)
        else:
            print(f"Removing contents of: {dest}")
            for item in os.listdir(dest):
                path = os.path.join(dest, item)
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
    for item in os.listdir(root):
        src_path = os.path.join(root, item)
        if os.path.isfile(src_path):
            print(f"Copying {item} to {dest}")
            shutil.copy(src_path, dest)
        else:
            dest_path = os.path.join(dest, item)
            print(f"Making directory: {dest_path}")
            os.mkdir(dest_path)
            r_copy(src_path, dest_path)


if __name__ == "__main__":
    main()
