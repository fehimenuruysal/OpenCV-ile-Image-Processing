# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:27:35 2021

@author: Fehime Nur Uysall
"""

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.JPG")
img2 = cv2.imread("img2.JPG")

# Matplotlib görselleştirme kütüphanesi ile resimleri gösterme
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


"""
 Yukarıdaki ekranda gösterme işleminde orijinal resimlerdeki renklerden farklı renkler gösterildi.
 Sebebi BGR olarak resimlerin içeri aktarılmasıdır.
 
 Bunu RGB türüne dönüştürmek için kullanılan fonksiyon : cvtColor
 Parametreler : 
     - İşlenecek resim
     - Dönüşüm özelliği
"""

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# Karıştırma yaparken resimlerin boyutları aynı olmalıdır.
img1 = cv2.resize(img1, (600,600))
img2 = cv2.resize(img2, (600,600))

"""
 Resimlerin karıştırılması için kullanılan fonksiyon : addWeighted
 Parametreler :
     - Birinci resim
     - Birinci resmin katsayısı
     - İkinci resim
     - İkinci resmin katsayısı
"""
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.2, gamma=0)

plt.figure()
plt.imshow(blended)