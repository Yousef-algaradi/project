# 🎓 المستشار الأكاديمي

منصة ويب ذكية لتوجيه طلاب الثانوية نحو تخصصهم الجامعي المناسب، مع مسارات مهنية من الصفر إلى الاحتراف.

---

## 📖 نظرة عامة

**المستشار الأكاديمي** منصة مبنية بـ **Flask + Python**، تساعد طلاب الثانوية على:

1. 🎯 اختيار تخصصهم الجامعي بناءً على درجاتهم وميولهم
2. 🛤️ اكتشاف المسارات المهنية المناسبة من الصفر إلى الاحتراف
3. 📊 الحصول على توصيات دقيقة عبر محرك تحليل ذكي

---

## ✨ المميزات

### 🎓 قسم الثانوية
- نظام تسجيل ودخول كامل
- إدخال بيانات الثانوية (القسم، الدرجات، الاهتمامات، النسبة)
- اختبار الميول (7 أسئلة) + اختبار المواد (حسب الفرع)
- محرك تحليل ذكي يقدم أفضل 3 تخصصات بنسب توافق
- عرض الأسباب ونقاط التطوير لكل توصية

### 🏛️ قسم الجامعة
- 3 تخصصات: علوم البيانات / الذكاء الاصطناعي / الأمن السيبراني
- 9 مسارات مهنية (3 لكل تخصص)
- ** 1335 سؤال** موزعة على 89 مرحلة
- نظام XP و Streak لتحفيز التعلم
- تتبع التقدم في كل مسار

### 🎨 واجهة المستخدم
- تصميم متجاوب لجميع الأجهزة
- الوضع المظلم/الفاتح (Dark/Light Mode)
- دعم كامل للعربية (RTL)
- تصميم حديث وأنيق

---

## 🚀 كيفية التشغيل

### 📋 المتطلبات

| المتطلب | الإصدار |
|---------|---------|
| Python | 3.10 أو أحدث |
| pip | آخر إصدار |
| Git | (اختياري) |

---

### 🔧 خطوات التثبيت

#### 1️⃣ نسخ المشروع

git clone https://github.com/YOUR_USERNAME/academic-advisor.git
cd academic-advisor

#### 2️⃣ إنشاء بيئة افتراضية

**Windows:**
python -m venv venv
venv\Scripts\activate

**Linux / Mac:**
python3 -m venv venv
source venv/bin/activate

#### 3️⃣ تثبيت المكتبات

pip install -r requirements.txt

#### 4️⃣ إعداد متغيرات البيئة

**انسخ الملف النموذجي:**

Windows:
copy .env.example .env

Linux / Mac:
cp .env.example .env

**افتح `.env` وعدّل `SECRET_KEY`:**

SECRET_KEY=your-super-secret-random-key-here
FLASK_DEBUG=True
FLASK_ENV=development

**توليد مفتاح سري قوي:**
python -c "import secrets; print(secrets.token_hex(32))"

#### 5️⃣ تهيئة قاعدة البيانات (مرة واحدة)

python data/seed_careers.py

**المتوقع:**
🌱 بدء إدخال المسارات المهنية...
✅ اكتمل الإدخال بنجاح!
📊 المسارات المُدخلة: 9
📚  المراحل المُدخلة:89         
❓ الأسئلة المُدخلة: 1335

#### 6️⃣ تشغيل المشروع

python app.py

#### 7️⃣ افتح المتصفح

http://localhost:5000

---

## 📁 هيكل المشروع

academic-advisor/
│
├── app.py                    ← نقطة تشغيل Flask
├── config.py                 ← الإعدادات
├── database.py               ← إعداد SQLAlchemy
├── requirements.txt          ← المكتبات المطلوبة
├── .env.example              ← نموذج متغيرات البيئة
├── .gitignore                ← ملفات مستثناة
├── README.md                 ← هذا الملف
│
├── models/                   ← نماذج قاعدة البيانات
│   ├── user.py
│   ├── high_school.py
│   ├── recommendation.py
│   └── university.py
│
├── services/                 ← المحركات الذكية
│   ├── auth_service.py
│   ├── analysis_engine.py
│   ├── assessment_engine.py
│   └── career_engine.py
│
├── routes/                   ← المسارات (Blueprints)
│   ├── main.py
│   ├── auth.py
│   ├── student.py
│   ├── dashboard.py
│   └── university.py
│
├── data/                     ← محتوى المسارات
│   ├── seed_careers.py
│   └── career_content_*.py
│
├── templates/                ← صفحات HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── welcome_choice.html
│   ├── hs_profile.html
│   ├── assessment.html
│   ├── dashboard.html
│   └── university/
│
├── static/                   ← ملفات ثابتة
│   ├── css/style.css
│   └── js/main.js
│
├── utils/                    ← أدوات مساعدة
│   └── decorators.py
│
└── instance/                 ← قاعدة البيانات (تُنشأ تلقائياً)

---

## 🛠️ التقنيات المستخدمة

| التقنية | الإصدار | الاستخدام |
|---------|---------|-----------|
| Python | 3.10+ | اللغة الأساسية |
| Flask | 3.1.3 | إطار الويب |
| Flask-SQLAlchemy | 3.1.1 | ORM |
| SQLAlchemy | 2.0.51 | ORM الأساسي |
| Jinja2 | 3.1.6 | محرك القوالب |
| Werkzeug | 3.1.8 | أدوات الأمان |
| SQLite | مدمج | قاعدة البيانات |
| Font Awesome | 6.5.0 | الأيقونات |

---

## 🔒 الأمان

- تشفير كلمات السر بـ PBKDF2-SHA256 (600,000 دورة)
- حماية من Session Fixation عبر session.clear()
- كوكيز آمنة (HttpOnly + SameSite=Lax)
- تحقق من صحة الإيميل (Regex)
- تحقق من قوة كلمة السر (6+ أحرف + رقم + حرف)
- رسائل خطأ موحّدة (لا تكشف وجود الإيميل)
- حد أقصى لحجم الطلبات (1MB)
- تسجيل الخروج بـ POST (ضد CSRF)
- SECRET_KEY من متغيرات البيئة

---

## 📊 إحصائيات المشروع

| المقياس | العدد |
|---------|-------|
| Blueprints | 5 |
| Models | 5 |
| Services | 4 |
| Routes | ~25 |
| Templates | ~15 |
| المسارات المهنية | 9 |
| المراحل التعليمية | 90 |
| الأسئلة | 1350 |

---

## 🎬 سيناريو الاستخدام

### 👤 رحلة الطالب الثانوي

1. التسجيل → تسجيل الدخول
2. اختيار "طالب ثانوية"
3. إدخال بيانات الثانوية
4. اختبار الميول (اختياري)
5. محرك التحليل → 3 توصيات
6. عرض المسارات المهنية

### 🎓 رحلة الطالب الجامعي

1. التسجيل → تسجيل الدخول
2. اختيار "طالب جامعي"
3. اختيار التخصص والمسار
4. دراسة المراحل (10 مراحل)
5. اختبار كل مرحلة
6. جمع XP + الحفاظ على Streak

---

## 🐛 استكشاف الأخطاء

**ModuleNotFoundError: No module named 'flask'**
الحل: pip install -r requirements.txt

**sqlite3.OperationalError: unable to open database file**
الحل: احذف instance/highschool.db وأعد التشغيل

**RuntimeError: SECRET_KEY not set**
الحل: تأكد من وجود .env بقيمة SECRET_KEY

---

## 📄 الترخيص

هذا المشروع للاستخدام التعليمي.
يمكنك استخدامه وتعديله ومشاركته مع ذكر المصدر.

---



---

⭐ إذا أعجبك المشروع، لا تنسَ إعطاءه نجمة!
صُنع بـ ❤️ لخدمة الطلاب العرب