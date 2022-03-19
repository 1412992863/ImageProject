import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

if __name__ == "__main__":
    im = Image.open("test01.JPG")
    print(im.mode)
    a = np.asarray(im)
    # print(a)
    # b = 255 - a
    # a += 50
    a = np.where(a > 205, 255, a + 50)
    im_out = Image.fromarray(a)
    # im_out_b = Image.fromarray(b)
    # im_out = im_out.convert('L')
    # im_out_b=im_out_b.convert('L')
    im_out.save("test02.JPG")
    # im_out_b.save("test03.JPG")
    # im_out.save("")
