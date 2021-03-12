# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:03:47 2021

@author: Fehime Nur Uysal
"""

import cv2

# Resim eklemek yerine siyah bir resim oluşturmak için numpy kütüphanesini eklemek
import numpy as np

# Siyah 512x512'lik bir resim oluşturmak
img = np.zeros((512,512,3),np.uint8)
print("Resmin boyutu : " , img.shape)

# Resmi göstermek
cv2.imshow("Siyah Resim" , img)

"""
 Resmin üzerine çizgi ekleme fonksiyonu : line
 Parametreler : 
     - İşlenecek resim ,
     - Çizginin başlangıç noktası , 
     - Çizginin bitiş noktası , 
     - Çizginin rengi (BGR),
     - Çizgi kalınlığı
"""
cv2.line(img, (0,0), (512,512), (0,255,0) , 5)
cv2.imshow("Line" , img)

"""
 Resmin üzerine dikdörtgen ekleme fonksiyonu : rectangle
 Parametreler :
     - İşlenecek resim,
     - Dikdörtgenin başlangıç noktası,
     - Dikdörtgenin bitiş noktası,
     - Dikdörtgenin rengi (BGR),
     - Dikdörtgenin içini doldurmak
"""
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen" , img)

"""
 Resmin üzerine çember ekleme fonksiyonu : circle
 Parametreler :
     - İşlenecek resim
     - Çemberin merkez noktası
     - Çemberin yarıçapı
     - Çemberin rengi
     - Çemberin çizgi kalınlığı
"""
cv2.circle(img, (300,300),45,(0,0,255) , 4)
cv2.imshow("Cember", img)

"""
 Resmin üzerine metin ekleme fonksiyonu : putText
 Parametreler : 
     - İşlenecek resim 
     - Metnin kendisi 
     - Resim üzerindeki konumu 
     - Metnin fontu
     - Kalınlığı
     - Renk
"""
cv2.putText(img, "Metin", (350,350), cv2.FONT_HERSHEY_COMPLEX , 1 ,  (255,255,255))
cv2.imshow("Metin",img)

cv2.waitKey()