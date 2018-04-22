# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread("./../images/yoz.png")


cv2.imshow('dst_rt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()