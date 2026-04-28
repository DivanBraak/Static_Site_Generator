import os, shutil

def copy_static_to_public(source, dest):

    #Deletes and makes new public directory
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    
    copy_files(source,dest)

def copy_files(source, dest):
    if os.path.isfile(source):
        shutil.copy(source, dest)
    else:
        if not os.path.exists(dest):
            os.mkdir(dest)

        directories = os.listdir(source)
        for dir in directories:
            new_source = os.path.join(source,dir)
            new_dest = os.path.join(dest,dir)
            copy_files(new_source,new_dest)