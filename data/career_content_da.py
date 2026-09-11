# data/career_content.py
# ==========================================
# بنك محتوى المسارات المهنية
# ==========================================
# هذا الملف يحتوي على:
# - المسار المهني "محلل بيانات" (Data Analyst)
# - 9 مراحل تعليمية كاملة
# - 15 سؤالاً لكل مرحلة (135 سؤالاً إجمالاً)
# ==========================================

DATA_SCIENCE_PATHS = [
    # ==========================================
    # المسار 1: محلل بيانات (Data Analyst)
    # ==========================================
    {
        "major_key": "data_science",
        "slug": "data-analyst",
        "title": "محلل بيانات (Data Analyst)",
        "description": "مسار متكامل من الصفر إلى الاحتراف لتصبح محلل بيانات محترف. يغطي Excel و SQL و Python و Power BI مع مشاريع واقعية.",
        "icon": "📊",
        "difficulty": "مبتدئ",
        "estimated_hours": 120,
        "order_index": 1,
        "stages": [
            # ==========================================
            # المرحلة 1
            # ==========================================
            {
                "stage_number": 1,
                "title": "🎯 أساسيات تحليل البيانات",
                "description": "فهم مجال تحليل البيانات وطريقة تفكير محلل البيانات وكيف تتحول البيانات إلى قرارات.",
                "objectives": [
                    "مفهوم البيانات وتحليل البيانات",
                    "دورة حياة تحليل البيانات",
                    "أنواع التحليل (Descriptive, Diagnostic, Predictive, Prescriptive)",
                    "دور Data Analyst",
                    "تحويل البيانات إلى Insights و Recommendations"
                ],
                "practical_task": "اختر مشكلة بسيطة، وحدد: Business Question → Data → Analysis → Insight → Recommendation",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.youtube.com/watch?v=ua-CiDNNj30",
                "questions": [
                    # Easy
                    {"text": "ما المقصود بـ Data Analysis؟", "options": {"A": "تصميم مواقع الإنترنت", "B": "فحص البيانات لاستخراج معلومات واستنتاجات مفيدة", "C": "كتابة أنظمة تشغيل", "D": "تصميم شبكات"}, "correct": "B", "difficulty": "easy"},
                    {"text": "من أهم أهداف محلل البيانات:", "options": {"A": "استبدال قواعد البيانات", "B": "إنشاء أنظمة تشغيل", "C": "استخراج Insights تساعد في اتخاذ القرار", "D": "تركيب أجهزة الكمبيوتر"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Dataset؟", "options": {"A": "مجموعة منظمة من البيانات", "B": "برنامج حماية", "C": "لغة برمجة", "D": "جهاز شبكي"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي مما يلي مثال على بيانات رقمية؟", "options": {"A": "اسم العميل", "B": "لون المنتج", "C": "المدينة", "D": "قيمة المبيعات"}, "correct": "D", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Insight؟", "options": {"A": "ملف Excel", "B": "استنتاج مفيد تم استخراجه من البيانات", "C": "قاعدة بيانات فارغة", "D": "لغة برمجة"}, "correct": "B", "difficulty": "easy"},
                    # Medium
                    {"text": "التحليل الذي يجيب عن سؤال 'ماذا حدث؟' هو:", "options": {"A": "Descriptive Analytics", "B": "Predictive Analytics", "C": "Prescriptive Analytics", "D": "Diagnostic Analytics"}, "correct": "A", "difficulty": "medium"},
                    {"text": "التحليل الذي يبحث عن سبب حدوث مشكلة هو:", "options": {"A": "Predictive", "B": "Prescriptive", "C": "Diagnostic", "D": "Descriptive"}, "correct": "C", "difficulty": "medium"},
                    {"text": "إذا أردت معرفة المبيعات المتوقعة الشهر القادم فأنت تستخدم:", "options": {"A": "Diagnostic Analytics", "B": "Predictive Analytics", "C": "Descriptive Analytics", "D": "Data Cleaning"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما أفضل بداية لمشكلة تحليل بيانات؟", "options": {"A": "اختيار الرسم البياني", "B": "كتابة كود Python", "C": "تحميل Power BI", "D": "تحديد السؤال أو المشكلة التجارية"}, "correct": "D", "difficulty": "medium"},
                    {"text": "لماذا يجب فهم Business Question قبل تحليل البيانات؟", "options": {"A": "لتحديد ما البيانات والتحليل المطلوبان", "B": "لتقليل حجم الشاشة", "C": "لتغيير نظام التشغيل", "D": "لإنشاء شبكة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي ترتيب أكثر منطقية؟", "options": {"A": "Recommendation → Data → Question → Insight", "B": "Dashboard → Question → Data → Cleaning", "C": "Question → Data → Analysis → Insight → Recommendation", "D": "Code → Recommendation → Data"}, "correct": "C", "difficulty": "medium"},
                    # Hard
                    {"text": "ارتفعت المبيعات بنسبة 20%. لمعرفة سبب الارتفاع، ما النوع الأنسب؟", "options": {"A": "Descriptive", "B": "Diagnostic", "C": "Predictive", "D": "Prescriptive"}, "correct": "B", "difficulty": "hard"},
                    {"text": "شركة تريد معرفة الإجراء الأفضل لتقليل إلغاء الطلبات. هذا أقرب إلى:", "options": {"A": "Descriptive", "B": "Diagnostic", "C": "Predictive", "D": "Prescriptive"}, "correct": "D", "difficulty": "hard"},
                    {"text": "اكتشف المحلل أن المبيعات انخفضت بعد زيادة السعر. ما الخطوة الأفضل قبل إعلان أن السعر هو السبب؟", "options": {"A": "التحقق من عوامل أخرى ووجود علاقة سببية حقيقية", "B": "حذف البيانات", "C": "إنشاء Dashboard مباشرة", "D": "تغيير قاعدة البيانات"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أي نتيجة تعتبر Insight أفضل؟", "options": {"A": "عدد الصفوف 10,000", "B": "العمود اسمه Sales", "C": "العملاء الجدد في المنطقة A زادت مشترياتهم 35% بعد الحملة", "D": "الملف بصيغة CSV"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2
            # ==========================================
            {
                "stage_number": 2,
                "title": "📊 Excel لتحليل البيانات",
                "description": "إتقان Excel لتنظيف البيانات وتحليلها وإنشاء التقارير والرسوم.",
                "objectives": [
                    "Functions & Formulas",
                    "IF و SUMIFS و COUNTIFS",
                    "VLOOKUP / XLOOKUP",
                    "تنظيف البيانات",
                    "Pivot Tables",
                    "Charts و Dashboards"
                ],
                "practical_task": "استخدم جدول مبيعات: احسب الإجمالي، استخدم SUMIFS، أنشئ Pivot Table، أنشئ Chart، استخرج أعلى منطقة مبيعاً.",
                "youtube_ar": "https://www.youtube.com/watch?v=0FwIPtRhLi4",
                "youtube_en": "https://www.youtube.com/watch?v=opJgMj1IUrc",
                "questions": [
                    # Easy
                    {"text": "ما وظيفة SUM؟", "options": {"A": "حساب المتوسط", "B": "جمع القيم", "C": "البحث", "D": "التصفية"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة AVERAGE؟", "options": {"A": "حساب المتوسط", "B": "حساب المجموع", "C": "حذف التكرار", "D": "البحث"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي أداة تستخدم لإنشاء ملخص تفاعلي للبيانات؟", "options": {"A": "Word", "B": "Paint", "C": "Pivot Table", "D": "Notepad"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما وظيفة Filter؟", "options": {"A": "حذف الملف", "B": "تغيير نظام التشغيل", "C": "إنشاء قاعدة بيانات", "D": "عرض الصفوف التي تحقق شرطًا"}, "correct": "D", "difficulty": "easy"},
                    {"text": "ما فائدة Charts؟", "options": {"A": "تمثيل البيانات بصريًا", "B": "تشفير البيانات", "C": "إنشاء كلمات مرور", "D": "حذف الأعمدة"}, "correct": "A", "difficulty": "easy"},
                    # Medium
                    {"text": "أي دالة مناسبة لجمع المبيعات حسب Region؟", "options": {"A": "COUNT", "B": "SUMIFS", "C": "AVERAGE", "D": "LEFT"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما وظيفة IF؟", "options": {"A": "إنشاء Pivot Table", "B": "حذف الصفوف", "C": "اختبار شرط وإرجاع نتيجة حسب الشرط", "D": "رسم Chart"}, "correct": "C", "difficulty": "medium"},
                    {"text": "لديك Customer ID وتريد إحضار اسم العميل من جدول آخر. ما الأداة المناسبة؟", "options": {"A": "XLOOKUP", "B": "SUM", "C": "COUNT", "D": "ROUND"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك بيانات تحتوي على صفوف مكررة. ما الأداة المناسبة لإزالتها؟", "options": {"A": "Freeze Panes", "B": "Sort", "C": "Remove Duplicates", "D": "Format Painter"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما وظيفة VLOOKUP؟", "options": {"A": "البحث عن قيمة في جدول وإرجاع قيمة من عمود آخر", "B": "حساب المجموع", "C": "إنشاء Pivot Table", "D": "رسم Chart"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة لتنظيم بيانات كبيرة؟", "options": {"A": "استخدام جداول Excel (Ctrl+T)", "B": "حذف الصفوف", "C": "دمج الخلايا", "D": "تلوين يدوي"}, "correct": "A", "difficulty": "medium"},
                    # Hard
                    {"text": "تريد معرفة إجمالي Sales للـ Laptop في Aden فقط. ما الأنسب؟", "options": {"A": "SUM", "B": "SUMIFS", "C": "COUNT", "D": "AVERAGE"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا كان لديك 10,000 صف وتريد تلخيص المبيعات حسب Region و Product بسرعة، ما الخيار الأفضل؟", "options": {"A": "Pivot Table", "B": "كتابة كل النتائج يدويًا", "C": "Paint", "D": "Word"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كانت بعض الخلايا فارغة في عمود Sales، فما الخطوة الصحيحة أولًا؟", "options": {"A": "حذف الملف", "B": "تجاهل المشكلة دائمًا", "C": "تحويل الملف إلى صورة", "D": "فحص سبب القيم المفقودة وتحديد طريقة التعامل معها"}, "correct": "D", "difficulty": "hard"},
                    {"text": "لديك بيانات مبيعات يومية وتريد إظهار اتجاه المبيعات مع الزمن. ما الرسم الأنسب غالبًا؟", "options": {"A": "Pie Chart", "B": "Line Chart", "C": "Donut Chart", "D": "Radar Chart"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3
            # ==========================================
            {
                "stage_number": 3,
                "title": "🗄️ SQL لتحليل البيانات",
                "description": "استخدام SQL لاستخراج البيانات وتحليلها من قواعد البيانات.",
                "objectives": [
                    "SELECT و WHERE و ORDER BY",
                    "GROUP BY و HAVING",
                    "JOINs",
                    "CASE",
                    "Subqueries و CTEs",
                    "Window Functions",
                    "تنظيف واستكشاف البيانات"
                ],
                "practical_task": "استخدم جدولين (Customers + Orders). نفّذ: SELECT → WHERE → GROUP BY → JOIN → CASE → Aggregation.",
                "youtube_ar": "https://www.udemy.com/course/learn-sql-basics-for-beginners-in-arabic-2021/",
                "youtube_en": "https://www.youtube.com/watch?v=OT1RErkfLNQ",
                "questions": [
                    # Easy
                    {"text": "ما الأمر المستخدم لعرض بيانات من جدول؟", "options": {"A": "SELECT", "B": "DELETE", "C": "DROP", "D": "UPDATE"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة WHERE؟", "options": {"A": "ترتيب النتائج", "B": "تصفية الصفوف حسب شرط", "C": "حذف الجدول", "D": "إنشاء قاعدة بيانات"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة ORDER BY؟", "options": {"A": "تجميع البيانات", "B": "حذف البيانات", "C": "ترتيب النتائج", "D": "ربط الجداول"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما وظيفة COUNT؟", "options": {"A": "حساب عدد القيم / الصفوف", "B": "حساب المتوسط", "C": "ترتيب البيانات", "D": "تغيير البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي أمر يستخدم لتجميع النتائج؟", "options": {"A": "WHERE", "B": "GROUP BY", "C": "ORDER BY", "D": "LIMIT"}, "correct": "B", "difficulty": "easy"},
                    # Medium
                    {"text": "الاستعلام الصحيح لإظهار الطلبات التي amount أكبر من 500 هو:", "options": {"A": "SELECT * FROM Orders WHERE amount > 500;", "B": "SELECT * FROM Orders GROUP amount > 500;", "C": "SELECT amount > 500 FROM Orders;", "D": "WHERE amount > 500 SELECT Orders;"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة JOIN؟", "options": {"A": "حذف البيانات", "B": "دمج بيانات مرتبطة من جداول مختلفة", "C": "ترتيب النتائج", "D": "إنشاء ملف CSV"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي JOIN يعرض الصفوف المتطابقة بين الجدولين؟", "options": {"A": "FULL DELETE", "B": "CROSS DROP", "C": "INNER JOIN", "D": "ORDER JOIN"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما وظيفة HAVING؟", "options": {"A": "تصفية المجموعات بعد GROUP BY", "B": "ترتيب الأعمدة", "C": "حذف الصفوف", "D": "إنشاء جدول"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي دالة تستخدم لحساب متوسط amount؟", "options": {"A": "SUM", "B": "AVG", "C": "COUNT", "D": "MAX"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الفرق بين WHERE و HAVING؟", "options": {"A": "WHERE تُصفّي الصفوف قبل GROUP BY، وHAVING تُصفّي المجموعات بعده", "B": "لا فرق", "C": "HAVING أسرع", "D": "WHERE للحذف"}, "correct": "A", "difficulty": "medium"},
                    # Hard
                    {"text": "ما نتيجة الاستعلام المفاهيمي الذي يجمع amount لكل customer_id؟", "options": {"A": "SELECT customer_id, SUM(amount) FROM Orders GROUP BY customer_id;", "B": "SELECT SUM customer_id FROM Orders;", "C": "GROUP Orders BY amount;", "D": "SELECT customer_id FROM SUM(Orders);"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الهدف الأساسي من Window Functions؟", "options": {"A": "حذف الجداول", "B": "تنفيذ حسابات على مجموعة من الصفوف مع الاحتفاظ بتفاصيل الصفوف", "C": "إنشاء قاعدة بيانات", "D": "تغيير نوع الملف"}, "correct": "B", "difficulty": "hard"},
                    {"text": "أي خيار يمثل CTE؟", "options": {"A": "CREATE TEMP EMPTY", "B": "WITH sales AS (...)", "C": "TABLE WITH DELETE", "D": "GROUP WITH DROP"}, "correct": "B", "difficulty": "hard"},
                                        {"text": "إذا أردت ترتيب العملاء حسب مجموع مشترياتهم وإعطاء Ranking لكل عميل، ما الأنسب؟", "options": {"A": "WHERE فقط", "B": "DROP TABLE", "C": "Window Function مع Ranking", "D": "DELETE"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4
            # ==========================================
            {
                "stage_number": 4,
                "title": "📐 الإحصاء التطبيقي",
                "description": "فهم الإحصاء واستخدامه لتفسير البيانات والوصول إلى استنتاجات صحيحة.",
                "objectives": [
                    "Mean / Median / Mode",
                    "Variance / Standard Deviation",
                    "Distributions",
                    "Probability",
                    "Sampling",
                    "Correlation",
                    "Confidence Intervals",
                    "Hypothesis Testing و P-value"
                ],
                "practical_task": "على مجموعة بيانات صغيرة احسب: Mean + Median + Standard Deviation + Correlation، ثم اكتب استنتاجًا من النتائج.",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.youtube.com/watch?v=xxpc-HPKN28",
                "questions": [
                    {"text": "ما هو Mean؟", "options": {"A": "أكبر قيمة", "B": "المتوسط الحسابي", "C": "أصغر قيمة", "D": "المدى"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما هو Median؟", "options": {"A": "القيمة الوسطى بعد ترتيب البيانات", "B": "مجموع البيانات", "C": "أكبر قيمة", "D": "الانحراف المعياري"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما هو Mode؟", "options": {"A": "المتوسط", "B": "الوسيط", "C": "القيمة الأكثر تكرارًا", "D": "المدى"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ماذا يقيس Standard Deviation؟", "options": {"A": "عدد الصفوف", "B": "العلاقة بين متغيرين", "C": "المتوسط", "D": "مدى تشتت البيانات حول المتوسط"}, "correct": "D", "difficulty": "easy"},
                    {"text": "إذا كانت القيم 2, 4, 6، فما Mean؟", "options": {"A": "3", "B": "4", "C": "5", "D": "6"}, "correct": "B", "difficulty": "easy"},
                    {"text": "إذا كانت البيانات 1, 2, 3, 100، فأي مقياس أقل تأثرًا بالقيمة المتطرفة؟", "options": {"A": "Median", "B": "Mean", "C": "Variance", "D": "Standard Deviation"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Correlation؟", "options": {"A": "إثبات أن أحد المتغيرين سبب الآخر", "B": "قياس العلاقة بين متغيرين", "C": "حذف القيم المتطرفة", "D": "حساب المتوسط"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كان Correlation قريبًا من +1 فهذا يعني:", "options": {"A": "لا توجد علاقة", "B": "علاقة سالبة قوية", "C": "علاقة موجبة قوية", "D": "البيانات خاطئة"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما الهدف من Sampling؟", "options": {"A": "دراسة عينة تمثل مجتمعًا أكبر", "B": "حذف البيانات", "C": "تغيير المتوسط", "D": "إنشاء Dashboard"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Probability؟", "options": {"A": "المتوسط", "B": "احتمال حدوث حدث", "C": "الانحراف", "D": "المدى"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما وظيفة Confidence Interval؟", "options": {"A": "تحديد نطاق معقول لمعلمة المجتمع", "B": "حذف القيم", "C": "ترتيب البيانات", "D": "إنشاء SQL Query"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان p-value أقل من مستوى الدلالة المحدد، فعادةً:", "options": {"A": "نرفض Null Hypothesis", "B": "نثبت أنها صحيحة دائمًا", "C": "نحذف البيانات", "D": "نحسب Mean"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا تعني Correlation بالضرورة Causation؟", "options": {"A": "لأن البيانات لا تحتوي أرقامًا", "B": "لأن وجود علاقة لا يثبت أن أحد المتغيرين سبب الآخر", "C": "لأن Mean غير موجود", "D": "لأن Median أكبر"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لديك بيانات شديدة الانحراف بسبب Outliers. أي مقياس مركزي مناسب غالبًا؟", "options": {"A": "Median", "B": "Mean فقط", "C": "Maximum", "D": "Variance"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا ارتفعت مبيعات الإعلانات وارتفعت المبيعات في الوقت نفسه، ما الاستنتاج الصحيح؟", "options": {"A": "الإعلان تسبب بالتأكيد في الزيادة", "B": "لا توجد علاقة إطلاقًا", "C": "توجد علاقة محتملة، لكن يجب تحليل السببية والعوامل الأخرى", "D": "يجب حذف البيانات"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5
            # ==========================================
            {
                "stage_number": 5,
                "title": "🐍 التحليل والاستكشاف باستخدام Python (EDA)",
                "description": "استخدام Python لتحضير البيانات وتنظيفها واستكشافها وتحليلها بصريًا.",
                "objectives": [
                    "Python الأساسي المطلوب للتحليل",
                    "NumPy",
                    "Pandas",
                    "Data Cleaning",
                    "Data Manipulation",
                    "Exploratory Data Analysis",
                    "Matplotlib و Seaborn",
                    "استخراج Insights"
                ],
                "practical_task": "Dataset حقيقي: Read → Clean → Explore → Visualize → Find Insights",
                "youtube_ar": "https://www.youtube.com/watch?v=o3paqBstP9Y",
                "youtube_en": "https://www.youtube.com/watch?v=wUSDVGivd-8",
                "questions": [
                    {"text": "ما المكتبة الأشهر للتعامل مع DataFrames؟", "options": {"A": "Pandas", "B": "Flask", "C": "Requests", "D": "Scapy"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المكتبة المستخدمة للحسابات والمصفوفات الرقمية؟", "options": {"A": "Django", "B": "NumPy", "C": "BeautifulSoup", "D": "Selenium"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المقصود بـ DataFrame؟", "options": {"A": "قاعدة بيانات كاملة", "B": "صفحة ويب", "C": "هيكل جدولي للبيانات في Pandas", "D": "ملف نصي فقط"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الأمر الشائع لقراءة CSV؟", "options": {"A": "pd.open_csv()", "B": "pandas.csv()", "C": "pd.read_csv()", "D": "csv.pandas()"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الهدف من EDA؟", "options": {"A": "استكشاف البيانات وفهم الأنماط والمشكلات", "B": "إنشاء نظام تشغيل", "C": "بناء شبكة", "D": "تشفير الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الدالة التي تعطي ملخصًا إحصائيًا للبيانات؟", "options": {"A": "head()", "B": "describe()", "C": "delete()", "D": "graph()"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الدالة التي تعرض أول صفوف DataFrame؟", "options": {"A": "head()", "B": "firstrow()", "C": "start()", "D": "beginning()"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Missing Values؟", "options": {"A": "قيم مفقودة أو فارغة", "B": "قيم مكررة فقط", "C": "قيم صحيحة", "D": "أعمدة جديدة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي خيار مناسب لاكتشاف القيم المفقودة في Pandas؟", "options": {"A": "df.empty_values()", "B": "df.isnull()", "C": "df.find_missing()", "D": "df.delete_null()"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا يتم تنظيف البيانات قبل التحليل؟", "options": {"A": "لتغيير اسم الملف", "B": "لتحسين جودة النتائج وتقليل الأخطاء", "C": "لتقليل حجم الشاشة", "D": "لإنشاء نظام تشغيل"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي مكتبة تستخدم غالبًا لإنشاء الرسوم البيانية؟", "options": {"A": "Matplotlib", "B": "SQL", "C": "Flask", "D": "NumPy فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك عمود Salary يحتوي على قيم مفقودة. ما أول خطوة مناسبة؟", "options": {"A": "استبدالها عشوائيًا", "B": "حذف قاعدة البيانات", "C": "فهم سبب ونسبة القيم المفقودة ثم اختيار المعالجة المناسبة", "D": "تجاهلها دائمًا"}, "correct": "C", "difficulty": "hard"},
                    {"text": "ما الهدف من GroupBy في Pandas؟", "options": {"A": "تجميع البيانات حسب فئة لتنفيذ عمليات تحليلية", "B": "حذف الأعمدة", "C": "إنشاء ملف PDF", "D": "تحميل Python"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان لديك Outliers في Salary، ما التصرف الأفضل؟", "options": {"A": "حذفها تلقائيًا دائمًا", "B": "تجاهلها دائمًا", "C": "فحصها وفهم سببها قبل اتخاذ قرار", "D": "تحويلها إلى نص"}, "correct": "C", "difficulty": "hard"},
                    {"text": "أي تسلسل يمثل EDA بشكل أفضل؟", "options": {"A": "Visualization → Delete → Read", "B": "Read → Inspect → Clean → Explore → Visualize → Insights", "C": "SQL → Shutdown → Delete", "D": "Chart → Database → Operating System"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6
            # ==========================================
            {
                "stage_number": 6,
                "title": "📈 تصور البيانات و Power BI",
                "description": "تحويل البيانات والتحليلات إلى Dashboards وتقارير تفاعلية تساعد على اتخاذ القرار.",
                "objectives": [
                    "Data Visualization",
                    "Power Query",
                    "Data Modeling",
                    "Relationships",
                    "DAX الأساسي",
                    "KPIs",
                    "Dashboards",
                    "Data Storytelling"
                ],
                "practical_task": "Dataset مبيعات: Power Query → Data Model → Measures → KPIs → Charts → Interactive Dashboard",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/powerplatform/power-bi/",
                "youtube_en": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/",
                "questions": [
                    {"text": "ما الهدف الأساسي من Data Visualization؟", "options": {"A": "جعل البيانات أكثر صعوبة", "B": "عرض البيانات بطريقة تسهل فهمها", "C": "حذف البيانات", "D": "إنشاء قاعدة بيانات"}, "correct": "B", "difficulty": "easy"},
                    {"text": "Power BI هو:", "options": {"A": "نظام تشغيل", "B": "لغة برمجة", "C": "منصة لتحليل البيانات وإنشاء التقارير والتصورات", "D": "برنامج مضاد فيروسات"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الأداة المستخدمة داخل Power BI لتحويل وتنظيف البيانات؟", "options": {"A": "Power Query", "B": "PowerPoint", "C": "Word", "D": "Paint"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ KPI؟", "options": {"A": "Key Performance Indicator", "B": "Key Python Interface", "C": "Known Power Input", "D": "Kernel Processing Index"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Dashboard؟", "options": {"A": "عرض مؤشرات وتحليلات مهمة في مكان واحد", "B": "حذف البيانات", "C": "إنشاء نظام تشغيل", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Data Modeling؟", "options": {"A": "تصميم العلاقات والبنية المناسبة للبيانات", "B": "تغيير ألوان Windows", "C": "حذف كل الجداول", "D": "إنشاء بريد إلكتروني"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة Relationship بين جدولين؟", "options": {"A": "ربط البيانات المرتبطة بين الجداول", "B": "حذف البيانات", "C": "تحويل الصور إلى نص", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما لغة الصيغ المستخدمة في Power BI لإنشاء Measures؟", "options": {"A": "HTML", "B": "CSS", "C": "DAX", "D": "Bash"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما فائدة Slicer؟", "options": {"A": "تصفية البيانات تفاعليًا في التقرير", "B": "حذف البيانات", "C": "إنشاء قاعدة بيانات", "D": "كتابة Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي رسم مناسب غالبًا لمقارنة المبيعات بين المناطق؟", "options": {"A": "Bar / Column Chart", "B": "Scatter فقط", "C": "Gauge فقط", "D": "Map دائمًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب تجنب وضع عدد كبير جدًا من الرسوم في Dashboard؟", "options": {"A": "لأنه قد يصعب فهم المعلومات الأساسية", "B": "لأنه يمنع تشغيل Power BI", "C": "لأنه يحذف البيانات", "D": "لأنه يغير SQL"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك Sales و Cost وتريد KPI للربح. ما الأفضل؟", "options": {"A": "تجاهل Cost", "B": "إنشاء Measure مثل Profit = Sales - Cost", "C": "حذف Sales", "D": "استخدام صورة"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا كانت لديك جداول Sales و Customers و Products، فما التصميم الشائع للتحليل؟", "options": {"A": "نموذج بيانات بعلاقات مناسبة بين الجداول", "B": "وضع كل شيء في Chart", "C": "حذف المفاتيح", "D": "عدم وجود علاقات"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الفرق الأساسي بين Measure و Calculated Column؟", "options": {"A": "Measure تحسب عادةً حسب سياق التقرير، بينما Column تُحسب على مستوى الصفوف", "B": "لا يوجد فرق", "C": "Column تستخدم للرسم فقط", "D": "Measure لا تستخدم الأرقام"}, "correct": "A", "difficulty": "hard"},
                                        {"text": "Dashboard جيد يجب أن:", "options": {"A": "يحتوي أكبر عدد ممكن من الألوان والرسوم", "B": "يعرض كل البيانات دون ترتيب", "C": "يركز على KPIs و Insights المهمة ويجعل القرار أسهل", "D": "يخفي الأرقام"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7
            # ==========================================
            {
                "stage_number": 7,
                "title": "💼 Business Analytics",
                "description": "فهم الأعمال وتحويل نتائج تحليل البيانات إلى قرارات وتوصيات عملية.",
                "objectives": [
                    "Business Questions",
                    "KPIs",
                    "أنواع Business Analytics",
                    "Segmentation",
                    "Trends",
                    "مقارنة الأداء",
                    "A/B Testing بشكل أساسي",
                    "Recommendations"
                ],
                "practical_task": "خذ Dashboard أو Dataset وأجب: ما المشكلة؟ → ماذا تقول البيانات؟ → لماذا؟ → ما القرار المقترح؟",
                "youtube_ar": "https://www.simplilearn.com/fundamentals-of-business-analytics-free-course-skillup",
                "youtube_en": "https://www.youtube.com/watch?v=rkyzSU9I8Hk",
                "questions": [
                    {"text": "ما المقصود بـ KPI؟", "options": {"A": "مؤشر يستخدم لقياس الأداء", "B": "لغة برمجة", "C": "قاعدة بيانات", "D": "ملف نصي"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Business Analytics يركز على:", "options": {"A": "كتابة أنظمة التشغيل", "B": "استخدام البيانات لفهم وتحسين الأعمال", "C": "إصلاح الأجهزة", "D": "تصميم الشبكات"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما السؤال الأساسي في Descriptive Analytics؟", "options": {"A": "ماذا حدث؟", "B": "ماذا سيحدث؟", "C": "ماذا يجب أن نفعل؟", "D": "لماذا حدث؟"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Customer Segmentation؟", "options": {"A": "حذف العملاء", "B": "تقسيم العملاء إلى مجموعات ذات خصائص مشتركة", "C": "تغيير أسماء العملاء", "D": "تشفير العملاء"}, "correct": "B", "difficulty": "easy"},
                    {"text": "Recommendation تعني:", "options": {"A": "بيانات خام", "B": "توصية مبنية على التحليل", "C": "جدول SQL", "D": "رسم فقط"}, "correct": "B", "difficulty": "easy"},
                    {"text": "إذا أرادت الشركة معرفة سبب انخفاض المبيعات، تستخدم:", "options": {"A": "Diagnostic Analytics", "B": "Descriptive فقط", "C": "Prescriptive فقط", "D": "Data Entry"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا أرادت الشركة توقع الطلب القادم، فهذا:", "options": {"A": "Descriptive", "B": "Predictive", "C": "Diagnostic", "D": "Manual"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا أرادت الشركة تحديد أفضل إجراء بناءً على التحليل، فهذا:", "options": {"A": "Prescriptive Analytics", "B": "Descriptive", "C": "Diagnostic", "D": "Data Cleaning"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أهمية KPI الجيد؟", "options": {"A": "يقيس جانبًا مهمًا من أداء العمل", "B": "يزيد حجم البيانات فقط", "C": "يمنع التحليل", "D": "يحذف البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا ارتفع عدد العملاء لكن انخفض متوسط قيمة الطلب، فما الأفضل؟", "options": {"A": "النظر إلى المؤشرين معًا وفهم السبب", "B": "تجاهل متوسط الطلب", "C": "إعلان نجاح كامل", "D": "حذف العملاء"}, "correct": "A", "difficulty": "medium"},
                    {"text": "A/B Testing يستخدم غالبًا لـ:", "options": {"A": "مقارنة نسختين لمعرفة أيهما يحقق نتيجة أفضل", "B": "حذف البيانات", "C": "إنشاء SQL Server", "D": "بناء شبكة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "المبيعات انخفضت 10%، لكن عدد العملاء ارتفع 20%. ما التحليل الأفضل؟", "options": {"A": "النظر إلى عدد العملاء فقط", "B": "تحليل Average Order Value و Customer Segments والعوامل المؤثرة", "C": "حذف البيانات", "D": "تغيير الرسم فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ما التوصية الأفضل بناءً على Insight؟", "options": {"A": "\"البيانات جميلة\"", "B": "\"عدد الصفوف 20,000\"", "C": "\"العملاء الجدد في المنطقة A لديهم معدل شراء أعلى؛ نقترح زيادة الحملة هناك واختبار أثرها\"", "D": "\"يوجد عمود Sales\""}, "correct": "C", "difficulty": "hard"},
                    {"text": "لماذا يجب ربط التحليل بأهداف العمل؟", "options": {"A": "حتى تكون النتائج قابلة للاستخدام في اتخاذ القرار", "B": "لأن Excel يتطلب ذلك", "C": "لتقليل عدد الأعمدة", "D": "لتغيير شكل Dashboard"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا أظهر A/B Test أن النسخة B أفضل، ما الخطوة المهنية التالية؟", "options": {"A": "إعلان السببية دون فحص", "B": "تجاهل النتائج", "C": "فحص النتائج إحصائيًا وسياق التجربة ثم اتخاذ القرار", "D": "حذف النسخة A فورًا"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8
            # ==========================================
            {
                "stage_number": 8,
                "title": "🚀 مشاريع تحليل بيانات واقعية",
                "description": "تحويل المهارات التي تعلمتها إلى مشاريع حقيقية قابلة للعرض في Portfolio.",
                "objectives": [
                    "اختيار Dataset ومشكلة حقيقية",
                    "Data Cleaning",
                    "SQL Analysis",
                    "Python EDA",
                    "Visualization",
                    "Power BI",
                    "Business Insights",
                    "توثيق المشروع"
                ],
                "practical_task": "إنجاز 3 مشاريع Portfolio رئيسية: (1) Excel / Business Analysis (2) SQL / Data Exploration (3) Python + Power BI / End-to-End Analysis",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.youtube.com/watch?v=qfyynHBFOsM",
                "questions": [
                    {"text": "ما الهدف من Portfolio؟", "options": {"A": "عرض المهارات والمشاريع العملية", "B": "تخزين كلمات المرور", "C": "تشغيل SQL Server", "D": "تثبيت Windows"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أول خطوة جيدة عند بدء مشروع تحليل بيانات؟", "options": {"A": "اختيار لون Dashboard", "B": "فهم المشكلة والهدف", "C": "كتابة 1000 سطر Python", "D": "إنشاء CV"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Data Cleaning؟", "options": {"A": "تحسين جودة البيانات ومعالجة المشكلات فيها", "B": "حذف كل البيانات", "C": "تصميم موقع", "D": "إنشاء بريد"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا تستخدم GitHub في Portfolio؟", "options": {"A": "لعرض وإدارة الكود والمشاريع", "B": "لتصميم Power BI", "C": "لتحليل SQL تلقائيًا", "D": "لاستبدال Excel"}, "correct": "A", "difficulty": "easy"},
                    {"text": "README الجيد يشرح:", "options": {"A": "المشروع وطريقته ونتائجه", "B": "كلمة مرور GitHub", "C": "إعدادات Windows", "D": "مواصفات الكمبيوتر فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "مشروع SQL جيد يجب أن يظهر:", "options": {"A": "فقط صورة SQL", "B": "القدرة على استخراج وتحليل البيانات", "C": "نظام تشغيل", "D": "تصميم Logo"}, "correct": "B", "difficulty": "medium"},
                    {"text": "مشروع Python EDA يجب أن يتضمن:", "options": {"A": "استكشاف وتنظيف وتحليل وتصوير البيانات", "B": "لعبة فقط", "C": "نظام تسجيل دخول فقط", "D": "صفحة HTML فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Dashboard المشروع يجب أن يركز على:", "options": {"A": "كل البيانات دون ترتيب", "B": "KPIs و Insights المهمة", "C": "الأكواد فقط", "D": "الصور فقط"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة توثيق المشروع؟", "options": {"A": "جعل الآخرين يفهمون المشكلة والمنهج والنتائج", "B": "زيادة حجم الملف فقط", "C": "حذف البيانات", "D": "منع استخدام GitHub"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي مشروع أقوى للـ Data Analyst؟", "options": {"A": "مشروع يعرض Dataset فقط", "B": "مشروع يوضح Problem → Cleaning → Analysis → Visualization → Insights", "C": "صورة Excel فقط", "D": "ملف فارغ"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نستخدم أكثر من أداة في بعض المشاريع؟", "options": {"A": "لأن كل أداة قد تخدم جزءًا مختلفًا من سير العمل", "B": "لإظهار عدد أكبر من البرامج فقط", "C": "لأن Excel لا يعمل", "D": "لأن SQL غير مفيد"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل مشروع Portfolio من ناحية إظهار مهارات متعددة؟", "options": {"A": "ملف بيانات خام", "B": "مشروع يجمع SQL و Python و Power BI مع Business Insights", "C": "Screenshot واحد", "D": "ملف Word فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا اكتشفت خطأ في البيانات أثناء المشروع، ما التصرف الأفضل؟", "options": {"A": "إخفاؤه", "B": "توثيقه ومعالجته بطريقة مناسبة وشرح أثره", "C": "حذف المشروع", "D": "تجاهله دائمًا"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ما الذي يجعل مشروعًا يبدو احترافيًا؟", "options": {"A": "كثرة الرسوم فقط", "B": "وجود مشكلة واضحة، تحليل منطقي، نتائج، توصيات وتوثيق جيد", "C": "استخدام أكبر عدد من المكتبات", "D": "طول الكود"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا كان لديك مشروع ممتاز لكن لا يعرف القارئ ما المشكلة التي يحلها، ما المشكلة الأساسية؟", "options": {"A": "نقص في Business Context وشرح المشروع", "B": "نقص في Python", "C": "نقص في Excel", "D": "حجم Dataset"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9
            # ==========================================
            {
                "stage_number": 9,
                "title": "🎓 Portfolio & Job Ready",
                "description": "تحويل المهارات والمشاريع إلى ملف مهني جاهز للتقديم على وظائف Data Analyst.",
                "objectives": [
                    "GitHub Portfolio",
                    "README احترافي",
                    "Data Analyst CV",
                    "LinkedIn",
                    "عرض المشاريع",
                    "Case Studies",
                    "Technical Interviews",
                    "SQL Interview Questions",
                    "التقديم على الوظائف"
                ],
                "practical_task": "إنشاء: GitHub Portfolio + 3 Projects + CV + LinkedIn + Case Study، ثم الاستعداد للمقابلات والتقديم على الوظائف.",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.youtube.com/watch?v=wQQR60KtnFY",
                "questions": [
                    {"text": "ما الهدف من CV لمحلل البيانات؟", "options": {"A": "عرض المهارات والخبرات والمشاريع المرتبطة بالوظيفة", "B": "كتابة كل شيء عن الشخص", "C": "عرض كلمات المرور", "D": "شرح نظام التشغيل"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة LinkedIn؟", "options": {"A": "منصة مهنية لبناء شبكة وعرض الملف المهني", "B": "برنامج تحليل بيانات", "C": "قاعدة بيانات", "D": "لغة برمجة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يجب أن يحتوي Portfolio؟", "options": {"A": "مشاريع ذات صلة بالمهارات المطلوبة", "B": "صور شخصية فقط", "C": "ألعاب فقط", "D": "ملفات عشوائية"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة README؟", "options": {"A": "شرح المشروع", "B": "حذف المشروع", "C": "تشغيل Power BI", "D": "كتابة SQL تلقائيًا"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Technical Interview؟", "options": {"A": "مقابلة لاختبار المعرفة والمهارات التقنية", "B": "مقابلة اجتماعية فقط", "C": "اختبار لغة فقط", "D": "مقابلة شخصية فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم شيء عند عرض مشروع في مقابلة؟", "options": {"A": "شرح المشكلة والمنهج والنتائج والتوصيات", "B": "قراءة الكود كاملًا", "C": "عرض عدد الملفات", "D": "الحديث عن الألوان"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا تعتبر SQL مهمة لوظيفة Data Analyst؟", "options": {"A": "لأنها تستخدم لاستخراج وتحليل البيانات من قواعد البيانات", "B": "لأنها لغة تصميم مواقع", "C": "لأنها نظام تشغيل", "D": "لأنها بديل لـ Python دائمًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "CV مناسب للـ ATS يجب أن يكون:", "options": {"A": "واضحًا ويستخدم كلمات ومهارات مرتبطة بالوظيفة", "B": "مليئًا بالصور", "C": "عبارة عن صورة فقط", "D": "بدون عناوين"}, "correct": "A", "difficulty": "medium"},
                    {"text": "عند التقديم لوظيفة Data Analyst، الأفضل:", "options": {"A": "إرسال نفس CV لكل الوظائف دون قراءة الوصف", "B": "مواءمة CV مع متطلبات الوظيفة", "C": "حذف المشاريع", "D": "حذف المهارات التقنية"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة لإثبات أنك تعرف Power BI؟", "options": {"A": "كتابة Power BI فقط في CV", "B": "عرض Dashboard حقيقي ضمن Portfolio", "C": "ذكر اسم البرنامج فقط", "D": "مشاهدة فيديو"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الأفضل في GitHub Portfolio؟", "options": {"A": "مشاريع منظمة مع README واضح", "B": "ملفات بدون أسماء", "C": "أكواد غير مشروحة", "D": "مجلد فارغ"}, "correct": "A", "difficulty": "medium"},
                    {"text": "في مقابلة سألك المحاور: \"كيف ستتعامل مع Dataset جديد؟\" ما الإجابة الأقوى؟", "options": {"A": "أبدأ بالرسم مباشرة", "B": "أفهم Business Problem ثم أفحص البيانات وأنظفها وأحللها وأتحقق من النتائج وأقدم Insights", "C": "أستخدم Python فقط", "D": "أستخدم Power BI فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا سألك المحاور عن مشروعك، أي عرض أفضل؟", "options": {"A": "\"استخدمت Pandas.\"", "B": "\"استخدمت Excel.\"", "C": "\"كانت المشكلة كذا، استخدمت البيانات كذا، أجريت التحليل، اكتشفت كذا، وأوصيت بكذا.\"", "D": "\"المشروع كان طويلًا.\""}, "correct": "C", "difficulty": "hard"},
                    {"text": "إذا لم تعرف إجابة سؤال SQL في المقابلة، ما التصرف المهني الأفضل؟", "options": {"A": "اختلاق إجابة", "B": "توضيح ما تعرفه ومحاولة التفكير في الحل بشكل منطقي", "C": "مغادرة المقابلة", "D": "تغيير الموضوع"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ما العلامة الأقوى على أنك Job Ready كمحلل بيانات مبتدئ؟", "options": {"A": "مشاهدة عشرات الكورسات", "B": "معرفة أسماء أدوات كثيرة", "C": "القدرة على حل مشكلة بيانات كاملة وتحويلها إلى Insight و Recommendation وعرضها في Portfolio", "D": "امتلاك أكبر عدد من الشهادات فقط"}, "correct": "C", "difficulty": "hard"}
                ]
            }
        ]
    }
]