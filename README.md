# Kalp Sağlığı Risk Tahmin Sistemi

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.7+
- pip (Python paket yöneticisi)

### Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/GulfemKupeli/Takim-205-Proje.git
   cd Takim-205-Proje
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Uygulamayı başlatın:
   ```bash
   uvicorn main:app --reload
   ```

4. Tarayıcınızda açın:
   - API Dokümantasyonu: http://127.0.0.1:8000/docs
   - Varsayılan Arayüz: http://127.0.0.1:8000

## 📚 API Dokümantasyonu

### Endpoint'ler

#### 1. Yeni Analiz Yap
- **URL**: `/api/analyze`
- **Method**: `POST`
- **Açıklama**: Yeni bir kalp sağlığı analizi yapar

#### 2. Tüm Kayıtları Listele
- **URL**: `/api/records`
- **Method**: `GET`
- **Açıklama**: Tüm analiz kayıtlarını listeler

#### 3. Tek Bir Kaydı Getir
- **URL**: `/api/records/{record_id}`
- **Method**: `GET`
- **Açıklama**: Belirli bir analiz kaydının detaylarını getirir

## 🛠 Geliştirme

### Ortam Değişkenleri
`.env` dosyası oluşturarak aşağıdaki değişkenleri ayarlayabilirsiniz:
```
DATABASE_URL=sqlite:///./kalp_sagligi.db
DEBUG=True
```

### Test
```bash
# Testleri çalıştır
pytest
```

## Takım Üyeleri

* Selay Yırtımcı - Product Owner
* Muhammet Yasir Kılıç - Scrum Master
* Gülfem Küpeli - Developer
* Cevdet Satar - Developer
* Döne Beyza Kurt - Developer

## Proje Açıklaması

Bu proje, kullanıcıların yaş, cinsiyet, kilo, tansiyon, kolesterol ve sigara kullanımı gibi sağlık ve yaşam tarzı verilerini toplayarak, makine öğrenimi algoritmaları aracılığıyla bireysel kalp hastalığı riskini tahmin etmeyi amaçlamaktadır.

Temel hedefimiz, risk altındaki bireyler için erken uyarı sistemi oluşturmaktır. Bu sayede kişilerin yaşam alışkanlıklarını değiştirerek sağlıklarını iyileştirmelerine yardımcı olmak ve sağlık profesyonellerinin önleyici tedbirler almasını kolaylaştırmak hedeflenmektedir. Bu projenin, sağlık yönetiminde daha proaktif bir yaklaşım benimsenmesine olanak sağlayacağına inanıyoruz.

## Proje Özellikleri

### Detaylı Sağlık Veri Girişi
Kullanıcılar, yaş, cinsiyet, kilo, boy, tansiyon (sistolik/diyastolik), kolesterol (LDL/HDL/total), sigara kullanımı, alkol tüketimi ve fiziksel aktivite düzeyi gibi hayati sağlık verilerini kolayca sisteme girebilirler.

### Güçlü Veri Validasyonu
Girilen tüm veriler, hem kullanıcı arayüzünde (frontend) anında geri bildirimle hem de sunucu tarafında (backend) titizlikle doğrulanır. Bu, hatalı veya tutarsız veri girişlerini engelleyerek sistemin güvenilirliğini artırır.

### Akıllı Kalp Hastalığı Riski Tahmini

* Kullanıcının girdiği veriler, gelişmiş makine öğrenmesi algoritmaları (örneğin, Lojistik Regresyon, Destek Vektör Makineleri) kullanılarak analiz edilir.
* Sistem, kullanıcının bireysel kalp hastalığı riskini gösteren sayısal bir risk puanı üretir.
* Bu puan, "düşük riskli", "orta riskli" veya "yüksek riskli" gibi anlaşılır kategorilere dönüştürülerek sunulur.
* Kullanıcılar, risk puanlarını etkileyen ana faktörleri (örneğin, yüksek tansiyon, LDL kolesterol seviyesi, sigara alışkanlığı) açıklayıcı bir şekilde görebilirler.

### Yapay Zeka Destekli Kişiselleştirilmiş Sağlık Rehberliği

* **Diyet Önerileri:** Kullanıcının risk profili, sağlık verileri ve mevcut alışkanlıkları temel alınarak, kalp sağlığını destekleyici kişiselleştirilmiş diyet planları ve beslenme önerileri sunulur. Bu öneriler, dış yapay zeka API'leri (örneğin, beslenme veri tabanları ve öneri motorları) ile entegre çalışır.
* **Günlük Rutin ve Egzersiz Tavsiyeleri:** Yaş, fiziksel aktivite düzeyi ve risk durumu gibi faktörler göz önünde bulundurularak, kullanıcının kalp sağlığını iyileştirecek kişiselleştirilmiş günlük rutinler ve egzersiz programları önerilir. Bu tavsiyeler de dinamik olarak yapay zeka API'leri aracılığıyla üretilir.

### Proaktif Yaklaşım ve Kullanıcı Bilinçlendirmesi

* Kullanıcılara, girdi verileri ve tahmin edilen risk puanlarını içeren detaylı bir risk raporu sunulur.
* Bu raporlar, bireyleri potansiyel riskler hakkında bilgilendirir ve risklerini düşürmeye yönelik genel yaşam tarzı önerileri (örn. stresten kaçınma, yeterli uyku) sunarak sağlık yönetiminde bilinçli adımlar atmalarını teşvik eder.

## Hedef Kitle

* **Kalp Hastalığı Riski Taşıyan Bireyler:** Ailesinde kalp hastalığı öyküsü olanlar, yüksek tansiyon, yüksek kolesterol, diyabet gibi risk faktörlerine sahip olanlar veya sigara içen, hareketsiz bir yaşam süren kişiler. Bu bireyler, risklerini anlamak ve önleyici adımlar atmak konusunda bilinçlenmek isterler.
* **Sağlık Bilincine Sahip Bireyler:** Kendi sağlıklarını aktif olarak yönetmek isteyen, düzenli kontrollerini yaptıran ve yaşam kalitelerini artırmak için kişiselleştirilmiş sağlık önerileri arayan herkes.
* **Sağlık Profesyonelleri (Dolaylı olarak):** Doktorlar, diyetisyenler ve sağlık koçları gibi profesyoneller, hastalarına veya danışanlarına daha iyi hizmet sunmak için bu tür bir aracı bir ön bilgi kaynağı veya destekleyici bir araç olarak kullanılabilir. Proje, profesyonellerin önleyici tedbirler almasını kolaylaştırarak hasta yönetiminde proaktif bir yaklaşım benimsemelerine yardımcı olabilir.
* **7/24 Sağlık Takibi Arayanlar:** Geleneksel sağlık hizmetlerine ek olarak, sürekli erişilebilir bir risk analizi ve yaşam tarzı rehberliği arayan kişiler.




# Sprint 1 Raporu

## Puan Tamamlama Mantığı

Takımın geç toplanması ve fikre karar verme noktasında kaybedilen zamanlar göz önünde bulundurularak ilk sprint için **10 puan** hedeflenmiştir.

İkinci sprint'te makine öğrenmesi (ML) algoritmalarına uygun veri toplanması, algoritmaların eğitimi ve ekstra olarak API entegrasyonu planlandığından dolayı puan **30 olarak belirlenmiştir**.

Son sprint'te ise Model optimizasyonu ve UI/UX iyileştirmeleri planlanmakta olup puan yine **30 olarak belirlenmiştir**.

Proje boyunca tamamlanması gereken toplam puan **70'dir**.

## Sprint İçi Beklenen Puan

10

## Product Backlogs

[Kalp Krizi Risk Tahmini Uygulaması](https://trello.com/invite/b/686640d8a2c4224f0b593859/ATTI209ccfdb3a91d40d26b764babd0083e3EB0389C8/kalp-krizi-risk-tahmini-uygulamasige)

## Daily Scrum

* Whatsapp üzerinden iletişim sağlanmıştır. [Whattsapp SS](https://imgur.com/a/daily-scrum-q37h1rj)

## Sprint board update
<img width="865" height="631" alt="Image" src="https://github.com/user-attachments/assets/98765ecf-eccb-417d-a17a-32570a77c121" />

## Ürün fotoğrafı
<img width="665" height="1231" alt="Image" src="https://github.com/user-attachments/assets/0281fd92-5a09-484a-88c7-d68efafa66e4" />

## Sprint Review

Gerçekleşen toplantıda şu ana kadar yapılanlar üzerinden genel bir değerlendirme yapıldı. Projede ihtiyaç duyulacak altyapıların numuneleri üzerinden hangi noktaların geliştirilmesi gerektiği gözden geçirildi.

## Sprint Retrospective

Grubun 3'e bölünmesi kararlaştırıldı:

* **1. Grup:** ML entegrasyonu üzerine çalışacak (veri setlerinin keşfi, EDA, Model eğitimi).
    * Üyeler: Cevdet Satar, Muhammet Yasir Kılıç
* **2. Grup:** Yapay zeka API entegrasyonu ve veritabanı üzerine çalışacak.
    * Üyeler: Selay Yırtımcı, Döne Beyza Kurt
* **3. Grup:** UI/UX dizaynı ile ilgilenecek.
    * Üyeler: Gülfem Küpeli
 

# 🩺 Sprint 2 Raporu – Kalp Hastalığı Risk Tahmin Uygulaması
🎯 Sprint Hedefi
Sprint 2'nin ana amacı, kullanıcıdan sağlık ve yaşam tarzı verilerinin alındığı bir web arayüzü geliştirmek, bu verileri FastAPI backend'ine aktarmak ve kurala dayalı basit bir kalp hastalığı risk tahmin sistemi oluşturmaktı.

✅ Tamamlanan Başlıca Geliştirmeler
🔹 Kullanıcı Arayüzü (UI)
Modern ve kullanıcı dostu bir HTML/CSS tabanlı form tasarlandı.

Kullanıcıdan alınan veriler form aracılığıyla backend’e gönderilebiliyor.

Responsive (mobil uyumlu) ve sezgisel bir tasarım oluşturuldu.

✏️ Alınan Bilgiler:
Yaş, Cinsiyet, Kilo, Boy

Tansiyon (Sistolik / Diyastolik)

Toplam Kolesterol

Sigara Kullanımı

Alkol Kullanımı

Fiziksel Aktivite Düzeyi

<p align="center"> <img width="300" alt="form-ss" src="https://github.com/user-attachments/assets/f4ed4a5e-2fb0-4327-b76c-e671aaf98015" /> </p>
🔹 Backend ve API Geliştirmeleri (FastAPI)
/api/analyze endpoint'i geliştirildi.

Kullanıcının gönderdiği veriler alınarak işleniyor.

Kurala dayalı risk hesaplama sistemi oluşturuldu:

Yüksek tansiyon, yüksek kolesterol, sigara/alkol kullanımı gibi durumlara göre risk belirleniyor.

Risk düzeyleri: Düşük, Orta, Yüksek

🔹 Veritabanı Altyapısı
SQLite ile temel veritabanı bağlantısı kuruldu.

Kullanıcı verilerinin kalıcı şekilde saklanmasına yönelik model şeması hazırlandı.

Gelecek sprint’te kullanıcı geçmişi ve analiz sonuçlarının saklanması sağlanacak.

##  👥 Ekip ve Görev Dağılımı
Grup No	Görev Tanımı	Üyeler
1	ML entegrasyonu ve veri analizi	Cevdet Satar, Muhammet Yasir Kılıç
2	Yapay Zeka API’leri ve veritabanı bağlantısı	Selay Yırtımcı, Döne Beyza Kurt
3	UI/UX tasarımı ve form veri akışı	Gülfem Küpeli

##🔎 Sprint Detayları
🧮 Puan Tamamlama Durumu
Hedeflenen puan: 30

Gerçekleşen: 28/30

Eksik kalan işler:

ML modelinin backend’e tam entegrasyonu

Öneri sisteminin temel yapısının başlatılması

## 📆 Daily Scrum Süreci
WhatsApp üzerinden her gün takım içi iletişim sağlandı.

Durum güncellemeleri, sorun bildirimi ve planlama aksatılmadan yürütüldü.

## ✅ Sprint Review
Uygulama formu başarıyla çalıştı ve backend ile entegre oldu.

Risk hesaplama mekanizması test edilip çalışır hale getirildi.

Arayüz geri bildirimlere göre daha sezgisel hale getirildi.

## 🔄 Sprint Retrospective
UI geliştirmesi beklenenden fazla zaman aldı fakat projenin temeli sağlandı.

Backend ve veri iletimi sorunsuz tamamlandığı için Sprint 3'te ML modeline daha fazla odaklanılabilecek.

Erken veritabanı bağlantısı, ileride yapılacak kullanıcı takip sistemine zemin hazırladı.

## 📌 Sprint 3 İçin Planlananlar
Makine öğrenmesi modeli entegrasyonu (sklearn veya tensorflow kullanımı).

Kullanıcıya özel risk geçmişi ve görselleştirme ekranları.

Öneri sisteminin geliştirilmesi (beslenme, egzersiz vb.).

Risk skorlarının grafiklerle desteklenmesi.
