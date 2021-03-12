# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:09:05 2021

@author: Fehime Nur Uysal
"""

import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg",0)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal")

# X gradyan tespiti (ddeppth : output derinliği, ksize: kernel boyutu)
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure()
plt.imshow(sobelx, cmap="gray")
plt.axis("off")
plt.title("X Gradyan")

# Y gradyan tespiti (ddeppth : output derinliği, ksize: kernel boyutu)
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure()
plt.imshow(sobely, cmap="gray")
plt.axis("off")
plt.title("Y Gradyan")

# Laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap="gray")
plt.axis("off")
plt.title("Laplacian Gradyan")
