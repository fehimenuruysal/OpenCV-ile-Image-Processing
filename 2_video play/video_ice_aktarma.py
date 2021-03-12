# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:35:55 2021

@author: Fehime Nur Uysal
"""

# OpenCV kütüphanesinin import edilmesi
import cv2

# Video gösterim hızını ayarlamak için time kütüphanesinin import edilmesi
import time

#Video isminin kolaylık olması için değişkene aktarma
video = "MOT17-04-DPM.mp4"

"""
 Video içeri aktarma fonksiyonu : VideoCapture
 Parametre : Video adı
"""
cap = cv2.VideoCapture(video)

"""
  Video bilgilerine bakmak için kullanılan fonksiyon : get
  Parametre : Property Id
  
  Property Id :
      3 - Genişlik
      4 - Yükseklik
      
      Diğerleri için url :
      https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
"""
print("Genişlik : " , cap.get(3))
print("Yükseklik :" , cap.get(4))


"""
 Videonun açılıp açılmadığına bakmak gerekir.
 cap içerisine aktarım yapılmasa da aktarılmadı uyarısı alınmaz.
 Bu yüzden programın görüntü işleme kısımlarında hatalara oluşabilir.
 Hatalarla karşılaşmamak için kontrol etmek gerekir.
"""
if cap.isOpened() == False:
    print("HATA : Video içe aktarım işlemi gerçekleşmedi !")
    
"""
 Capture okuma fonksiyonu : read
 Fonksiyonun geri döndürdüğü değerler :
     - return : İşlemin gerçekleşip gerçekleşmediğine göre True / False
     - frame  : Video içindeki her bir resim
"""

# While True ile tüm frameleri okumak amaçlıdır.
while True :
    ret , frame = cap.read()
    
    # Okuma işlemi gerçekleşmişse 
    if ret == True:
        # Video hızını ayarlamak 
        time.sleep(0.01)
    
        #Okunan resmin gösterimi
        cv2.imshow("Video", frame)
    
    # Okuma işlemi gerçekleşmemişse yani frame bittiyse döngüyü kırar.
    else :
        break
    
    # Tüm video izlenmek istenmezse "q" tuşu ile video gösterimini sonlandırmak
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
"""
 Video alma işlemini durdurma yani kaynağı serbest bırakma fonksiyonu : release
"""
cap.release()

cv2.destroyAllWindows()

    
    
    
    
    