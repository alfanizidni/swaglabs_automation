# Test Final: Mobile Automation Project

## Deskripsi Project
Project ini adalah automation testing untuk aplikasi mobile Swag Labs menggunakan Appium, Pytest, dan Allure sebagai reporting. Project ini menguji fitur login (positif & negatif) dan proses checkout pada aplikasi.

## Struktur Project
- `locators/` : Menyimpan file locator elemen aplikasi
- `pages/` : Implementasi Page Object Model untuk setiap halaman aplikasi
- `tests/` : Berisi file-file test case utama
- `allure-results/` : Output hasil eksekusi untuk Allure
- `allure-report/` : Laporan HTML yang dihasilkan oleh Allure
- `run.bat` : Script untuk menjalankan test dan generate report
- `pytest.ini` : Konfigurasi Pytest

## Tools & Library
- Python
- Appium
- Pytest
- Allure-pytest
- Selenium

## Cara Menjalankan
1. Pastikan Appium server sudah berjalan dan device/emulator sudah terhubung.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan test dan generate report dengan:
   ```bat
   run.bat
   ```
   atau manual:
   ```bash
   pytest --alluredir=allure-results
   allure generate allure-results -o allure-report --single-file --clean
   ```
4. Buka laporan Allure:
   - Buka file `allure-report/index.html` di browser.

## Fitur yang Diuji
- **Login Negative:** Validasi error message untuk kombinasi username/password salah atau kosong
- **Login Positive:** Login dengan kredensial valid
- **Checkout:** End-to-end login, pilih produk, checkout, dan validasi harga

## Catatan
- Pastikan Appium, Allure, dan driver Android sudah terinstall.
- Konfigurasi device dan aplikasi dapat diubah di `conftest.py`.

---
Automation by: [Nama Anda]
