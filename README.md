# mysite — پروژهٔ تمرینی Django

 
یک پروژه تمرینی Django و بدون رست فریمورک است که شامل اپلیکیشن‌هایی مانند `accounts` و `blog` می‌شود. هدف این پروژه، تمرین ساختار MVC در Django، پیاده‌سازی احراز هویت، نمایش محتوای داینامیک، مدیریت فایل‌های استاتیک و قالب‌هاست.

---

## ساختار پروژه

- `accounts/`: مدیریت کاربران (ثبت‌نام، ورود، ...)
- `blog/`: مدیریت محتوا (ارسال و نمایش پست‌ها)
- `templates/`: قالب‌های HTML برای صفحات
- `statics/`: فایل‌های CSS/JS/تصویر
- `media/`: فایل‌های آپلود‌شده (در صورت وجود)
- `manage.py` و `mysite/`: هستهٔ پروژه Django

---

## فناوری‌ها

-  **Backend**: Python • Django  
-  **Frontend**: HTML • CSS (via SCSS)  
-  ساختار **MVC با جداسازی اپ‌ها** (`accounts`, `blog`).

---

## نصب و اجرا — محیط توسعه

```bash
git clone https://github.com/Sepehr2S/mysite.git
cd mysite
python -m venv .venv
source .venv/bin/activate  # یا .venv\Scripts\activate در ویندوز
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
