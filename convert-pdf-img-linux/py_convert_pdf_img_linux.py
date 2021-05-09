# -*- coding: utf-8 -*-
# Using Python 3.x

""" 
Convert pdf - img 
** Apenas para PDFs com 1 página / only for PDF with 1 page
"""

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "15-nov-2020"
__version__ = "0.1"
__status__ = ""

import os
import re
from pathlib import Path

home = str(Path.home())


def main():
    global home

    # path to the folder containing the pdfs / caminho para o dir com os pdfs
    src = home + "/pdfs/"
    # path to the folder to store the images / caminho para o dir para armazenar as imgs
    dst = src
    # allowed extensions / extensões permitidas
    pdf_extension = (".pdf", ".PDF", ".Pdf", ".PdF", ".PDf", ".pDF", ".pdF")

    for (
        count,
        filename,
    ) in enumerate(sorted(os.listdir(src))):
        if filename.endswith(pdf_extension):
            # complete filepath / caminho completo do arquivo
            srcf = src + filename

            # output filename / nome do arquivo de saída
            filename_output = filename.split(".")[-2]
            # removes special chars from the file name / remove caracteres especiais do nome do arquivo
            filename_output = re.sub("[^A-Za-z0-9]+", "", filename_output)

            dstf = dst + filename_output + "_JPEG_" + str(count)
            os.system("pdftoppm -jpeg {} {}".format(srcf, dstf))


if __name__ == "__main__":
    main()
