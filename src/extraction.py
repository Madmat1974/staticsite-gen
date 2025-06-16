import os
from markdown_blocks import markdown_to_html_node
from htmlnode import *


def extract_title(markdown):
    print (markdown)
    headerline = ""
    #if markdown == "":
        #markdown = get_markdown_file()
    
    break_into_lines = markdown.split("\n")
    for line in break_into_lines:
        if line.startswith("# "):
            headerline = line.lstrip("# ")
            headerline = headerline.strip(" ")
            print (headerline)
            return headerline
    raise Exception("no header found")
        
    
def get_markdown_file():
    source_file = ""# to be filled in
    markdown = open(source_file).read()
    return markdown

def generate_page(from_path, template_path, basepath, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    mdpath_var = open(from_path).read()
    tfpath_var = open(template_path).read()
    mdhtml = markdown_to_html_node(mdpath_var).to_html()
    wbtitle = extract_title(mdpath_var)
    tfpath_var = tfpath_var.replace("{{ Title }}", wbtitle)
    tfpath_var = tfpath_var.replace("{{ Content }}", mdhtml)
    tfpath_var = tfpath_var.replace('href="/', f'href="{basepath}')
    tfpath_var = tfpath_var.replace('src="/', f'scr="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(tfpath_var)

    
    
        

