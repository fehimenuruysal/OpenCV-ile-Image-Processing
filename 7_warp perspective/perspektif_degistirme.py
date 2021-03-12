# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:07:13 2021

@author: Fehime Nur Uysal
"""

import cv2
import numpy as np 

# Resmi içe aktarma
img = cv2.imread("kart.png")

# Resmi gösterme
cv2.imshow("Orijinal" , img)

# Resmin boyutunu belirleme
width = 400
height = 500

# Köşelerin koordinatları belirlenir (Burada paint kullanılabilir)
mevcut_koseler = np.float32([[205,1],[1,472],[540,150],[338,617]])
istenen_koseler = np.float32([[0,0],[0,height],[width,0],[width,height]])

"""
 Perspektif transform matrisini elde etmek için kullanılan fonksiyon : getPerspectiveTransform
 Parametreler :
     - Mevcut köşe koordinatları
     - İstenen köşe koordinatları
"""
matrix = cv2.getPerspectiveTransform(mevcut_koseler, istenen_koseler)


"""
 Çevirme işlemi için kullanılan fonksiyon : warpPerspective
 Parametreler :
     - İşlenecek resim
     - Rotasyon matrisi
     - İşlenmiş resmin boyutu (genişlik, yükseklik)
"""
result_img = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Perspektif Degismis Resim", result_img)

cv2.waitKey()