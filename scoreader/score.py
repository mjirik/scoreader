#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.
#
# you have to install tesseract
# https://github.com/tesseract-ocr/tesseract/wiki/Downloads
# and
# VC2015 redistributables
# and
# tessdata for eng
# https://github.com/tesseract-ocr/tessdata


"""
%HERE%
"""

import logging
logger = logging.getLogger(__name__)
import argparse

import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.misc
import skimage
import skimage.io
import pytesseract
import os.path as op
from PIL import Image

def get_image():
    URL = "http://uc452cam01-kky.fav.zcu.cz/snapshot.jpjjg"
# URL = "http://plzen.cz/kamera.php?0.8989779513794929"
# URL = "http://www.chmi.cz/files/portal/docs/meteo/kam/pribram.jpg"
    fn = "~/Dropbox/Screenshots/20160611183123_1.jpg"



    fn_abs = op.expanduser(fn)
    print fn_abs
    im = skimage.io.imread(fn_abs)
    # im = skimage.io.imread(URL, as_grey=True)
    plt.imshow(im)
    plt.show()
    # print pytesseract.image_to_string(Image.open(fn_abs), lang='eng')
    print pytesseract.image_to_string(Image.open(fn_abs))# , lang='eng')
    # print pytesseract.image_to_string(im, lang='eng')

def main():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    # create file handler which logs even debug messages
    # fh = logging.FileHandler('log.txt')
    # fh.setLevel(logging.DEBUG)
    # formatter = logging.Formatter(
    #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)
    # logger.debug('start')

    # input parser
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        '-i', '--inputfile',
        default=None,
        # required=True,
        help='input file'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Debug mode')
    args = parser.parse_args()

    if args.debug:
        ch.setLevel(logging.DEBUG)

    get_image()



if __name__ == "__main__":
    main()