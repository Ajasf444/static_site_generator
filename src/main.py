import os
import shutil

from page_generation import generate_page, generate_pages_recursive


def main():
    source_directory = "content/"
    source_path = os.path.join(source_directory, "index.md")
    destination_path = "public/"
    template_path = "template.html"
    static_directory = "static/"
    recursive_copy(static_directory, destination_path)
    generate_page(source_path, template_path, destination_path)


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
