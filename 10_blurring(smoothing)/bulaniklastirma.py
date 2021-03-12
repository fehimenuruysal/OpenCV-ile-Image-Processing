# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:04:13 2021

@author: Fehime Nur Uysal
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()


"""
 Ortalama bulaklaştırma yöntemi
 
 Bulanıklaştırma fonksiyonu : blur
 Parametreler :
     - İşlenecek resim
     - Çerçeve boyutu
"""
ort_blur = cv2.blur(img, ksize=(3,3))
plt.figure()
plt.imshow(ort_blur)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırma")
plt.show()


# Gaussian gürültüsü oluşturma
def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0 
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    
    noisy = image + gauss
    
    return noisy

# Normalize etme
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255

noisy_img = gaussianNoise(img) 
plt.figure()
plt.imshow(noisy_img)
plt.axis("off")
plt.title("Gaussian Gürültülü Resim")
plt.show()

"""
 Gauss bulanıklaştırma yöntemi
 
 Bulanıklaştırma  fonksiyonu : GaussianBlur
 Parametreler : 
     - İşlenecek resim
     - Çerçeve boyutu
     - X yönündeki sigma
"""
gaussian_blur = cv2.GaussianBlur(noisy_img, ksize=(3,3), sigmaX=8)
plt.figure()
plt.imshow(gaussian_blur)
plt.axis("off")
plt.title("Gaussian Bulanıklaştırma ile Gürültü Kaldırma")
plt.show()


# Tuz-Karabiber gürültüsü oluşturma
def salt_pepper_noise(image):
    row, col, ch = image.shape
    
    # Siyah ve beyazın oranları
    s_vs_p = 0.4
    
    # Miktarı
    amount = 0.004
    
    noisy = np.copy(image)
    
    #Tuz 
    num_salt = np.ceil(amount * image.size * s_vs_p)
    #Tuzun koordinatları
    coords = [np.random.randint(0,i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    #Karabiber
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    #Karabiber koordinatları
    coords = [np.random.randint(0,i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

sp_img = salt_pepper_noise(img)
plt.figure()
plt.imshow(sp_img)
plt.axis("off")
plt.title("Tuz Biber Gürültülü Resim")
plt.show()   
    
"""
 Medyan bulanıklaştırma yöntemi
 
 Bulanıklaştırma  fonksiyonu : medianBlur
 Parametreler : 
     - İşlenecek resim
     - Kernel boyutu
"""
median_blur = cv2.medianBlur(sp_img.astype(np.float32), ksize=3)
plt.figure()
plt.imshow(median_blur)
plt.axis("off")
plt.title("Medyan Bulanıklaştırma ile Gürültü Kaldırma")
plt.show()

    
    
    
    
    
    
    
    
    
    
    