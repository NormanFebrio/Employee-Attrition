# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

Berdasarkan latar belakang di atas, dapat diambil kesimpulan masalah yang sedang dihadapi adalah:

1. Sulitnya mengelola kriteria tiap karyawan
2. Tingginya _attrition rate_

### Cakupan Proyek

Adapun cakupan proyek yang akan dikerjakan antara lain:

1. Membuat _dashboard_ yang dapat memonitori performa karyawan
2. Menganalisis penyebab karyawan memilih untuk mengundurkan diri (_attrition_)

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

1. Membuat environment baru dengan nama hr-problem

```
conda create --name hr-problem python
```

2. Mengaktifkan environment yang telah dibuat

```
conda activate hr-problem
```

3. _Install_ semua library yang dibutuhkan

```
pip install -r requirements.txt
```

4. Jalankan jupyter notebook

```
jupyter-notebook .
```

5. Buat folder baru yang akan menampung proyek ini dan beri nama **human_resource_project**

6. Unggah dataset yang akan digunakan

7. Buat _notebook.ipynb_ baru dan mulai melaksanakan proyek pada _notebook_ tersebut.

## Business Dashboard

Business yang dibuat dikembangkan menggunakan **Tableau Public**. _Dashboard_ tersebut dapat dilihat pada link berikut: https://public.tableau.com/views/AttritionAnalysis_17145268888530/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link.

_Dashboard_ tersebut dikembangkan untuk lebih memudahkan analisis kriteria karyawan yang mengundurkan diri. Fitur yang mungkin menjadi faktor karyawan mengundurkan diri adalah seperti yang ditunjukkan pada _dashboard_. Agar HR lebih mudah dalam memahami _dashboard_ tersebut, warna yang digunakan hanya dua warna yaitu hijau dan merah. Hijau merepresentasikan bahwa karyawan tidak mengundurkan diri, dan merah sebaliknya.

## Conclusion

Kesimpulan yang didapatkan setelah dilakukan analisis adalah sebagai berikut:

1. Tiap departemen memiliki rasio atrisi yang tidak terlalu berbeda jauh, yaitu di antara 14 - 16%.
2. Jika dilihat berdasarkan _Job Role_, **Sales Representative** memiliki rasio tertinggi yang mencapai 32% dari total karyawan pada _job role_ ini (83 karyawan), kemudian disusul oleh **Laboratory Technician** (22%) dan **Human Resources** (17%)
3. Dari segi performa, karyawan yang mengundurkan diri dan tidak mengundurkan diri memiliki nilai performa yang tidak beda jauh. Artinya, baik karyawan yang mengundurkan diri maupun tidak memiliki rata-rata performa yang sama.
4. Dari segi kepuasan, dapat dilihat bahwa karyawan yang mengundurkan diri selalu memiliki nilai rata-rata kepuasan di bawah karyawan yang tidak mengundurkan diri. Artinya, karyawan yang mengundurkan diri memang sudah merasa kurang puas, baik itu dari segi lingkungan, pekerjaan, ataupun relasi.
5. Karyawan yang melakukan lembur juga cenderung untuk mengundurkan diri yang mana persentasenya mencapai 25% dari total karyawan yang lembur.
6. Dari segi _work life balance_, karyawan yang memiliki _work life balance_ yang rendah juga cenderung mengundurkan diri daripada karyawan yang _work life balance_-nya lebih baik.
7. Dari segi segmen, karyawan yang berada pada segmen **Entry-level** dan **Experienced Newcomers** cenderung lebih banyak yang mengundurkan diri. Kedua segmen ini memiliki kesamaan yaitu pada lamanya bekerja pada perusahaan ini yang mana sama sama di bawah 4 tahun.
8. Dari segi _business travel_, semakin sering karyawan tersebut melakukan perjalanan bisnis, semakin besar peluang karyawan tersebut untuk mengundurkan diri.

## Rekomendasi Action Items

Setelah dilakukan analisis, berikut beberapa rekomendasi yang dapat diterapkan agar rasio atrisi pada perusahaan ini berkurang:

1. Adakan kegiatan yang dapat meningkatkan kepuasan karyawan pada perusahaan ini. Untuk mengetahui kegiatan apa yang disukai oleh para karyawan, bisa dilakukan survei mengenai kegiatan apa saja yang disukai oleh tiap karyawan. Dengan mengetahui apa yang disukai oleh karyawan dan kemudian menerapkannya, tentu akan membuat merasa semakin puas bekerja di perusahaan ini.
2. Sediakan program fleksibilitas kerja, waktu istirahat yang memadai, dan dukungan untuk keseimbangan kerja dan hidup karyawan.
3. Khusus untuk segmen Entry-level dan Experienced Newcomers, sediakan jalur pengembangan karir yang jelas dan jaminan dukungan untuk pertumbuhan profesional mereka.
4. Tinjau kebutuhan perjalanan bisnis dan pastikan kebijakan yang sesuai untuk mengurangi beban yang berlebihan bagi karyawan yang sering melakukan perjalanan bisnis.
5. Lanjutkan analisis performa dan kepuasan karyawan secara berkala untuk memantau dampak dari implementasi perubahan dan inisiatif yang telah dilakukan.
6. Tingkatkan komunikasi dan keterlibatan karyawan dalam kebijakan, perubahan organisasi, dan keputusan yang mempengaruhi mereka secara langsung.
