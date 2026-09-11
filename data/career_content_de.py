# data/career_content_de.py
# بنك محتوى مسار "مهندس بيانات (Data Engineer)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

DATA_ENGINEER_PATHS = [
    {
        "major_key": "data_science",
        "slug": "data-engineer",
        "title": "مهندس بيانات (Data Engineer)",
        "description": "مسار متكامل لتصبح مهندس بيانات محترف. يغطي Python، SQL، Data Modeling، ETL، Airflow، Spark، Kafka، Cloud، ومشاريع واقعية.",
        "icon": "⚙️",
        "difficulty": "متقدم",
        "estimated_hours": 260,
        "order_index": 3,
        "stages": [
            # ==========================================
            # المرحلة 1: Programming & Engineering Foundations
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات البرمجة وبيئة مهندس البيانات",
                "description": "بناء أساس برمجي وهندسي قوي يمكّن الطالب من كتابة Python بشكل عملي والتعامل مع الملفات وAPIs وGit وبيئة العمل.",
                "objectives": [
                    "Python fundamentals",
                    "Variables & data types",
                    "Conditions & loops",
                    "Functions",
                    "Lists / tuples / sets / dictionaries",
                    "File handling",
                    "Exceptions",
                    "Modules & packages",
                    "JSON / CSV",
                    "APIs basics",
                    "Virtual environments",
                    "Linux/CLI basics",
                    "Git & GitHub basics",
                    "Basic testing"
                ],
                "practical_task": "أنشئ برنامج Python: CSV/API → قراءة البيانات → تنظيفها → معالجة الأخطاء → حفظ JSON/CSV. ثم أنشئ Git repository، استخدم virtual environment، اكتب README، وأضف اختبارات.",
                "youtube_ar": "https://elzero.org/learning-python/",
                "youtube_en": "https://cs50.harvard.edu/python/",
                "questions": [
                    {"text": "ما نوع البيانات المناسب لتخزين أزواج key:value؟", "options": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الكلمة المستخدمة لتعريف Function في Python؟", "options": {"A": "function", "B": "define", "C": "def", "D": "func"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما المكتبة الشائعة للتعامل مع JSON؟", "options": {"A": "json", "B": "csv", "C": "os", "D": "sys"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Virtual Environment؟", "options": {"A": "زيادة سرعة الإنترنت", "B": "عزل dependencies للمشروع", "C": "ضغط الملفات", "D": "إنشاء قاعدة بيانات"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الأداة المستخدمة لتتبع إصدارات الكود؟", "options": {"A": "Docker", "B": "Git", "C": "Airflow", "D": "Spark"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ماذا يحدث عند استخدام try/except؟", "options": {"A": "حذف البرنامج", "B": "التعامل مع الاستثناءات", "C": "إنشاء Function", "D": "تشغيل SQL"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي بنية أفضل لتخزين name → age؟", "options": {"A": "Set", "B": "Dictionary", "C": "Tuple", "D": "String"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما وظيفة git commit؟", "options": {"A": "رفع المشروع إلى Cloud", "B": "تسجيل التغييرات محلياً", "C": "حذف repository", "D": "تثبيت Python"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الطريقة الأنسب لقراءة JSON في Python؟", "options": {"A": "json.load()", "B": "json.read()", "C": "json.open()", "D": "json.parsefile()"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم requirements.txt؟", "options": {"A": "لتخزين SQL", "B": "لتوثيق dependencies", "C": "لتخزين Git commits", "D": "لتشغيل Airflow"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كان API يعيد JSON، فما الخطوة المنطقية التالية؟", "options": {"A": "تحويله إلى executable", "B": "Parse للبيانات", "C": "حذف JSON", "D": "تشغيل Spark مباشرة"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك Pipeline تعيد التشغيل بعد فشل مؤقت. ما أفضل ممارسة؟", "options": {"A": "حذف البيانات", "B": "معالجة الأخطاء وإعادة المحاولة عند الحاجة", "C": "تعطيل logging", "D": "تغيير قاعدة البيانات كل مرة"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا يفضل استخدام Environment Variables للأسرار؟", "options": {"A": "لتحسين شكل الكود", "B": "لتجنب وضع credentials مباشرة في source code", "C": "لزيادة حجم الملفات", "D": "لاستبدال Git"}, "correct": "B", "difficulty": "hard"},
                    {"text": "برنامج يقرأ CSV ويجد قيمة غير صالحة. ما التصميم الأفضل؟", "options": {"A": "إيقاف كل النظام دائماً", "B": "تجاهل المشكلة بصمت", "C": "معالجة/تسجيل الخطأ وفق سياسة واضحة", "D": "حذف الملف الأصلي"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لديك مشروع Python يحتاج إصدار مكتبات مختلفاً عن مشروع آخر. الحل الأفضل؟", "options": {"A": "استخدام نفس البيئة دائماً", "B": "Virtual environments منفصلة", "C": "حذف المكتبات", "D": "وضع كل شيء في النظام"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2: SQL, Databases & Data Modeling
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ SQL وقواعد البيانات ونمذجة البيانات",
                "description": "إتقان SQL وقواعد البيانات العلائقية وبناء نماذج بيانات يستطيع الطالب استخدامها كأساس لجميع عمليات Data Engineering.",
                "objectives": [
                    "SQL",
                    "SELECT / WHERE",
                    "GROUP BY",
                    "JOIN",
                    "Aggregation",
                    "Subqueries",
                    "CTE",
                    "Window Functions",
                    "PostgreSQL",
                    "Primary/Foreign Keys",
                    "Constraints",
                    "Indexes",
                    "Transactions",
                    "Normalization",
                    "OLTP / OLAP",
                    "Fact & Dimension",
                    "Star Schema"
                ],
                "practical_task": "أنشئ قاعدة PostgreSQL لمتجر: customers → orders → products. ثم نفذ 20 Query، 5 JOIN، 5 Aggregations، 3 CTE، 3 Window Functions، Index واحد، Star Schema بسيط.",
                "youtube_ar": "https://elzero.org/",
                "youtube_en": "https://www.postgresql.org/docs/current/tutorial.html",
                "questions": [
                    {"text": "ما الأمر الذي يسترجع البيانات؟", "options": {"A": "SELECT", "B": "PUSH", "C": "GETDATA", "D": "READ"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة WHERE؟", "options": {"A": "إنشاء جدول", "B": "تصفية الصفوف", "C": "حذف قاعدة البيانات", "D": "إنشاء Index"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المفتاح الذي يميز الصف بشكل فريد؟", "options": {"A": "Foreign Key", "B": "Primary Key", "C": "Index", "D": "View"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة GROUP BY؟", "options": {"A": "تجميع النتائج", "B": "حذف النتائج", "C": "إنشاء قاعدة", "D": "تعديل Schema"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الغرض الأساسي من Foreign Key؟", "options": {"A": "ضغط البيانات", "B": "ربط الجداول", "C": "تشفير البيانات", "D": "تسريع الإنترنت"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي JOIN يعيد الصفوف المتطابقة من الجدولين فقط؟", "options": {"A": "LEFT", "B": "RIGHT", "C": "INNER", "D": "FULL"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما وظيفة COUNT(*)؟", "options": {"A": "حساب الصفوف", "B": "ترتيب الأعمدة", "C": "حذف الصفوف", "D": "إنشاء Index"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Index؟", "options": {"A": "غالباً تحسين الوصول إلى البيانات", "B": "حذف duplicates تلقائياً", "C": "استبدال Primary Key", "D": "تشفير الجدول"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما CTE؟", "options": {"A": "Common Table Expression", "B": "Column Table Engine", "C": "Central Transaction Entry", "D": "Current Table Export"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يميز Window Function؟", "options": {"A": "تعمل فقط على قاعدة فارغة", "B": "تحسب عبر مجموعة مرتبطة دون فقد الصفوف الأصلية", "C": "تحذف البيانات", "D": "تنشئ database"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Transactions؟", "options": {"A": "لإدارة مجموعة عمليات كوحدة منطقية", "B": "لتغيير لغة SQL", "C": "لتخزين الصور", "D": "لرفع الملفات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك مبيعات وتريد ترتيب المنتجات داخل كل فئة. الأنسب؟", "options": {"A": "DROP", "B": "ROW_NUMBER/RANK مع PARTITION BY", "C": "DELETE", "D": "UNION فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "جدول Orders يحتوي ملايين الصفوف والاستعلام يفلتر باستمرار حسب customer_id. ما التحسين المحتمل؟", "options": {"A": "حذف العمود", "B": "Index مناسب", "C": "تحويله إلى JSON", "D": "إزالة Primary Key"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا قد يكون Star Schema مناسباً للتحليلات؟", "options": {"A": "لأنه يبسط الاستعلامات التحليلية", "B": "لأنه يمنع كل JOIN", "C": "لأنه لا يحتاج Tables", "D": "لأنه يخزن كل شيء في عمود واحد"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك جدول Fact للمبيعات. أين يجب أن توجد معلومات العميل التفصيلية عادةً؟", "options": {"A": "Dimension Customer", "B": "Fact نفسه دائماً", "C": "Index", "D": "Transaction Log"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3: Data Warehousing, Data Lakes & ETL/ELT
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ Data Warehousing وData Lakes وETL/ELT",
                "description": "فهم كيفية نقل البيانات من المصادر الخام إلى طبقات منظمة قابلة للتحليل باستخدام ETL/ELT وWarehouses وData Lakes.",
                "objectives": [
                    "ETL / ELT",
                    "Batch processing",
                    "Staging",
                    "Data Warehouse",
                    "Data Lake",
                    "Data Lakehouse concepts",
                    "Raw / Processed / Curated",
                    "Parquet",
                    "CSV / JSON",
                    "Schema",
                    "Data transformations",
                    "Incremental loads",
                    "Fact / Dimension"
                ],
                "practical_task": "أنشئ Pipeline: Raw CSV → Staging PostgreSQL → Transformation → Warehouse. ثم احفظ Raw data، نظف البيانات، طبق Schema، أنشئ Fact + Dimensions، احفظ نسخة Parquet، ونفذ Incremental Load.",
                "youtube_ar": "https://aws.amazon.com/ar/what-is/etl/",
                "youtube_en": "https://datatalksclub.github.io/docs/courses/data-engineering-zoomcamp/",
                "questions": [
                    {"text": "ماذا يعني ETL؟", "options": {"A": "Extract Transform Load", "B": "Execute Transfer Link", "C": "Export Table Logic", "D": "Extract Test Linux"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أين تحفظ البيانات الخام عادة في Pipeline؟", "options": {"A": "Raw layer", "B": "Dashboard", "C": "Index", "D": "API response فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما Parquet؟", "options": {"A": "Database server", "B": "Columnar file format", "C": "Programming language", "D": "Scheduler"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة Staging Layer؟", "options": {"A": "منطقة وسيطة للبيانات", "B": "واجهة مستخدم", "C": "نظام تشغيل", "D": "Firewall"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Data Warehouse يستخدم أساساً لـ؟", "options": {"A": "التحليلات", "B": "تشغيل نظام التشغيل", "C": "DNS", "D": "كتابة Python"}, "correct": "A", "difficulty": "easy"},
                    {"text": "الفرق الأساسي بين ETL وELT هو؟", "options": {"A": "مكان/توقيت التحويل", "B": "لغة البرمجة", "C": "نوع الشبكة", "D": "نظام التشغيل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهدف من Data Lake؟", "options": {"A": "تخزين أنواع مختلفة من البيانات على نطاق واسع", "B": "استبدال كل قواعد البيانات", "C": "تشغيل Git", "D": "إنشاء APIs فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يستخدم Parquet كثيراً في Data Engineering؟", "options": {"A": "Columnar + مناسب للتحليلات", "B": "لأنه executable", "C": "لأنه database server", "D": "لأنه scheduler"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Incremental Load؟", "options": {"A": "تحميل كل البيانات دائماً", "B": "تحميل البيانات الجديدة/المتغيرة فقط", "C": "حذف البيانات", "D": "ضغط الصور"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نحتفظ بـ Raw Layer؟", "options": {"A": "للاحتفاظ بالمصدر وإمكانية إعادة المعالجة", "B": "لإخفاء الأخطاء", "C": "لحذف التاريخ", "D": "لإنشاء واجهة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين Fact وDimension؟", "options": {"A": "Fact للقياسات/الأحداث وDimension للسياق الوصفي", "B": "كلاهما نفس الشيء", "C": "Dimension دائماً أرقام فقط", "D": "Fact لا يحتوي بيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Pipeline تعيد معالجة 5 سنوات يومياً رغم وصول يوم واحد فقط. ما التحسين؟", "options": {"A": "Full reload دائماً", "B": "Incremental processing", "C": "حذف Warehouse", "D": "تحويل SQL إلى HTML"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا يجب الاحتفاظ بالبيانات الخام غير المعدلة؟", "options": {"A": "لإمكانية إعادة بناء الطبقات لاحقاً", "B": "لتقليل البيانات", "C": "لمنع التحليل", "D": "لإلغاء Schema"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أي تصميم أقرب إلى Data Lake layering؟", "options": {"A": "Raw → Processed → Curated", "B": "UI → CSS → JS", "C": "DNS → TCP → IP", "D": "Index → Primary Key → API"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك مصدر بيانات تتغير فيه السجلات القديمة. ما الذي يجب أن يدعمه التصميم؟", "options": {"A": "Incremental/Change handling", "B": "تجاهل التغييرات", "C": "حذف السجلات القديمة", "D": "إعادة تسمية الأعمدة فقط"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4: Data Pipelines & Engineering Practices
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ Data Pipelines وممارسات هندسة البيانات",
                "description": "تحويل المعرفة السابقة إلى Pipelines موثوقة وقابلة لإعادة التشغيل والصيانة، مع التعامل مع APIs والبيانات والأخطاء.",
                "objectives": [
                    "Pipeline architecture",
                    "Ingestion",
                    "APIs",
                    "Batch pipelines",
                    "Incremental loading",
                    "Idempotency",
                    "Retries",
                    "Logging",
                    "Configuration",
                    "Error handling",
                    "Reusable code",
                    "Schema handling",
                    "Data validation"
                ],
                "practical_task": "ابنِ Pipeline: Public API → Python → Validation → Transformation → PostgreSQL. أضف Logging، Error handling، Retry، Configuration file، Incremental loading، Duplicate protection.",
                "youtube_ar": "https://aws.amazon.com/ar/what-is/etl/",
                "youtube_en": "https://datatalksclub.github.io/docs/courses/data-engineering-zoomcamp/",
                "questions": [
                    {"text": "ما وظيفة Pipeline؟", "options": {"A": "نقل ومعالجة البيانات", "B": "تصميم الصور", "C": "تشغيل نظام التشغيل", "D": "إدارة DNS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Logging؟", "options": {"A": "تسجيل أحداث التنفيذ", "B": "حذف البيانات", "C": "تشفير القرص", "D": "إنشاء جدول تلقائياً"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ API؟", "options": {"A": "واجهة للتفاعل بين الأنظمة", "B": "نوع قاعدة بيانات فقط", "C": "ملف مضغوط", "D": "نظام تشغيل"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بالـ Ingestion؟", "options": {"A": "إدخال البيانات إلى النظام", "B": "حذف البيانات", "C": "عرض البيانات", "D": "ضغط البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Configuration؟", "options": {"A": "فصل الإعدادات عن منطق الكود", "B": "حذف الكود", "C": "إلغاء Git", "D": "إنشاء Spark cluster"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Pipeline Idempotent تعني أن إعادة التشغيل؟", "options": {"A": "تسبب تكراراً دائماً", "B": "لا تسبب نتائج غير مرغوبة بسبب التكرار", "C": "تحذف كل شيء", "D": "تمنع التشغيل"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نحتاج Retry؟", "options": {"A": "لمعالجة بعض الأخطاء المؤقتة", "B": "لحذف logs", "C": "لتغيير schema", "D": "لتعطيل pipeline"}, "correct": "A", "difficulty": "medium"},
                    {"text": "API يعيد HTTP 500. ما التصرف الأفضل؟", "options": {"A": "اعتبار العملية ناجحة", "B": "التعامل مع الخطأ وإعادة المحاولة وفق سياسة", "C": "حذف المصدر", "D": "تجاهل المشكلة دائماً"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا Data Validation قبل التخزين؟", "options": {"A": "لاكتشاف بيانات غير صالحة", "B": "لزيادة حجم البيانات", "C": "لتغيير نظام التشغيل", "D": "لمنع SQL"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق بين Full وIncremental ingestion؟", "options": {"A": "Incremental يجلب التغييرات فقط عادة", "B": "لا فرق", "C": "Full يجلب التغييرات فقط", "D": "كلاهما يحذف البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا فصل business logic عن configuration؟", "options": {"A": "يسهل الصيانة والتشغيل في بيئات مختلفة", "B": "يقلل الأمان", "C": "يمنع testing", "D": "يلغي logging"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Pipeline تُشغّل مرتين وتضاعف البيانات. ما المشكلة الأساسية؟", "options": {"A": "عدم Idempotency", "B": "وجود Logging", "C": "وجود Validation", "D": "استخدام JSON"}, "correct": "A", "difficulty": "hard"},
                    {"text": "API يفشل أحياناً بسبب Network timeout. ما التصميم الأنسب؟", "options": {"A": "Retry مع Backoff وحد أقصى", "B": "حذف API", "C": "تشغيل SQL", "D": "تجاهل الخطأ"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Pipeline تستقبل schema مختلفاً فجأة. ما الممارسة الأفضل؟", "options": {"A": "Schema validation + handling", "B": "إدخال البيانات عشوائياً", "C": "حذف كل البيانات", "D": "إلغاء logging"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Pipeline كبيرة ومعقدة ويحتاج الفريق معرفة مكان الفشل. ما أهم تحسين؟", "options": {"A": "Structured logging + clear task boundaries", "B": "حذف logs", "C": "دمج كل شيء في Function واحدة", "D": "إزالة validation"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5: Orchestration, Data Quality, Testing & Monitoring
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ Orchestration وData Quality وTesting وMonitoring",
                "description": "تعلم تشغيل Pipelines بطريقة احترافية مع Airflow، واختبار البيانات ومراقبتها واكتشاف الأخطاء قبل وصولها للمستخدم.",
                "objectives": [
                    "Apache Airflow",
                    "DAGs",
                    "Tasks",
                    "Dependencies",
                    "Scheduling",
                    "Retries",
                    "Backfills basics",
                    "Logs",
                    "Data Quality",
                    "Schema validation",
                    "Null checks",
                    "Duplicate checks",
                    "Unit tests",
                    "Pipeline tests",
                    "Monitoring",
                    "Alerts"
                ],
                "practical_task": "أنشئ Airflow DAG: Extract → Validate → Transform → Load → Quality Check. أضف Dependencies، Retry، Logging، Failure handling، Data quality checks، Alert simulation.",
                "youtube_ar": "https://www.namaait.com/ar/articles/72/هندسة-البيانات",
                "youtube_en": "https://airflow.apache.org/docs/",
                "questions": [
                    {"text": "ما الوظيفة الأساسية لـ Airflow؟", "options": {"A": "Orchestration", "B": "Database encryption", "C": "Image editing", "D": "DNS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يمثل DAG؟", "options": {"A": "Directed Acyclic Graph", "B": "Data Access Group", "C": "Database API Gateway", "D": "Distributed Analytics Grid"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Task؟", "options": {"A": "وحدة عمل داخل workflow", "B": "Database", "C": "Cloud account", "D": "File format"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Logs؟", "options": {"A": "معرفة ما حدث أثناء التنفيذ", "B": "حذف البيانات", "C": "إنشاء schema", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Data Quality تعني؟", "options": {"A": "التأكد من صلاحية البيانات", "B": "زيادة حجم البيانات", "C": "تغيير Python", "D": "إنشاء Cloud"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كانت Task B تعتمد على Task A، يجب؟", "options": {"A": "تعريف dependency", "B": "تشغيل B أولاً", "C": "حذف A", "D": "تشغيلهما عشوائياً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Retry؟", "options": {"A": "التعامل مع الفشل المؤقت", "B": "حذف Task", "C": "منع Scheduler", "D": "حذف Logs"}, "correct": "A", "difficulty": "medium"},
                    {"text": "فحص NOT NULL يكتشف؟", "options": {"A": "القيم المفقودة", "B": "سرعة الشبكة", "C": "duplicates فقط", "D": "schema name"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نختبر Pipeline؟", "options": {"A": "اكتشاف المشاكل قبل الإنتاج", "B": "زيادة حجم الكود", "C": "حذف البيانات", "D": "تعطيل monitoring"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفائدة من Duplicate Check؟", "options": {"A": "اكتشاف التكرار غير المرغوب", "B": "إنشاء API", "C": "تشغيل Spark", "D": "إنشاء Docker image"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجب مراقبته في Pipeline؟", "options": {"A": "Status + failures + duration + logs", "B": "لون الشاشة", "C": "اسم الكمبيوتر فقط", "D": "سرعة لوحة المفاتيح"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Task تفشل بسبب API مؤقتاً. ما الإعداد الأنسب؟", "options": {"A": "Retry policy", "B": "حذف DAG", "C": "Disable scheduler", "D": "Remove logs"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Pipeline نجحت تقنياً لكن عدد السجلات أقل من المتوقع. ما الحل؟", "options": {"A": "Data quality/row-count check", "B": "تجاهل الأمر", "C": "تغيير Python", "D": "حذف warehouse"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا يكفي اختبار الكود فقط؟", "options": {"A": "قد تكون البيانات أو العلاقات نفسها خاطئة", "B": "لأن Python لا يعمل", "C": "لأن SQL غير موجود", "D": "لأن Airflow يمنع testing"}, "correct": "A", "difficulty": "hard"},
                                        {"text": "DAG تحتوي على مراحل كثيرة وفشل غير واضح. أفضل تحسين؟", "options": {"A": "Tasks واضحة + logging + monitoring", "B": "Task واحدة ضخمة", "C": "حذف logs", "D": "تعطيل retries"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6: Big Data & Apache Spark
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ Big Data وApache Spark",
                "description": "فهم Distributed Data Processing واستخدام PySpark لمعالجة بيانات أكبر من أن تكون معالجة تقليدية مناسبة لها.",
                "objectives": [
                    "Distributed computing",
                    "Apache Spark",
                    "PySpark",
                    "Spark DataFrames",
                    "Transformations",
                    "Actions",
                    "Spark SQL",
                    "Joins",
                    "Aggregations",
                    "Partitioning",
                    "Shuffle",
                    "Caching basics",
                    "Performance basics",
                    "Parquet"
                ],
                "practical_task": "استخدم Dataset كبيراً: CSV/Parquet → PySpark → Cleaning → Join → Aggregation → Parquet. ثم قارن Python/Pandas approach مع Spark approach.",
                "youtube_ar": "https://spark.apache.org/docs/latest/api/python/",
                "youtube_en": "https://spark.apache.org/docs/latest/api/python/",
                "questions": [
                    {"text": "ما وظيفة Spark الأساسية؟", "options": {"A": "Distributed Data Processing", "B": "Web design", "C": "DNS", "D": "Version control"}, "correct": "A", "difficulty": "easy"},
                    {"text": "PySpark هو؟", "options": {"A": "Python API لـ Spark", "B": "Database", "C": "Cloud provider", "D": "Linux distribution"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما البنية الأساسية الشائعة في Spark SQL؟", "options": {"A": "DataFrame", "B": "HTML", "C": "Socket", "D": "Repository"}, "correct": "A", "difficulty": "easy"},
                    {"text": "filter تعتبر؟", "options": {"A": "Transformation", "B": "Database", "C": "Action فقط", "D": "File system"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Parquet هو؟", "options": {"A": "File format", "B": "Scheduler", "C": "Database", "D": "Language"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الفرق العام بين Transformation وAction؟", "options": {"A": "Transformation تبني خطة معالجة، Action تطلب تنفيذ النتيجة", "B": "كلاهما Database", "C": "Action تنشئ Python", "D": "لا فرق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Partitioning مهم؟", "options": {"A": "لتوزيع البيانات والمعالجة", "B": "لتشفير البيانات", "C": "لإنشاء Git repository", "D": "لمنع SQL"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Shuffle؟", "options": {"A": "إعادة توزيع بيانات بين مراحل المعالجة", "B": "حذف الملفات", "C": "تشغيل API", "D": "ضغط JSON"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Spark مناسب للبيانات الكبيرة؟", "options": {"A": "يمكنه توزيع المعالجة", "B": "لأنه يعمل فقط على ملف واحد", "C": "لأنه لا يستخدم memory", "D": "لأنه قاعدة بيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Parquet مناسب للتحليل؟", "options": {"A": "Columnar format", "B": "لأنه executable", "C": "لأنه API", "D": "لأنه scheduler"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما تأثير Join ضخم غير محسّن؟", "options": {"A": "قد يسبب Shuffle مكلف", "B": "يمنع Python", "C": "يحذف Spark", "D": "يلغي schema"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Dataset كبير جداً وJoin بين جدولين يسبب Shuffle ضخم. ما الذي تبحث فيه؟", "options": {"A": "Partitioning / join strategy / data size", "B": "تغيير Git", "C": "حذف schema", "D": "استخدام HTML"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا يعني استخدام Spark تلقائياً أداءً أفضل؟", "options": {"A": "تكلفة التوزيع والـoverhead قد تجعل Dataset صغيراً أسرع بأداة أبسط", "B": "Spark دائماً بطيء", "C": "Spark لا يعالج البيانات", "D": "Spark لا يستخدم parallelism"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك transformation كثيرة ولا تحتاج intermediate result إلا مرة واحدة. ما الاعتبار؟", "options": {"A": "تجنب caching غير الضروري", "B": "Cache كل شيء", "C": "حذف البيانات", "D": "استخدام Kafka"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Pipeline Spark أصبحت بطيئة بعد إضافة Join ضخم. ما أول شيء منطقي للتحقيق فيه؟", "options": {"A": "Execution plan + Shuffle + partitions + join strategy", "B": "لون terminal", "C": "Git username", "D": "API key"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7: Real-Time Data & Apache Kafka
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ Real-Time Data وApache Kafka",
                "description": "فهم Event Streaming وبناء Pipelines لمعالجة البيانات المتدفقة باستخدام Kafka وربطها بأنظمة المعالجة والتخزين.",
                "objectives": [
                    "Event streaming",
                    "Apache Kafka",
                    "Topics",
                    "Partitions",
                    "Producers",
                    "Consumers",
                    "Consumer groups",
                    "Offsets",
                    "Retention",
                    "Ordering basics",
                    "Delivery concepts",
                    "Streaming pipelines",
                    "Kafka + Spark basics"
                ],
                "practical_task": "أنشئ: Python Producer → Kafka Topic → Consumer → Storage. ثم أضف: Kafka → Spark Structured Streaming → PostgreSQL/Parquet. اختبر Partitions، Consumer groups، Offsets، Failure/restart، Duplicate handling.",
                "youtube_ar": "https://kafka.apache.org/documentation/",
                "youtube_en": "https://www.confluent.io/training/",
                "questions": [
                    {"text": "Kafka يستخدم أساساً لـ؟", "options": {"A": "Event Streaming", "B": "Image editing", "C": "SQL database فقط", "D": "Web hosting"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أين تُرسل الرسائل؟", "options": {"A": "Topic", "B": "Index", "C": "DAG", "D": "Schema فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "من ينتج الأحداث؟", "options": {"A": "Producer", "B": "Consumer", "C": "Scheduler", "D": "Database"}, "correct": "A", "difficulty": "easy"},
                    {"text": "من يقرأ الأحداث؟", "options": {"A": "Consumer", "B": "Producer", "C": "Docker", "D": "SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Topic يمكن تقسيمه إلى؟", "options": {"A": "Partitions", "B": "Functions", "C": "Tables فقط", "D": "DAGs"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Partition؟", "options": {"A": "توزيع الرسائل والمعالجة", "B": "تشفير Kafka", "C": "إنشاء SQL", "D": "حذف Events"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما Consumer Group؟", "options": {"A": "مجموعة Consumers تتشارك استهلاك partitions", "B": "مجموعة Topics", "C": "قاعدة بيانات", "D": "Cloud account"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما Offset؟", "options": {"A": "موضع/رقم رسالة في Partition", "B": "اسم Database", "C": "نوع SQL", "D": "Docker image"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Kafka مناسب للStreaming؟", "options": {"A": "مصمم للتعامل مع تدفق الأحداث", "B": "لأنه فقط Excel", "C": "لأنه ORM", "D": "لأنه Web framework"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا زاد عدد partitions ويمكن زيادة consumers ضمن group، ما الفائدة؟", "options": {"A": "إمكانية توزيع العمل", "B": "حذف الرسائل", "C": "إلغاء topic", "D": "منع parallelism"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يجب أن يحدث عند إعادة تشغيل Consumer؟", "options": {"A": "يمكنه المتابعة حسب offset/commit strategy", "B": "يجب حذف topic", "C": "يجب حذف Kafka", "D": "يجب إعادة إنشاء كل البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Consumer بطيء جداً مقارنة بالمنتج. ماذا يحدث غالباً؟", "options": {"A": "تتراكم الرسائل/lag", "B": "تختفي Kafka", "C": "يتحول topic إلى database", "D": "يتوقف Python دائماً"}, "correct": "A", "difficulty": "hard"},
                    {"text": "تريد أكثر من Consumer يقرأ نفس الأحداث لأغراض مختلفة. ماذا تستخدم؟", "options": {"A": "Consumer Groups مختلفة", "B": "نفس Consumer فقط", "C": "حذف partitions", "D": "تغيير PostgreSQL"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا يكفي قول \"Kafka يمنع duplicates\"؟", "options": {"A": "لأن semantics والمعالجة والتصميم قد تؤدي إلى إعادة معالجة", "B": "لأن Kafka لا يحتوي Topics", "C": "لأن Kafka SQL فقط", "D": "لأن Producer لا يرسل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Streaming pipeline تحتاج إعادة معالجة آمنة للرسائل. أهم مفهوم؟", "options": {"A": "Idempotent processing / correct offset handling", "B": "حذف offsets", "C": "تعطيل partitions", "D": "تخزين كل شيء في RAM"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8: Cloud, Docker, DevOps & Production
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ Cloud وDocker وDevOps وProduction Data Engineering",
                "description": "نقل مهارات Data Engineering إلى بيئة تشغيل أقرب للإنتاج باستخدام Cloud وDocker وGit وممارسات Deployment وSecurity الأساسية.",
                "objectives": [
                    "Cloud concepts",
                    "Object storage",
                    "Compute",
                    "IAM",
                    "Cloud databases",
                    "Cloud data services",
                    "Docker",
                    "Docker Compose",
                    "Environment variables",
                    "GitHub",
                    "CI/CD concepts",
                    "Deployment basics",
                    "Monitoring",
                    "Security basics",
                    "Production configuration"
                ],
                "practical_task": "حوّل Pipeline سابقة إلى Docker Compose: Python + PostgreSQL + Airflow. ضع secrets في Environment Variables، ارفع المشروع على GitHub، أنشئ Dockerfile و compose file، وثق deployment، نفذ Cloud storage بسيط.",
                "youtube_ar": "https://ar.inskillops.com/docs/decouverte/docker/toc/",
                "youtube_en": "https://docs.docker.com/get-started/",
                "questions": [
                    {"text": "Docker يستخدم لـ؟", "options": {"A": "Containerization", "B": "SQL فقط", "C": "Spreadsheet", "D": "DNS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Cloud Object Storage مناسب لـ؟", "options": {"A": "تخزين الملفات/objects", "B": "كتابة Python", "C": "Git commits فقط", "D": "Scheduling فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "IAM يهتم بـ؟", "options": {"A": "Identity and Access", "B": "Image Animation", "C": "Internal API Memory", "D": "Index Allocation"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Dockerfile يستخدم لـ؟", "options": {"A": "تعريف كيفية بناء Image", "B": "إنشاء SQL table", "C": "كتابة Airflow DAG فقط", "D": "تخزين البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "GitHub يستخدم لـ؟", "options": {"A": "استضافة وإدارة repositories", "B": "تشغيل Spark فقط", "C": "Cloud storage فقط", "D": "SQL engine"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Docker Compose؟", "options": {"A": "إدارة عدة services معاً", "B": "إنشاء Database فقط", "C": "كتابة Python", "D": "تشغيل Kafka فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا لا تضع password داخل Git repository؟", "options": {"A": "خطر أمني", "B": "لأنه يبطئ Python", "C": "لأنه يمنع SQL", "D": "لأنه يوقف Docker"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أين يمكن وضع secrets للتطبيق؟", "options": {"A": "Environment variables/secret manager", "B": "README العام", "C": "source code العام", "D": "اسم المشروع"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Cloud مفيد لـData Engineering؟", "options": {"A": "موارد وخدمات قابلة للتوسع", "B": "لأنه يلغي SQL", "C": "لأنه يمنع Pipelines", "D": "لأنه بديل Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهدف من CI/CD؟", "options": {"A": "أتمتة build/test/deployment", "B": "حذف Git", "C": "تخزين SQL", "D": "تشغيل Browser"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل ممارسة عند تشغيل نفس Pipeline في dev وproduction؟", "options": {"A": "فصل configuration عن code", "B": "نسخ passwords داخل الكود", "C": "تغيير الكود يدوياً دائماً", "D": "حذف Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Container يعمل محلياً لكنه يفشل بسبب credentials في الإنتاج. ما السبب المحتمل؟", "options": {"A": "Configuration/secrets management", "B": "Spark DataFrame", "C": "SQL JOIN", "D": "Kafka topic"}, "correct": "A", "difficulty": "hard"},
                    {"text": "فريق يريد تشغيل PostgreSQL + Airflow + Python معاً محلياً. ما الأنسب؟", "options": {"A": "Docker Compose", "B": "HTML", "C": "Git commit", "D": "CSV"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Pipeline تحتاج صلاحية قراءة Bucket فقط. ما أفضل ممارسة؟", "options": {"A": "Least privilege IAM", "B": "Admin access دائماً", "C": "مشاركة root credentials", "D": "وضع password في README"}, "correct": "A", "difficulty": "hard"},
                    {"text": "قبل نشر Pipeline للإنتاج، ما المجموعة الأهم؟", "options": {"A": "Testing + configuration + logging + monitoring + security", "B": "تغيير اسم الملفات فقط", "C": "حذف tests", "D": "إزالة logs"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9: Practical Projects
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية المتكاملة",
                "description": "دمج جميع المهارات السابقة في مشاريع حقيقية متدرجة تثبت أن الطالب يستطيع بناء أنظمة Data Engineering وليس مجرد دراسة الأدوات.",
                "objectives": [
                    "Python",
                    "SQL",
                    "PostgreSQL",
                    "Data Modeling",
                    "ETL/ELT",
                    "Data Warehouse",
                    "Data Lake",
                    "Airflow",
                    "Data Quality",
                    "Testing",
                    "Spark",
                    "Kafka",
                    "Cloud",
                    "Docker",
                    "GitHub",
                    "Documentation",
                    "Architecture"
                ],
                "practical_task": "ابنِ 6 مشاريع تدريجية + Capstone كامل: (1) Beginner Pipeline (2) Data Warehouse (3) Airflow (4) Spark (5) Kafka Streaming (6) Cloud + Capstone: نظام متكامل من المصدر إلى Analytics مع Documentation كامل.",
                "youtube_ar": "https://www.udemy.com/course/data-engineering-bootcamp-from-zero-to-job-ready-arabic/",
                "youtube_en": "https://datatalksclub.github.io/docs/courses/data-engineering-zoomcamp/",
                "questions": [
                    {"text": "ما الهدف من Project Portfolio؟", "options": {"A": "إثبات القدرة العملية", "B": "جمع فيديوهات", "C": "تخزين passwords", "D": "كتابة CV فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أين يجب توثيق المشروع؟", "options": {"A": "README", "B": "RAM", "C": "BIOS", "D": "DNS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يوضح مكونات النظام والعلاقات بينها؟", "options": {"A": "Architecture Diagram", "B": "Password", "C": "SQL password", "D": "Git commit message فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Project Pipeline يجب أن يبدأ بـ؟", "options": {"A": "فهم Problem/Requirements", "B": "Kafka مباشرة", "C": "Spark مباشرة", "D": "Cloud مباشرة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Git في المشاريع؟", "options": {"A": "Version control", "B": "Data Warehouse", "C": "Streaming", "D": "Monitoring فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "مشروع Warehouse يجب أن يحتوي على؟", "options": {"A": "Fact/Dimensions عند استخدام Star Schema", "B": "HTML فقط", "C": "Kafka فقط", "D": "Docker فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Airflow في مشروع Pipeline؟", "options": {"A": "Scheduling/Orchestration", "B": "Database storage", "C": "File compression", "D": "Web design"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Spark في مشروع Big Data؟", "options": {"A": "Distributed processing", "B": "Git hosting", "C": "Password management", "D": "DNS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Kafka في مشروع Streaming؟", "options": {"A": "Event streaming", "B": "SQL queries", "C": "Static file editing", "D": "CV building"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن يحتوي المشروع على Data Quality؟", "options": {"A": "للتأكد من صحة البيانات", "B": "لإضافة حشو", "C": "لتغيير اللغة", "D": "لتصميم UI"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل المشروع أقرب للإنتاج؟", "options": {"A": "Testing + monitoring + logging + documentation", "B": "screenshots فقط", "C": "عنوان جميل", "D": "عدد ملفات كبير"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك Project يستخدم Spark لكن Dataset صغير جداً. ما القرار المهني؟", "options": {"A": "توضيح سبب استخدام Spark أو اختيار أداة أبسط", "B": "استخدام Spark لمجرد أنه مشهور", "C": "إضافة Kafka", "D": "إضافة Kubernetes"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Capstone يعمل لكن لا يستطيع شخص آخر تشغيله. ما الناقص؟", "options": {"A": "Setup documentation + environment/containerization", "B": "SQL فقط", "C": "Screenshot", "D": "Logo"}, "correct": "A", "difficulty": "hard"},
                    {"text": "مشروع Streaming يفقد البيانات بعد restart. ما الذي يجب التحقيق فيه؟", "options": {"A": "offsets/persistence/processing semantics", "B": "لون Dashboard", "C": "Git username", "D": "README title"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في مقابلة طلب منك شرح مشروعك. أفضل طريقة؟", "options": {"A": "Problem → Architecture → Data Flow → Tools → Decisions → Results → Trade-offs", "B": "ذكر أسماء الأدوات فقط", "C": "عرض screenshots فقط", "D": "قراءة README حرفياً"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10: Professional Preparation & Job Ready
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 Portfolio وProfessional Preparation وJob Ready",
                "description": "تحويل المهارات والمشاريع إلى جاهزية فعلية لوظائف Junior/Entry-Level Data Engineer من خلال Portfolio وCV والمقابلات.",
                "objectives": [
                    "GitHub Portfolio",
                    "Project Documentation",
                    "CV",
                    "LinkedIn",
                    "Case Studies",
                    "SQL Interviews",
                    "Python Interviews",
                    "Data Engineering Interviews",
                    "System Design Basics",
                    "Practical Assessments",
                    "Job Search",
                    "Technical Communication",
                    "Project Presentation"
                ],
                "practical_task": "أنشئ Job-Ready Package: GitHub مرتب، 3-5 مشاريع قوية، Capstone كامل، CV مخصص لـData Engineer، LinkedIn، README احترافي، Architecture diagrams، SQL interview practice، Python interview practice، Mock interview.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/career-paths/data-engineer",
                "youtube_en": "https://learn.microsoft.com/en-us/training/career-paths/data-engineer",
                "questions": [
                    {"text": "ما أهم شيء في Data Engineer Portfolio؟", "options": {"A": "مشاريع حقيقية موثقة", "B": "عدد المتابعين فقط", "C": "صورة شخصية", "D": "عدد الشهادات فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يجب أن يوضح README؟", "options": {"A": "الهدف وطريقة التشغيل والنتائج", "B": "password", "C": "بيانات شخصية", "D": "كود عشوائي"}, "correct": "A", "difficulty": "easy"},
                    {"text": "CV يجب أن يكون؟", "options": {"A": "مخصصاً للوظيفة", "B": "عاماً دائماً", "C": "مليئاً بالمهارات غير المستخدمة", "D": "بلا مشاريع"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة LinkedIn؟", "options": {"A": "Professional presence/networking", "B": "Database processing", "C": "Spark execution", "D": "Kafka management"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يعني Junior/Entry-Level؟", "options": {"A": "مستوى بداية مهني مع Core Skills", "B": "Senior", "C": "Architect", "D": "CTO"}, "correct": "A", "difficulty": "easy"},
                    {"text": "سُئلت عن مشروعك في مقابلة. ماذا تبدأ به؟", "options": {"A": "Problem", "B": "أسماء المكتبات", "C": "لون الواجهة", "D": "عدد commits"}, "correct": "A", "difficulty": "medium"},
                    {"text": "سُئلت عن SQL. الأفضل أن تتوقع؟", "options": {"A": "كتابة وتحليل Queries", "B": "تعريف SQL فقط", "C": "تاريخ SQL", "D": "HTML"}, "correct": "A", "difficulty": "medium"},
                    {"text": "سُئلت لماذا اخترت Airflow. ماذا يجب أن تشرح؟", "options": {"A": "المشكلة التي يحلها والـtrade-offs", "B": "اسمه فقط", "C": "الشركة التي صنعته", "D": "لون واجهته"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يثبت مهارة Data Engineering أكثر؟", "options": {"A": "مشروع يعمل وموثق", "B": "مشاهدة 100 ساعة فيديو", "C": "شهادة فقط", "D": "قائمة Tools"}, "correct": "A", "difficulty": "medium"},
                    {"text": "System Design interview قد يطلب منك؟", "options": {"A": "تصميم Pipeline/Architecture", "B": "كتابة CSS", "C": "تعديل صورة", "D": "كتابة CV"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا لم تعرف إجابة في مقابلة، الأفضل؟", "options": {"A": "توضيح ما تعرفه وشرح طريقة تفكيرك", "B": "اختلاق الإجابة", "C": "تغيير الموضوع", "D": "إغلاق المقابلة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك CV يحتوي 40 تقنية لكن مشروعك يستخدم 5 فقط. الأفضل؟", "options": {"A": "التركيز على المهارات المثبتة بالمشاريع", "B": "إضافة 20 تقنية أخرى", "C": "حذف المشاريع", "D": "كتابة Senior"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في Interview طلب منك تصميم Pipeline لمليارات الأحداث اليومية. ما أول خطوة؟", "options": {"A": "تحديد المتطلبات والـconstraints", "B": "اختيار Kafka فوراً", "C": "اختيار AWS فوراً", "D": "كتابة Python فوراً"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب مناقشة Trade-offs في System Design؟", "options": {"A": "لأن التصميم الواقعي يتطلب موازنة التكلفة والأداء والموثوقية والتعقيد", "B": "لأنها غير مهمة", "C": "لأنها تخص Frontend فقط", "D": "لأنها بديل عن Architecture"}, "correct": "A", "difficulty": "hard"},
                    {"text": "متى تعلن نفسك Job Ready؟", "options": {"A": "بعد اجتياز المهارات الأساسية والمشاريع والتقييم العملي", "B": "بعد أول كورس", "C": "بعد شهادة واحدة", "D": "بعد حفظ أسماء الأدوات"}, "correct": "A", "difficulty": "hard"}
                ]
            }
        ]
    }
]