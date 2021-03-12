# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:36:00 2021

@author: Fehime Nur Uysal
"""
# OpenCV kütüphanesini import etmek
import cv2

# Resim içe aktarma ve boyutuna bakmak
img_gri = cv2.imread("lenna.png" , 0)
img_renkli = cv2.imread("lenna.png")
print("Gri resmin bouyutu : " , img_gri.shape)
print("Renkli resmin bouyutu : " , img_renkli.shape)

"""
    Renkli de (512,512,3) boyutlarında olduğunu görüyoruz.
    Burada yer alan 3 aslında RGB resminin renk kanallarını göstermektedir.
"""

# Resmin gri ve renkli halini göstermek
cv2.imshow("Siyah Beyaz Resim" , img_gri)
cv2.imshow("Renkli Resim" , img_renkli)

"""
 Yeniden boyutlandırma fonksiyonu : resize
 Parametreler : İşlenecek resim , istenen yeni boyut
"""
img_resized = cv2.resize(img_renkli , (200,200))
print("Resmin yeni boyutu : " , img_resized.shape)
cv2.imshow("Yeniden boyutlandırılmış resim" , img_resized)

"""
 Resimler piksellerden oluşan arraylerdir.
 Bu yüzden arraylerdeki gibi belirli elemanları alma işlemini uygulayarak
 kırpma yapılabilinir.
 
 Bu işlemde [yükseklik , genişlik] sırası ile aralık girilir.
"""
img_cropped = img_renkli[:400,200:500]
cv2.imshow("Kirpilana Resim", img_cropped)

cv2.waitKey()