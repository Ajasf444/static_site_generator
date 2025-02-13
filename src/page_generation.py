from block_operations import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("No header found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path, exist_ok=True)
    file_name = "index.html"
    file_path = os.path.join(dest_path, file_name)
    with open(file_path, "w") as file:
        file.write(html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for dir in os.listdir(dir_path_content):
        if os.path.isfile(dir):
            if is_markdown_file(dir):
                generate_page(dir_path_content, template_path, dest_dir_path)

        else:
            generate_pages_recursive(
                os.path.join(dir_path_content, dir),
                template_path,
                os.path.join(dest_dir_path, dir),
            )


def is_markdown_file(file: str):
    return file.endswith(".md")
