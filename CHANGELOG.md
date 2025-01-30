# Changelog



## [1.1.0] - 2024-01-30

### JSON Çıktı Formatı Güncellemesi
#### Eklenenler
- Detaylı JSON formatında sonuç çıktısı
- Her tarama sonucu için timestamp bilgisi
- IP adresi kayıtları
- Hata mesajları için detaylı raporlama
- Tarama başlangıç ve bitiş zamanı kayıtları

#### Değişenler
- Tüm metotlar JSON formatında veri döndürecek şekilde güncellendi
- Çıktı dosyaları hem .txt hem de .json formatında kaydediliyor
- Sonuç formatı daha detaylı ve yapılandırılmış hale getirildi

#### Düzeltilenler
- Veri tipi tanımlamaları güncellendi
- Hata yakalama mekanizması iyileştirildi

## [1.0.0] - 2024-01-30

### Gün 3 - Windows Uyumluluğu ve Performans İyileştirmeleri
#### Eklenenler
- Windows işletim sistemi için SelectorEventLoop desteği
- Detaylı hata yakalama ve loglama sistemi

#### Değişenler
- aiodns ve aiohttp bağımlılıkları kaldırıldı
- DNS sorgulama sistemi yeniden yapılandırıldı
- Asenkron yapı optimize edildi

#### Düzeltilenler
- Windows'ta çalışmama sorunu giderildi
- DNS sorgulamalarındaki performans sorunları çözüldü

### Gün 2 - Temel Özelliklerin Geliştirilmesi
#### Eklenenler
- Certificate Transparency (crt.sh) entegrasyonu
- Wildcard DNS yapılandırması tespit sistemi
- Rate limiting özelliği
- İlerleme çubuğu (tqdm) entegrasyonu

#### Değişenler
- DNS sorgulama sistemi paralel hale getirildi
- Sonuç formatı standartlaştırıldı
- Loglama sistemi geliştirildi

#### Düzeltilenler
- Subdomain doğrulama algoritması iyileştirildi
- Bellek kullanımı optimize edildi

### Gün 1 - Temel Altyapı
#### Eklenenler
- Proje temel dosya yapısı oluşturuldu
- Asenkron tarama altyapısı kuruldu
- Çoklu DNS sunucu desteği
- Temel subdomain tarama fonksiyonları
- requirements.txt dosyası
- README.md dokümantasyonu

#### Değişenler
- Proje yapısı modüler hale getirildi
- DNS sunucu listesi genişletildi

#### Düzeltilenler
- Temel kod yapısındaki hatalar giderildi
- Dosya okuma/yazma işlemleri iyileştirildi


