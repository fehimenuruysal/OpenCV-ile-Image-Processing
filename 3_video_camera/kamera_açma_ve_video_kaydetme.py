# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:15:51 2021

@author: Fehime Nur Uysal
"""

# OpenCV kütüphanesini import etmek
import cv2

"""
 Video yakalamak için fonksiyon : VideoCapture
 Parametre : Kamera seçim işlemi için flag 
 
 Flag : 
     - 0  : Default kamera seçimi
"""
cap = cv2.VideoCapture(0)

# Kamera genişliğini öğrenmek
genislik = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Kamera yüksekliğini öğrenmek
yukseklik = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(genislik , yukseklik)

"""
 Video kaydetmek için kullanılan fonksyion : VideoWriter
 Parametreler : 
     - Video kaydına verilmek istenen isim , 
     - Windows için kullanılan frameleri sıkıştırmak için kullanılan codec kodu
     - Saniyedeki frame sayısı , 
     - Frame genişliği , 
     - Frame yüksekliği        
"""
writer = cv2.VideoWriter("video_kaydi.mp4" , cv2.VideoWriter_fourcc(*"DIVX"), 20, (genislik , yukseklik))

while True :
    
    ret , frame = cap.read()
    cv2.imshow("Viddeo" , frame)
    
    # Frame kaydetme
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
writer.release()
cv2.destroyAllWindows()
    
    