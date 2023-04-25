from PIL import Image
  
# Import an image from directory:
input_image = Image.open("hi.png")
  
# Extracting pixel map:
pixel_map = input_image.load()
  
# Extracting the width and height 
# of the image:
awidth, height = input_image.size
  
# taking half of the width:
for i in range(width):
                for j in range(height):
                                # getting the RGB pixel value.
                                r, g, b, p = input_image.getpixel((i, j))
                                if r>125:
                                                r = 255
                                else:
                                                r = 0
                                if g>125:
                                                g = 255
                                else:
                                                g = 0
                                if b>125:
                                                b = 255
                                else:
                                                b = 0
                                # Apply formula of grayscale:
                                grayscale = (0.299*r + 0.587*g + 0.114*b)
                                # setting the pixel value.
                                pixel_map[i, j] = (int(r), int(g), int(b))
  
# Saving the final output
# as "grayscale.png":
input_image.save("deepfried", format="PNG")
  
# use input_image.show() to see the image on the
# output screen.
