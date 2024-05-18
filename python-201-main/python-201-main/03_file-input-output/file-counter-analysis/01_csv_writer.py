# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.
# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib
import posixpath

# pathlib.Path().cwd()  # Prints the path to your current working directory
# print(pathlib)

import pathlib


path = pathlib.Path("/Users/Ranganath/Desktop")


# Find the path to my Desktp
desktop = pathlib.Path('/Users/Ranganath/Desktop')
# Create a new folder
new_path = pathlib.Path('/Users/Ranganath/Desktop/Screens')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
    # Filter for screenshots only
    if filepath.suffix == '.jpeg':
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)
# Move the screenshots in there