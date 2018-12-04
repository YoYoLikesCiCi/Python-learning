from PIL import Image
pil_im = Image.open("example.jpg")
pil_im.show()
box = (100,100,400,400)  # （左，上，右，下） 默认左上角坐标为（0，0）
region = pil_im.crop(box)

r,g,b, = region.split()
newr = (r+g+b)/3
newg = (r+g+b)/3
newb = (r+g+b)/3
om = Image.merge("RGB",(newr,newg,newb))

pil_im.show()
box = (300,300,600,600)
pil_im.paste(om,box)
pil_im.show()
