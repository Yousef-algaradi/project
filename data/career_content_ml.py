# data/career_content_ml.py
# بنك محتوى مسار "مهندس تعلم آلي (ML Engineer)"
# 10 مراحل × 15 سؤال = 150 سؤال
# الإجابات موزعة بشكل متوازن (A/B/C/D)
# ==========================================

ML_ENGINEER_PATHS = [
    {
        "major_key": "ai",
        "slug": "ml-engineer",
        "title": "مهندس تعلم آلي (ML Engineer)",
        "description": "مسار متكامل: Python + NumPy/Pandas + SQL + scikit-learn + PyTorch + FastAPI + MLflow + Docker + AWS.",
        "icon": "🤖",
        "difficulty": "متقدم",
        "estimated_hours": 280,
        "order_index": 1,
        "stages": [
            # ==========================================
            # المرحلة 1: Programming & Engineering Foundations
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات البرمجة وبيئة مهندس ML",
                "description": "بناء أساس برمجي وهندسي قوي يسمح بكتابة Python نظيف وقابل للاختبار والتطوير.",
                "objectives": [
                    "Python syntax",
                    "Variables & data types",
                    "Conditions & loops",
                    "Functions",
                    "Lists / tuples / sets / dictionaries",
                    "Modules & packages",
                    "OOP basics",
                    "Exceptions",
                    "File handling",
                    "JSON / CSV",
                    "Virtual environments / pip",
                    "Git & GitHub basics",
                    "CLI / Linux basics",
                    "Unit testing basics",
                    "Debugging"
                ],
                "practical_task": "أنشئ Dataset CLI Analyzer: يقرأ CSV، يتحقق من الملف، يعالج الأخطاء، يحسب إحصائيات، يصدر JSON، يقسم الكود إلى modules، 8 Unit Tests، Git، README.",
                "youtube_ar": "https://elzero.org/",
                "youtube_en": "https://cs50.harvard.edu/python/courses/",
                "questions": [
                    {"text": "أي بنية بيانات Python قابلة للتعديل؟", "options": {"A": "tuple", "B": "list", "C": "string", "D": "int"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الغرض الأساسي من Virtual Environment؟", "options": {"A": "تسريع Python", "B": "حذف المكتبات", "C": "عزل dependencies الخاصة بالمشروع", "D": "تحويل Python إلى C"}, "correct": "C", "difficulty": "easy"},
                    {"text": "إذا كان لدينا d={\"name\":\"Ali\"} فما طريقة الحصول على الاسم؟", "options": {"A": "d[\"name\"]", "B": "d.name()", "C": "d(name)", "D": "d->name"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الأمر الذي يسجل التغييرات في Git؟", "options": {"A": "git start", "B": "git save", "C": "git upload", "D": "git commit"}, "correct": "D", "difficulty": "easy"},
                    {"text": "أين نضع الكود الذي قد يسبب exception؟", "options": {"A": "if", "B": "try", "C": "loop", "D": "import"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما ناتج len([10,20,30])؟", "options": {"A": "2", "B": "4", "C": "3", "D": "30"}, "correct": "C", "difficulty": "medium"},
                    {"text": "أي نوع بيانات غير قابل للتعديل؟", "options": {"A": "tuple", "B": "list", "C": "dict", "D": "set"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يُستخدم with open(...) غالبًا؟", "options": {"A": "لتسريع القرص", "B": "لتحويل الملف إلى JSON", "C": "لتشفير الملف", "D": "لإدارة إغلاق الملف تلقائيًا"}, "correct": "D", "difficulty": "medium"},
                    {"text": "ماذا يفعل git clone؟", "options": {"A": "يحذف repository", "B": "ينسخ repository إلى الجهاز", "C": "ينشئ Python environment", "D": "يشغل الاختبارات"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كانت API تعيد JSON، فما المكتبة المدمجة المناسبة لتحليله؟", "options": {"A": "math", "B": "os", "C": "json", "D": "random"}, "correct": "C", "difficulty": "medium"},
                    {"text": "أين يُفضل تنفيذ pip install لمشروع معزول؟", "options": {"A": "داخل virtual environment", "B": "داخل BIOS", "C": "داخل Git", "D": "داخل المتصفح"}, "correct": "A", "difficulty": "medium"},
                    {"text": "دالة تقوم بتعديل قائمة ثم لا تحتوي على return. ماذا تعيد عند استدعائها؟", "options": {"A": "القائمة تلقائيًا", "B": "نسخة من القائمة", "C": "صفر", "D": "None"}, "correct": "D", "difficulty": "hard"},
                    {"text": "لديك برنامج يفشل أحيانًا بسبب API مؤقتة. ما التصميم الأفضل؟", "options": {"A": "تجاهل الخطأ", "B": "exception handling + retry مناسب", "C": "حذف البيانات", "D": "إعادة تثبيت Python"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا نكتب Unit Tests؟", "options": {"A": "لتكبير المشروع", "B": "لاستبدال Git", "C": "للتحقق من أجزاء محددة من الكود تلقائيًا", "D": "لتشغيل Docker"}, "correct": "C", "difficulty": "hard"},
                    {"text": "إذا كان البرنامج يعمل على جهازك ويفشل بسبب اختلاف المكتبات، ما الحل الهندسي الأفضل؟", "options": {"A": "تثبيت dependencies محددة داخل environment", "B": "حذف المشروع", "C": "تغيير لغة البرمجة", "D": "إلغاء الاختبارات"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2: Math, Statistics, Data & SQL
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ الرياضيات والإحصاء والبيانات وSQL",
                "description": "فهم الرياضيات والإحصاء والبيانات التي يعتمد عليها ML، مع امتلاك SQL أساسي للتعامل مع البيانات الواقعية.",
                "objectives": [
                    "NumPy / Pandas",
                    "Data cleaning",
                    "Exploratory Data Analysis",
                    "Mean / median / variance",
                    "Probability basics",
                    "Distributions",
                    "Correlation",
                    "Linear algebra basics",
                    "Vectors / Matrices / Dot product",
                    "Derivatives intuition",
                    "SQL SELECT / WHERE / GROUP BY / JOIN",
                    "NULL",
                    "PostgreSQL basics"
                ],
                "practical_task": "استخدم Dataset حقيقي: تحميل، تنظيف missing values، إزالة duplicates، تحليل distributions، حساب correlation، 5 visualizations، 15 استعلام SQL، تقرير EDA.",
                "youtube_ar": "https://elzero.org/",
                "youtube_en": "https://developers.google.com/machine-learning/crash-course",
                "questions": [
                    {"text": "ما وظيفة SELECT في SQL؟", "options": {"A": "قراءة بيانات محددة", "B": "حذف قاعدة البيانات", "C": "إنشاء Python environment", "D": "تشغيل Docker"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي مقياس أكثر مقاومة للقيم الشاذة؟", "options": {"A": "Mean", "B": "Median", "C": "Variance", "D": "Sum"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة GROUP BY؟", "options": {"A": "حذف الصفوف", "B": "إنشاء index", "C": "تجميع الصفوف حسب قيم", "D": "تغيير نوع البيانات"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الهدف الأساسي من NumPy؟", "options": {"A": "Web development", "B": "Git management", "C": "API authentication", "D": "Numerical computing"}, "correct": "D", "difficulty": "easy"},
                    {"text": "ما الذي يمثله Vector رياضيًا؟", "options": {"A": "مجموعة مرتبة من القيم", "B": "قاعدة بيانات", "C": "ملف نصي", "D": "HTTP request"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كانت لديك قيم [2,2,3,3,100] فأي مقياس سيتأثر بشدة بالقيمة 100؟", "options": {"A": "Mean", "B": "Median", "C": "Mode", "D": "Count"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي JOIN يعيد كل سجلات الجدول الأيسر حتى دون وجود تطابق؟", "options": {"A": "INNER", "B": "RIGHT", "C": "LEFT", "D": "CROSS"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ماذا يفعل df.dropna() افتراضيًا في Pandas؟", "options": {"A": "يملأ القيم", "B": "يحذف الصفوف التي تحتوي على missing values", "C": "يحذف الأعمدة فقط", "D": "يحول البيانات إلى SQL"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ماذا تعني correlation عالية؟", "options": {"A": "وجود علاقة إحصائية قوية بين متغيرين", "B": "أن أحد المتغيرين سبب الآخر بالضرورة", "C": "أن البيانات خالية من الأخطاء", "D": "أن النموذج جاهز"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يحدث غالبًا إذا كانت features على مقاييس مختلفة جدًا؟", "options": {"A": "لا يمكن قراءة CSV", "B": "قد تتأثر خوارزميات تعتمد على المسافة/gradient", "C": "تختفي البيانات", "D": "تصبح SQL أسرع"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ماذا يعيد COUNT(*)؟", "options": {"A": "متوسط القيم", "B": "عدد الصفوف", "C": "أكبر قيمة", "D": "أصغر قيمة"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك جدول Customers وجدول Orders وتريد العملاء حتى الذين لم يطلبوا شيئًا. ماذا تستخدم؟", "options": {"A": "INNER JOIN", "B": "LEFT JOIN", "C": "CROSS JOIN", "D": "SELF JOIN"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا كان متوسط الدخل 1000 والانحراف المعياري 100، فالقيمة 1300 تبعد تقريبًا:", "options": {"A": "1 SD", "B": "2 SD", "C": "3 SD", "D": "4 SD"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لماذا لا يكفي correlation لإثبات causation؟", "options": {"A": "لأن correlation لا يمكن حسابها", "B": "لأن البيانات لا تحتوي أرقامًا", "C": "لأن العلاقة قد تكون ناتجة عن عامل آخر", "D": "لأن SQL تمنعها"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لديك feature بقيم من 0–1 وأخرى من 0–1,000,000. ما الخطوة المحتملة قبل خوارزمية تعتمد على المسافات؟", "options": {"A": "Scaling", "B": "حذف SQL", "C": "تحويلها إلى صور", "D": "تشغيل Kafka"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3: Classical Machine Learning
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ Machine Learning التقليدي",
                "description": "تعلم بناء نماذج Machine Learning تقليدية واختيار الخوارزمية المناسبة وتدريبها وتقييمها.",
                "objectives": [
                    "ML workflow",
                    "Supervised learning",
                    "Unsupervised learning",
                    "Regression / Classification",
                    "Linear Regression / Logistic Regression",
                    "Decision Trees / Random Forest",
                    "Gradient Boosting basics",
                    "KNN / K-Means / PCA basics",
                    "Training / Validation / Prediction",
                    "Baselines"
                ],
                "practical_task": "ابنِ مشروع Binary Classification: Dataset حقيقية، Baseline، Train/validation/test، Logistic Regression، Decision Tree، Random Forest، مقارنة النتائج، حفظ أفضل model، تقرير.",
                "youtube_ar": "https://elzero.org/",
                "youtube_en": "https://developers.google.com/machine-learning/crash-course",
                "questions": [
                    {"text": "ما الهدف من Supervised Learning؟", "options": {"A": "التعلم من بيانات تحتوي target/labels", "B": "حذف البيانات", "C": "تشغيل API", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Regression تستخدم غالبًا للتنبؤ بـ:", "options": {"A": "فئة", "B": "قيمة مستمرة", "C": "صورة فقط", "D": "نص فقط"}, "correct": "B", "difficulty": "easy"},
                    {"text": "Classification تستخدم للتنبؤ بـ:", "options": {"A": "classes", "B": "حجم الملف", "C": "عدد الأعمدة", "D": "SQL query"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ feature؟", "options": {"A": "المتغير المدخل للنموذج", "B": "نتيجة Git", "C": "اسم الجهاز", "D": "نوع قاعدة البيانات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة model training؟", "options": {"A": "حذف البيانات", "B": "تعلم parameters من البيانات", "C": "إنشاء API فقط", "D": "ضغط النموذج"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي نموذج مناسب كبداية لمشكلة binary classification؟", "options": {"A": "Logistic Regression", "B": "K-Means", "C": "PCA", "D": "DBSCAN"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم train/test split؟", "options": {"A": "لزيادة عدد الأعمدة", "B": "لتقييم التعميم على بيانات لم يرها النموذج", "C": "لتغيير SQL", "D": "لتقليل RAM فقط"}, "correct": "B", "difficulty": "medium"},
                    {"text": "Decision Tree تتخذ قرارات بناءً على:", "options": {"A": "splits على features", "B": "Kafka partitions", "C": "SQL joins", "D": "Docker images"}, "correct": "A", "difficulty": "medium"},
                    {"text": "K-Means هي خوارزمية:", "options": {"A": "Supervised regression", "B": "Unsupervised clustering", "C": "Database indexing", "D": "API serving"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الهدف من baseline model؟", "options": {"A": "وجود نقطة مقارنة بسيطة", "B": "منع التدريب", "C": "حذف features", "D": "تشغيل GPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان النموذج ممتازًا على training وضعيفًا على test، فالمشكلة المحتملة:", "options": {"A": "Underfitting", "B": "Overfitting", "C": "SQL error", "D": "Missing API"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك dataset غير متوازنة جدًا: 99% Negative و1% Positive. لماذا accuracy قد تكون مضللة؟", "options": {"A": "لأنها قد تكون 99% حتى دون اكتشاف الحالات الإيجابية", "B": "لأنها لا تعمل مع Python", "C": "لأنها تحذف البيانات", "D": "لأنها تعني precision"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج أعطى training accuracy = 99% وvalidation accuracy = 70%. ما الإجراء الأول المنطقي؟", "options": {"A": "افترض أن النموذج مثالي", "B": "افحص overfitting وdata leakage", "C": "احذف validation", "D": "زد learning rate دائمًا"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا يجب أن يكون baseline بسيطًا؟", "options": {"A": "لمقارنة قيمة النماذج الأكثر تعقيدًا", "B": "لأنه دائمًا الأفضل", "C": "لأنه يلغي testing", "D": "لأنه لا يحتاج بيانات"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كانت labels تحتوي خطأ منهجيًا، فما أثر ذلك؟", "options": {"A": "قد يتعلم النموذج pattern خاطئًا", "B": "يصبح النموذج أسرع", "C": "تختفي الحاجة للتقييم", "D": "يتحول classification إلى SQL"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4: Feature Engineering & Evaluation
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ Feature Engineering وEvaluation وExperimentation",
                "description": "الانتقال من 'تدريب نموذج' إلى بناء تجربة ML صحيحة تمنع Data Leakage وتستخدم Metrics مناسبة.",
                "objectives": [
                    "Feature engineering",
                    "Encoding / Scaling / Imputation",
                    "Pipelines",
                    "Cross-validation",
                    "Hyperparameter tuning",
                    "Grid Search / Random Search",
                    "Classification metrics: Precision/Recall/F1/ROC-AUC",
                    "Regression metrics: MAE/MSE/RMSE",
                    "Confusion Matrix",
                    "Data leakage",
                    "Experiment comparison"
                ],
                "practical_task": "خذ مشروع المرحلة السابقة وأعد بناءه باستخدام: preprocessing pipeline، train/test split صحيح، cross-validation، 3 hyperparameter configurations، Precision/Recall/F1، confusion matrix، leakage check، مقارنة 3 نماذج، تقرير Experiment.",
                "youtube_ar": "https://scikit-learn.org/",
                "youtube_en": "https://scikit-learn.org/stable/user_guide.html",
                "questions": [
                    {"text": "ماذا تعني Precision؟", "options": {"A": "نسبة التنبؤات الإيجابية الصحيحة من كل التنبؤات الإيجابية", "B": "نسبة كل البيانات الصحيحة", "C": "زمن التدريب", "D": "حجم dataset"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Recall يهتم أكثر بـ:", "options": {"A": "اكتشاف الحالات الإيجابية الحقيقية", "B": "حجم النموذج", "C": "سرعة API", "D": "عدد features فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة scaling؟", "options": {"A": "توحيد نطاق features", "B": "حذف labels", "C": "إنشاء database", "D": "تشغيل GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من confusion matrix؟", "options": {"A": "رؤية أنواع التنبؤات الصحيحة والخاطئة", "B": "تخزين النموذج", "C": "تشغيل Docker", "D": "إدارة Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "F1 يجمع بين:", "options": {"A": "Accuracy وRMSE", "B": "Precision وRecall", "C": "MAE وMSE", "D": "Mean وMedian"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما فائدة cross-validation؟", "options": {"A": "تقييم النموذج عبر تقسيمات متعددة للبيانات", "B": "حذف test set", "C": "زيادة labels", "D": "تشغيل Kafka"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نطبق preprocessing داخل Pipeline؟", "options": {"A": "لضمان تطبيق الخطوات بشكل متسق وتقليل leakage", "B": "لتغيير لغة البرمجة", "C": "لإلغاء التدريب", "D": "لتخزين الصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت تكلفة False Negative عالية، ما metric المهم غالبًا؟", "options": {"A": "Recall", "B": "RMSE", "C": "R² فقط", "D": "MAE"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المشكلة في استخدام test set لاختيار hyperparameters؟", "options": {"A": "يؤدي إلى تسرب معلومات الاختبار إلى عملية الاختيار", "B": "يجعل البيانات أكبر", "C": "يجعل النموذج unsupervised", "D": "يمنع التدريب"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الغرض من Grid Search؟", "options": {"A": "تجربة مجموعة محددة من hyperparameters", "B": "تنظيف SQL", "C": "تحويل الصور", "D": "نشر API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل سبب لاستخدام baseline؟", "options": {"A": "معرفة ما إذا كان التحسين فعليًا", "B": "منع النماذج الجديدة", "C": "استبدال test", "D": "حذف features"}, "correct": "A", "difficulty": "medium"},
                    {"text": "قمت بحساب mean وstandard deviation على كامل dataset قبل train/test split. ما المشكلة؟", "options": {"A": "Data leakage", "B": "Underfitting", "C": "Class balancing", "D": "Serialization"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج fraud detection يكتشف 98% من fraud لكنه يعطي إنذارات كاذبة كثيرة. أي metric تحتاج فحصه أيضًا؟", "options": {"A": "Precision", "B": "RAM", "C": "Epochs فقط", "D": "File size"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كانت metric الخاصة بك RMSE، فما الذي تقيسه؟", "options": {"A": "خطأ التنبؤ في regression مع معاقبة الأخطاء الكبيرة أكثر", "B": "عدد classes", "C": "زمن inference", "D": "نسبة fraud"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا تختار النموذج بناءً على metric واحدة فقط دون فهم business cost؟", "options": {"A": "لأن تكلفة الأخطاء تختلف حسب المشكلة", "B": "لأن metrics لا تعمل", "C": "لأن training غير ضروري", "D": "لأن Python لا يدعم metrics"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5: Deep Learning & PyTorch
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ Deep Learning وPyTorch",
                "description": "تعلم بناء وتدريب Neural Networks باستخدام PyTorch وفهم التدريب على مستوى عملي.",
                "objectives": [
                    "Tensors",
                    "Dataset / DataLoader",
                    "Neural Networks / Layers / Activations",
                    "Loss functions / Forward pass / Backpropagation",
                    "Gradients / Optimizers / Learning rate",
                    "Epochs / Batches / GPU basics",
                    "Regularization / Dropout",
                    "Model saving/loading",
                    "CNN basics / Transfer learning basics"
                ],
                "practical_task": "ابنِ Image Classifier بـ PyTorch: Fashion-MNIST أو CIFAR-10، Dataset/DataLoader، CNN بسيطة، Training loop، Validation، GPU إن توفر، Save/Load model، مقارنة نموذجين، تسجيل metrics.",
                "youtube_ar": "https://docs.pytorch.org/tutorials/",
                "youtube_en": "https://docs.pytorch.org/tutorials/intro.html",
                "questions": [
                    {"text": "ما نوع البيانات الأساسي في PyTorch لمعظم العمليات العددية؟", "options": {"A": "Tensor", "B": "SQL table", "C": "JSON", "D": "CSV"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة DataLoader؟", "options": {"A": "تحميل batches من البيانات", "B": "نشر API", "C": "إنشاء Git repository", "D": "حفظ SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة activation function؟", "options": {"A": "إضافة non-linearity للنموذج", "B": "تخزين البيانات", "C": "إنشاء Docker image", "D": "حذف labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة loss function؟", "options": {"A": "قياس خطأ النموذج", "B": "إنشاء dataset", "C": "تشغيل API", "D": "ضغط النموذج"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة optimizer؟", "options": {"A": "تحديث parameters", "B": "حذف model", "C": "إنشاء CSV", "D": "تشغيل SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يفعل backpropagation؟", "options": {"A": "يحسب gradients بالنسبة للparameters", "B": "يحذف dataset", "C": "ينشئ labels", "D": "يحول Python إلى C"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة batch training؟", "options": {"A": "معالجة مجموعة من samples في كل خطوة", "B": "منع التدريب", "C": "حذف GPU", "D": "تخزين API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يحدث عادة عند زيادة learning rate كثيرًا؟", "options": {"A": "قد يصبح التدريب غير مستقر", "B": "يصبح النموذج دائمًا أفضل", "C": "تختفي loss", "D": "تتحول classification إلى clustering"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Dropout؟", "options": {"A": "لتقليل overfitting", "B": "لتخزين النموذج", "C": "لزيادة database size", "D": "لإنشاء labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين training وevaluation mode في PyTorch؟", "options": {"A": "بعض الطبقات مثل Dropout/BatchNorm تتصرف بشكل مختلف", "B": "evaluation يدرب النموذج", "C": "training يحذف gradients دائمًا", "D": "لا يوجد فرق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم GPU في Deep Learning؟", "options": {"A": "لتسريع عمليات tensor المتوازية غالبًا", "B": "لأنه مطلوب لـSQL", "C": "لتخزين Git", "D": "لتحويل CSV"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت training loss تنخفض وvalidation loss ترتفع باستمرار، فالمشكلة المحتملة؟", "options": {"A": "Overfitting", "B": "Underfitting", "C": "Missing package", "D": "SQL injection"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب عدم استخدام test set بشكل متكرر أثناء التطوير؟", "options": {"A": "لأنه يتحول فعليًا إلى جزء من عملية الاختيار", "B": "لأنه لا يحتوي labels", "C": "لأنه لا يمكن قراءته", "D": "لأنه يبطئ Python فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما فائدة Transfer Learning؟", "options": {"A": "بدء نموذج من representation تم تعلمه مسبقًا", "B": "حذف التدريب", "C": "تحويل الصور إلى SQL", "D": "إلغاء validation"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك نموذج كبير جدًا وRAM محدودة. ما أول شيء تفكر فيه؟", "options": {"A": "تقليل batch/model memory أو استخدام streaming مناسب", "B": "حذف test", "C": "مضاعفة dataset", "D": "إلغاء optimizer"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6: ML Systems, APIs & Serving
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ ML Systems وAPIs وModel Serving",
                "description": "تحويل النموذج من Notebook إلى خدمة يمكن للتطبيقات استدعاؤها عبر API.",
                "objectives": [
                    "Model serialization",
                    "Inference / Batch inference / Online inference",
                    "FastAPI / REST",
                    "JSON requests/responses",
                    "Input validation",
                    "Error handling",
                    "API testing",
                    "Health endpoints",
                    "Model loading",
                    "Latency / Throughput",
                    "Basic concurrency",
                    "API security basics"
                ],
                "practical_task": "حوّل أفضل نموذج من المرحلة 5 إلى Client → FastAPI → Model → Prediction. يحتوي على /predict، /health، Pydantic validation، Error handling، Model loaded once، API tests، README، latency measurement.",
                "youtube_ar": "https://fastapi.tiangolo.com/",
                "youtube_en": "https://fastapi.tiangolo.com/",
                "questions": [
                    {"text": "ما وظيفة API في نظام ML؟", "options": {"A": "توفير واجهة لاستدعاء النموذج", "B": "تدريب Git", "C": "تنظيف القرص", "D": "إنشاء dataset تلقائيًا"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما صيغة شائعة للبيانات في REST API؟", "options": {"A": "JSON", "B": "EXE", "C": "DLL", "D": "ISO"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة /health؟", "options": {"A": "التحقق من جاهزية الخدمة", "B": "تدريب النموذج", "C": "حذف model", "D": "إنشاء database"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ inference؟", "options": {"A": "استخدام نموذج مدرب لإنتاج prediction", "B": "تدريب من الصفر", "C": "تنظيف Git", "D": "إنشاء Dockerfile"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نتحقق من input؟", "options": {"A": "لمنع بيانات غير صالحة من الوصول للنموذج", "B": "لزيادة حجم النموذج", "C": "لتقليل accuracy", "D": "لحذف API"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا يجب تحميل النموذج مرة واحدة بدل تحميله لكل request؟", "options": {"A": "لتقليل latency والموارد", "B": "لزيادة حجم API", "C": "لتغيير labels", "D": "لمنع JSON"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ latency؟", "options": {"A": "الزمن المستغرق للاستجابة", "B": "عدد features", "C": "حجم dataset", "D": "عدد classes"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا أرسل العميل قيمة نصية بينما النموذج يتوقع رقمًا، ماذا ينبغي أن يحدث؟", "options": {"A": "validation error واضح", "B": "تدريب النموذج", "C": "حذف request", "D": "تغيير model تلقائيًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة batch inference؟", "options": {"A": "معالجة عدد كبير من predictions معًا", "B": "منع model loading", "C": "إنشاء Git branch", "D": "حذف API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نحتاج versioning للنموذج؟", "options": {"A": "لمعرفة أي model version أعطت prediction", "B": "لتغيير Python", "C": "لحذف logs", "D": "لتقليل database"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين online وbatch inference؟", "options": {"A": "online يستجيب عند الطلب، batch يعالج مجموعة مجدولة", "B": "online لا يستخدم model", "C": "batch دائمًا أسرع", "D": "لا يوجد فرق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "API latency ارتفعت بشدة بعد زيادة حجم النموذج. ما أول شيء تقيسه؟", "options": {"A": "inference time وresource usage", "B": "اسم Git branch", "C": "عدد README lines", "D": "حجم CSV فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب ألا يحتوي endpoint على model training في كل request؟", "options": {"A": "لأنه يجعل الخدمة بطيئة وغير مناسبة للإنتاج", "B": "لأنه يمنع JSON", "C": "لأنه يزيد accuracy", "D": "لأنه يحذف model"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كانت API تعيد 500 عند input غير صالح، ما التحسين؟", "options": {"A": "validation + 4xx response مناسب", "B": "إعادة تدريب النموذج", "C": "حذف endpoint", "D": "إزالة schema"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما التصميم الأفضل لخدمة ML؟", "options": {"A": "Load model → validate input → predict → validate output → respond", "B": "Train → delete → predict", "C": "Predict → load model → train", "D": "SQL → Git → prediction"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7: MLOps
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ MLOps — Tracking وRegistry وTesting وMonitoring",
                "description": "تعلم إدارة دورة حياة النموذج: التجارب → التسجيل → النسخ → الاختبار → النشر → المراقبة.",
                "objectives": [
                    "ML lifecycle",
                    "Experiment tracking / MLflow",
                    "Parameters / Metrics / Artifacts",
                    "Model Registry / Model versions",
                    "Reproducibility",
                    "Model packaging",
                    "Unit tests / Data tests / Model tests",
                    "CI basics / Logging",
                    "Drift concepts / Performance monitoring",
                    "Rollback basics"
                ],
                "practical_task": "أنشئ Training → MLflow Tracking → Best Model → Registry → Validation → API. سجل parameters, metrics, model, dataset version, Git commit, model version. نفذ اختبار يمنع تسجيل model إذا فشل metric threshold.",
                "youtube_ar": "https://mlflow.org/docs/latest/",
                "youtube_en": "https://mlflow.org/docs/latest/",
                "questions": [
                    {"text": "ما وظيفة Experiment Tracking؟", "options": {"A": "تسجيل نتائج التجارب", "B": "حذف النماذج", "C": "إنشاء SQL", "D": "تشغيل GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يمكن تسجيله في MLflow؟", "options": {"A": "parameters وmetrics وartifacts", "B": "IP فقط", "C": "كلمات المرور", "D": "BIOS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Model Registry؟", "options": {"A": "إدارة نسخ النماذج", "B": "تدريب CPU", "C": "حذف datasets", "D": "تشغيل Docker فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نحتاج reproducibility؟", "options": {"A": "لإعادة إنتاج النتائج", "B": "لتغيير labels", "C": "لحذف logs", "D": "لمنع testing"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ artifact؟", "options": {"A": "ملف ناتج عن experiment مثل model أو plot", "B": "قاعدة بيانات", "C": "API endpoint", "D": "Git user"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نربط model version بـ Git commit؟", "options": {"A": "لمعرفة الكود الذي أنتج النموذج", "B": "لزيادة accuracy", "C": "لتقليل RAM", "D": "لتغيير database"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان Model Registry يحتوي v1 وv2، ما الفائدة؟", "options": {"A": "مقارنة وإدارة الإصدارات", "B": "حذف الحاجة للاختبار", "C": "منع deployment", "D": "تغيير Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهدف من model validation قبل deployment؟", "options": {"A": "التأكد من استيفاء شروط الجودة", "B": "زيادة حجم model", "C": "حذف البيانات", "D": "إنشاء README"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا تعني model drift؟", "options": {"A": "تغير خصائص البيانات/العلاقة مع الزمن مما قد يؤثر على الأداء", "B": "زيادة Git commits", "C": "حذف model", "D": "تغير اسم API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم logging؟", "options": {"A": "لتشخيص ومتابعة النظام", "B": "لتدريب neural network", "C": "لتغيير labels", "D": "لحذف errors"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة rollback؟", "options": {"A": "العودة إلى إصدار سابق صالح", "B": "حذف جميع models", "C": "إلغاء Git", "D": "إعادة كتابة Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "نموذج جديد أفضل accuracy لكنه أسوأ recall في حالة fraud. ماذا تفعل؟", "options": {"A": "تختار مباشرة accuracy", "B": "تقارن metrics مع business requirement", "C": "تحذف النموذجين", "D": "تتجاهل recall"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ما أفضل مكان لتخزين credentials؟", "options": {"A": "داخل GitHub README", "B": "داخل source code", "C": "secret/environment management", "D": "داخل model artifact"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لماذا يجب اختبار preprocessing أيضًا؟", "options": {"A": "لأن preprocessing جزء من prediction pipeline", "B": "لأنه لا يؤثر على النموذج", "C": "لأنه خاص بـGit", "D": "لأنه يخص Docker فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان model يعمل محليًا ويفشل في production، ماذا تفحص؟", "options": {"A": "dependencies/environment/config/model artifact", "B": "اسم المشروع فقط", "C": "لون README", "D": "عدد Git stars"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8: Cloud, Docker, DevOps & Production
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ Cloud وDocker وDevOps وProduction ML",
                "description": "تشغيل ML system في بيئة production بسيطة باستخدام Docker وAWS ومبادئ CI/CD والمراقبة.",
                "objectives": [
                    "Docker / Dockerfile / Images / Containers",
                    "Docker Compose basics",
                    "Environment variables",
                    "GitHub Actions basics",
                    "AWS fundamentals",
                    "S3 / IAM / EC2 basics / ECR basics",
                    "CloudWatch basics",
                    "Container deployment",
                    "Secrets",
                    "Basic CI/CD",
                    "Production configuration",
                    "Security basics / Cost awareness"
                ],
                "practical_task": "حوّل API المرحلة 6 إلى Docker: FastAPI + Model + MLflow artifact. ثم Dockerfile، Build image، Run container، Environment variables، Push إلى GitHub، Push image إلى ECR، تشغيل الخدمة على AWS، basic monitoring.",
                "youtube_ar": "https://ar.inskillops.com/docs/decouverte/docker/toc/",
                "youtube_en": "https://docs.docker.com/get-started/",
                "questions": [
                    {"text": "ما هو Docker Container؟", "options": {"A": "بيئة تشغيل معزولة للتطبيق", "B": "Database فقط", "C": "Git repository", "D": "ML metric"}, "correct": "A", "difficulty": "easy"},
                    {"text": "S3 تستخدم أساسًا لـ:", "options": {"A": "Object storage", "B": "Model training algorithm", "C": "SQL joins", "D": "API validation"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة IAM؟", "options": {"A": "إدارة permissions والهوية", "B": "تدريب models", "C": "إنشاء plots", "D": "تشغيل Pandas"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Dockerfile؟", "options": {"A": "تعريف كيفية بناء image", "B": "تخزين SQL", "C": "تسجيل metrics", "D": "إنشاء labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من environment variable؟", "options": {"A": "تمرير configuration دون hard-coding", "B": "زيادة accuracy", "C": "تدريب النموذج", "D": "حذف Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا لا نضع AWS access key داخل GitHub؟", "options": {"A": "خطر تسريب credentials", "B": "لأنها تقلل accuracy", "C": "لأنها تمنع Docker", "D": "لأنها تمنع Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Docker image؟", "options": {"A": "حزمة قابلة لإعادة الاستخدام لتشغيل التطبيق", "B": "جدول SQL", "C": "metric", "D": "dataset"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة ECR؟", "options": {"A": "تخزين Docker images في AWS", "B": "تدريب model", "C": "كتابة SQL", "D": "تسجيل Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة CloudWatch؟", "options": {"A": "Monitoring/logging لخدمات AWS", "B": "بناء neural network", "C": "preprocessing", "D": "feature engineering"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما معنى CI؟", "options": {"A": "Continuous Integration", "B": "Cloud Inference", "C": "Computer Index", "D": "Container Input"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم least privilege؟", "options": {"A": "تقليل permissions إلى ما يلزم فقط", "B": "زيادة permissions للجميع", "C": "تعطيل IAM", "D": "حذف authentication"}, "correct": "A", "difficulty": "medium"},
                    {"text": "خدمة ML تحتاج قراءة model من S3 فقط. ما permission الأفضل؟", "options": {"A": "Full Administrator", "B": "S3 read محدد للمورد المطلوب", "C": "Root access", "D": "حذف IAM"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا Docker مفيد لـML deployment؟", "options": {"A": "لتوحيد environment/dependencies", "B": "لأنه يحسن model accuracy تلقائيًا", "C": "لأنه يلغي testing", "D": "لأنه يستبدل Python"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا فشل deployment بسبب missing package، ما السبب الأكثر احتمالًا؟", "options": {"A": "dependency غير موجودة في environment/image", "B": "metric خاطئة", "C": "dataset كبيرة", "D": "Git branch طويل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما التصميم الإنتاجي الأبسط؟", "options": {"A": "Git → CI → Docker → Registry → Deployment → Monitoring", "B": "Notebook → Production مباشرة", "C": "CSV → GitHub password → API", "D": "Training داخل كل API request"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9: Practical Projects
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية المتكاملة",
                "description": "تحويل المهارات إلى Portfolio حقيقي متدرج، بحيث ينتهي الطالب بمشروع Production-Style.",
                "objectives": [
                    "Project architecture",
                    "Requirements / Dataset selection",
                    "Reproducibility",
                    "Experiment design",
                    "Model development / Model serving",
                    "MLOps / Docker / Cloud",
                    "Documentation / Troubleshooting",
                    "Technical presentation"
                ],
                "practical_task": "نفذ 6 مشاريع + Capstone: (1) Beginner ML Pipeline (2) Production Classification (3) ML API (4) Deep Learning (5) MLOps (6) Cloud ML System + Capstone: Real-Time ML Platform مع GitHub كامل.",
                "youtube_ar": "https://mlflow.org/docs/latest/",
                "youtube_en": "https://mlflow.org/docs/latest/",
                "questions": [
                    {"text": "ما أول عنصر يجب تحديده في مشروع ML؟", "options": {"A": "Problem/requirements", "B": "Docker", "C": "Kubernetes", "D": "GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم README؟", "options": {"A": "شرح المشروع وتشغيله", "B": "تدريب النموذج", "C": "زيادة accuracy", "D": "تخزين passwords"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Model API؟", "options": {"A": "إتاحة prediction للأنظمة الأخرى", "B": "حذف dataset", "C": "إنشاء Git branch", "D": "كتابة SQL فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة MLflow في المشروع؟", "options": {"A": "Tracking وإدارة lifecycle", "B": "Image labeling فقط", "C": "Docker replacement", "D": "Database engine"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Docker في المشروع؟", "options": {"A": "توحيد environment", "B": "تحسين accuracy تلقائيًا", "C": "حذف testing", "D": "تغيير algorithm"}, "correct": "A", "difficulty": "easy"},
                    {"text": "مشروعك يحتوي notebook فقط ولا يوجد source code منظم. ما المشكلة؟", "options": {"A": "ضعف reproducibility والصيانة", "B": "accuracy عالية", "C": "Docker زائد", "D": "API سريع"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل مكان لتوثيق طريقة تشغيل المشروع؟", "options": {"A": "README", "B": "model weights فقط", "C": "Git commit message فقط", "D": "screenshot فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك model v1 وv2. ما الأداة المناسبة لإدارة الإصدارات؟", "options": {"A": "Model Registry", "B": "Pandas", "C": "FastAPI", "D": "NumPy"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن تحتوي المشاريع على tests؟", "options": {"A": "اكتشاف regressions والأخطاء", "B": "زيادة dataset", "C": "تغيير labels", "D": "حذف API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجب أن يحتويه Architecture Diagram؟", "options": {"A": "المكونات وتدفق البيانات بينها", "B": "أسماء أعضاء الفريق فقط", "C": "ألوان المشروع", "D": "Git stars"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نضيف monitoring؟", "options": {"A": "معرفة صحة النظام والأداء بعد deployment", "B": "تدريب model كل دقيقة", "C": "حذف logs", "D": "تغيير Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أعدت تشغيل training pipeline فأنتجت نتائج مختلفة دون تغيير الكود. ما الذي تفحصه؟", "options": {"A": "random seeds/data version/dependencies", "B": "لون README", "C": "اسم Docker image فقط", "D": "GitHub stars"}, "correct": "A", "difficulty": "hard"},
                    {"text": "النموذج جيد Offline لكنه سيئ بعد deployment. ما الاحتمال؟", "options": {"A": "Training-serving skew أو اختلاف البيانات", "B": "README ناقص", "C": "Git branch قصير", "D": "Docker logo"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أفضل ترتيب للمشروع؟", "options": {"A": "Problem → Data → Train → Evaluate → Package → Deploy → Monitor", "B": "Deploy → Problem → Train", "C": "API → Delete data → Train", "D": "Docker → README → Problem"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الذي يجعل Capstone قويًا وظيفيًا؟", "options": {"A": "التكامل بين model + engineering + deployment + monitoring", "B": "عدد notebooks فقط", "C": "عدد المكتبات", "D": "طول README"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10: Professional Preparation
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 Portfolio وProfessional Preparation وJob Ready",
                "description": "تحويل المعرفة والمشاريع إلى جاهزية حقيقية لوظيفة Junior / Entry-Level ML Engineer.",
                "objectives": [
                    "ML Engineer CV",
                    "GitHub portfolio",
                    "Project presentation",
                    "LinkedIn",
                    "Technical interview",
                    "Python interview / SQL basics",
                    "ML theory / Model evaluation",
                    "ML system design",
                    "Model serving / MLOps scenarios",
                    "Debugging / Behavioral questions",
                    "Job applications / Technical assessment"
                ],
                "practical_task": "أنشئ Job-Ready Package: GitHub مرتب، 5-6 مشاريع، Capstone كامل، CV مخصص، LinkedIn، README احترافي، Architecture diagrams، SQL practice، Python practice، Mock interview شامل.",
                "youtube_ar": "https://developers.google.com/machine-learning/crash-course",
                "youtube_en": "https://developers.google.com/machine-learning/crash-course",
                "questions": [
                    {"text": "ما أهم شيء في CV لمهندس ML مبتدئ؟", "options": {"A": "قائمة طويلة من الكورسات فقط", "B": "مشاريع ومهارات يمكن إثباتها", "C": "عدد المتابعين", "D": "صورة كبيرة"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ماذا يجب أن يحتوي GitHub project؟", "options": {"A": "README وتشغيل واضح وكود", "B": "screenshots فقط", "C": "model فقط", "D": "اسم المشروع فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Technical Interview؟", "options": {"A": "قياس القدرة على تطبيق المعرفة", "B": "معرفة عدد الشهادات فقط", "C": "معرفة عدد GitHub stars", "D": "معرفة سرعة الإنترنت"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن تشرحه في مشروع ML؟", "options": {"A": "المشكلة والبيانات والنموذج والنتائج والقيود", "B": "اسم Python فقط", "C": "لون الواجهة", "D": "عدد الملفات فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ model deployment؟", "options": {"A": "جعل النموذج متاحًا للاستخدام", "B": "تدريب dataset", "C": "حذف model", "D": "كتابة SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "في مقابلة سألك المحاور لماذا اخترت F1؟", "options": {"A": "يجب شرح العلاقة بين Precision وRecall وbusiness requirement", "B": "تقول لأنه أشهر metric", "C": "تقول لأنه دائمًا الأفضل", "D": "لا تحتاج تفسير"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا فشل model في production، ماذا تفعل؟", "options": {"A": "Debug logs + inputs + model version + dependencies", "B": "تحذف المشروع", "C": "تغير algorithm مباشرة", "D": "تعيد التدريب دون تحقيق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Architecture Diagram مهم؟", "options": {"A": "يوضح مكونات النظام وتدفق البيانات", "B": "يرفع accuracy", "C": "يسرع GPU", "D": "يستبدل README"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا سألك المحاور عن overfitting، ما الحلول المحتملة؟", "options": {"A": "regularization / more data / simpler model / augmentation حسب الحالة", "B": "حذف validation", "C": "زيادة epochs دائمًا", "D": "حذف test"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجب أن يكون في LinkedIn؟", "options": {"A": "مشاريع ومهارات وتقنيات حقيقية", "B": "شهادات غير موجودة", "C": "skills غير مستخدمة", "D": "أسماء أدوات فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا تفعل إذا لم تعرف إجابة سؤال تقني؟", "options": {"A": "توضح ما تعرفه وتشرح كيف ستبحث/تختبر الحل", "B": "تختلق الإجابة", "C": "تغير الموضوع", "D": "تقول إن السؤال خاطئ"}, "correct": "A", "difficulty": "medium"},
                    {"text": "صمم نظامًا يخدم ملايين predictions. ما أول شيء تفكر فيه؟", "options": {"A": "scalability + latency + availability + model versioning + monitoring", "B": "لون API", "C": "README", "D": "عدد notebooks"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج accuracy فيه 98% لكن business يقول إنه غير مفيد. ما الاحتمال؟", "options": {"A": "Metric لا تمثل الهدف الحقيقي", "B": "Python خطأ", "C": "Docker خطأ بالضرورة", "D": "Git ناقص"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في مقابلة طُلب منك تحسين model. ما أفضل إجابة؟", "options": {"A": "تحديد المشكلة والـbaseline ثم تحليل errors وتجربة تغييرات وقياسها", "B": "تغيير algorithm عشوائيًا", "C": "زيادة epochs فقط", "D": "إضافة 100 feature"}, "correct": "A", "difficulty": "hard"},
                    {"text": "متى تعلن نفسك Job Ready؟", "options": {"A": "بعد مشاهدة الكورسات", "B": "بعد الشهادة", "C": "بعد امتلاك Notebook واحد", "D": "بعد اجتياز التقييم العملي وإثبات المهارات الأساسية"}, "correct": "D", "difficulty": "hard"}
                ]
            }
        ]
    }
]