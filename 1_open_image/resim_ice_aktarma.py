# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:07:29 2021

@author: Fehime Nur Uysal
"""

# OpenCV kütüphanesinin dahil edilmesi
import cv2


"""
 Resmi içe aktarma fonksiyonu : imread
 Parametreler: Resim dosya yolu , flag 
 
 Flag : 
     Renkli 1 ,
     Gri    0 ,     
"""
img = cv2.imread("messi5.jpg" , 0)


"""
 Resmi gösterme fonksiyonu : imshow()
 Parametreler : Resim başlığı , gösterilecek resim
"""
cv2.imshow("Messi", img)

"""
 Gösterim sırasında hata ile karşılaşmamak adına 
 Klavyeden giriş olmadıkça gösterimin devam etmesini sağlayan fonksiyon : waitKey
 Klavye girişi geldiğinde açılan pencerelerin tümünü kapatan fonksiyon : destroyAllWindows 
"""
key = cv2.waitKey()

# Eğer klavyeden alınan girdi ESC ise
if key == 27 : 
    cv2.destroyAllWindows()

# 1.koşul sağlanmadıysa ve girdi s tuşu ise 
elif key == ord("s"):
    
    """
      Resim kaydetme fonksiyonu : imread
      Parametreler : Resmin kaydedileceği isim ve .dosya uzantısı , kaydedilecek resim
    """
    
    cv2.imwrite("Messi_Gray.png" , img)
    cv2.destroyAllWindows()

    