## Selenium ile web sitesinde oturum açma iþlemi

### Gereksinimler
```pip install selenium```
```pip install pyinstaller```
```pip install time```

### Kullaným

1. Proje dosyalarýný indirin
1. Kendi kullanýcý adýnýzý ve þifrenizi `CpKbuInternetConnection.py` dosyasýnda güncelleyin
1. `CpKbuInternetConnection.py` dosyasýný çalýþtýrýn ve hata alýp almadýðýnýzý kontrol edin eðer hata alýrsanýz chromedriver dosyasýný indirmeniz gerekebilir.
1. Eðer hata alýrsanýz [buradan](https://chromedriver.chromium.org/downloads) iþletim sisteminize uygun olan chromedriver dosyasýný indirin ve `CpKbuInternetConnection.py` dosyasýnýn olduðu dizine kopyalayýn.
1. `CpKbuInternetConnection.py` dosyasýný çalýþtýrýn ve oturum açma iþleminin baþarýlý olup olmadýðýný kontrol edin.
1. Eðer iþlem baþarýlý olduysa `CpKbuInternetConnection.py` dosyasýný `CpKbuInternetConnection.exe` dosyasýna dönüþtürmek için `pyinstaller --onefile --noconsole CpKbuInternetConnection.py` komutunu çalýþtýrýn.
1. `CpKbuInternetConnection.exe` dosyasýný baþlangýç uygulamalarýna ekleyerek bilgisayarýnýzý her açtýðýnýzda oturum açma iþlemini otomatikleþtirebilirsiniz.
1. Proje karabuk universitesinin internet aðýnda oturum açma iþlemini otomatikleleþtirmek için yazýlmýþtýr. Kendinize göre uyarlayabilirsiniz