# imported the requests library
import requests
import os 
import pathlib


            #   Create a folder Pokemon

main_dir = "C:/Users/Ranganath/Desktop/Pokemon"
os.mkdir(main_dir) 
print("Directory '% s' is built!" % main_dir)



image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("toto",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)


old_file = pathlib.Path('/Users/Ranganath/Desktop/Mon cours python')
destination = pathlib.Path('/Users/Ranganath/Desktop/Pokemon/toto')

old_file.rename(destination)