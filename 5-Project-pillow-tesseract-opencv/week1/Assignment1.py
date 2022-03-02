#Assignment 1: Building a Better Contact Sheet

#In the lectures for this week you were shown how to make a contact sheet for digital photographers, 
# and how you can take one image and create nine different variants based on the brightness of that image. 
# In this assignment you are going to change the colors of the image, creating variations based on a single photo. 
# There are many complex ways to change a photograph using variations, such as changing a black and white image 
# to either "cool" variants, which have light purple and blues in them, or "warm" variants, which have touches 
# of yellow and may look sepia toned. In this assignment, you'll be just changing the image one color channel 
# at a time

#Your assignment is to learn how to take the stub code provided in the lecture (cleaned up below), 
# and generate the following output image:

#From the image you can see there are two parameters which are being varied for each sub-image. 
# First, the rows are changed by color channel, where the top is the red channel, the middle is the green channel, 
# and the bottom is the blue channel. Wait, why don't the colors look more red, green, and blue, in that order? 
# Because the change you to be making is the ratio, or intensity, or that channel, 
# in relationship to the other channels. We're going to use three different intensities, 
# 0.1 (reduce the channel a lot), 0.5 (reduce the channel in half), and 0.9 (reduce the channel only a little bit).

#For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. 
# So the top row of changes would create three alternative pixels, varying the first channel (red). 
# one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). 
# The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), 
# (200, 50, 50) and (200, 90, 50).

#Note: A font is included for your usage if you would like! It's located in the file readonly/fanwood-webfont.ttf

#Need some hints? Use them sparingly, see how much you can get done on your own first! 
# The sample code given in the class has been cleaned up below, you might want to start from that.
import PIL
from PIL import Image, ImageFont, ImageDraw

# read image and convert to RGB
img=Image.open("readonly/msi_recruitment.gif").convert("RGB")
fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", 40)

#get the RGB
r,g,b = img.split() 

listIntesifiers=[0.1,0.5,0.9]
listImages=[]

#red
for idx in range(0,3):
    
    #calculate the new RED and appy to the image
    newR = r.point(lambda i:i*listIntesifiers[idx])
    newImg = Image.merge('RGB',(newR,g,b))
    
    #create a bigger canvas to insert the text below
    newCanvas = Image.new(newImg.mode, (newImg.width, newImg.height+60))
    newCanvas.paste(newImg,(0,0))
    
    #insert the text
    d = ImageDraw.Draw(newCanvas)
    d.text((0, newCanvas.height-50), "channel 0 intensity " + str(listIntesifiers[idx]), font=fnt, fill=(int(255*listIntesifiers[idx]),255,255, 128))

    listImages.append(newCanvas)
    

#green
for idx in range(0,3):
    
    #calculate the new RED and appy to the image
    newG = g.point(lambda i:i*listIntesifiers[idx])
    newImg = Image.merge('RGB',(r,newG,b))
    
    #create a bigger canvas to insert the text below
    newCanvas = Image.new(newImg.mode, (newImg.width, newImg.height+60))
    newCanvas.paste(newImg,(0,0))
    
    #insert the text
    d = ImageDraw.Draw(newCanvas)
    d.text((0, newCanvas.height-50), "channel 1 intensity " + str(listIntesifiers[idx]), font=fnt, fill=(255,int(255*listIntesifiers[idx]),255, 128))

    listImages.append(newCanvas)
    
#blue
for idx in range(0,3):
    
    #calculate the new RED and appy to the image
    newB = b.point(lambda i:i*listIntesifiers[idx])
    newImg = Image.merge('RGB',(r,g,newB))
    
    #create a bigger canvas to insert the text below
    newCanvas = Image.new(newImg.mode, (newImg.width, newImg.height+60))
    newCanvas.paste(newImg,(0,0))
    
    #insert the text
    d = ImageDraw.Draw(newCanvas)
    d.text((0, newCanvas.height-50), "channel 2 intensity " + str(listIntesifiers[idx]), font=fnt, fill=(255,255,int(255*listIntesifiers[idx]), 128))

    listImages.append(newCanvas)
    

first_image=listImages[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0    

for img in listImages:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
