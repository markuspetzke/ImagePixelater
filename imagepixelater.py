from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

try:
    Tk().withdraw()
    path = askopenfilename(
        title="Choose a Image",
        filetypes=[('image files aka png&jpg', ('.png', '.jpg'))]
        )

    img = Image.open(path)

    imgsmall = img.resize((256,256), resample=Image.BILINEAR)
    result = imgsmall.resize(img.size, Image.NEAREST)
    result.show()

except:
    print("Fehler")

