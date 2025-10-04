Sistem stok **single-warehouse** sederhana berbasis Django. Fitur utama:
- Master data **Product**, **Category**, **UoM**
- **Transaction** IN/OUT dengan validasi stok tidak boleh negatif
- Stok realtime di `Product.qty_on_hand` via signals
- UI Bootstrap 5 + Bootstrap Icons, layout DRY (`base.html`, partials)
- Form rapi pakai **django-crispy-forms** (Bootstrap 5)
- **Inventory → Ringkasan**: total IN/OUT, grafik tren harian (Chart.js), rekap per-produk, filter tanggal/kategori/produk, **Export CSV (ringkasan & detail)**
- Daftar Produk: **search**, filter, **low stock** toggle, pagination
- Auth: login/logout, **login page** yang rapi

- cp .env.example .env
python manage.py migrate
python manage.py createsuperuser --username $(grep ADMIN_USERNAME .env|cut -d= -f2) --email admin@example.com
# saat diminta password, isi Andalas2025Test (atau tulis script mgmt command jika mau otomatis)
python manage.py runserver

file .env
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=True
DB_NAME=warehouse
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=127.0.0.1
DB_PORT=5432
ADMIN_USERNAME=administrator
ADMIN_PASSWORD=Andalas2025Test


