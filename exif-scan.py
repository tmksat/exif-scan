#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image
import piexif

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename_ = sys.argv[1]
        print("ImageFile=", filename_)
        try:
            exif_dict = piexif.load(filename_)
            for x in range(0, 0xffff):
                try:
                    res = exif_dict["0th"][x]
                    print('index:', x, 'res=', res)
                except:
                    pass
                else:
                    pass
            for x in range(0, 0xffff):
                try:
                    res = exif_dict["Exif"][x]
                    print('index:', x, 'res=', res)
                except:
                    pass
                else:
                    pass
        except:
            print("Cannot open image file.")
        else:
            pass
    else:
        print("Arugument value error.")
