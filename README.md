# Kalp Sağlığı Risk Tahmin Sistemi

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
