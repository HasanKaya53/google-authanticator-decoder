# google authanticator decoder. 

OTP yardımıyla, telefon da üretilen google authanticator kodlarını bulma.

Kullanım:

my_secret kısmına google authanticator tarafındaki Kurulum anahtarını girin ve projeyi başlatın. 


Kurulum anahtarını bilmiyorsanız ve elinizde QR Kod varsa;
https://github.com/dim13/otpauth (Proje içersinde paylaştım.)
Projesini incelemenizi tavsiye ederim. 

 * Üstteki projeyi indirmeden önce GO programalama dilini bilgisayarınıza indirin.
 * Proje dizininde terminali başlatın ve "go install" komutunu çalıştırın.
 * Sonrasında go get github.com/dim13/otpauth ~/go/bin/otpauth -link "otpauth-migration://offline?data=CjEKCkhlbGxvId6tvu8SGEV4YW1wbGU6YWxpY2VAZ29vZ2xlLmNvbRoHRXhhbXBsZTAC" komutunu çalıştırın ve secret keyi elde edin.
 (alternatif: ~/go/bin/otpauth -link "otpauth-migration://offline?data=CjEKCkhlbGxvId6tvu8SGEV4YW1wbGU6YWxpY2VAZ29vZ2xlLmNvbRoHRXhhbXBsZTAC")
 
 
 (migration almak için bir kaç yol mevcut. Bunlardan en basiti QR kodu okuttuğunuz zaman link olarak size verilmekte ya da otpauth içersinde QR decoder methodu mevcut. Oraya dosyayı yollayıp çözebilirsiniz.)
 
 

