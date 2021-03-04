import os
import sys
import io
import zipfile
import shutil


def extract(filename):
    z = zipfile.ZipFile(filename)
    for f in z.namelist():
        # get directory name from file
        dirname = os.path.splitext(f)[0]  
        # create new directory
        os.mkdir(dirname)  
        # read inner zip file into bytes buffer 
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        
        file_path = ''# remembers entire file address of last file found per iteration 
        filename = ''# remembers name of last file found per iteration 
        cwd = os.getcwd()
        dir = os.path.join("C:\\",cwd,"Programs")# creates new folder 
        if not os.path.exists(dir): # makes sure that the folder is not made multiple times
            os.mkdir(dir)
        for file in zip_file.namelist():# this iterates every directory found in the namelist buffer
            
            for root, subdirs, files in os.walk(dirname):# this is how os.walk is used. 
                name = ''
                for files in file: #for some reason the files are found in characters so this loop iterates the name of the files found and updates the name sring variabe 
                    name += files
                    file_path = os.path.join(root, name)    
                    filename = name
                    
            zip_file.extract(file, dirname)
            #this code was suppose to move the directory of the files found to the new folder created
            #os.rename(os.path.abspath(name), os.path.join(dir, name))
            
        print('walk_dir (absolute) = ' + os.path.abspath(filename)) # just a test print statement showing file addresses
        print ('--------------------------------')  
    
#run the function here   
extract('1234.zip')
