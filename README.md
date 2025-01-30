# Subdomain Keşif Aracı

Bu araç, hedef domainler için kapsamlı bir subdomain tarama sistemi sunar. Pasif ve aktif tarama yöntemlerini birleştirerek, DNS kayıtlarını analiz eder ve wildcard DNS yapılandırmalarını tespit eder.

## Özellikler

- Çoklu DNS sunucusu kullanarak paralel sorgulama
- Certificate Transparency (crt.sh) loglarından subdomain keşfi
- Brute force ve permütasyon tabanlı tarama
- Wildcard DNS yapılandırması tespiti
- Sonuçların doğrulanması ve erişilebilirlik kontrolü
- Detaylı loglama sistemi

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Subdomain wordlist dosyasını hazırlayın (varsayılan: subdomains.txt)

## Kullanım

```bash
python subdomain_scanner.py
```

Program çalıştığında hedef domain'i girmeniz istenecektir. Örnek: example.com

## Çıktılar

1. `{domain}_subdomains.txt`: Bulunan tüm subdomainlerin listesi
2. `subdomain_scan.log`: Detaylı tarama logları

## Güvenlik Notları

- Bu aracı yalnızca izin verilen sistemler üzerinde kullanın
- Rate limiting özelliği ile hedef sistemlere aşırı yük bindirmekten kaçının
- Sonuçları güvenlik testleri için kullanmadan önce doğrulayın

## Teknik Detaylar

- Python 3.7+ gereklidir
- Asenkron programlama ile yüksek performans
- Modüler yapı sayesinde kolayca genişletilebilir
- Hata yönetimi ve loglama sistemi entegre edilmiş

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun 