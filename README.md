Nama : Naila Salsabila

NPM : 2506620702

Kelas : PBP C

Link Aplikasi (PWS): https://naila-salsabila51-myportofolio.pws.cs.ui.ac.id/


Saya senang mengambil mata kuliah PBP karena saya dapat belajar membuat website dengan kreativitas saya.

### Assignment 1

1. **Penggunaan Elemen Semantik HTML5**  
   Dalam merancang struktur web ini, saya secara eksplisit menggunakan tag semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<dl>`, dan `<footer>`. Elemen-elemen ini membantu saya membagi dokumen menjadi blok-blok informasi yang memiliki fungsi dan konteks yang jelas. Dibandingkan hanya menggunakan tag `<div>` generik, tag semantik membuat struktur kodenya jauh lebih mudah dibaca dan dipahami (*maintainable*). Selain itu, ini sangat penting untuk aksesibilitas (*screen reader*) agar navigasi halaman dapat teridentifikasi dengan baik berdasarkan perannya.

2. **Tantangan Responsivitas CSS & Evaluasi Layout Mobile**  
   Tantangan terbesar saat mengatur responsivitas adalah menyesuaikan tata letak komponen yang berbasis dua kolom (seperti bagian Hero dan kartu *Experience*) agar tidak terlihat sempit atau rusak saat dibuka di layar ponsel. Untuk mengatasi hal ini, saya mengevaluasi hirarki visual: informasi utama seperti nama, status, dan foto profil harus menjadi prioritas yang pertama kali dilihat oleh pengunjung. Saya memanfaatkan Media Query (`@media (max-width: 600px)`) serta properti CSS Grid (`grid-template-areas`) untuk merestrukturisasi layout secara fleksibel dari bentuk *multi-column* di desktop menjadi *single-column* di mobile, sehingga pengguna tidak perlu melakukan *horizontal scrolling*.

3. **Batasan Web Statis & Rencana Fitur Dinamis**  
   Batasan utama yang saya rasakan pada web statis ini adalah seluruh konten (seperti daftar *skills*, riwayat pendidikan, dan pengalaman) bersifat kaku (*hardcoded*) di dalam berkas HTML. Jika di masa depan saya ingin menambahkan pengalaman baru, saya harus mengubah kode sumbernya secara langsung. Pada iterasi berikutnya, fitur dinamis yang sangat ingin saya implementasikan adalah pemanfaatan MVT Django dan database. Dengan mengintegrasikan database, saya bisa mengelola isi portofolio secara dinamis melalui Django Admin atau form input tanpa perlu menyentuh struktur kode HTML lagi.

---

#### AI Disclosure

Dalam pengerjaan Assignment 1 ini, saya memanfaatkan Generator AI (Gemini AI) sebagai *thought partner* untuk mengeksplorasi ide dan membantu memverifikasi konsep teknis.

* **Tools Used:** Gemini AI
* **Prompt Strategy:**
  * Diskusi dan eksplorasi contoh penerapan CSS Grid/Flexbox yang efisien untuk layout kartu dan *timeline*.
  * Brainstorming ide penataan struktur HTML semantik yang ramah terhadap pembacaan *screen reader*.
  * Diskusi reflektif mengenai perbedaan mendasar antara web statis dan web dinamis berbasis MVT.
* **Assisted Parts:** Memberikan gambaran awal (*scaffolding*) opsi styling CSS serta kerangka berpikir untuk poin-poin refleksi.
* **Manual Problem-Solving & Verification:**
  * **Penyusunan Konten Mandiri:** Seluruh data riwayat pendidikan, organisasi, dan informasi pribadi ditulis manual sesuai identitas asli saya.
  * **Debugging Kode & Refactoring:** Memperbaiki kesalahan sintaks CSS (seperti kurung kurawal media query yang tidak tertutup), menyesuaikan skema warna (*color palette*), serta memastikan integrasi navigasi tautan antar-section berjalan lancar.
  * **Pengujian Lokal:** Menjalankan `python manage.py runserver` dan melakukan inspeksi elemen (*Inspect Element*) di browser untuk menguji responsivitas di berbagai ukuran layar.

# Tugas 2 PBP

## Jawaban Pertanyaan Tugas

### 1. Buatlah peta alur data (request-response) pada Django dan jelaskan keterkaitannya!
Alur permintaan dan tanggapan (*request-response*) pada Django bekerja dengan tahapan berikut:
1. **Client Request:** Pengguna mengirimkan permintaan (*request*) dengan mengakses URL tertentu melalui *browser* (misalnya `/projects/`).
2. **URL Routing (`urls.py`):** Django mencocokkan pola URL yang diminta dengan pemetaan yang ada di `urls.py` untuk menentukan fungsi *view* mana yang harus dipanggil.
3. **View Logic (`views.py`):** Fungsi *view* memproses logika aplikasi, menyiapkan context data (baik dari database maupun struktur data Python), dan meneruskannya ke template.
4. **Model Interaction (`models.py`):** Model mengambil atau memanipulasi data di *database*, lalu mengembalikan data tersebut ke *view*.
5. **Template Rendering (`templates/`):** *View* menyisipkan data ke dalam berkas HTML (*template*) menggunakan sintaks Django Template Language (DTL).
6. **HTTP Response:** Server mengirimkan berkas HTML yang sudah selesai dirender kembali ke *browser* pengguna sebagai tanggapan (*response*).

### 2. Apa fungsi dari Git dalam pengembangan perangkat lunak?
Git adalah sistem pengontrol versi (*Version Control System*) terdistribusi yang berfungsi untuk:
* Mencatat riwayat perubahan (*version history*) pada kode program secara terstruktur.
* Memudahkan kolaborasi tim dalam pengerjaan proyek tanpa saling menimpa kode satu sama lain.
* Memungkinkan pembuatan cabang (*branching*) untuk mengembangkan fitur baru secara terisolasi sebelum digabungkan (*merge*) ke kode utama.
* Memasilitasi proses *rollback* (kembali ke versi kode sebelumnya) jika terjadi masalah atau *error* pada kode terbaru.

### 3. Mengapa *virtual environment* digunakan? Apakah kita tetap bisa membuat aplikasi web Django tanpa *virtual environment*?

* **Alasan Penggunaan:** *Virtual environment* digunakan untuk mengisolasi pustaka (*packages/dependencies*) Python khusus untuk satu proyek tertentu. Hal ini mencegah terjadinya bentrok versi (*version conflict*) antar pustaka jika komputer kamu mengerjakan beberapa proyek Python berbeda.
* **Apakah tetap bisa tanpa *virtual environment*?** Ya, aplikasi tetap bisa dibuat. Namun, semua pustaka akan terpasang secara global di sistem komputer, yang berisiko merusak fungsionalitas proyek lain jika ada perubahan versi pustaka secara global.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!

1. **Inisialisasi Proyek & Environment:** Membuat *virtual environment*, menginstal Django, serta membuat proyek Django baru beserta *app* utama (`main`).
2. **Merancang Model (`models.py`):** Membuat struktur model data seperti `Project` dan `Experience` beserta atributnya (termasuk `URLField` untuk menyimpan tautan dokumen/Google Drive proyek), lalu melakukan `makemigrations` dan `migrate`.
3. **Membuat Views & URL Routing (`views.py` & `urls.py`):** Merancang fungsi *view* untuk menampilkan halaman Profile, Experience, dan Projects, menyusun *context data*, lalu menyambungkan pemetaan URL-nya.
4. **Mengubah Template HTML (`templates/`):** Mengintegrasikan data dinamis ke template HTML (`projects.html`) serta menambahkan tombol/tautan kondisional (`{% if project.link_url %}`) untuk membuka dokumen proyek di Google Drive.
5. **Deployment:** Membuat berkas `requirements.txt`, mengunggah seluruh kode ke repositori Git, dan melakukan *deployment* ke PWS agar situs dapat diakses secara publik.

# Tugas 3 PBP
### 1. Mengapa memerlukan Data Delivery dalam pengembangan aplikasi web?
Data Delivery (seperti format JSON atau XML) dibutuhkan sebagai media pertukaran data antara server dan *client*. Format ini mengirimkan data mentah tanpa tampilan HTML, sehingga lebih ringan, hemat *bandwidth*, dan bisa dikonsumsi oleh berbagai platform *client* (seperti frontend React/Vue, aplikasi mobile, maupun API pihak ketiga).

### 2. Perbedaan antara POST dan GET pada protokol HTTP
* **GET:** Digunakan untuk **mengambil/membaca** data dari server. Data dikirimkan lewat URL (*query string*), dapat disimpan di *cache* browser, dan kurang aman untuk data sensitif.
* **POST:** Digunakan untuk **mengirim, menambah, atau mengedit** data di server. Data dikirimkan melalui *request body* (tidak tampil di URL), tidak disimpan di *cache*, dan memerlukan proteksi CSRF.

### 3. Mengapa menggunakan `ModelForm` dibandingkan `Form` biasa di Django?
`ModelForm` secara otomatis terhubung langsung dengan model database yang sudah kita buat di `models.py`. Keunggulannya:
* Tidak perlu mendefinisikan ulang field form satu per satu (*DRY*).
* Menyediakan fungsi `.save()` bawaan untuk langsung menyimpan data ke database.
* Otomatis mengadopsi aturan validasi yang ada pada model.

### 4. Fungsi `csrf_token` pada form Django
`csrf_token` berfungsi melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF) dengan menghasilkan token unik saat pengiriman form POST. Tanpa tag `{% csrf_token %}`, Django akan menolak pengiriman form dan mengembalikan *error* **`403 Forbidden`**.

### 5. Langkah-langkah implementasi Tugas 3
1. **Membuat Form (`main/forms.py`):** Membuat kelas `ProjectForm` menggunakan `ModelForm` yang terhubung dengan model `Project`.
2. **Logika Views (`main/views.py`):**
   * Mengubah `show_project` untuk mengambil data dari database via ORM.
   * Membuat fungsi `create_project` untuk memproses input form POST.
   * Membuat fungsi `delete_project` untuk menghapus data berdasarkan ID (UUID).
   * Membuat fungsi `show_json` untuk menyajikan data proyek dalam format JSON menggunakan `serializers`.
3. **Routing (`main/urls.py`):** Mendaftarkan path untuk `projects/create/`, `projects/<uuid:id>/delete/`, dan `json/`.
4. **Template HTML (`templates/`):**
   * Membuat `projects_form.html` lengkap dengan tag form, CSRF token, dan tombol simpan.
   * Memperbarui `projects.html` dengan menambahkan tombol **+ Tambah Project** dan tombol **Hapus**.
5. **Django Admin (`main/admin.py`):** Mendaftarkan model `Experience` dan `Project` agar data bisa dikelola via dashboard admin.
6. **Migrasi & Deploy:** Jalankan migrasi database, uji coba seluruh alur di server lokal, lalu lakukan `git commit` dan `git push pws main`.

## Tugas 3

### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!

* **Kenapa pakai `ModelForm` daripada form HTML manual?**
  * **Otomatis & Hemat Waktu**: `ModelForm` bisa langsung membaca bidang (*fields*) dari model Django yang sudah kita buat (misal model `Project` dan `Experience`). Jadi kita tidak perlu repot mengetik tag `<input>` HTML satu per satu.
  * **Sudah ada Validasi bawaan**: `ModelForm` otomatis menyesuaikan tipe input dengan atribut di model. Contohnya jika di model berupa `DateField` atau `URLField`, maka form akan otomatis memvalidasi format tanggal dan link tanpa perlu kita buat kodenya dari nol.
  * **Mudah Dirawat (DRY)**: Kalau misal ada perubahan field di model, kita cukup ubah di satu tempat saja dan form-nya akan ikut menyesuaikan.
  * **Simpan Data Lebih Mudah**: Tinggal panggil method `.save()`, data dari form bisa langsung tersimpan ke database.

* **Kenapa wajib pakai `{% csrf_token %}`?**
  * Tag `{% csrf_token %}` berfungsi untuk mengamankan form dari serangan **CSRF (Cross-Site Request Forgery)**.
  * Token ini memicu Django untuk mengecek apakah request `POST` yang masuk benar-benar dikirim oleh user yang sah dari situs kita, bukan dari situs asing/peretas yang mencoba mengirim data jahat atas nama user kita.

---

### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

* **Ukurannya Lebih Ringan**: JSON menggunakan struktur kunci-nilai (*key-value*) yang lebih ringkas. XML memakai tag pembuka dan penutup (`<tag></tag>`) yang bikin ukuran datanya jadi lebih besar.
* **Cepat Diproses JavaScript**: Karena JSON secara native merupakan format data bawaan JavaScript, proses membaca/parsing datanya di browser (frontend) jauh lebih cepat dibanding XML.
* **Lebih Enak Dibaca**: Struktur data pada JSON lebih sederhana dan gampang dibaca oleh developer.
* **Standar Web Modern**: Mayoritas API dan framework frontend zaman sekarang (seperti React atau Vue) sudah menjadikan JSON sebagai standar utama untuk bertukar data.

---

### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

* **Alur Pengembalian Data JSON:**
  1. User/browser mengakses URL endpoint (misalnya `/json/`).
  2. Fungsi *view* di Django akan mengambil data dari database lewat ORM, contohnya `Experience.objects.all()`. Hasilnya berbentuk `QuerySet`.
  3. Data `QuerySet` tersebut diubah dulu menjadi data sederhana (string, angka, list) menggunakan fungsi serialisator Django (`django.core.serializers`).
  4. Data yang sudah diserialisasi dikembalikan ke browser sebagai respons HTTP berformat JSON.

* **Kenapa Data Model Perlu Di-serialize Dulu?**
  * Objek `QuerySet` bawaan Django adalah objek Python yang kompleks. Format JSON tidak paham cara membaca objek Python secara langsung.
  * Proses *serialization* berfungsi menerjemahkan objek Python/Django tersebut menjadi teks atau tipe data dasar yang sesuai dengan standar penulisan JSON, sehingga bisa dipahami oleh sistem lain atau frontend.

---

## AI Disclosure

* **Tool AI yang Digunakan**: Google Gemini.
* **Penggunaan**:
  * Membantu mencari penyebab error saat mengatasi `FieldError` di `forms.py` karena field `thumbnail`.
  * Membantu memberikan pemahaman konsep teoritis seputar `ModelForm`, CSRF, dan Serialisasi data Django.
* **Perbaikan & Analisis Manual**:
  * Penyesuaian isi file `forms.py` dan `views.py` tetap dikerjakan dan diperiksa secara manual agar pas dengan struktur model proyek tanpa field `thumbnail`.
  * Penataan tampilan template dan logika perbandingan tanggal di-test sendiri secara manual di browser.

# Tugas 4 PBP
### Implementasi Peran & Hak Akses
Aplikasi portofolio ini menerapkan sistem pengontrolan akses pengguna berdasarkan 4 tingkatan peran (*roles*) utama untuk menjaga keamanan server-side dan kenyamanan tampilan UI:

1. **Pengunjung (Guest / Tanpa Login)**
   * **Akses**: *Read-only*. Pengunjung hanya dapat melihat daftar proyek (*Projects*) dan riwayat pengalaman (*Experience*).
   * **Proteksi**: Tombol aksi (*Create, Edit, Delete*) disembunyikan. Jika pengunjung mencoba mengakses URL aksi secara manual, server akan secara otomatis melakukan *redirect* ke halaman Login.

2. **Pengguna Biasa (Registered User)**
   * **Akses**: *Read* + *Interactive Star*.
   * **Fitur**: Dapat memberikan atau membatalkan *Star* pada proyek portofolio. Setiap pengguna dibatasi maksimal 1 *star* per proyek.
   * **Proteksi**: Tidak memiliki akses ke fitur penambahan, pengubahan, atau penghapusan data. Jika mengakses URL terkait, server akan melempar *exception* `PermissionDenied` (**HTTP 403 Forbidden**).

3. **Editor (Django Group `Editor`)**
   * **Akses**: Hak Pengguna Biasa + *Update*.
   * **Fitur**: Pengguna yang dimasukkan ke dalam Django Group `Editor` (dikonfigurasi via Django Admin) dapat mengedit data proyek dan pengalaman yang sudah ada.
   * **Proteksi**: Diberikan akses ke tombol *Edit*, namun dibatasi dari aksi pembuatan data baru (*Create*) dan penghapusan (*Delete*) dengan balasan **HTTP 403 Forbidden**.

4. **Pemilik Portofolio (Superuser)**
   * **Akses**: *Full CRUD* (*Create, Read, Update, Delete*) + *Star*.
   * **Fitur**: Memiliki kontrol penuh atas seluruh manajemen data proyek dan pengalaman di portofolio.

---

## Proteksi Keamanan Server-Side & UI Access Control

- **Server-Side Check**: Setiap *view* yang melakukan modifikasi data dilindungi menggunakan *decorator* `@login_required` serta pengondisian hak akses menggunakan *helper function* `is_editor()` dan atribut `request.user.is_superuser`. Aksi yang tidak sesuai izin akan langsung memicu `raise PermissionDenied` yang menghasilkan respons **403 Forbidden**.
- **Template UI Control**: Elemen tombol pada templat `projects.html` dan `experience.html` dibungkus dengan logika *template tag* Django (seperti `{% if user.is_superuser or is_editor %}`) sehingga tombol hanya dirender untuk pengguna yang memiliki hak akses.

---

## AI Disclosure & Transparansi Kolaborasi AI

- **Tools AI yang Digunakan**: Gemini AI.
- **Strategi Prompting**:
  1. *Context Feeding*: Mengunggah instruksi dokumen Tugas 4 dan struktur kode proyek (`views.py`, `models.py`, `urls.py`, templat HTML) untuk memperoleh panduan yang tepat sasaran.
  2. *Step-by-step Guidance*: Mengajukan pertanyaan bertahap mulai dari perancangan relasi `ManyToManyField`, pembuatan fungsi *helper* otorisasi, penanganan `PermissionDenied` (HTTP 403), hingga penyesuaian kondisional templat.
- **Hasil Kolaborasi & Perbaikan Manual**:
  - **Dukungan AI**: AI memberikan draf awal logika *toggle star* dan pengondisian hak akses di *views* serta arahan pembuatan grup `Editor`.
  - **Analisis Kritis & Perbaikan Manual**: Terdapat penyesuaian manual pada templat `experience.html` agar tombol *Edit* dan *Hapus* tetap menyatu rapi dengan struktur visual *timeline* bawaan portofolio tanpa merusak tata letak CSS. Selain itu, penanganan pemisahan database lokal (SQLite) dan database PWS disesuaikan secara manual melalui pembuatan superuser via SSH/Terminal PWS.

### Tugas 5
1. **Debouncing adalah teknik untuk menunda eksekusi sebuah fungsi sampai pengguna berhenti melakukan suatu aktivitas selama waktu tertentu. Mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX?**
   * *Urgensi:* Tanpa *debouncing*, setiap kali pengguna mengetik satu karakter di kolom pencarian (misalnya kata `"Experience"`), browser akan langsung mengirimkan *request* HTTP ke server sebanyak 10 kali terpisah. Hal ini menyebabkan penumpukan pemanggilan API, memperlambat performa server, dan memboroskan konsumsi *bandwidth*. 
   * *Cara Kerja:* Dengan *debouncing* berdurasi 300 milidetik, *timer* akan di-reset di setiap ketikan baru, dan *request* AJAX baru akan benar-benar dikirimkan ke server hanya setelah pengguna berhenti mengetik selama waktu yang ditentukan.

2. **Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
   * *Fungsi `await`:* `fetch()` bersifat *asynchronous* dan mengembalikan sebuah `Promise`. Penggunaan kata kunci `await` memerintahkan JavaScript untuk menghentikan sementara baris eksekusi fungsi lokal tersebut sampai `Promise` terselesaikan (*resolved*) dan mengembalikan objek `Response` atau data JSON aktual.
   * *Konsekuensi Tanpa `await`:* Jika `await` tidak digunakan, variabel hasil dari `fetch()` masih berstatus *Unresolved Promise*, bukan objek respons data sesungguhnya. Ketika program mencoba mengakses properti dari variabel tersebut sebelum data siap, JavaScript akan melempar *runtime error* atau mengolah data kosong (*undefined*).

3. **Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**
   * *Pengertian XSS:* Serangan keamanan di mana peretas menyisipkan skrip jahat (HTML/JavaScript aktif) ke dalam aplikasi web yang kemudian dieksekusi oleh browser milik pengguna lain.
   * *Kerentanan pada AJAX/JavaScript:* Saat merender halaman via AJAX, data dari server disisipkan langsung ke dalam DOM menggunakan properti JavaScript seperti `element.innerHTML`. Jika data masukan pengguna mengandung tag skrip jahat (misal `<img src="x" onerror="alert('XSS')">`) dan tidak disanitasi secara manual, browser akan langsung mengeksekusi skrip tersebut.
   * *Perbandingan dengan Template Django:* Pada template Django, variabel DTL (`{{ data }}`) secara otomatis menerapkan *HTML Escaping* tingkat server sebelum dirender ke HTML, sehingga karakter khusus seperti `<` atau `>` dikonversi menjadi bentuk yang aman. Pada AJAX frontend, perlindungan otomatis ini hilang, sehingga pengembang wajib menerapkan sanitasi manual menggunakan fungsi seperti `escapeHtml()` pada JavaScript atau `strip_tags` pada server.

---

### AI Disclosure & Transparansi Kolaborasi AI (Tugas 5)

* **Tools AI yang Digunakan:** ChatGPT & Google Gemini.
* **Strategi Prompting:**
  1. *Context Feeding:* Memberikan konteks berupa instruksi Tugas 5, struktur README, kode Django, templat HTML, dan skrip JavaScript.
  2. *Step-by-step Guidance:* Meminta penjelasan bertahap mengenai AJAX, Fetch API, `async/await`, *debouncing*, CSRF, dan XSS.
  3. *Debugging Berbasis Error:* Mengirimkan gejala *error* saat implementasi untuk mencari akar permasalahan.
  4. *Code Review:* Meminta AI meninjau validitas kode AJAX, *debounce*, CSRF, dan fungsi *escaping*.

* **Bagian Spesifik yang Dibantu AI:**
  * Menjelaskan konsep dasar AJAX menggunakan Fetch API dan penggunaan `async/await`.
  * Memberikan draf implementasi teknik *debouncing* pada fitur pencarian judul pengalaman.
  * Membantu merancang fungsi helper `escapeHtml()` untuk sanitasi string di sisi client (`utils.js`).
* **Keterbatasan AI & Analisis Kritis Mandiri (Perbaikan Manual):**
  * *Keterbatasan:* Solusi yang diberikan AI terkadang menggunakan asumsi generik yang tidak sesuai dengan struktur lokal atau konfigurasi server proyek yang sesungguhnya.
  * *Perbaikan Manual:* 
    1. **Debugging Static Files:** Masalah pemuatan berkas `utils.js` yang menghasilkan error `404 Not Found` tidak cukup diselesaikan dengan saran umum AI. Saya memeriksa ulang struktur direktori proyek secara mandiri, memindahkan berkas ke folder `main/static/js/`, dan memastikan pemanggilan tag `{% static 'js/utils.js' %}` terpasang dengan benar di `base.html`.
    2. **Penanganan Error Runtime Date/Time (Backend):** AI sempat menyarankan pemanggilan `.strftime()` secara langsung yang memicu *crash* `500 Internal Server Error` saat tanggal bernilai kosong. Saya melakukan perbaikan manual di `views.py` dengan menambahkan pengecekan kondisional eksplisit menggunakan `getattr()` untuk mengamankan nilai tanggal yang bernilai `None`.

### Tugas 6

**1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!**

REST (*Representational State Transfer*) merupakan gaya arsitektur yang digunakan dalam pengembangan API untuk mengatur komunikasi antara client dan server. REST menggunakan resource yang dapat diakses melalui URL serta HTTP methods seperti GET, POST, PUT, PATCH, dan DELETE untuk melakukan operasi terhadap data.

Mengembalikan data dalam format JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON hanya merupakan format pertukaran data. API juga perlu menerapkan prinsip REST, seperti:

- **Resource-based:** Setiap data atau resource memiliki URL yang jelas.
- **HTTP Methods:** Penggunaan method HTTP harus sesuai dengan fungsinya.
- **Stateless:** Setiap request harus membawa informasi yang diperlukan untuk diproses tanpa bergantung pada konteks request sebelumnya.
- **HTTP Status Code:** Server memberikan status code yang sesuai dengan hasil pemrosesan request.

Perbedaan PUT dan PATCH terletak pada cakupan perubahan data:

- **PUT:** Digunakan untuk memperbarui keseluruhan representasi resource. Contohnya, ketika ingin memperbarui seluruh informasi pengalaman kerja, seperti title, description, category, started_at, dan ended_at.
- **PATCH:** Digunakan untuk memperbarui sebagian data tanpa harus mengirimkan seluruh field. Contohnya, ketika hanya ingin mengubah title pengalaman kerja tanpa mengubah deskripsi dan tanggalnya.

Pada implementasi Experience API, kedua method tersebut digunakan melalui endpoint detail Experience berdasarkan UUID.

**2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?**

Serializer pada Django REST Framework berfungsi untuk mengubah objek model Django menjadi format data yang dapat dikirimkan melalui API, seperti JSON. Serializer juga dapat melakukan proses sebaliknya, yaitu menerima data dari client, melakukan validasi, dan mengubahnya menjadi objek yang dapat disimpan ke database.

Dalam proyek ini, saya menggunakan `ExperienceSerializer` dengan `ModelSerializer` untuk mengelola data dari model Experience. Serializer tersebut juga digunakan untuk melakukan validasi pada field title dan description serta menampilkan informasi tambahan berupa `star_count` dan `is_starred`.

Dibandingkan menyusun dictionary secara manual menggunakan `JsonResponse` seperti pada Tutorial 05, serializer memiliki beberapa keuntungan:

- **Lebih praktis:** `ModelSerializer` dapat mengambil field dari model secara otomatis sehingga tidak perlu menyusun dictionary satu per satu.
- **Validasi data:** Serializer dapat memeriksa input yang dikirimkan client sebelum data disimpan ke database.
- **Konsistensi data:** Struktur JSON yang dihasilkan lebih teratur dan konsisten.
- **Mendukung operasi CRUD:** Serializer menyediakan method seperti `create()` dan `update()` untuk membantu proses penambahan dan pembaruan data.
- **Mudah dikembangkan:** Perubahan field pada model dapat disesuaikan melalui konfigurasi serializer.

Dengan demikian, serializer membuat proses pengelolaan dan pertukaran data menjadi lebih terstruktur serta mudah dipelihara.

**3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?**

Autentikasi (*authentication*) dan otorisasi (*authorization*) merupakan dua konsep keamanan yang berbeda.

- **Autentikasi:** Proses untuk memverifikasi identitas pengguna yang mengakses aplikasi. Tujuannya adalah mengetahui siapa pengguna yang melakukan request.
- **Otorisasi:** Proses untuk menentukan tindakan apa saja yang boleh dilakukan oleh pengguna berdasarkan identitas dan hak aksesnya.

Pada proyek ini, autentikasi diterapkan menggunakan `SessionAuthentication`, sedangkan pengaturan hak akses dilakukan menggunakan custom permission class `IsPortfolioOwnerOrEditorOrReadOnly`.

Pembagian hak akses pada Experience API adalah sebagai berikut:

1. **Guest:** Dapat melihat data Experience tanpa melakukan perubahan.
2. **Registered User:** Dapat melihat data dan menggunakan fitur star setelah login.
3. **Editor:** Dapat melihat data, menggunakan fitur star, serta memperbarui data menggunakan PUT dan PATCH.
4. **Superuser:** Memiliki hak akses penuh, termasuk menambahkan, membaca, memperbarui, dan menghapus data Experience.

Hak akses harus diperiksa melalui permission class di sisi server karena menyembunyikan tombol pada template hanya membatasi tampilan antarmuka, bukan benar-benar mengamankan endpoint API.

Pengguna masih dapat mencoba mengakses endpoint secara langsung melalui browser atau aplikasi lain tanpa menggunakan tombol pada website. Oleh karena itu, server harus tetap memeriksa izin setiap kali menerima request.

Dengan permission class, server dapat menolak request yang tidak memiliki izin dan memberikan respons HTTP 403 Forbidden. Hal ini membuat keamanan aplikasi tidak hanya bergantung pada tampilan frontend.

**4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?**

CSRF (*Cross-Site Request Forgery*) merupakan serangan yang memanfaatkan kondisi ketika pengguna sedang memiliki sesi login untuk mengirimkan request yang tidak diinginkan ke suatu aplikasi.

Pada Django REST Framework, `SessionAuthentication` menggunakan session dan cookie untuk mengenali pengguna yang sudah login. Browser dapat mengirimkan cookie session secara otomatis ketika melakukan request ke website yang sama. Kondisi ini dapat dimanfaatkan oleh pihak lain untuk mencoba mengirimkan request tanpa persetujuan pengguna.

Oleh karena itu, request yang mengubah data seperti POST, PUT, PATCH, dan DELETE tetap memerlukan token CSRF. Token tersebut digunakan untuk memastikan bahwa request memiliki token perlindungan yang valid, bukan hanya mengandalkan cookie session.

Penggunaan `force_authenticate()` dalam pengujian API tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan karena metode tersebut secara langsung menetapkan pengguna sebagai pengguna yang sudah terautentikasi. Dengan demikian, proses autentikasi normal melalui `SessionAuthentication`, termasuk pemeriksaan CSRF, tidak dijalankan seperti pada request biasa.

Untuk menguji perlindungan CSRF secara tepat, pengujian perlu menggunakan session authentication melalui proses login dan mengaktifkan pemeriksaan CSRF pada test client. Selanjutnya, request yang mengubah data dapat diuji menggunakan token CSRF yang valid maupun tanpa token untuk memastikan bahwa request tanpa perlindungan yang sesuai ditolak oleh server.

---

**### AI Disclosure & Transparansi Kolaborasi AI (Tugas 6)**

- **Tools AI yang Digunakan:** ChatGPT dan Google Gemini.

- **Strategi Prompting:**
  1. **Context Feeding:** Memberikan instruksi Tugas 6 serta struktur proyek Django, termasuk model Experience, serializer, API views, permissions, dan URL routing.
  2. **Step-by-step Guidance:** Meminta penjelasan bertahap mengenai REST API, Django REST Framework, serializer, autentikasi, otorisasi, dan CSRF.
  3. **Debugging Berbasis Error:** Mengirimkan pesan error dan hasil terminal untuk membantu mengidentifikasi penyebab masalah.
  4. **Code Review:** Meminta AI memeriksa implementasi serializer, endpoint CRUD, permission, dan integrasi frontend.
  5. **Testing Guidance:** Meminta arahan untuk menjalankan automated tests dan menguji fitur secara langsung melalui browser.

- **Bagian Spesifik yang Dibantu AI:**
  - Membantu memahami konsep REST dan perbedaan HTTP methods PUT dan PATCH.
  - Memberikan arahan implementasi `ExperienceSerializer` menggunakan `ModelSerializer`.
  - Membantu merancang endpoint CRUD pada `api_views.py`.
  - Membantu memahami custom permission dan pembagian hak akses pengguna.
  - Membantu mengintegrasikan REST API dengan halaman `experience.html`.
  - Memberikan panduan pengujian API dan debugging.

- **Keterbatasan AI & Analisis Kritis Mandiri (Perbaikan Manual):**
  - **Keterbatasan AI:** Saran AI terkadang menggunakan asumsi umum yang belum tentu sesuai dengan struktur proyek Django yang sedang dikembangkan. Kode yang diberikan juga tetap perlu diperiksa agar tidak mengganggu fitur dari tugas sebelumnya.
  - **Penyesuaian URL Routing:** Memeriksa dan menyesuaikan pemisahan URL halaman website dan URL REST API agar tidak terjadi konflik dengan routing yang sudah ada.
  - **Pemeriksaan Hak Akses:** Memastikan pembatasan akses dilakukan melalui permission di backend, bukan hanya menyembunyikan tombol pada frontend.
  - **Pengujian Manual:** Menjalankan `python manage.py check`, menguji 26 automated tests, serta mencoba fitur star, tambah, edit, dan hapus secara langsung melalui browser.
  - **Verifikasi Git:** Memeriksa perubahan menggunakan `git status`, membuat commit, dan melakukan push ke GitHub setelah pengujian berhasil.

Melalui proses ini, saya memahami bahwa AI dapat membantu mempercepat pemahaman konsep dan proses debugging, tetapi hasilnya tetap perlu diperiksa, disesuaikan, dan diuji secara mandiri oleh pengembang.

- **Riwayat Prompt dan Percakapan AI:**
  - ChatGPT: https://chatgpt.com/share/6af12609-7e54-83ec-8167-b21ef9c7165d

Riwayat prompt lengkap disertakan secara manual sebagai dokumentasi penggunaan AI, termasuk prompt yang diberikan dan respons AI selama proses pengerjaan.