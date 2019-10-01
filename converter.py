from PIL import Image, ImageEnhance, ImageFilter
import pytesseract 
import numpy



import pytesseract
path = 'text.jpg'
img = Image.open(path)
image = img.convert('RGB')


# pix = image.load()

# for y in range(image.size[1]):
#     for x in range(image.size[0]):
#         if pix[x,y][0] < 102 or pix[x,y][1]< pix[x,y][2] <102:
#             pix[x,y] = (0,0,0,225)
#         else:
#             pix[x,y] = (225,225,225,225)
#     image.save('text.jpg')
# text = pytesseract.image_to_string(Image.open(path))
text1 = pytesseract.image_to_string(Image.open(path))
# image.save('text.txt')
file1=open("text1.txt","a")
file1.writelines(text1)
file1.close()
print(text1)