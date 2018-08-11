import os
from urllib.request import urlretrieve


# Assign variable with specific path/file info
url = "https://s3-us-west-2.amazonaws.com/msds-projects/data/"
urlc="http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/"
path = "./reviews_Sports_and_Outdoors_5.json.gz"
filename = "reviews_Sports_and_Outdoors_5.json.gz"
path_meta = "./meta_Sports_and_Outdoors.json.gz"
filemeta= "meta_Sports_and_Outdoors.json.gz"
#Clothing_Shoes_and_Jewelry
#http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Clothing_Shoes_and_Jewelry_5.json.gz
pathc = "./reviews_Clothing_Shoes_and_Jewelry_5.json.gz"
filenamec = "reviews_Clothing_Shoes_and_Jewelry_5.json.gz"


def retrieve_data(filename, url, path):
    if not os.path.exists(path):
        filename, _ = urlretrieve(url+filename, filename)
        print("Data Succesfully Retrieved!")
    else:
        print("Your data already exists in the directory. Enjoy.")


if __name__ == "__main__":
    retrieve_data(filename, url, path)
    retrieve_data(filenamec, urlc, pathc)
    retrieve_data(filemeta,urlc,path_meta)
