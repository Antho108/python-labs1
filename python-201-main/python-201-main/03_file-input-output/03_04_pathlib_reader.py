# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import pathlib
import csv







file_location = pathlib.Path("/Users/Ranganath/Desktop/Mon cours python/filecounts.csv")
count = {"": 89, ".csv": 77, ".md": 289, ".png": 619}

with open(file_location, "a") as csvfile:

    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)

