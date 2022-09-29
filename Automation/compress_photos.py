import PIL
from PIL import Image
from tkinter.filedialog import *

pfiles = askopenfilenames()
targ_img = Image.open(pfiles[0])
targ_img.save('compressed.jpg',"JPEG",optimize=True,quality=10)