# Dekoratör Sırası ve Fibonnaci Çağrı Sayıları

'fib(20) hesabı çalıştırıldığında dekoratör sıralamalarının ürettiği çağrı sayıları ve nedenleri:

## 1.Yalnızca '@say'
-**Çağrı Sayısı:** '21891'
-**Aaçıklama:** Önbellekleme yapılmadığı için özyinelemeli Fibonnaci ağacındaki bütün adımlar tekrar tekrar hesaplanır.$F(20)$ için toplam $21891$ fonksiyon çağrısı gerçekleşir.

##2. '@say' Üstte, '@lru_cache' Altta
-**Çağrı Sayısı:** '39'
-**Açıklama:**Dekoratörler 'say(lru_cache(fib))'biçiminde sarmallanır.Çağrı yapıldığında kod önce dıştaki '@say' dekoratörüne uğrayarak sayacı arttırır, ardından '@lru_cache' katmanına geçer.Sonuç önbellekte olsa bile !@say' en dışta yer aldığı için her çağrıda tetiklenir.

##3. '@lru_cache' Üstte, '@say' Altta
-**Çağrı Sayısı:** '21'
-**Açıklama:** Sarmallama 'lru_cache(say(fib))' şeklindedir.En dışta '@lru_cache' olduğu için önceden hesaplanan değerler içteki '@say' dekoratörüne ulaşmadan önbellekten dönülür. '@say' yalnızca önbellekte bulunmayan $0$'dan $20$'ye kadar olan $21$ denzersiz değer için çalışır.Sayaca 'fib.__wrapped__.cagri' üzerinden erişilir.