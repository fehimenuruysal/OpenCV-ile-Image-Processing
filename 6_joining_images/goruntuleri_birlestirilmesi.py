# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:51:48 2021

@author: Fehime Nur Uysal
"""

import cv2
import numpy as np

# Resmi içe aktarma
img = cv2.imread("lenna.png")

# Resmi gösterme
cv2.imshow("Orijinal", img)

"""
 Resmi yatayda birleştirme fonksiyonu : np.hstack
 Parametreler: 
     - Birleştirilecek resimler
"""
hor = np.hstack((img , img))
cv2.imshow("Yatay" , hor)

"""
 Resmi dikey birleştirme fonksiyonu : np.vstack
 Parametreler:
     - Birleştirilecek resimler
"""
ver = np.vstack((img,img))
cv2.imshow("Dikey", ver)


cv2.waitKey()