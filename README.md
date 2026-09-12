Nama : Naila Salsabila

NPM : 2506620702

Kelas : PBP C

Link Aplikasi (PWS): contoh: https://pws.cs.ui.ac.id/web/project/naila.salsabila51/myportofolio/env


Saya senang pengambil mata kuliah PBP karena saya dapat belajar membuat website dengan kereativitas saya.

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

---

## Jawaban Pertanyaan Tugas

### 1. Buatlah peta alur data (request-response) pada Django dan jelaskan keterkaitannya!
Alur permintaan dan tanggapan (*request-response*) pada Django bekerja dengan tahapan berikut:
1. **Client Request:** Pengguna mengirimkan permintaan (*request*) dengan mengakses URL tertentu melalui *browser* (misalnya `/projects/`).
2. **URL Routing (`urls.py`):** Django mencocokkan pola URL yang diminta dengan pemetaan yang ada di `urls.py` untuk menentukan fungsi *view* mana yang harus dipanggil.
3. **View Logic (`views.py`):** Fungsi *view* memproses logika aplikasi. Jika membutuhkan data dari *database*, *view* akan berkomunikasi dengan *Model*.
4. **Model Interaction (`models.py`):** Model mengambil atau memanipulasi data di *database* (SQLite), lalu mengembalikan data tersebut ke *view*.
5. **Template Rendering (`templates/`):** *View* menyisipkan data ke dalam berkas HTML (*template*) menggunakan sintaks Django Template Language (DTL).
6. **HTTP Response:** Server mengirimkan berkas HTML yang sudah selesai dirender kembali ke *browser* pengguna sebagai tanggapan (*response*).

### 2. Apa fungsi dari Git dalam pengembangan perangkat lunak?
Git adalah sistem pengontrol versi (*Version Control System*) terdistribusi yang berfungsi untuk:
* Mencatat riwayat perubahan (*version history*) pada kode program secara terstruktur.
* Memudahkan kolaborasi tim dalam pengerjaan proyek tanpa saling menimpa kode satu sama lain.
* Memungkinkan pembuatan cabang (*branching*) untuk mengembangkan fitur baru secara terisolasi sebelum digabungkan (*merge*) ke kode utama.
* Memfasilitasi proses *rollback* (kembali ke versi kode sebelumnya) jika terjadi masalah atau *error* pada kode terbaru.

### 3. Mengapa *virtual environment* digunakan? Apakah kita tetap bisa membuat aplikasi web Django tanpa *virtual environment*?

* **Alasan Penggunaan:** *Virtual environment* digunakan untuk mengisolasi pustaka (*packages/dependencies*) Python khusus untuk satu proyek tertentu. Hal ini mencegah terjadinya bentrok versi (*version conflict*) antar pustaka jika komputer kamu mengerjakan beberapa proyek Python berbeda.
* **Apakah tetap bisa tanpa *virtual environment*?** Ya, aplikasi tetap bisa dibuat. Namun, semua pustaka akan terpasang secara global di sistem komputer, yang berisiko merusak fungsionalidad proyek lain jika ada perubahan versi pustaka secara global.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!

1. **Inisialisasi Proyek & Environment:** Membuat *virtual environment*, menginstal Django, serta membuat proyek Django baru beserta *app* utama (`main`).
2. **Merancang Model (`models.py`):** Membuat struktur model data seperti `Project` dan `Experience` beserta atributnya (termasuk `FileField` untuk dokumen PDF), lalu melakukan `makemigrations` dan `migrate`.
3. **Membuat Views & URL Routing (`views.py` & `urls.py`):** Merancang fungsi *view* untuk menampilkan halaman Profile, Experience, dan Projects, lalu menyambungkan pemetaan URL-nya.
4. **Mengubah Template HTML (`templates/`):** Mengintegrasikan data dinamis dari *database* ke template HTML serta menambahkan tautan kondisional untuk mengunduh/melihat PDF projek.
5. **Konfigurasi Admin & Media:** Mendaftarkan model di `admin.py`, mengatur `MEDIA_URL` dan `MEDIA_ROOT` di `settings.py`, lalu memasukkan data projek dan berkas PDF melalui Django Admin.
6. **Deployment:** Membuat berkas `requirements.txt`, mengunggah seluruh kode ke GitHub, dan melakukan *deployment* ke PWS.