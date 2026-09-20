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