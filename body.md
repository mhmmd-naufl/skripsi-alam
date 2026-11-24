# BAB I PENDAHULUAN


## 1.1 Latar Belakang

Arugula (*Eruca sativa* Mill.) adalah sayuran daun dari famili Brassicaceae yang semakin dicari sebagai bahan salad, pizza, dan hidangan restoran modern. Harganya per kilogram relatif tinggi dibanding sayuran daun lokal seperti sawi, dan permintaannya terutama datang dari kafe, restoran, dan hotel. Banyuwangi memiliki sektor pariwisata yang besar, sehingga ada peluang pasar bagi sayuran premium yang diproduksi di dekat konsumennya.

Kecamatan Licin berada di kaki Pegunungan Ijen dan Raung dengan udara yang sejuk, curah hujan cukup tinggi, dan tanah vulkanik yang subur. Kondisi ini sesuai untuk sayuran daun yang menyukai iklim sejuk. Namun lahan di Licin banyak yang miring dan terbatas, sehingga budidaya dalam polybag di pekarangan atau lahan sempit menjadi pilihan yang realistis bagi petani kecil. Arugula berakar dangkal sehingga peka terhadap kekurangan maupun kelebihan air. Pengelolaan air karena itu sangat menentukan pertumbuhan dan hasilnya. Irigasi tetes dikenal hemat air karena air diberikan langsung ke zona perakaran. Pada sistem polybag, efektivitasnya sangat bergantung pada kemampuan media tanam menahan air. Kompos meningkatkan daya tahan air, sedangkan sekam bakar membuat media lebih porous dan cepat meloloskan air. Interval irigasi yang cocok untuk satu komposisi media belum tentu cocok untuk media lain.

Kajian yang menggabungkan komposisi media tanam dan interval irigasi tetes pada arugula skala polybag masih terbatas, terutama untuk kondisi dataran tinggi seperti Licin. Penelitian ini dilakukan untuk menjawab kebutuhan tersebut. Hasilnya diharapkan menjadi dasar paket budidaya arugula polybag (resep media dan jadwal penyiraman) yang efisien air dan dapat dikembangkan menjadi usaha.

Sebagai pendukung, penelitian ini memakai sensor kelembapan dan suhu media berbasis mikrokontroler untuk memantau kondisi media secara kontinu. Data sensor membantu menjelaskan mengapa suatu kombinasi perlakuan menghasilkan pertumbuhan yang berbeda. Sensor berfungsi sebagai alat ukur pendukung dan bukan variabel yang diuji.

## 1.2 Rumusan Masalah

1. Bagaimana pengaruh komposisi media tanam terhadap pertumbuhan dan hasil arugula?
2. Bagaimana pengaruh interval irigasi tetes terhadap pertumbuhan dan hasil arugula?
3. Bagaimana interaksi antara komposisi media tanam dan interval irigasi tetes terhadap pertumbuhan, hasil, dan efisiensi penggunaan air, serta kombinasi mana yang paling baik?

## 1.3 Tujuan Penelitian

1. Mengetahui pengaruh komposisi media tanam terhadap pertumbuhan dan hasil arugula.
2. Mengetahui pengaruh interval irigasi tetes terhadap pertumbuhan dan hasil arugula.
3. Menentukan ada tidaknya interaksi antara kedua faktor serta kombinasi perlakuan yang menghasilkan pertumbuhan, hasil, dan efisiensi penggunaan air terbaik.

## 1.4 Hipotesis

1. Komposisi media tanam berpengaruh nyata terhadap pertumbuhan dan hasil arugula.
2. Interval irigasi tetes berpengaruh nyata terhadap pertumbuhan dan hasil arugula.
3. Terdapat interaksi nyata antara komposisi media tanam dan interval irigasi tetes, dan kombinasi perlakuan tertentu menghasilkan hasil serta efisiensi penggunaan air tertinggi.

## 1.5 Manfaat Penelitian

- **Ilmiah:** menyediakan data respon arugula terhadap media tanam dan interval irigasi tetes di dataran tinggi.
- **Praktis:** memberi rekomendasi paket budidaya arugula polybag bagi petani dan pengelola pekarangan.
- **Bisnis:** menjadi dasar pengembangan usaha sayuran premium untuk kafe dan hotel di Banyuwangi.
- **Teknologi:** menunjukkan penggunaan monitoring sensor berbiaya rendah dalam penelitian budidaya skala kecil.

## 1.6 Batasan Penelitian

- Hanya menggunakan satu varietas arugula dan satu lokasi.
- Volume air per penyiraman ditetapkan sama untuk semua perlakuan; yang divariasikan hanya interval penyiraman.
- Percobaan dilakukan dalam polybag di bawah rain shelter, sehingga hasilnya tidak langsung berlaku untuk lahan terbuka.
- Monitoring sensor dilakukan pada polybag sampel dan bersifat pendukung.
- Analisis usaha hanya bersifat pendukung.

---

# BAB II TINJAUAN PUSTAKA


## 2.1 Tanaman Arugula

Arugula (*Eruca sativa* Mill., sinonim *E. vesicaria* (L.) Cav.) termasuk famili Brassicaceae dan merupakan sayuran daun tahunan (annual garden rocket) yang berasal dari wilayah Mediterania. Di Indonesia, arugula mulai dikenal sebagai sayuran salad premium, tetapi budidayanya masih terbatas pada skala kecil, umumnya secara hidroponik atau dalam polybag.

Dari sisi fisiologi, arugula lebih cocok pada iklim sejuk. Hall et al. (2015) melaporkan bahwa perkecambahan optimal *E. sativa* berada pada kisaran suhu 20–25 °C, dan suhu pertumbuhan tinggi (40 °C) secara nyata menekan pertumbuhan serta kelangsungan hidup tanaman. Penelitian pada sistem aeroponik menunjukkan suhu zona akar (root-zone temperature) 20 °C menghasilkan bobot segar tertinggi, sedangkan suhu akar fluktuatif tinggi menurunkan fotosintesis dan hasil (He et al., 2016). Hasil serupa pada penelitian Nutrient Solution Heating menunjukkan tanaman berdaun aroma seperti arugula peka terhadap cekaman suhu rendah pada zona akar (Korean Society for Horticultural Science, 2024). Kondisi dataran tinggi Licin dengan suhu udara sejuk relatif sesuai dengan preferensi tersebut, meskipun variasi suhu siang hari tetap perlu dicatat.

Dari sisi budidaya, arugula relatif cepat dipanen. Buitrago-Villanueva et al. (2023) menunjukkan bahwa panen pada 21 hari setelah tanam menghasilkan bahan "baby leaf", sedangkan panen konvensional dilakukan sekitar 42 hari setelah tanam. Pada budidaya hidroponik, arugula 'Standard' mencapai panen penuh sekitar 28 hari setelah transplantasi dengan kisaran EC larutan nutrisi optimum 1,5–1,8 dS m⁻¹ (Yang et al., 2021). Budidaya tanpa tanah (soilless) dilaporkan meningkatkan hasil segar hingga ±75% dibanding sistem tanah konvensional (Acta Horticulturae, 2002).

Di Indonesia, penelitian arugula masih sedikit tetapi mulai berkembang. Nilasari et al. (2025) menguji ampas kopi dan pupuk organik cair pada arugula dalam polybag dengan rancangan faktorial RAK dan memperoleh pengaruh nyata ampos kopi terhadap pertumbuhan dan hasil. Widiyanto dan Banjarnahor (2024) menguji serabut kelapa dan arang sekam sebagai media tanam arugula pada sistem vertikultur dan menemukan pengaruh nyata komposisi media terhadap bobot basah, bobot kering, serta kandungan gizi. Gumilar et al. (2023) melaporkan pupuk organik cair limbah sayuran hidroponik berpengaruh nyata terhadap produktivitas arugula. Temuan-temuan tersebut menunjukkan bahwa komposisi media tanam merupakan faktor penting, tetapi kombinasi media dan interval irigasi tetes pada sistem polybag belum banyak diteliti.

## 2.2 Media Tanam

Media tanam berfungsi menopang tanaman, menyediakan air dan udara di zona perakaran, serta menyuplai hara. Sifat fisiknya yang penting antara lain bulk density, porositas total, porositas udara (air-filled porosity), dan water holding capacity (WHC). Media yang baik untuk sayuran daun harus memiliki aerasi cukup agar akar tidak kekurangan oksigen, sekaligus daya simpan air yang memadai untuk menahan air di antara interval penyiraman (Ferrarezi et al., 2024).

Kompos dan bahan organik lainnya umumnya meningkatkan WHC karena kandungan bahan organiknya yang tinggi, tetapi dapat menurunkan porositas udara bila proporsinya berlebihan (FALL et al., 2026). Sebaliknya, arang sekam (sekam bakar) bersifat porous dan ringan, meningkatkan drainase dan aerasi, tetapi menurunkan kemampuan menahan air (Abubakari et al., 2017). Abu sekam padi (rice husk ash) yang dipakai sebagai pengganti sebagian peat pada substrat terbukti meningkatkan ventilasi dan pertumbuhan tanaman (Li et al., 2024). Abubakari et al. (2017) juga menunjukkan bahwa kompos jerami gergaji dan sekam yang diamendemen dengan pupuk kandang berpengaruh nyata terhadap hasil selada pada media polybag. Pada tanaman arugula secara khusus, Widiyanto dan Banjarnahor (2024) menemukan bahwa perbandingan serabut kelapa dan arang sekam berpengaruh nyata terhadap bobot basah dan kering tanaman.

Karena karakteristik air kedua bahan saling berlawanan, perbedaan komposisi media diperkirakan mengubah laju pengeringan media di antara penyiraman. Inilah dasar pemilihan media M1 (tanah + kompos) dan M2 (tanah + kompos + sekam bakar) pada penelitian ini.

## 2.3 Kebutuhan Air dan Irigasi Tetes

Sayuran daun umumnya memiliki sistem perakaran dangkal sehingga volume zona perakaran yang tersedia untuk menyimpan air relatif kecil; ketahanan tanaman terhadap cekaman air bergantung pada seberapa lama media mampu mempertahankan kadar air di atas titik layu permanen. Kebutuhan air tanaman sering dinyatakan melalui evapotranspirasi, tetapi pada budidaya polybag kecil, manajemen irigasi lebih praktis diatur berdasarkan interval dan volume pemberian.

Irigasi tetes (drip irrigation) memberikan air secara langsung ke zona perakaran dengan laju rendah dan berkelanjutan, sehingga efisiensi penggunaannya tinggi dan risiko erosi serta penyebaran penyakit daun rendah. Pada polybag, sistem tetes gravitasi (tandon lebih tinggi dari polybag) sudah cukup untuk menciptakan beda tekanan dan aliran yang stabil tanpa pompa.

Frekuensi atau interval pemberian air terbukti berpengaruh terhadap hasil sayuran, tetapi arahnya tidak selalu sama antar penelitian. Hanson et al. (2003) menemukan bahwa frekuensi irigasi harian, dua hari, dan mingguan pada selada, paprika, bawang, dan tomat tidak berpengaruh nyata pada hasil, kecuali untuk tanaman berakar dangkal pada tanah berpasir yang sensitif terhadap kekeringan. Sefer dan Mansuroğlu (2011) menunjukkan bahwa tingkat pemberian air (bukan kedalaman selang) lebih menentukan hasil dan water use efficiency (WUE) selada pada irigasi tetes, di mana WUE meningkat saat pemberian air dikurangi. Zakka et al. (2020) pada mentimun menunjukkan irigasi harian menghasilkan hasil tertinggi tetapi produktivitas air lebih rendah dibanding interval yang lebih jarang. Penelitian pada selada di Iran (JISE) menemukan frekuensi irigasi 1 dan 2 hari tidak berbeda nyata pada WUE, sedangkan pengurangan kebutuhan air meningkatkan WUE. Secara umum, interval yang lebih rapat menjaga media tetap lembap tetapi berisiko boros air dan memicu penyakit; interval yang lebih jarang hemat air tetapi berisiko cekaman air, terutama bila media cepat kering. Titik optimumnya bergantung pada sifat media, yang menjadi alasan penelitian ini menguji interaksi media × interval.

## 2.4 Interval Irigasi dan Interaksinya dengan Media

Hubungan antara sifat media dan interval irigasi jarang diteliti secara eksplisit pada sayuran daun skala kecil, padahal keduanya saling menentukan ketersediaan air di zona perakaran. Media dengan WHC tinggi (misalnya banyak kompos) dapat mempertahankan air lebih lama sehingga interval yang sama menghasilkan kondisi kelembapan yang lebih stabil; media yang porous (banyak sekam bakar) mengering lebih cepat sehingga interval yang sama berisiko membuat tanaman mengalami siklus basah–kering yang lebih ekstrem.

Monitoring kelembapan media secara kontinu dapat menjelaskan mekanisme tersebut: kurva kelembapan media pada tiap kombinasi perlakuan menunjukkan berapa lama media bertahan di atas atau di bawah ambang kritis. Data ini menjadi jembatan antara perlakuan dan respons tanaman, sekaligus dasar rekomendasi interval irigasi untuk masing-masing resep media.

## 2.5 Sensor Kelembapan Tanah untuk Pemantauan Budidaya

Sensor kelembapan tanah komersial umumnya berbasis resistif atau kapasitif. Sensor resistif mengukur resistansi antara dua elektroda dan cepat korosi serta terpengaruh salinitas; sensor kapasitif mengukur perubahan dielektrik media sehingga lebih stabil untuk pemantauan jangka panjang (Abdelmoneim et al., 2025).

Akurasi sensor kapasitif murah sangat bergantung pada kalibrasi terhadap media yang dipakai. Metode gravimetri — menimbang sampel media basah, mengoven pada ±105 °C, menimbang kering, lalu menghitung kadar air sebenarnya — merupakan acuan standar kalibrasi (Abdelmoneim et al., 2025). Pada penelitian di Indonesia, Sudarmaji et al. (2024) mengalibrasi enam sensor kapasitif dengan metode GWC pada tanah pesisir dan memperoleh MAPE ±10%; sistem serupa memakai ESP32, Node-RED, dan Google Spreadsheet untuk monitoring dan kontrol irigasi. Karena respons dielektrik media berbeda antar komposisi, kalibrasi pada penelitian ini dibuat terpisah untuk media M1 dan M2.

## 2.6 Analisis Kelayakan Usaha

Analisis usaha sederhana pada penelitian budidaya skala kecil umumnya memakai indikator R/C ratio (penerimaan dibagi biaya) dan Break Even Point (BEP) untuk menilai kelayakan suatu perlakuan (Kurniawati, 2023). R/C > 1 menunjukkan usaha menguntungkan; makin besar nilainya makin baik. BEP menyatakan titik produksi atau harga minimum agar usaha tidak rugi. Pada penelitian ini analisis usaha hanya bersifat pendukung untuk membandingkan kombinasi perlakuan, bukan tujuan utama.

## 2.7 Kerangka Pemikiran

Media tanam menentukan kemampuan menahan air dan laju pengeringannya. Interval irigasi menentukan frekuensi pasokan air. Kombinasi keduanya menentukan ketersediaan air di zona perakaran arugula, yang berdampak pada pertumbuhan dan hasil. Monitoring sensor merekam kelembapan dan suhu media sebagai penjelas hubungan tersebut.

---

# BAB III METODE PENELITIAN


## 3.1 Waktu dan Tempat

Penelitian dilakukan di [lokasi spesifik], Kecamatan Licin, Kabupaten Banyuwangi, pada [bulan dan tahun], dengan total waktu kurang lebih 2 bulan: persiapan dan uji pendahuluan sekitar 1 bulan, tanam sampai panen sekitar 5–6 minggu. Jika dilaksanakan pada musim hujan, percobaan wajib berada di bawah rain shelter.

## 3.2 Alat dan Bahan

- **Bahan tanam dan media:** benih arugula [varietas], polybag [ukuran], tanah, kompos (satu sumber dan satu batch), sekam bakar.
- **Sistem irigasi:** tandon air, selang tetos, emitter, filter, kran per jalur, konektor, rain shelter.
- **Alat ukur:** soil moisture meter manual, penggaris, timbangan digital, gelas ukur, oven atau alat pengering (untuk kalibrasi gravimetri).
- **Perangkat monitoring:** ESP32, sensor kelembapan tanah kapasitif (6 unit), sensor suhu DS18B20 (6 unit), modul SD card, modul RTC (jam waktu nyata), sumber daya (power bank atau adaptor), casing tahan air, kabel dan konektor.

## 3.3 Rancangan Percobaan

Percobaan menggunakan Rancangan Acak Lengkap (RAL) faktorial 2 × 3 dengan 3 ulangan. Jika lokasi tidak seragam (miring atau sebagian terkena naungan), digunakan Rancangan Acak Kelompok (RAK) dengan kelompok mengikuti gradien lokasi.

**Faktor A — Media tanam:**

| Level | Komposisi (v/v) | Keterangan |
|---|---|---|
| M1 | Tanah : kompos = 1 : 1 | Media kontrol kaya bahan organik, daya simpan air tinggi |
| M2 | Tanah : kompos : sekam bakar = 1 : 1 : 1 | Media lebih porous, drainase lebih baik |

Catatan: pada M1, tanah dan kompos masing-masing menyusun 50% volume media; pada M2, masing-masing komponen menyusun ±33% volume. Seluruh media dicampur merata per batch dan diisi ke polybag dengan berat/volume yang sama.

**Faktor B — Interval irigasi tetos:**

| Level | Interval | Keterangan |
|---|---|---|
| I1 | Setiap hari | Interval rapat |
| I2 | 2 hari sekali | Interval sedang |
| I3 | 3 hari sekali | Interval jarang |

Pemilihan rentang interval didasarkan pada kajian irigasi tetes sayuran daun, di mana frekuensi harian hingga beberapa hari merupakan rentang yang umum diteliti (Hanson et al., 2003; Sefer & Mansuroğlu, 2011; Zakka et al., 2020). Interval lebih dari 3 hari tidak dipakai karena arugula berakar dangkal dan berisiko mengalami cekaman air berat.

Terdapat 6 kombinasi perlakuan (M1I1, M1I2, M1I3, M2I1, M2I2, M2I3) yang masing-masing diulang 3 kali, sehingga total 18 unit percobaan. Setiap unit terdiri dari 4 polybag, dua di antaranya dijadikan sampel pengamatan. Total sekitar 72 polybag. Jumlah polybag dan tanaman per polybag disesuaikan dengan arahan pembimbing.

Jumlah ulangan 3 merupakan jumlah minimum yang lazim untuk RAL di percobaan polybag skala kecil dan sejalan dengan penelitian serupa pada arugula (Nilasari et al., 2025). Homogenitas antar unit dijaga melalui pencampuran media per batch, pengisian polybag dengan volume yang seragam, dan randomisasi penempatan perlakuan.

**Volume air per penyiraman:** ditetapkan sama untuk semua perlakuan dalam satuan liter per polybag per penyiraman, berdasarkan hasil uji pendahuluan (bagian 3.4 butir 3) dan konfirmasi pembimbing. Karena sifat menahan air M1 dan M2 berbeda, volume yang sama menghasilkan kadar air media yang berbeda — perbedaan inilah yang menjadi objek pengamatan interaksi perlakuan. Volume total air per unit percobaan dicatat untuk perhitungan WUE.

## 3.4 Pelaksanaan Penelitian

1. **Persiapan media.** Kompos dan sekam bakar disiapkan, lalu dicampur sesuai perlakuan dan dimasukkan ke polybag.
2. **Pemasangan rain shelter dan jaringan irigasi.** Dibuat minimal 3 jalur selang tetos, satu per interval, masing-masing dengan kran. Tandon diletakkan lebih tinggi dari polybag agar sistem gravitasi berjalan. Debit emitter diukur dahulu dengan menampung air selama waktu tertentu.
3. **Uji pendahuluan.** Dilakukan uji kecil, terutama pada interval 3 hari, untuk memastikan bibit tidak mati karena media terlalu kering dan untuk menetapkan volume air per penyiraman yang membasahi zona perakaran tanpa kebocoran berarti.
4. **Penanaman.** Benih disemai atau ditanam langsung, lalu penempatan perlakuan diacak.
5. **Pemeliharaan.** Meliputi penyulaman, penyiangan, dan pengendalian hama. Perlu diwaspadai kutu loncat (flea beetle) dan busuk daun saat lembap.
6. **Pemasangan dan pengoperasian sensor.** Dijelaskan pada subbab 3.6.
7. **Panen.** Dilakukan pada kisaran 28–35 HST ketika tanaman mencapai kriteria panen komersial yang seragam untuk semua unit (misalnya seluruh tanaman pada fase 8–12 daun atau setara baby leaf), mengacu pada kisaran umur panen arugula yang dilaporkan Buitrago-Villanueva et al. (2023) dan Yang et al. (2021). Kriteria pastinya disesuaikan dengan varietas dan arahan pembimbing.

## 3.5 Parameter Pengamatan

- **Pertumbuhan:** tinggi tanaman dan jumlah daun pada 7, 14, dan 21 HST (opsional 28 HST) pada tanaman sampel.
- **Hasil:** bobot segar per tanaman dan bobot segar per unit percobaan.
- **Efisiensi air:** Water Use Efficiency (WUE) = bobot segar hasil dibagi total volume air yang diberikan.
- **Pendukung (monitoring):** kelembapan dan suhu media dari sensor serta pembacaan manual soil moisture meter sebagai pembanding.
- **Opsional:** uji organoleptik sederhana (rasa pedas dan kerenyahan) pada panelis terbatas.

## 3.6 Sistem Monitoring Sensor (Pendukung)

Sistem monitoring dipakai sebagai alat bantu pengukuran dan tidak menjadi variabel yang diuji.

**Perangkat dan penempatan.** Satu polybag sampel pada tiap kombinasi perlakuan (6 titik) dipasang sensor kelembapan kapasitif dan sensor suhu. Sensor ditempatkan pada kedalaman zona perakaran yang sama di semua titik. Pemantauan dilakukan pada satu ulangan yang sama selama penelitian, sedangkan ulangan lain dipantau manual.

**Pengendali dan penyimpanan data.** Sensor dibaca oleh ESP32 pada selang waktu tetap (misalnya tiap 15–30 menit). Data disimpan ke SD card sebagai cadangan utama dan dikirim ke Google Sheets atau platform IoT (misalnya ThingSpeak) bila sinyal tersedia. Modul RTC memastikan stempel waktu tetap benar saat koneksi terputus.

**Kalibrasi.** Sensor dikalibrasi terhadap metode gravimetri: sampel media pada beberapa tingkat kebasahan dibaca sensor, kemudian ditimbang basah, dikeringkan pada ±105 °C, dan ditimbang kering untuk memperoleh kadar air sebenarnya. Dari data ini dibuat persamaan kalibrasi pembacaan sensor ke kadar air media. Karena M1 dan M2 berbeda komposisi, kalibrasi dibuat terpisah untuk tiap media.

**Pembanding manual.** Soil moisture meter dibaca pada jam yang sama setiap hari untuk memverifikasi sensor dan sebagai cadangan jika sensor gagal.

**Pengolahan dan visualisasi.** Data dibersihkan dan divisualisasikan sebagai kurva kelembapan media sepanjang hari pada tiap kombinasi di Google Sheets atau Looker Studio. Pencatatan pengamatan agronomi (tinggi, jumlah daun, bobot, volume air) dilakukan lewat Google Form ke Google Sheets dengan kode unit seperti M1I2-U3 untuk mencegah salah ketik, dan WUE dihitung otomatis dengan rumus di spreadsheet.

**Mitigasi risiko.** Sensor dan sambungan kabel diberi casing dan pelindung tahan air. Sumber daya disiapkan dengan power bank atau adaptor, dengan cadangan jika listrik tidak tersedia di lokasi. Jika sensor rusak atau data hilang, penelitian tetap dapat dianalisis karena data utama adalah pertumbuhan dan hasil tanaman.

## 3.7 Analisis Data

1. Data pertumbuhan dan hasil dianalisis dengan ANOVA dua faktor pada taraf 5%. Asumsi (kenormalan dan kehomogenan ragam) diperiksa terlebih dahulu.
2. Jika berpengaruh nyata, dilanjutkan dengan uji BNT atau Duncan (DMRT) taraf 5%. Jika interaksi nyata, pembahasan difokuskan pada kombinasi perlakuan, bukan faktor tunggal.
3. Data sensor dianalisis secara deskriptif (grafik kelembapan dan suhu per kombinasi) untuk menjelaskan hasil. Data sensor tidak diuji ANOVA sebagai variabel utama.
4. Analisis usaha sederhana: R/C ratio = total penerimaan / total biaya, dan BEP dihitung per kombinasi perlakuan. Biaya meliputi benih, media, polybag, tenaga kerja, air, dan penyusutan alat irigasi. Perangkat sensor tidak dimasukkan ke biaya usaha karena merupakan alat penelitian.

Perangkat lunak yang dipakai: Microsoft Excel atau Google Sheets, dan perangkat lunak statistik seperti SPSS atau R (sesuaikan dengan yang tersedia di kampus).

---

# BAB IV JADWAL DAN RENCANA ANGGARAN


## 4.1 Jadwal Penelitian (perkiraan)

| Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Persiapan lokasi, media, rain shelter | X | X | | | | | | | | |
| Pemasangan irigasi dan sensor, kalibrasi | | X | X | | | | | | | |
| Uji pendahuluan | | | X | | | | | | | |
| Penanaman dan pemeliharaan | | | | X | X | X | | | | |
| Pengamatan dan monitoring | | | | | X | X | X | X | | |
| Panen | | | | | | | | X | | |
| Analisis data dan penulisan | | | | | | | | X | X | X |

## 4.2 Rencana Anggaran (perkiraan kasar, perlu disesuaikan dengan harga terbaru)

| Komponen | Perkiraan Biaya |
|---|---|
| Sistem irigasi tetes (tandon, selang, emitter, filter, kran) | Rp 500.000 – 1.500.000 |
| Rain shelter (rangka dan plastik UV) | Rp 500.000 – 1.500.000 |
| Polybag, tanah, kompos, sekam bakar | Rp 300.000 – 600.000 |
| Benih dan perawatan | Rp 100.000 – 300.000 |
| Sensor dan ESP32 (6 titik, SD card, RTC, casing) | Rp 300.000 – 600.000 |
| Alat ukur (timbangan, soil moisture meter, gelas ukur) | Rp 200.000 – 500.000 |
| Transportasi dan lain-lain | Rp 200.000 – 500.000 |
| **Total perkiraan** | **Rp 2.100.000 – 5.500.000** |

Angka di atas hanya perkiraan awal. Banyak komponen bisa dipinjam dari kampus, laboratorium, atau petani sekitar.

---

# DAFTAR PUSTAKA


*Format sitasi menyesuaikan pedoman kampus; daftar berikut disusun dalam gaya APA sebagai rujukan awal.*

Abubakari, A. R., Atuah, L. A., & Banful, B. (2017). Growth and yield response of lettuce to irrigation and growth media from composted sawdust and rice husk. *Journal of Plant Nutrition*. https://doi.org/10.1080/01904167.2017.1384013

Acta Horticulturae. (2002). Comparison between traditional and soilless culture systems to produce rocket (*Eruca sativa*) with low nitrate content. *Acta Horticulturae*, 697, 503–508. [periksa kembali nomor halaman]

Abdelmoneim, A., Al Kalaany, C., Khadra, R., Derardja, B., & Dragonetti, G. (2025). Calibration of low-cost capacitive soil moisture sensors for irrigation management applications. *Sensors*, 25(2), 343. https://doi.org/10.3390/s25020343

Buitrago-Villanueva, I., Barbosa-Cornelio, R., & Coy-Barrera, E. (2023). Influence of the culture system and harvest time on the specialized metabolite composition of rocket salad (*Eruca sativa*) leaves. *Horticulturae*, 9(2), 235. https://doi.org/10.3390/horticulturae9020235

Bonasia, A., Lazzizera, C., Elia, A., & Conversa, G. (2017). Nutritional, biophysical and physiological characteristics of wild rocket genotypes as affected by soilless cultivation system, salinity level of nutrient solution and growing period. *Frontiers in Plant Science*, 8, 300. https://doi.org/10.3389/fpls.2017.00300

FALL, M., Sarr, S., Gueye, N., et al. (2026). Evaluation of the physicochemical properties of innovative substrates based on rice husk biochar and compost inoculated with *Trichoderma* for soilless horticulture. *Asian Journal of Biotechnology and Bioresource Technology*, 12(1). https://doi.org/10.9734/ajb2t/2026/v12i1273

Ferrarezi, R. S., Qin, K., Nguyen, L., Poole, S. D., Cárdenas-Gallegos, J. S., de Oliveira, H. F. E., & Housley, M. J. (2024). Multi-season evaluation of substrates for optimized arugula and lettuce production in hydroponics. *HortScience*, 59(3), 403–411. https://doi.org/10.21273/HORTSCI17606-23

Gumilar, M., Syahr Banu, L., & Suryani, S. (2023). Pengaruh pupuk organik cair limbah sayuran hidroponik terhadap produktivitas tanaman arugula (*Eruca vesicaria* Mill). *Jurnal Ilmiah Respati*. [periksa volume dan halaman]

Hall, M. K. D., Jobling, J. J., & Rogers, G. S. (2012). Factors affecting growth of perennial wall rocket and annual garden rocket. *International Journal of Vegetable Science*, 18(4), 393–411. https://doi.org/10.1080/19315260.2012.660565

Hall, M. K. D., Jobling, J. J., & Rogers, G. S. (2015). Fundamental differences between perennial wall rocket and annual garden rocket influence the commercial year-round supply of these crops. *Journal of Agricultural Science*, 7(3), 1–13. https://doi.org/10.5539/jas.v7n3p1

Hanson, B. R., May, D. M., & Schwankl, L. J. (2003). Effect of irrigation frequency on subsurface drip irrigated vegetables. *HortTechnology*, 13(1), 115–120. https://doi.org/10.21273/HORTTECH.13.1.0115

He, J., See, X., Qin, L., & Choong, T. (2016). Effects of root-zone temperature on photosynthesis, productivity and nutritional quality of aeroponically grown salad rocket (*Eruca sativa*) vegetable. *American Journal of Plant Sciences*, 7(14), 1993–2005. https://doi.org/10.4236/ajps.2016.714181

Kurniawati, A. D. (2023). *Pengembangan produk pangan: Rancangan penelitian dan aplikasinya*. Malang: Universitas Brawijaya Press.

Li, M., Ning, X., Gao, T., Fazry, S., Othman, B., & Najm, A. A. (2024). Rice husk ash based growing media impact on cucumber and melon growth and quality. *Scientific Reports*, 14, 5147. https://doi.org/10.1038/s41598-024-55622-4

Nilasari, Z. A., Pribadi, E. M., & Yulianti, F. (2025). Pengaruh pemberian ampas kopi dan konsentrasi POC terhadap pertumbuhan dan hasil arugula (*Eruca sativa*). *Jurnal Agroekoteknologi dan Agribisnis*, 9(2), 84–95. https://doi.org/10.51852/638msh59

Sefer, B., & Mansuroğlu, G. S. (2011). The effects of drip line depths and irrigation levels on yield, quality and water use characteristics of lettuce under greenhouse condition. *African Journal of Biotechnology*, 10(17), 3370–3379. https://doi.org/10.5897/ajb10.1899

Sudarmaji, A., Gunawan, B., Nugraha, F., Arini, N., & Mulyani, S. (2024). Smart soil moisture control based on IoT ESP-32 for horticulture cultivation in coastal area. *BIO Web of Conferences*, 96, 04001. https://doi.org/10.1051/bioconf/20249604001

Widiyanto, W., & Banjarnahor, D. (2024). Pengaruh serabut kelapa dan arang sekam untuk media tanam terhadap pertumbuhan dan produktivitas tanaman arugula (*Eruca sativa*) pada sistem vertikultur. *Jurnal Pertanian Agros*, 26(2), 460. https://doi.org/10.37159/jpa.v26i2.4554

Yang, T., Samarakoon, U., Altland, J., & Ling, P. (2021). Photosynthesis, biomass production, nutritional quality, and flavor-related phytochemical properties of hydroponic-grown arugula (*Eruca sativa* Mill.) 'Standard' under different electrical conductivities of nutrient solution. *Agronomy*, 11(7), 1340. https://doi.org/10.3390/agronomy11071340

Zakka, E., Onwuegbunam, N., Dare, A., Onwuegbunam, D., & Emeghara, U. (2020). Yield, water use and water productivity of drip-irrigated cucumber in response to irrigation depths and intervals in Kaduna, Nigeria. *Nigerian Journal of Technology*, 39(2), 613–620. https://doi.org/10.4314/njt.v39i2.33

---
