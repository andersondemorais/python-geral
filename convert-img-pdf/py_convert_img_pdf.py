# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "01-dez-2020"
__version__ = "0.1"
__status__ = ""

""" Convert img - pdf  """


from PIL import Image
from pathlib import Path

home = str(Path.home())


def convert_one_img(src, dst):
    try:
        with Image.open(src, "r") as f_jpeg:
            f_pdf = f_jpeg.convert("RGB")
            f_pdf.save(dst)
    except Exception as e:
        print(e)
        raise Exception("Something went wrong")
    else:
        print("All's fine")


def convert_many_img(srcs, dst):
    try:
        img = Image.open(srcs[0]).convert("RGB")
        image_list = []
        for i in range(1, len(srcs)):
            f_pdf = Image.open(srcs[i]).convert("RGB")
            image_list.append(f_pdf)
        img.save(dst, save_all=True, append_images=image_list)
    except Exception as e:
        print(e)
        raise Exception("Something went wrong")
    else:
        print("All's fine")


def main():
    global home

    """CONVERT 1 img"""
    # img file to be converted / arquivo img a ser convertido
    src = home + "/img.jpg"
    # name of the pdf file that'll be generated / nome arquivo pdf que sera gerado
    dst = home + "/pdf.pdf"

    convert_one_img(src, dst)

    """ CONVERT +1 img """
    # img files to be converted / arquivos img a ser convertidos em um unico pdf
    src1 = home + "/img1.jpg"
    src2 = home + "/img2.jpg"
    srcs = [src1, src2]
    # name of the pdf file that'll be generated / nome arquivo pdf que sera gerado
    dst = home + "/pdf.pdf"

    convert_many_img(srcs, dst)


if __name__ == "__main__":
    main()
