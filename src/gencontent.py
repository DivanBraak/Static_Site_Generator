from markdown_blocks import markdown_to_html_nodes,extract_title
import os

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