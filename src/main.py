from copystatic import copy_static_to_public
from gencontent import generate_page,generate_pages_recursive
import sys

def main():

    basepath = sys.argv[1]

    copy_static_to_public("static","docs")
    
    #generate_page("content/index.md","template.html","public/index.html")

    generate_pages_recursive("content","template.html","docs",basepath)






main()