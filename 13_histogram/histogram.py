# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:20:38 2021

@author: Fehime Nur Uysal
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img_vis)
plt.axis("off")

print("Resim boyutu : " , img_vis.shape)

# Histogram
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)

color = ("b", "g", "r")
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color= c)

"""
 Histogram yorumu : 
     (R,G,B) olarak bakıldığında kırmızı ve mavi olan yerlerde yeşil renk değeri 0 olmaktadır.
     Bu yüzden 0 değerinde yeşil renk piksel sayısı kadardır.
     Daha sonra mavi olan piksellerde (0,0,255) durumu gözlenirken
     kırmızı olan yerlerde (255,0,0) gözlenir. Bu yüzden hem sıfırda hem 255 değerinde kırmızı 
     ve mavi görünmektedir.
     Ayrıca 255 noktasında bakılırsa mavi renk bölgesinin çok az bir farkla daha fazla olduğu 
     gözükmektedir.
"""

# İkinci resim incelemesi
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(golden_gate_vis)
plt.axis("off")

# Resim çok büyük olduğundan küçük bir alana odaklanmak için maske oluşturma
mask = np.zeros(golden_gate.shape[:2], np.uint8)
mask[1500:2000, 1000:2000] = 255

masked_img = cv2.bitwise_and(golden_gate_vis,golden_gate_vis, mask = mask)
plt.figure()
plt.imshow(masked_img)
plt.axis("off")

hist = cv2.calcHist([masked_img], channels=[0], mask=mask, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(hist)  



img = cv2.imread("hist_equ.jpg")
plt.figure()
plt.imshow(img)
plt.axis("off")

hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(hist)  


"""
 Histogram Eşitleme : Kontrastı arttırmayı sağlar.
 
 Histogram eşitleme fonksiyonu : equalizeHist
 Parametre : İşlenecek resim
"""
img = cv2.imread("hist_equ.jpg", 0)

eq_hist_img = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist_img , cmap="gray")
plt.axis("off")


eq_hist = cv2.calcHist([eq_hist_img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(eq_hist)









