# Fisika Semester 3

Situs belajar statis (HTML + CSS + JS, tanpa build) berisi ringkasan, ilustrasi, dan latihan soal
untuk 8 mata kuliah semester 3, plus kode Python Komputasi Fisika.

```
index.html                    # seluruh situs
python/latihan_komputasi.py   # Euler, RK4, Newton, trapesium, Monte Carlo
requirements.txt
```

Lokal: buka `index.html`, atau `python -m http.server`.
Python: `pip install -r requirements.txt && python python/latihan_komputasi.py`

Deploy: push ke GitHub, lalu Import Project di vercel.com (Framework Preset: Other, tanpa build command).
