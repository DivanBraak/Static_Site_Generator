from markdown_blocks import markdown_to_html_nodes,extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path)
    markdown = from_file.read()

    template_file = open(template_path)
    template = template_file.read()

    html_nodes = markdown_to_html_nodes(markdown)
    html = html_nodes.to_html()

    title = extract_title(markdown)

    final = template.replace("{{ Title }}",title)
    final = final.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    
    dest_file = open(dest_path, mode="w")

    dest_file.write(final)

def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):

    content_directories = os.listdir(dir_path_content)
    

    for item in content_directories:

        current_path = os.path.join(dir_path_content,item)

        if os.path.isfile(current_path):

            dest_path = os.path.join(dest_dir_path,item)
            new_dest_path = (Path(dest_path).with_suffix(".html"))
            generate_page(current_path,template_path,new_dest_path)
        else:
            new_dir = os.path.join(dir_path_content,item)
            new_dest = os.path.join(dest_dir_path,item)
            generate_pages_recursive(new_dir,template_path,new_dest)