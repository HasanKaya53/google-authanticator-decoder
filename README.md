# google authanticator decoder. 

<b> OTP yardımıyla, telefon da üretilen google authanticator kodlarını bulma. </b>

<h3> Kullanım: </h3>

my_secret kısmına google authanticator tarafındaki kurulum anahtarını (Secret key) girin ve projeyi başlatın. 


<b> Kurulum anahtarını bilmiyorsanız ve elinizde QR Kod varsa; </b> https://github.com/dim13/otpauth (Proje içersinde paylaştım.) Projesini incelemenizi tavsiye ederim. 

<h3> Proje Kullanımı </h3>
<ul>
<li>  Üstteki projeyi indirmeden önce GO programalama dilini bilgisayarınıza indirin. </li>
<li> Proje dizininde terminali başlatın ve "go install" komutunu çalıştırın. </li>
<li> Sonrasında go get github.com/dim13/otpauth ~/go/bin/otpauth -link "otpauth-migration://offline?data=CjEKCkhlbGxvId6tvu8SGEV4YW1wbGU6YWxpY2VAZ29vZ2xlLmNvbRoHRXhhbXBsZTAC" komutunu çalıştırın ve secret keyi elde edin. <br> <small> (alternatif: ~/go/bin/otpauth -link "otpauth-migration://offline?data=CjEKCkhlbGxvId6tvu8SGEV4YW1wbGU6YWxpY2VAZ29vZ2xlLmNvbRoHRXhhbXBsZTAC")  </small>
</li>
</ul>
<br>

 <small> 
 (migration almak için bir kaç yol mevcut. Bunlardan en basiti QR kodu okuttuğunuz zaman link olarak size verilmekte ya da otpauth içersinde QR decoder methodu mevcut. Oraya dosyayı yollayıp çözebilirsiniz.)
 
 </small>
 


 
 

