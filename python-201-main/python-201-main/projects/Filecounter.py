# To get that information, write a script that locates your Desktop, fetches all the files that are on there,
# and counts how many files of each different file type are on your desktop. Use a dictionary to collect
# this data, and print it to your console at the end in order to get an overview of what is there.
#You can now expand on your file mover script and add logic that moves all file types 
#that have e.g. more than five files on the desktop into their own separate folder. 
#Will it help to keep your desktop cleaner?


import pathlib

desktop = pathlib.Path('/Users/Ranganath/Desktop')
docx = pathlib.Path("/Users/Ranganath/Desktop/Docx2")

counter_files = 0 
my_dict = {'jpg': 0, 'docx' : 0, 'html' : 0, 'msi' : 0, 'lnk' : 0 }


# View of the desktop & files 
for filepath in desktop.iterdir():
    counter_files += 1
    # fetches all the files that are on there
    print(filepath)
    # # counts how many file
    print(counter_files)




for filepath in desktop.iterdir():
    if filepath.suffix == ".jpg" : 
       my_dict['jpg'] += 1 
    
    elif filepath.suffix == ".docx": 
        my_dict['docx'] += 1

        if my_dict['docx'] > 3 : 
           
            docx.mkdir(exist_ok=True)
            new_png_path = docx.joinpath(filepath.name)
            filepath.replace(new_png_path)
            
            
    
    elif filepath.suffix == ".html": 
        my_dict['html'] += 1 

    elif filepath.suffix == "lnk": 
        my_dict['lnk'] += 1 

    elif filepath.suffix == "msi":
        my_dict['msi'] += 1

print(my_dict)


#You can now expand on your file mover script and add logic that moves all file types 
#that have e.g. more than five files on the desktop into their own separate folder. 
#Will it help to keep your desktop cleaner?


