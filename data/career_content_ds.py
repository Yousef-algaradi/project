# data/career_content_ds.py
# ==========================================
# بنك محتوى مسار "عالم بيانات (Data Scientist)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

DATA_SCIENTIST_PATHS = [
    {
        "major_key": "data_science",
        "slug": "data-scientist",
        "title": "عالم بيانات (Data Scientist)",
        "description": "مسار متقدم لتصبح عالم بيانات محترف. يغطي الإحصاء، Python، SQL، Machine Learning، Deep Learning، MLOps، ومشاريع واقعية.",
        "icon": "🤖",
        "difficulty": "متقدم",
        "estimated_hours": 250,
        "order_index": 2,
        "stages": [
            # ==========================================
            # المرحلة 1: أساسيات علم البيانات
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات علم البيانات والمنهجية",
                "description": "بناء فهم صحيح لدور عالم البيانات، دورة حياة مشروع Data Science، وطريقة تحويل المشكلة التجارية إلى مشكلة بيانات قابلة للحل.",
                "objectives": [
                    "مفهوم Data Science و Data Scientist",
                    "أنواع البيانات ومصادرها",
                    "Data Science Lifecycle",
                    "CRISP-DM",
                    "Business Understanding",
                    "أنواع التحليل الأربعة",
                    "صياغة الأسئلة والفرضيات",
                    "Data Ethics و Data Privacy"
                ],
                "practical_task": "اختر مشكلة حقيقية مثل: لماذا انخفضت مبيعات متجر إلكتروني؟ ثم اكتب: Business Problem → Data Needed → Questions → Analysis → Expected Insight → Recommendation",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.coursera.org/professional-certificates/ibm-data-science",
                "questions": [
                    {"text": "ما المقصود بـ Data Science؟", "options": {"A": "تصميم الشبكات", "B": "استخدام البيانات والأساليب الإحصائية والحاسوبية لاستخراج المعرفة", "C": "إدارة أنظمة التشغيل", "D": "تصميم المواقع"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي عنصر يمثل بيانات خام؟", "options": {"A": "توصية بزيادة الأسعار", "B": "قرار إداري", "C": "رسم بياني نهائي", "D": "سجل مبيعات العملاء"}, "correct": "D", "difficulty": "easy"},
                    {"text": "ما الهدف الأساسي من Business Understanding؟", "options": {"A": "فهم المشكلة والهدف التجاري", "B": "اختيار لغة البرمجة", "C": "تثبيت Python", "D": "إنشاء قاعدة بيانات فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي تخصص يركز أساساً على بناء النماذج التنبؤية؟", "options": {"A": "Graphic Design", "B": "Networking", "C": "Data Science", "D": "Technical Support"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Dataset؟", "options": {"A": "برنامج", "B": "شبكة", "C": "مجموعة منظمة من البيانات", "D": "نظام تشغيل"}, "correct": "C", "difficulty": "easy"},
                    {"text": "شركة تريد معرفة سبب ارتفاع إلغاء الطلبات. هذا أقرب إلى:", "options": {"A": "Diagnostic Analytics", "B": "Predictive Analytics", "C": "Descriptive Analytics", "D": "Prescriptive Analytics"}, "correct": "A", "difficulty": "medium"},
                    {"text": "تريد الشركة توقع المبيعات الشهر القادم. النوع المناسب هو:", "options": {"A": "Diagnostic", "B": "Descriptive", "C": "Prescriptive", "D": "Predictive"}, "correct": "D", "difficulty": "medium"},
                    {"text": "أي ترتيب منطقي لمشروع Data Science؟", "options": {"A": "Model → Problem → Data", "B": "Problem → Data → Analysis → Model/Insight → Decision", "C": "Dashboard → Model → Problem", "D": "Code → Deployment → Question"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا يجب تحديد المشكلة قبل اختيار النموذج؟", "options": {"A": "لتحديد الهدف ونوع الحل المناسب", "B": "لتقليل حجم البيانات", "C": "لتغيير نظام التشغيل", "D": "لإنشاء حساب GitHub"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان النموذج دقيقًا لكنه لا يحل المشكلة التجارية، فالمشكلة غالبًا في:", "options": {"A": "CPU", "B": "Python", "C": "Business Understanding", "D": "RAM"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما الهدف من CRISP-DM؟", "options": {"A": "إدارة الشبكات", "B": "تنظيم دورة مشروع تحليل البيانات", "C": "كتابة HTML", "D": "تصميم قواعد البيانات فقط"}, "correct": "B", "difficulty": "medium"},
                    {"text": "شركة تريد معرفة أي العملاء أكثر عرضة لترك الخدمة. المشكلة الأساسية هي:", "options": {"A": "Classification/Predictive Problem", "B": "Visualization Problem فقط", "C": "Database Backup", "D": "Data Entry"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا وجدت علاقة بين زيادة الإعلانات والمبيعات، فهذا لا يعني بالضرورة أن:", "options": {"A": "هناك ارتباط", "B": "هناك بيانات", "C": "الإعلان سبب الزيادة", "D": "يمكن تحليل العلاقة"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لديك Dataset ضخمة لكن لا تعرف ما القرار المطلوب اتخاذه. ما الخطوة الصحيحة؟", "options": {"A": "تدريب Neural Network", "B": "تحديد Business Question", "C": "حذف نصف البيانات", "D": "نشر النموذج"}, "correct": "B", "difficulty": "hard"},
                    {"text": "أفضل مخرج لعالم البيانات ليس مجرد Model Accuracy، بل:", "options": {"A": "عدد الأسطر البرمجية", "B": "حجم Dataset", "C": "اسم المكتبة", "D": "نتيجة قابلة للاستخدام لحل مشكلة حقيقية"}, "correct": "D", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2: الإحصاء والاحتمالات
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ الرياضيات والإحصاء والاحتمالات",
                "description": "بناء الأساس الرياضي والإحصائي اللازم لفهم البيانات وتقييم النماذج.",
                "objectives": [
                    "Mean / Median / Mode",
                    "Variance / Standard Deviation",
                    "Probability",
                    "Distributions",
                    "Sampling",
                    "Confidence Intervals",
                    "Hypothesis Testing و p-value",
                    "Correlation vs Causation",
                    "Linear Algebra basics"
                ],
                "practical_task": "استخدم Dataset للمبيعات واحسب: Mean, Median, Standard Deviation, Quartiles, Correlation. ثم اكتب 3 Insights من النتائج.",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.youtube.com/watch?v=xxpc-HPKN28",
                "questions": [
                    {"text": "متوسط 10 و20 و30 هو:", "options": {"A": "10", "B": "20", "C": "25", "D": "30"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي مقياس يتأثر بشدة بالقيم الشاذة؟", "options": {"A": "Mean", "B": "Median", "C": "Mode", "D": "Quartile"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Standard Deviation يقيس:", "options": {"A": "عدد الصفوف", "B": "حجم الملف", "C": "تشتت البيانات", "D": "عدد الأعمدة"}, "correct": "C", "difficulty": "easy"},
                    {"text": "إذا كانت كل القيم متساوية فإن Standard Deviation يساوي:", "options": {"A": "1", "B": "100", "C": "-1", "D": "0"}, "correct": "D", "difficulty": "easy"},
                    {"text": "Probability لقيمة مستحيلة تساوي:", "options": {"A": "0", "B": "0.5", "C": "1", "D": "100"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كان Mean أكبر بكثير من Median فهذا قد يشير إلى:", "options": {"A": "توزيع مائل لليسار", "B": "توزيع مائل لليمين", "C": "عدم وجود بيانات", "D": "ارتباط كامل"}, "correct": "B", "difficulty": "medium"},
                    {"text": "Correlation = 0.9 تعني:", "options": {"A": "علاقة خطية موجبة قوية", "B": "لا توجد بيانات", "C": "السببية مؤكدة", "D": "النموذج مثالي"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهدف من Confidence Interval؟", "options": {"A": "حذف البيانات", "B": "تقدير نطاق محتمل لمعلمة المجتمع", "C": "زيادة حجم Dataset", "D": "اختيار لغة البرمجة"}, "correct": "B", "difficulty": "medium"},
                    {"text": "p-value صغيرة جدًا قد تعني:", "options": {"A": "وجود دليل ضد Null Hypothesis", "B": "أن البيانات خاطئة دائمًا", "C": "أن Mean يساوي صفرًا", "D": "أن النموذج غير قابل للتدريب"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Sampling؟", "options": {"A": "لأن دراسة المجتمع الكامل قد تكون مكلفة أو غير عملية", "B": "لتغيير البيانات", "C": "لتقليل دقة النموذج", "D": "لحذف القيم الصحيحة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي عملية تناسب Matrix؟", "options": {"A": "جمع نصوص HTML", "B": "تمثيل البيانات في صورة صفوف وأعمدة", "C": "ضغط الملفات", "D": "إدارة البريد"}, "correct": "B", "difficulty": "medium"},
                    {"text": "Dataset فيها Outliers شديدة. أي مقياس مركزي أكثر مقاومة؟", "options": {"A": "Mean", "B": "Variance", "C": "Median", "D": "Standard Error"}, "correct": "C", "difficulty": "hard"},
                    {"text": "إذا كان معامل الارتباط 0.02، فالاستنتاج الصحيح هو:", "options": {"A": "لا يوجد بالضرورة ارتباط خطي قوي", "B": "توجد سببية مؤكدة", "C": "النموذج 98% دقيق", "D": "البيانات غير صالحة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا تكفي Accuracy وحدها في حالة Class Imbalance؟", "options": {"A": "لأنها قد تكون مرتفعة رغم ضعف اكتشاف الفئة المهمة", "B": "لأنها لا تحسب أي شيء", "C": "لأنها تستخدم Python", "D": "لأنها تحتاج Excel"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الفرق الأساسي بين Correlation و Causation؟", "options": {"A": "لا يوجد فرق", "B": "Correlation تثبت السبب", "C": "Causation تعني مجرد تشابه", "D": "Correlation لا تثبت أن أحد المتغيرين سبب الآخر"}, "correct": "D", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3: Python
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ Python لعلم البيانات",
                "description": "إتقان Python بالقدر المطلوب لبناء حلول Data Science والعمل مع البيانات والمكتبات العلمية.",
                "objectives": [
                    "Python syntax",
                    "Variables / Data Types",
                    "Conditions / Loops / Functions",
                    "Lists / Tuples / Dictionaries / Sets",
                    "File handling",
                    "Jupyter / Google Colab",
                    "NumPy basics",
                    "Pandas basics"
                ],
                "practical_task": "أنشئ Notebook يقوم بـ: قراءة CSV، تنظيف أسماء الأعمدة، حساب الإحصائيات، إنشاء دوال بسيطة، استخدام Pandas و NumPy، إنشاء 3 رسوم بيانية.",
                "youtube_ar": "https://www.youtube.com/watch?v=o3paqBstP9Y",
                "youtube_en": "https://www.youtube.com/watch?v=LHBE6Q9XlzI",
                "questions": [
                    {"text": "ما نوع [1,2,3]؟", "options": {"A": "Tuple", "B": "List", "C": "Set", "D": "Dictionary"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي كلمة تستخدم لتعريف Function؟", "options": {"A": "def", "B": "function", "C": "func", "D": "define"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ناتج len([10,20,30]) هو:", "options": {"A": "2", "B": "10", "C": "30", "D": "3"}, "correct": "D", "difficulty": "easy"},
                    {"text": "أي مكتبة تستخدم غالبًا للتعامل مع DataFrames؟", "options": {"A": "Flask", "B": "Requests", "C": "Pandas", "D": "Socket"}, "correct": "C", "difficulty": "easy"},
                    {"text": "NumPy تستخدم أساسًا في:", "options": {"A": "العمليات العددية والمصفوفات", "B": "تصميم المواقع", "C": "البريد الإلكتروني", "D": "إدارة المستخدمين"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما ناتج: x=5; x+=3؟", "options": {"A": "2", "B": "8", "C": "15", "D": "53"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي بنية مناسبة لتخزين key-value؟", "options": {"A": "List", "B": "Tuple", "C": "Dictionary", "D": "String"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما فائدة Function؟", "options": {"A": "إعادة استخدام منطق برمجي", "B": "حذف Python", "C": "إنشاء نظام تشغيل", "D": "ضغط البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي أمر يقرأ CSV في Pandas؟", "options": {"A": "pd.open()", "B": "pd.read_csv()", "C": "pd.csv()", "D": "pd.load_csv_file()"}, "correct": "B", "difficulty": "medium"},
                    {"text": "df.head() يستخدم عادة لـ:", "options": {"A": "حذف البيانات", "B": "عرض أول صفوف", "C": "تدريب نموذج", "D": "تغيير نوع الملف"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة Jupyter Notebook؟", "options": {"A": "تشغيل الكود مع توثيق وتحليل تفاعلي", "B": "استبدال نظام التشغيل", "C": "بناء شبكات", "D": "إدارة قواعد البيانات فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان لديك 1,000,000 صف، لماذا Pandas/NumPy مفيدان؟", "options": {"A": "لأنهما يوفران عمليات معالجة وتحليل فعالة للبيانات", "B": "لأنهما يمنعان استخدام الذاكرة", "C": "لأنهما يحولان كل البيانات إلى صور", "D": "لأنهما لا يحتاجان أي موارد"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يفضل تجنب تكرار نفس الكود داخل حلقات متعددة؟", "options": {"A": "لأنه يجعل الكود أصعب للصيانة وإعادة الاستخدام", "B": "لأنه يمنع Python من العمل", "C": "لأنه يزيد دقة النموذج", "D": "لأنه يحذف البيانات"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك DataFrame وعمود Age يحتوي نصوصًا رقمية. الخطوة المناسبة هي:", "options": {"A": "حذف Pandas", "B": "تحويل العمود إلى نوع رقمي بطريقة آمنة", "C": "تحويله إلى صورة", "D": "تجاهله دائمًا"}, "correct": "B", "difficulty": "hard"},
                    {"text": "عند تحليل بيانات كبيرة، أفضل ممارسة هي:", "options": {"A": "قراءة كل شيء دون فحص", "B": "نسخ Dataset مرات متعددة", "C": "فحص الأنواع والحجم والذاكرة قبل المعالجة", "D": "حذف القيم عشوائيًا"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4: SQL
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ SQL وقواعد البيانات",
                "description": "إتقان استخراج البيانات من قواعد البيانات وربط الجداول وتحضير البيانات قبل النمذجة.",
                "objectives": [
                    "Relational Databases",
                    "Primary Keys / Foreign Keys",
                    "SELECT / WHERE / ORDER BY",
                    "GROUP BY / HAVING",
                    "JOINs",
                    "CASE / Subqueries",
                    "CTEs",
                    "Window Functions"
                ],
                "practical_task": "أنشئ جدولين Customers و Orders. اكتب Queries لإيجاد: إجمالي المبيعات، مبيعات كل عميل، العملاء الذين تجاوزت مشترياتهم 250، ترتيب العملاء، أعلى عميل.",
                "youtube_ar": "https://www.udemy.com/course/learn-sql-basics-for-beginners-in-arabic-2021/",
                "youtube_en": "https://www.youtube.com/watch?v=OT1RErkfLNQ",
                "questions": [
                    {"text": "أي SQL تستخدم لاختيار أعمدة؟", "options": {"A": "SELECT", "B": "DELETE", "C": "DROP", "D": "UPDATE"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي عبارة لتصفية الصفوف؟", "options": {"A": "ORDER BY", "B": "WHERE", "C": "GROUP BY", "D": "JOIN"}, "correct": "B", "difficulty": "easy"},
                    {"text": "COUNT(*) تحسب:", "options": {"A": "الأعمدة", "B": "الجداول", "C": "الصفوف", "D": "قواعد البيانات"}, "correct": "C", "difficulty": "easy"},
                    {"text": "Primary Key يجب أن يكون:", "options": {"A": "مكررًا", "B": "فريدًا لكل سجل", "C": "نصًا فقط", "D": "فارغًا دائمًا"}, "correct": "B", "difficulty": "easy"},
                    {"text": "SUM(amount) تستخدم لـ:", "options": {"A": "حساب المجموع", "B": "الترتيب", "C": "الدمج", "D": "حذف البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي clause تجمع الصفوف حسب قيمة؟", "options": {"A": "WHERE", "B": "GROUP BY", "C": "ORDER BY", "D": "LIMIT"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا أردت فقط المجموعات التي مجموعها أكبر من 1000 تستخدم:", "options": {"A": "WHERE", "B": "SELECT", "C": "HAVING", "D": "JOIN"}, "correct": "C", "difficulty": "medium"},
                    {"text": "INNER JOIN يعيد عادة:", "options": {"A": "الصفوف المتطابقة بين الجدولين", "B": "الجدول الأول فقط", "C": "الجدول الثاني فقط", "D": "كل قواعد البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما نتيجة: SELECT SUM(amount) FROM Orders; إذا كانت القيم 100، 200، 500؟", "options": {"A": "300", "B": "500", "C": "700", "D": "800"}, "correct": "D", "difficulty": "medium"},
                    {"text": "ما وظيفة ORDER BY؟", "options": {"A": "ترتيب النتائج", "B": "حذف الصفوف", "C": "إنشاء قاعدة", "D": "دمج الجداول"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Window Function مناسبة لـ:", "options": {"A": "ترتيب أو حسابات عبر مجموعة الصفوف دون فقدان الصفوف", "B": "حذف قاعدة البيانات", "C": "تغيير نظام التشغيل", "D": "إنشاء API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "تريد معرفة العميل صاحب أعلى مجموع مشتريات. أفضل نهج:", "options": {"A": "GROUP BY customer ثم SUM ثم ترتيب النتائج", "B": "DELETE", "C": "DROP", "D": "LIMIT فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان Customer 1 لديه طلبان 100 و 200، فإن SUM له =:", "options": {"A": "100", "B": "200", "C": "300", "D": "400"}, "correct": "C", "difficulty": "hard"},
                    {"text": "ما ميزة CTE؟", "options": {"A": "تجعل Query المعقدة أكثر تنظيمًا وقابلية للقراءة", "B": "تزيد حجم القرص", "C": "تحذف البيانات", "D": "تستبدل Python"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا SQL مهمة لعالم البيانات؟", "options": {"A": "لأن البيانات المؤسسية غالبًا توجد في قواعد بيانات", "B": "لأنها لغة تصميم", "C": "لأنها بديل كامل للإحصاء", "D": "لأنها تستخدم فقط في المواقع"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5: تنظيف البيانات و EDA
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ تنظيف البيانات و EDA والتصور",
                "description": "تحويل البيانات الخام إلى Dataset موثوقة وفهم الأنماط والعلاقات قبل بناء النماذج.",
                "objectives": [
                    "Data Quality",
                    "Missing Values",
                    "Duplicates",
                    "Outliers",
                    "Encoding",
                    "EDA",
                    "Matplotlib / Seaborn",
                    "Data Storytelling"
                ],
                "practical_task": "خذ Dataset حقيقية: تنظيف → استكشاف → إحصاءات → Correlation → 5 Visualizations → 10 Insights. ثم اكتب تقريراً قصيراً.",
                "youtube_ar": "https://www.youtube.com/watch?v=Ad9ejj0ZOKQ",
                "youtube_en": "https://www.youtube.com/watch?v=wUSDVGivd-8",
                "questions": [
                    {"text": "ما المقصود بـ Missing Value؟", "options": {"A": "قيمة مفقودة أو غير مسجلة", "B": "قيمة صحيحة", "C": "صف مكرر", "D": "رسم بياني"}, "correct": "A", "difficulty": "easy"},
                    {"text": "df.info() مفيدة لمعرفة:", "options": {"A": "أنواع الأعمدة وحجم البيانات", "B": "كلمة المرور", "C": "عنوان IP", "D": "نموذج ML"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Duplicate يعني:", "options": {"A": "قيمة ناقصة", "B": "سجل مكرر", "C": "عمود جديد", "D": "رسم"}, "correct": "B", "difficulty": "easy"},
                    {"text": "Histogram يستخدم غالبًا لعرض:", "options": {"A": "توزيع متغير عددي", "B": "العلاقات بين الجداول", "C": "SQL Query", "D": "الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Scatter Plot مناسب لفحص:", "options": {"A": "العلاقة بين متغيرين عدديين", "B": "أسماء الملفات", "C": "النصوص فقط", "D": "قواعد البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كانت نسبة Missing Values صغيرة جدًا، يمكن:", "options": {"A": "حذف الصفوف المناسبة بعد التحقق", "B": "حذف Dataset كلها", "C": "تغيير نظام التشغيل", "D": "تجاهل المشكلة دائمًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما خطر Outliers؟", "options": {"A": "قد تؤثر على بعض الإحصاءات والنماذج", "B": "تزيد عدد الأعمدة", "C": "تمنع SQL", "D": "تحذف Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Correlation Heatmap تستخدم لـ:", "options": {"A": "رؤية العلاقات الارتباطية بين المتغيرات", "B": "ضغط Dataset", "C": "إنشاء API", "D": "تدريب الشبكة مباشرة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان Age يحتوي \"25\" كنص، فهذا مثال على مشكلة:", "options": {"A": "Data Type", "B": "Duplicate", "C": "Visualization", "D": "SQL Join"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نعمل EDA قبل ML؟", "options": {"A": "لفهم البيانات واكتشاف المشاكل والأنماط", "B": "لتجنب استخدام Python", "C": "لزيادة حجم الملف", "D": "لتغيير Labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أفضل رسم لمقارنة مبيعات 5 منتجات:", "options": {"A": "Bar Chart", "B": "Scatter فقط", "C": "Histogram فقط", "D": "Heatmap فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان Missing Values في عمود الراتب مرتبطًا بنوع الموظف، فملء القيم بالمتوسط العام قد:", "options": {"A": "يخفي اختلافًا مهمًا ويؤدي لتحيز", "B": "يحل المشكلة دائمًا", "C": "يزيد الدقة دائمًا", "D": "لا يؤثر إطلاقًا"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان Feature A و Feature B مرتبطين جدًا، فقد تحتاج إلى فحص:", "options": {"A": "Multicollinearity", "B": "HTML", "C": "DNS", "D": "Firewall"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا يعني Correlation = 0.8 أن A يسبب B؟", "options": {"A": "لأن الارتباط لا يثبت السببية", "B": "لأن 0.8 قيمة سالبة", "C": "لأن البيانات لا يمكن تحليلها", "D": "لأن Python لا تدعمها"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أفضل EDA هو الذي ينتهي بـ:", "options": {"A": "Insights وأسئلة جديدة قابلة للاختبار", "B": "رسوم كثيرة بلا تفسير", "C": "حذف البيانات", "D": "ملف فارغ"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6: Machine Learning - الأساسيات
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ Machine Learning — الأساسيات",
                "description": "تعلم بناء وتقييم نماذج Machine Learning الأساسية لحل مشكلات Regression و Classification.",
                "objectives": [
                    "ML Workflow",
                    "Features / Labels",
                    "Train / Validation / Test",
                    "Linear Regression",
                    "Logistic Regression",
                    "Decision Trees",
                    "Random Forest",
                    "KNN",
                    "Overfitting / Underfitting",
                    "Cross Validation",
                    "Data Leakage"
                ],
                "practical_task": "استخدم Dataset للتنبؤ بسعر المنازل: EDA → Train/Test Split → Linear Regression → Random Forest → Evaluation → Comparison",
                "youtube_ar": "https://www.youtube.com/playlist?list=PLO4jXE-LdDTTIILQGjB9fWZAg9R0eMYlQ",
                "youtube_en": "https://developers.google.com/machine-learning/crash-course",
                "questions": [
                    {"text": "ما المقصود بـ Feature؟", "options": {"A": "المتغير المستخدم لمساعدة النموذج على التنبؤ", "B": "النتيجة فقط", "C": "ملف Python", "D": "الرسم البياني"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Label هو:", "options": {"A": "الهدف الذي نريد التنبؤ به", "B": "اسم المكتبة", "C": "حجم Dataset", "D": "رقم الصف"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Regression تتنبأ غالبًا بـ:", "options": {"A": "قيمة رقمية", "B": "فئة فقط", "C": "ملف", "D": "صورة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Classification تتنبأ بـ:", "options": {"A": "فئة/Label", "B": "حجم القرص", "C": "عدد الأعمدة فقط", "D": "قيمة عشوائية"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Train Set تستخدم لـ:", "options": {"A": "تدريب النموذج", "B": "حذف البيانات", "C": "عرض الرسوم", "D": "تخزين Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Test Set؟", "options": {"A": "لتقييم الأداء على بيانات لم يرها النموذج أثناء التدريب", "B": "لتدريب النموذج مرة ثانية", "C": "لتغيير البيانات", "D": "لحذف Outliers"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Overfitting يعني أن النموذج:", "options": {"A": "تعلم بيانات التدريب بشكل مفرط وضعف تعميمه", "B": "لم يتعلم شيئًا", "C": "لا يستخدم Features", "D": "لا يحتوي Parameters"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Logistic Regression تستخدم غالبًا لـ:", "options": {"A": "Classification", "B": "Image storage", "C": "SQL", "D": "Visualization"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Accuracy تساوي:", "options": {"A": "Correct Predictions / Total Predictions", "B": "Errors / Features", "C": "Features / Rows", "D": "Loss / Epochs"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Cross-validation تساعد في:", "options": {"A": "تقدير أداء النموذج بصورة أكثر موثوقية", "B": "حذف Dataset", "C": "كتابة SQL", "D": "تغيير نوع الملف"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Data Leakage تعني:", "options": {"A": "تسرب معلومات من خارج التدريب إلى عملية التعلم بطريقة غير صحيحة", "B": "فقدان الإنترنت", "C": "حذف البيانات", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Dataset غير متوازنة جدًا. أي Metric قد تكون أهم من Accuracy؟", "options": {"A": "Precision/Recall/F1", "B": "File Size", "C": "Number of Columns", "D": "RAM"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان Training Accuracy = 99% و Test Accuracy = 65%، فالاحتمال الأكبر:", "options": {"A": "Overfitting", "B": "Underfitting", "C": "Perfect Model", "D": "No Data"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا يجوز عمل Scaling باستخدام كامل Dataset قبل Train/Test Split؟", "options": {"A": "لأنه قد يسبب Data Leakage", "B": "لأنه يحذف Labels", "C": "لأنه يمنع Python", "D": "لأنه يزيد عدد الصفوف"}, "correct": "A", "difficulty": "hard"},
                    {"text": "النموذج الأفضل ليس بالضرورة صاحب أعلى Accuracy لأن:", "options": {"A": "يجب ربط التقييم بهدف المشكلة وتكلفة الأخطاء", "B": "Accuracy غير مفيدة دائمًا", "C": "Random Forest دائمًا أفضل", "D": "Linear Regression دائمًا أفضل"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7: Advanced ML
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ Advanced ML وهندسة الميزات",
                "description": "تحسين النماذج واختيارها وبناء Features قوية ومعالجة المشكلات الواقعية.",
                "objectives": [
                    "Feature Engineering",
                    "Feature Selection",
                    "Scaling / Encoding",
                    "Pipelines",
                    "Hyperparameter Tuning",
                    "Ensemble Learning",
                    "Gradient Boosting",
                    "PCA / Clustering",
                    "K-Means / DBSCAN",
                    "Model Explainability"
                ],
                "practical_task": "خذ Dataset تصنيف العملاء: Baseline Model → Feature Engineering → Scaling/Encoding → 3 Models → Hyperparameter Tuning → Cross Validation → Model Selection",
                "youtube_ar": "https://www.youtube.com/playlist?list=PLO4jXE-LdDTTIILQGjB9fWZAg9R0eMYlQ",
                "youtube_en": "https://www.coursera.org/professional-certificates/ibm-machine-learning",
                "questions": [
                    {"text": "Feature Engineering تعني:", "options": {"A": "إنشاء أو تحويل Features لتحسين النموذج", "B": "حذف Python", "C": "إنشاء حساب GitHub", "D": "ضغط البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "K-Means تستخدم أساسًا في:", "options": {"A": "Clustering", "B": "Regression", "C": "SQL", "D": "Web Development"}, "correct": "A", "difficulty": "easy"},
                    {"text": "PCA تستخدم غالبًا في:", "options": {"A": "Dimensionality Reduction", "B": "Data Entry", "C": "Networking", "D": "Authentication"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Scaling مهم لبعض الخوارزميات لأن:", "options": {"A": "اختلاف المقاييس قد يؤثر في التعلم", "B": "يزيد عدد الصفوف", "C": "يحذف Features", "D": "يمنع Overfitting دائمًا"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Ensemble يعني:", "options": {"A": "دمج عدة نماذج/متعلمين", "B": "حذف النماذج", "C": "استخدام Dataset واحدة فقط", "D": "إيقاف التدريب"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Random Forest يتكون من:", "options": {"A": "عدة Decision Trees", "B": "عدة SQL Tables", "C": "عدة Dashboards", "D": "عدة CSV فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Hyperparameter هو:", "options": {"A": "إعداد يحدد قبل/أثناء التدريب ولا يتعلم مباشرة من البيانات", "B": "Label", "C": "Missing Value", "D": "Dataset"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Grid Search تستخدم لـ:", "options": {"A": "البحث عن أفضل Hyperparameters ضمن قيم محددة", "B": "تنظيف CSV", "C": "إنشاء الرسوم", "D": "تخزين النموذج"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Clustering يستخدم عندما:", "options": {"A": "لا تكون Labels معروفة ونريد اكتشاف مجموعات", "B": "نعرف Label دائمًا", "C": "نريد SQL", "D": "نريد حذف البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Pipeline تساعد على:", "options": {"A": "تنظيم خطوات preprocessing والتدريب", "B": "حذف Features", "C": "إنشاء Dashboard فقط", "D": "تغيير نظام التشغيل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Gradient Boosting يبني:", "options": {"A": "نماذج تدريجية تركز على أخطاء النماذج السابقة", "B": "قواعد بيانات", "C": "صورًا", "D": "جداول Excel"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا أجريت Feature Selection على كامل Dataset قبل Cross Validation، فقد:", "options": {"A": "يحدث Leakage", "B": "يتحسن التعميم دائمًا", "C": "تختفي Labels", "D": "تصبح البيانات أكبر"}, "correct": "A", "difficulty": "hard"},
                    {"text": "PCA قد تفقد:", "options": {"A": "بعض قابلية التفسير الأصلية لل Features", "B": "كل البيانات دائمًا", "C": "جميع Labels", "D": "Python"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان النموذج ممتازًا على التدريب والـ CV ضعيفًا، فالخطوة الأنسب:", "options": {"A": "فحص Overfitting و Features و Hyperparameters", "B": "نشره فورًا", "C": "حذف Test Set", "D": "زيادة Accuracy يدويًا"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أفضل مقارنة للنماذج تكون عبر:", "options": {"A": "Metric مناسبة + Cross Validation + Test Set نهائي", "B": "اسم الخوارزمية فقط", "C": "عدد أسطر الكود", "D": "سرعة تشغيل Jupyter فقط"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8: Deep Learning + NLP + Time Series
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ Deep Learning + NLP + Time Series",
                "description": "فهم متى ينتقل عالم البيانات من ML التقليدي إلى Deep Learning والنصوص والبيانات الزمنية.",
                "objectives": [
                    "Neural Networks",
                    "Layers / Neurons",
                    "Activation Functions",
                    "Loss / Backpropagation",
                    "CNN basics",
                    "NLP fundamentals",
                    "Text preprocessing",
                    "Embeddings",
                    "Time Series / Forecasting",
                    "RNN / LSTM concepts"
                ],
                "practical_task": "اختر واحدًا: تصنيف نصوص Reviews إلى Positive/Negative، أو توقع مبيعات زمنية، أو تصنيف صور بسيط.",
                "youtube_ar": "https://www.youtube.com/watch?v=o3paqBstP9Y",
                "youtube_en": "https://developers.google.com/machine-learning/crash-course/neural-networks",
                "questions": [
                    {"text": "Neural Network تتكون من:", "options": {"A": "Layers و Neurons", "B": "SQL Tables", "C": "CSV فقط", "D": "Routers"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Activation Function تستخدم لـ:", "options": {"A": "إدخال Non-linearity", "B": "حذف البيانات", "C": "إنشاء SQL", "D": "ضغط الصور فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "NLP تتعامل أساسًا مع:", "options": {"A": "اللغة والنصوص", "B": "الشبكات", "C": "قواعد البيانات فقط", "D": "أنظمة التشغيل"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Time Series تتميز بوجود:", "options": {"A": "بُعد زمني", "B": "Passwords", "C": "SQL فقط", "D": "صور فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Loss Function تقيس:", "options": {"A": "مقدار خطأ النموذج وفق مقياس محدد", "B": "حجم Dataset", "C": "سرعة الإنترنت", "D": "عدد المستخدمين"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Backpropagation تستخدم لتحديث:", "options": {"A": "أوزان الشبكة", "B": "أسماء الملفات", "C": "SQL Tables", "D": "Labels يدويًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Embedding يحول عادة:", "options": {"A": "عناصر مثل الكلمات إلى تمثيل عددي", "B": "CSV إلى PDF", "C": "SQL إلى HTML", "D": "Image إلى Router"}, "correct": "A", "difficulty": "medium"},
                    {"text": "CNN مفيدة خصوصًا في:", "options": {"A": "الصور والأنماط المكانية", "B": "قواعد البيانات فقط", "C": "SQL", "D": "Excel"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا لا نخلط بيانات المستقبل في تدريب Time Series؟", "options": {"A": "لمنع تسرب معلومات المستقبل", "B": "لزيادة Accuracy", "C": "لتقليل RAM", "D": "لتغيير Labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "RNN/LSTM مناسبة تاريخيًا لـ:", "options": {"A": "بيانات متسلسلة", "B": "قواعد البيانات فقط", "C": "Static HTML", "D": "ملفات ZIP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Text Classification قد تستخدم لـ:", "options": {"A": "Spam Detection", "B": "IP Routing", "C": "Disk Partitioning", "D": "SQL Backup"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان هناك Data Leakage من المستقبل في Forecasting، فالنتيجة:", "options": {"A": "تقييم غير واقعي للنموذج", "B": "نموذج أكثر موثوقية", "C": "بيانات أكثر صحة", "D": "لا تأثير"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Neural Network ليست الخيار الأفضل تلقائيًا لأن:", "options": {"A": "ML التقليدي قد يكون كافيًا وأبسط في بعض المشكلات", "B": "الشبكات العصبية لا تتعلم", "C": "Python لا تدعمها", "D": "تحتاج SQL"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في NLP، تنظيف النص يجب أن يكون:", "options": {"A": "مرتبطًا بالمشكلة حتى لا نحذف معلومات مهمة", "B": "حذف كل الكلمات", "C": "تحويل كل شيء إلى أرقام عشوائية", "D": "إزالة Labels"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أفضل اختيار بين ML و Deep Learning يعتمد على:", "options": {"A": "طبيعة البيانات وحجمها والهدف والموارد والأداء المطلوب", "B": "شهرة النموذج", "C": "طول الكود", "D": "اسم الشركة"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9: MLOps
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ Production Data Science — Deployment & MLOps",
                "description": "نقل النموذج من Notebook إلى نظام قابل للتشغيل والمراقبة وإعادة التدريب.",
                "objectives": [
                    "Git / GitHub",
                    "Environment Management",
                    "APIs / FastAPI",
                    "Model Serialization",
                    "Docker basics",
                    "MLflow",
                    "CI/CD concepts",
                    "Model Deployment",
                    "Monitoring / Model Drift",
                    "Cloud ML basics"
                ],
                "practical_task": "خذ أفضل نموذج: Train → Save Model → FastAPI → Docker → API Endpoint → Test → Logging. ثم أنشئ نسخة بسيطة من Monitoring.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/paths/build-ai-solutions-with-azure-ml-service/",
                "youtube_en": "https://www.youtube.com/watch?v=9m4P0WGs7lQ",
                "questions": [
                    {"text": "Git يستخدم لـ:", "options": {"A": "Version Control", "B": "Statistics", "C": "Visualization فقط", "D": "Database Backup فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "API تسمح عادةً بـ:", "options": {"A": "التواصل البرمجي بين الأنظمة", "B": "تنظيف الشاشة", "C": "حذف Git", "D": "إنشاء Dataset تلقائيًا"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Docker يستخدم لـ:", "options": {"A": "Packaging وتشغيل التطبيقات في Containers", "B": "حساب Mean", "C": "بناء Neural Network فقط", "D": "كتابة SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "MLflow يستخدم في:", "options": {"A": "تتبع التجارب والنماذج", "B": "تصميم المواقع", "C": "الشبكات", "D": "تحرير الصور"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Deployment يعني:", "options": {"A": "إتاحة النموذج للاستخدام", "B": "حذف النموذج", "C": "تدريب البيانات فقط", "D": "إنشاء CSV"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Model Registry يساعد على:", "options": {"A": "إدارة إصدارات النماذج", "B": "حذف Logs", "C": "إنشاء HTML", "D": "حساب Median"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Reproducibility تعني:", "options": {"A": "إمكانية إعادة إنتاج النتائج باستخدام نفس الإعدادات والبيانات المناسبة", "B": "تغيير النموذج يوميًا", "C": "حذف Environment", "D": "منع Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Data Drift يعني:", "options": {"A": "تغير توزيع البيانات بمرور الوقت", "B": "حذف البيانات", "C": "توقف الإنترنت", "D": "تغير اسم النموذج"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Model Monitoring مهم لأن:", "options": {"A": "أداء النموذج قد يتغير بعد النشر", "B": "التدريب ينتهي للأبد", "C": "البيانات لا تتغير", "D": "API لا تحتاج مراقبة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Docker مفيد؟", "options": {"A": "يقلل مشاكل اختلاف البيئات", "B": "يزيد Accuracy تلقائيًا", "C": "يحل Data Leakage", "D": "يحسب p-value"}, "correct": "A", "difficulty": "medium"},
                    {"text": "CI/CD يساعد في:", "options": {"A": "أتمتة الاختبار والبناء والنشر", "B": "حذف النماذج", "C": "إنشاء Features يدويًا", "D": "حساب Correlation"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Model Accuracy انخفضت بعد عدة أشهر رغم عدم تغيير الكود. سبب محتمل:", "options": {"A": "Data/Concept Drift", "B": "Python Syntax", "C": "Git Branch", "D": "Docker Image فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب حفظ preprocessing مع النموذج؟", "options": {"A": "لضمان أن بيانات الإنتاج تعالج بالطريقة نفسها", "B": "لتقليل عدد الصفوف", "C": "لإلغاء التدريب", "D": "لمنع API"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Azure ML يمكن استخدامه لـ:", "options": {"A": "تدريب وتسجيل ونشر ومراقبة نماذج ML", "B": "تحرير الفيديو", "C": "تصميم الشبكات المحلية فقط", "D": "كتابة Excel"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أفضل Production Workflow هو:", "options": {"A": "Experiment → Track → Validate → Register → Deploy → Monitor", "B": "Train → Delete → Deploy", "C": "Notebook → Screenshot → CV", "D": "CSV → PDF"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10: مشاريع + Portfolio
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 مشاريع Data Science + Portfolio + Job Ready",
                "description": "تحويل المهارات إلى مشاريع احترافية تثبت قدرة الطالب على العمل كـ Junior Data Scientist.",
                "objectives": [
                    "End-to-End Projects",
                    "GitHub Portfolio",
                    "README احترافي",
                    "Model Comparison",
                    "Business Communication",
                    "Case Studies",
                    "CV / LinkedIn",
                    "Technical Interviews"
                ],
                "practical_task": "أنهِ 3 مشاريع Portfolio: (1) Customer Churn Prediction (2) House Price Prediction (3) End-to-End Project مع API + Docker + GitHub.",
                "youtube_ar": "https://teracourses.com/ar/course/data-analysis-course1",
                "youtube_en": "https://www.coursera.org/professional-certificates/ibm-data-science",
                "questions": [
                    {"text": "أهم هدف من Portfolio هو:", "options": {"A": "إثبات القدرة العملية", "B": "زيادة عدد الصور", "C": "كتابة CV فقط", "D": "جمع الشهادات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "README يجب أن يوضح:", "options": {"A": "المشكلة والحل وطريقة التشغيل والنتائج", "B": "اسم الطالب فقط", "C": "كلمة المرور", "D": "حجم الجهاز"}, "correct": "A", "difficulty": "easy"},
                    {"text": "GitHub يستخدم لـ:", "options": {"A": "استضافة وإدارة الكود والمشاريع", "B": "حساب المتوسط", "C": "تدريب النموذج تلقائيًا دائمًا", "D": "إنشاء SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "CV لعالم البيانات يجب أن يركز على:", "options": {"A": "المهارات والمشاريع والنتائج", "B": "الهوايات فقط", "C": "عدد ساعات الدراسة فقط", "D": "أسماء البرامج دون تطبيق"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Case Study تعرض:", "options": {"A": "كيف تم حل مشكلة واقعية باستخدام البيانات", "B": "قائمة كلمات فقط", "C": "تعريف Python", "D": "جدول أسماء"}, "correct": "A", "difficulty": "easy"},
                    {"text": "في مشروع Portfolio، لماذا تشرح Model Selection؟", "options": {"A": "لإظهار أنك تفهم المفاضلة بين النماذج", "B": "لأن الاسم غير مهم", "C": "لتقليل حجم GitHub", "D": "لاستبدال README"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Technical Interview قد يسأل عن:", "options": {"A": "SQL و Statistics و ML و Python", "B": "التصميم فقط", "C": "Word فقط", "D": "الشبكات فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أفضل README يبدأ عادةً بـ:", "options": {"A": "Project Problem/Goal", "B": "Random Code", "C": "Password", "D": "Screenshot فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا حصل نموذجك على 95% Accuracy، يجب أيضًا أن تعرض:", "options": {"A": "Metrics مناسبة ونتائج Test وأخطاء النموذج", "B": "Accuracy فقط", "C": "عدد أسطر الكود", "D": "حجم Dataset"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب ذكر Limitations؟", "options": {"A": "لإظهار الفهم النقدي للنموذج", "B": "لتقليل قيمة المشروع", "C": "لأنها مطلوبة في Python", "D": "لأنها تزيد Accuracy"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أفضل مشروع Portfolio هو:", "options": {"A": "مشروع يوضح مشكلة وبيانات وتحليلًا ونموذجًا ونتيجة", "B": "مشروع منسوخ دون فهم", "C": "Notebook فارغ", "D": "Screenshot من كورس"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أثناء مقابلة Data Scientist طُلب منك حل مشكلة ولم تعرف Dataset. الأفضل أن تبدأ بـ:", "options": {"A": "توضيح المشكلة والهدف والـ Metric والقيود", "B": "اختيار Random Forest مباشرة", "C": "كتابة Neural Network", "D": "فتح Power BI"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان Model A دقته أعلى قليلاً لكن غير قابل للتفسير، و B أقل قليلاً وقابل للتفسير، فالاختيار:", "options": {"A": "يعتمد على طبيعة المشكلة وتكلفة الخطأ ومتطلبات العمل", "B": "A دائمًا", "C": "B دائمًا", "D": "لا يمكن المقارنة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في مشروع Churn، أهم شيء ليس فقط التنبؤ بالعملاء، بل:", "options": {"A": "تحويل التنبؤ إلى قرار قابل للتنفيذ", "B": "زيادة عدد Features بلا نهاية", "C": "استخدام Deep Learning دائمًا", "D": "حذف العملاء"}, "correct": "A", "difficulty": "hard"},
                    {"text": "متى يمكن القول إن المتعلم أصبح Junior Data Scientist جاهزًا مبدئيًا؟", "options": {"A": "عندما يستطيع تنفيذ مشروع End-to-End وشرح قراراته ونتائجه والدفاع عنها", "B": "عندما يشاهد 20 كورسًا", "C": "عندما يحفظ 100 تعريف", "D": "عندما يحصل على شهادة واحدة فقط"}, "correct": "A", "difficulty": "hard"}
                ]
            }
        ]
    }
]