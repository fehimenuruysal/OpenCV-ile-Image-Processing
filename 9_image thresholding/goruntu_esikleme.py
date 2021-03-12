# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:30:43 2021

@author: Fehime Nur Uysal
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.JPG")

# Resmi gray scale dönüşümü
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
 Gray Scale : Resimdeki renklerin gri skalada olmasıdır.
              Renk tonlarının bu skalada ifade edilmesidir.
              0-255 arasında değerler vardır.
"""

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()


"""
 Eşikleme sayesinde resimdeki ana hatlar ortaya çıkartılır.
 
 Görüntü eşikleme fonksiyonu : threshold
 Parametreler: 
     - İşlenecek resim
     - Threshold (eşik) alt sınırı 
     - Threshold üst sınırı
     - Threshold tipi
 Return : 
     - İşlem uygulanmış resim
"""
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

#THRESH_BINARY : Alt ve üst sınır arasındaki değerleri 255 yapar.
#THRESH_BINARY_INV : Alt ve üst sınır dışındaki değerler 255 yapar.

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()


"""
 Adaptive Thresholding : Bir nesnenin farklı ışıklandırma durumundan dolayı bütünlüğünü bozmamak için tercih edilir.

 Adaptive thresholding fonksiyonu : adaptiveThreshold
 Parametreler : 
     - İşlenecek resim
     - Maksimum değer
     - Yöntem
     - Eşikleme türü
     - Block size yani 11 komşu piksel
     - Ortalaamadan veya ağırlıklı ortalamadan çıkartılacak değer
"""
adaptive_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11 , 8)

plt.figure()
plt.imshow(adaptive_img, cmap="gray")
plt.axis("off")
plt.show()