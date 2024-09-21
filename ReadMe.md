## Selenium ile web sitesinde oturum a�ma i�lemi

### Gereksinimler
```pip install selenium```
```pip install pyinstaller```
```pip install time```

### Kullan�m

1. Proje dosyalar�n� indirin
1. Kendi kullan�c� ad�n�z� ve �ifrenizi `CpKbuInternetConnection.py` dosyas�nda g�ncelleyin
1. `CpKbuInternetConnection.py` dosyas�n� �al��t�r�n ve hata al�p almad���n�z� kontrol edin e�er hata al�rsan�z chromedriver dosyas�n� indirmeniz gerekebilir.
1. E�er hata al�rsan�z [buradan](https://chromedriver.chromium.org/downloads) i�letim sisteminize uygun olan chromedriver dosyas�n� indirin ve `CpKbuInternetConnection.py` dosyas�n�n oldu�u dizine kopyalay�n.
1. `CpKbuInternetConnection.py` dosyas�n� �al��t�r�n ve oturum a�ma i�leminin ba�ar�l� olup olmad���n� kontrol edin.
1. E�er i�lem ba�ar�l� olduysa `CpKbuInternetConnection.py` dosyas�n� `CpKbuInternetConnection.exe` dosyas�na d�n��t�rmek i�in `pyinstaller --onefile --noconsole CpKbuInternetConnection.py` komutunu �al��t�r�n.
1. `CpKbuInternetConnection.exe` dosyas�n� ba�lang�� uygulamalar�na ekleyerek bilgisayar�n�z� her a�t���n�zda oturum a�ma i�lemini otomatikle�tirebilirsiniz.
1. Proje karabuk universitesinin internet a��nda oturum a�ma i�lemini otomatiklele�tirmek i�in yaz�lm��t�r. Kendinize g�re uyarlayabilirsiniz