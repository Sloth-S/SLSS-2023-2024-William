from PIL import Image
import os

current_directory = os.path.dirname(__file__)

light_name = "p.jpg"

light_path = os.path.join(current_directory,islight_name)

light=Image.open(light_path)

width, height = light.size

pixels = list(light.getdata())

sum_brightness=list(light.getdata())

i=0

for pixel in pixels :
    sum_brightness[i]=sum(pixel)/ 3 
    i=i+1

average = sum(sum_brightness) / len(sum_brightness)

print("The average brightness is:",average)

if(average<128):
    print("LIGHT")
else:
    print("DARK")
