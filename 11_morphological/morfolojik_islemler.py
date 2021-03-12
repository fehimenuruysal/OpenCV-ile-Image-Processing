# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 23:15:47 2021

@author: Fehime Nur Uysal
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.png",0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal")
plt.show()


"""
 Erozyon : Sınırların aşındırılmasıdır.
 Erozyon için bir kernel oluşturulur. Bu kernel resim üzerinde gezinir.
 
 Erozyon fonksiyonu : erode
 Paramertreler : 
     - İşlenecek resim
     - Gezecek kernel
     - İterasyon sayısı 
"""
kernel = np.ones((5,5), dtype=np.uint8)
erozyon = cv2.erode(img, kernel, iterations = 2)
plt.figure()
plt.imshow(erozyon, cmap="gray")
plt.axis("off")
plt.title("Erozyon Uygulanan Resim")
plt.show()

"""
 Genişlerme (Dilation) : Sınırları arttırır.
 
 Dilation fonksiyonu : dilate
 Parametreler :
     - İşlenecek resim
     - Gezecek kernel
     - İterasyon sayısı
"""
dilation = cv2.dilate(img, kernel, iterations=4)
plt.figure()
plt.imshow(dilation, cmap="gray")
plt.axis("off")
plt.title("Genisleme Uygulanan Resim")
plt.show()


# White Noise
white_noise = np.random.randint(0,2,size=img.shape[:2])
white_noise = white_noise * 255

noise_img = white_noise + img
plt.figure()
plt.imshow(noise_img, cmap="gray")
plt.axis("off")
plt.title("White Noise Olan Resim")
plt.show()

"""
 Açılma white noise azaltmak için kullanılır.
 Açılma aslında erozyon + genişlemedir.
 
 Açılma fonksiyonu : morphologyEx
 Parametreler : 
     - İşlenecek resim
     - İşlemi seçme
     - Kernel
"""
opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening, cmap="gray")
plt.axis("off")
plt.title("Acilma Uygulanilan Resim")
plt.show()


# Black Noise
black_noise = np.random.randint(0,2,size=img.shape[:2])
black_noise = black_noise * -255
noise_img = black_noise + img
noise_img[noise_img <= -245] = 0


plt.figure()
plt.imshow(noise_img, cmap="gray")
plt.axis("off")
plt.title("Black Noise Olan Resim")
plt.show()

"""
 Kapatma ön plandaki nesnelerin içerisinde yer alan küçük delikleri kapatır.
 Kapatma aslında genişleme + erozyondur.
 
 Kapatma fonksiyonu : morphologyEx
 Parametreler : 
     - İşlenecek resim
     - İşlemi seçme
     - Kernel
"""
closing = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing, cmap="gray")
plt.axis("off")
plt.title("Kapama Uygulanilan Resim")
plt.show()

"""
 Gradient aslında kenar tespit yöntemidir.
"""
gradient = cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap="gray")
plt.axis("off")
plt.title("Gradient Uygulanilan Resim")
plt.show()



































