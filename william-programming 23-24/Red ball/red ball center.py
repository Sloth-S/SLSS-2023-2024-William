from PIL import Image
import os

def isred(a):
    r,g,b = a
    if r>150 and g+b<r:
        return True
    return False
    
def center(picture_path):

    picture = Image.open(picture_path)

    data = picture.getdata()
    first = (0,0)
    last = (0,0)

    for x in range(picture.width):
        for y in range(picture.height):
            if isred(data[y*picture.width+x]):
                if first==(0,0):
                    first=(x,y)
                last=(x,y)
    a,b=first
    x,y=last
    print((a+x)/2,",",(b+y)/2)

current_directory = os.path.dirname(__file__)


picture_file_name = "Redball.png"  

picture_path = os.path.join(current_directory,  picture_file_name)


center(picture_path)
