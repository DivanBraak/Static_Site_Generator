from copystatic import copy_static_to_public
from gencontent import generate_page,generate_pages_recursive

def main():
    copy_static_to_public("static","public")
    
    #generate_page("content/index.md","template.html","public/index.html")

    generate_pages_recursive("content","template.html","public")






main()