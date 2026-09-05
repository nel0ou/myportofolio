Nama : Nela

NPM : 2506620702

Kelas : PBP C

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