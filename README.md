# PATEL store - Modern Django E-Commerce Platform

A feature-rich e-commerce web application built using Python and Django, ready for local development and live deployment on Render.

---

## 🚀 Live Deployment on Render (Step-by-Step Guide)

You can easily deploy this repository to **Render (render.com)** for free:

### Method 1: Render Web Service (Manual)
1. Push this project repository to **GitHub**.
2. Go to [Render Dashboard](https://dashboard.render.com/) and click **New +** > **Web Service**.
3. Connect your GitHub repository (`eshopping`).
4. Set the following settings:
   - **Name**: `patel-store-live` (or any name you prefer)
   - **Region**: Choose the closest region (e.g. Singapore or Frankfurt)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `bash build.sh`
   - **Start Command**: `gunicorn eshopping.wsgi:application`
   - **Instance Type**: Free
5. Under **Environment Variables**, add:
   - `PYTHON_VERSION` = `3.11.9`
   - `DEBUG` = `False`
   - `SECRET_KEY` = *(click Generate or enter a long random string)*
   - `ALLOWED_HOSTS` = `*`
   - `CSRF_TRUSTED_ORIGINS` = `https://*.onrender.com`
   - `ADMIN_USERNAME` = `teerthpatel`
   - `ADMIN_PASSWORD` = `teerth2611`
   - `ADMIN_EMAIL` = `teerthpatel@example.com`
6. Click **Deploy Web Service**.
7. Render will automatically run `build.sh` (installs dependencies, collects static files, applies migrations, and loads demo products).

---

## 🛠️ Local Development Setup

### 1. Clone & Environment
```bash
git clone <repository_url>
cd eshopping
```

### 2. Configure `.env`
Copy `.env.example` to `.env`:
```bash
# Windows
copy .env.example .env

# Mac / Linux
cp .env.example .env
```
Adjust `.env` variables if necessary:
```env
SECRET_KEY=django-insecure-your-key-here
DEBUG=True
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=https://*.onrender.com,http://127.0.0.1:8000,http://localhost:8000
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Load Demo Data
```bash
python manage.py migrate
python manage.py init_data
```

### 5. Start Local Server
```bash
python manage.py runserver
```
Visit:
- **Online Store**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Store Admin Panel**: [http://127.0.0.1:8000/admin-panel/](http://127.0.0.1:8000/admin-panel/)
- **Django Core Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🌟 Features
- **Public Storefront**: Browse products, search, category filter, responsive design.
- **Product Details & Reviews**: Ratings, dynamic stock notices, savings calculation, customer reviews.
- **Cart & Wishlist**: Session-based cart, quantity adjustments, wishlist bookmarking.
- **Checkout & Order History**: Seamless checkout with Cash on Delivery or UPI QR, customer order history tracking.
- **Custom Admin Dashboard**: Product catalog management (CRUD), order status updating, customer directory, revenue & analytics overview.
