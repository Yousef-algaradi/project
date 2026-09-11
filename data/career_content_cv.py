# data/career_content_cv.py
# بنك محتوى مسار "مهندس الرؤية الحاسوبية (Computer Vision Engineer)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

CV_ENGINEER_PATHS = [
    {
        "major_key": "ai",
        "slug": "cv-engineer",
        "title": "مهندس رؤية حاسوبية (Computer Vision)",
        "description": "مسار متكامل: Python + NumPy + OpenCV + PyTorch + YOLO + FastAPI + Docker + AWS.",
        "icon": "👁️",
        "difficulty": "متقدم",
        "estimated_hours": 280,
        "order_index": 2,
        "stages": [
            # ==========================================
            # المرحلة 1: Programming, Mathematics & AI Foundations
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات البرمجة والرياضيات وAI",
                "description": "بناء الأساس البرمجي والرياضي الذي تحتاجه لفهم وتنفيذ خوارزميات Computer Vision وDeep Learning.",
                "objectives": [
                    "Python fundamentals",
                    "Functions & OOP basics",
                    "Lists, dictionaries, NumPy arrays",
                    "File handling",
                    "Virtual environments",
                    "Git/GitHub basics",
                    "Jupyter/Colab",
                    "Linear algebra basics",
                    "Vectors & matrices",
                    "Probability & statistics basics",
                    "Derivatives & gradients",
                    "Train/validation/test concepts"
                ],
                "practical_task": "أنشئ مشروع cv-foundations: قراءة CSV، معالجة البيانات باستخدام NumPy، دوال حسابية، 5 unit tests، Git repository، Notebook يطبق vector operations و matrix multiplication و mean و variance و normalization.",
                "youtube_ar": "https://elzero.org/learning-python/",
                "youtube_en": "https://cs50.harvard.edu/python/courses/",
                "questions": [
                    {"text": "ما نوع البيانات الأنسب لتخزين عدة قيم مرتبة ويمكن تعديلها في Python؟", "options": {"A": "Tuple", "B": "List", "C": "Set", "D": "String"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما نتيجة np.array([1,2,3]) * 2؟", "options": {"A": "[1,2,3,2]", "B": "[2]", "C": "[2,4,6]", "D": "Error"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما وظيفة Virtual Environment؟", "options": {"A": "عزل dependencies الخاصة بالمشروع", "B": "تسريع الإنترنت", "C": "ضغط الصور", "D": "تدريب النموذج"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي أمر ينشئ Git repository؟", "options": {"A": "git push", "B": "git clone", "C": "git commit", "D": "git init"}, "correct": "D", "difficulty": "easy"},
                    {"text": "أي مقياس يعبّر عن متوسط مربعات الانحراف عن المتوسط؟", "options": {"A": "Mean", "B": "Variance", "C": "Median", "D": "Mode"}, "correct": "B", "difficulty": "easy"},
                    {"text": "إذا كان vector = [1,2,3]، فما ناتج ضربه في scalar قيمته 3؟", "options": {"A": "[1,2,9]", "B": "[3,2,1]", "C": "[3,6,9]", "D": "[1,6,3]"}, "correct": "C", "difficulty": "medium"},
                    {"text": "لماذا نستخدم normalization للبيانات؟", "options": {"A": "لتوحيد نطاق القيم وتحسين بعض الخوارزميات", "B": "لحذف جميع البيانات", "C": "لزيادة حجم الصور", "D": "لتحويل Python إلى C++"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك بيانات 1000 صورة. قسمت 800 للتدريب و100 للتحقق و100 للاختبار. ما وظيفة test set؟", "options": {"A": "تعديل الأوزان", "B": "اختيار learning rate", "C": "التدريب", "D": "التقييم النهائي غير المستخدم أثناء التدريب"}, "correct": "D", "difficulty": "medium"},
                    {"text": "ما وظيفة try/except؟", "options": {"A": "إنشاء صورة", "B": "التعامل مع exceptions", "C": "إنشاء Git branch", "D": "تحميل GPU"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كان Matrix A أبعاده 2×3 وB أبعاده 3×4، فما أبعاد A×B؟", "options": {"A": "2×4", "B": "3×3", "C": "4×2", "D": "2×3"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Git في مشروع Computer Vision؟", "options": {"A": "لتحويل الصور", "B": "لتدريب CNN", "C": "لتتبع تغييرات الكود", "D": "لزيادة دقة النموذج"}, "correct": "C", "difficulty": "medium"},
                    {"text": "لديك نموذج يعطي دقة عالية على التدريب ودقة منخفضة على validation. ما المشكلة الأكثر احتمالًا؟", "options": {"A": "Underflow", "B": "Overfitting", "C": "Missing GPU", "D": "Git conflict"}, "correct": "B", "difficulty": "hard"},
                    {"text": "إذا كان gradient موجبًا في اتجاه معين، ماذا يحدث عادة عند تطبيق Gradient Descent؟", "options": {"A": "يتحرك parameter في الاتجاه المعاكس للـgradient", "B": "يثبت parameter دائمًا", "C": "يزيد loss عمدًا", "D": "يحذف parameter"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا ينبغي استخدام test set لاختيار hyperparameters؟", "options": {"A": "لأنه صغير دائمًا", "B": "لأنه لا يحتوي صورًا", "C": "لأنه يسبب تسريبًا لمعلومات الاختبار", "D": "لأنه لا يعمل مع Python"}, "correct": "C", "difficulty": "hard"},
                    {"text": "لديك مصفوفة NumPy بحجم (100, 64, 64, 3). ماذا تمثل غالبًا؟", "options": {"A": "100 صورة RGB بحجم 64×64", "B": "صورة واحدة بحجم 100×64", "C": "3 صور فقط", "D": "100 قناة لصورة واحدة"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2: Image Processing & OpenCV
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ معالجة الصور وOpenCV",
                "description": "فهم الصورة كبيانات رقمية والقدرة على قراءتها ومعالجتها وتحويلها واستخراج المعلومات الأساسية منها باستخدام OpenCV.",
                "objectives": [
                    "Pixels / Channels / RGB-BGR",
                    "Grayscale / Resolution",
                    "Image resizing / Cropping / Rotation / Translation",
                    "Thresholding / Blurring / Gaussian blur",
                    "Edge detection / Morphology",
                    "Histograms / Color spaces / Contours",
                    "Video frames / Webcam input"
                ],
                "practical_task": "أنشئ Image Processing Toolkit: Input Image → Resize → Grayscale → Blur → Canny → Threshold → Morphology → Contours → Output. معالجة صورة ومقطع فيديو، حفظ النتائج.",
                "youtube_ar": "https://docs.opencv.org/4.5.2/d6/d00/tutorial_py_root.html",
                "youtube_en": "https://docs.opencv.org/4.5.2/d6/d00/tutorial_py_root.html",
                "questions": [
                    {"text": "ما أصغر وحدة أساسية في الصورة الرقمية؟", "options": {"A": "Pixel", "B": "Layer", "C": "Kernel", "D": "Model"}, "correct": "A", "difficulty": "easy"},
                    {"text": "الصورة Grayscale تحتوي عادة على؟", "options": {"A": "قناة واحدة", "B": "4 قنوات", "C": "3 قنوات RGB", "D": "10 قنوات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة cv.imread()؟", "options": {"A": "تدريب نموذج", "B": "قراءة صورة", "C": "اكتشاف كائن", "D": "ضغط فيديو"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما فائدة Resize؟", "options": {"A": "تغيير أبعاد الصورة", "B": "حذف metadata", "C": "تدريب CNN", "D": "اكتشاف الحواف فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي Color Space يحتوي على Hue وSaturation وValue؟", "options": {"A": "RGB", "B": "BGR", "C": "HSV", "D": "Gray"}, "correct": "C", "difficulty": "easy"},
                    {"text": "لماذا يستخدم Gaussian Blur قبل Edge Detection أحيانًا؟", "options": {"A": "لإضافة noise", "B": "لتقليل noise", "C": "لزيادة عدد القنوات", "D": "لتغيير النموذج"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ماذا تنتج Canny Edge Detection أساسًا؟", "options": {"A": "خريطة للحواف", "B": "تصنيفًا للصورة", "C": "Bounding boxes", "D": "Segmentation masks"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة Thresholding؟", "options": {"A": "تحويل القيم وفق عتبة معينة", "B": "تدريب YOLO", "C": "حساب Accuracy", "D": "تحميل CUDA"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Morphological Opening؟", "options": {"A": "إزالة بعض الأجسام/النقاط الصغيرة noise", "B": "زيادة resolution", "C": "تدريب CNN", "D": "إضافة RGB channel"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت صورة RGB حجمها 640×480، فكم عدد القنوات؟", "options": {"A": "1", "B": "2", "C": "3", "D": "640"}, "correct": "C", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Contours؟", "options": {"A": "لتتبع أشكال/حدود الأجسام", "B": "لتدريب transformer", "C": "لإنشاء database", "D": "لتثبيت OpenCV"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك صورة فيها نص أسود على خلفية بيضاء غير متجانسة الإضاءة. أي خيار قد يكون أفضل من global threshold؟", "options": {"A": "Adaptive thresholding", "B": "Random crop", "C": "Max pooling", "D": "Dropout"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا استخدمت img[100:200, 50:150] في NumPy/OpenCV، ماذا تحصل؟", "options": {"A": "Channel جديد", "B": "Region of Interest", "C": "Model", "D": "Histogram فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا قد تفشل Edge Detection إذا كانت الصورة مليئة بالـnoise؟", "options": {"A": "لأن noise ينتج edges وهمية", "B": "لأن الصورة تصبح RGB", "C": "لأن OpenCV لا يدعم الصور", "D": "لأن Canny يحتاج SQL"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك فيديو 30 FPS وتريد معالجة كل frame. ماذا يمثل كل iteration في loop؟", "options": {"A": "Epoch", "B": "Batch", "C": "Frame", "D": "Kernel"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3: ML for Computer Vision
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ Machine Learning للرؤية الحاسوبية",
                "description": "فهم أساسيات Machine Learning وتقييم النماذج وتحضير البيانات، ثم استخدامها كنقطة انتقال إلى Deep Learning.",
                "objectives": [
                    "Supervised / Unsupervised learning",
                    "Features / Labels",
                    "Classification / Regression",
                    "Train/validation/test",
                    "Data leakage / Overfitting / Underfitting",
                    "Cross-validation",
                    "Precision / Recall / F1-score",
                    "Confusion matrix",
                    "ROC-AUC basics",
                    "scikit-learn / Feature extraction"
                ],
                "practical_task": "استخدم Dataset للصور: Images → Feature Extraction → Train/Validation/Test → SVM/Random Forest → Confusion Matrix → Precision/Recall/F1. اكتب تقريرًا من صفحة واحدة.",
                "youtube_ar": "https://academy.hsoub.com/programming/artificial-intelligence/تعلم-الآلة/",
                "youtube_en": "https://www.deeplearning.ai/courses/machine-learning-specialization/",
                "questions": [
                    {"text": "في Classification، ما المقصود بالLabel؟", "options": {"A": "Target class", "B": "Image resolution", "C": "GPU", "D": "Optimizer"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة confusion matrix؟", "options": {"A": "ضغط الصور", "B": "عرض أنواع التوقعات الصحيحة والخاطئة", "C": "تدريب CNN", "D": "تغيير learning rate"}, "correct": "B", "difficulty": "easy"},
                    {"text": "Precision يقيس؟", "options": {"A": "نسبة التوقعات الموجبة الصحيحة من كل التوقعات الموجبة", "B": "حجم الصورة", "C": "سرعة GPU", "D": "عدد epochs"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المشكلة عندما يكون النموذج ممتازًا على training وضعيفًا على unseen data؟", "options": {"A": "Underfitting", "B": "Overfitting", "C": "Quantization", "D": "Padding"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي مكتبة تستخدم كثيرًا في classical ML في Python؟", "options": {"A": "scikit-learn", "B": "OpenCV فقط", "C": "FastAPI", "D": "Docker"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كان FN مرتفعًا، فما الذي يعاني منه النموذج؟", "options": {"A": "يكتشف positives أكثر من اللازم", "B": "يفشل في اكتشاف positives كثيرة", "C": "لا يستخدم GPU", "D": "لا يستطيع قراءة الصور"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نستخدم validation set؟", "options": {"A": "لاختيار model/hyperparameters أثناء التطوير", "B": "لتخزين الصور فقط", "C": "لتدريب database", "D": "لتثبيت Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما معنى Data Leakage؟", "options": {"A": "فقدان الصور", "B": "دخول معلومات من خارج التدريب بطريقة غير صحيحة إلى عملية التعلم", "C": "ضغط dataset", "D": "زيادة batch size"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كانت classes غير متوازنة جدًا، ما metric قد يكون أفضل من accuracy وحدها؟", "options": {"A": "F1", "B": "Resolution", "C": "FPS", "D": "RAM"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن يكون preprocessing في train وvalidation متسقًا؟", "options": {"A": "حتى يتلقى النموذج بيانات متشابهة التوزيع", "B": "لزيادة عدد labels", "C": "لحذف test set", "D": "لتقليل حجم GPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة cross-validation؟", "options": {"A": "تقدير أداء النموذج عبر تقسيمات متعددة للبيانات", "B": "تحويل RGB إلى BGR", "C": "تشغيل webcam", "D": "تصغير الصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "نموذج لديه Accuracy=98% على dataset يكون 98% منها class A. ما المشكلة؟", "options": {"A": "Accuracy قد تكون مضللة بسبب class imbalance", "B": "النموذج مثالي", "C": "الصور لا يمكن استخدامها", "D": "CNN لا تعمل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "تريد اكتشاف مرض نادر، وفقدان حالة إيجابية أخطر من false alarm. أي metric يجب التركيز عليه؟", "options": {"A": "Recall", "B": "Resolution", "C": "FPS", "D": "MAE"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا استخدمت test set لاختيار أفضل hyperparameter ثم أعلنت أداء الاختبار، ما المشكلة؟", "options": {"A": "Test leakage", "B": "Underfitting", "C": "Data augmentation", "D": "Normalization"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك feature extractor قوي لكن classifier ضعيف. ما أول شيء منطقي؟", "options": {"A": "تقييم جودة features وclassifier بشكل منفصل قبل تغيير كل النظام", "B": "حذف dataset", "C": "تغيير Python", "D": "إزالة labels"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4: Deep Learning & PyTorch
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ Deep Learning وPyTorch",
                "description": "الانتقال من ML التقليدي إلى Deep Learning وفهم كيفية بناء وتدريب Neural Networks باستخدام PyTorch.",
                "objectives": [
                    "Tensors / Neural networks",
                    "Layers / Forward pass",
                    "Loss functions / Backpropagation",
                    "Gradients / Optimizers / Learning rate",
                    "Batch size / Epoch",
                    "Dataset/DataLoader",
                    "GPU/CUDA basics",
                    "Training loop / Validation loop",
                    "Checkpoints",
                    "Overfitting / Regularization"
                ],
                "practical_task": "ابنِ classifier بسيطًا باستخدام PyTorch: Dataset → DataLoader → Model → Loss → Optimizer → Training → Validation → Checkpoint. طبقه على MNIST أو Fashion-MNIST.",
                "youtube_ar": "https://academy.hsoub.com/learn/artificial-intelligence/",
                "youtube_en": "https://docs.pytorch.org/tutorials/",
                "questions": [
                    {"text": "ما Tensor في PyTorch؟", "options": {"A": "بنية بيانات متعددة الأبعاد", "B": "صورة فقط", "C": "Database", "D": "API"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Loss Function؟", "options": {"A": "قياس خطأ التوقع", "B": "تحميل الصور فقط", "C": "حفظ Git", "D": "تشغيل webcam"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Optimizer؟", "options": {"A": "تحديث parameters", "B": "قراءة JPEG", "C": "رسم bounding box", "D": "ضغط النموذج"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Epoch تعني؟", "options": {"A": "مرور كامل على training dataset", "B": "صورة واحدة", "C": "طبقة واحدة", "D": "GPU واحدة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "DataLoader يساعد في؟", "options": {"A": "تحميل batches من البيانات", "B": "إنشاء API", "C": "Docker build", "D": "تغيير resolution فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم model.eval() أثناء validation؟", "options": {"A": "لتعطيل بعض سلوكيات التدريب مثل Dropout", "B": "لبدء training", "C": "لتغيير labels", "D": "لحذف gradients دائمًا"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة torch.no_grad() أثناء inference؟", "options": {"A": "تقليل حسابات gradients والذاكرة", "B": "زيادة حجم model", "C": "تدريب model أسرع", "D": "تغيير classes"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان learning rate كبيرًا جدًا، ماذا قد يحدث؟", "options": {"A": "التدريب قد يتذبذب أو لا يتقارب", "B": "النموذج يصبح دائمًا أفضل", "C": "الصور تختفي", "D": "GPU تتحول إلى CPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم checkpoint؟", "options": {"A": "حفظ حالة النموذج أثناء التدريب", "B": "تغيير الصورة", "C": "حذف البيانات", "D": "زيادة عدد classes"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما دور batch size؟", "options": {"A": "عدد العينات المستخدمة في خطوة تحديث واحدة", "B": "عدد classes", "C": "حجم الصورة فقط", "D": "عدد layers"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين training وinference؟", "options": {"A": "التدريب يحدث فيه تحديث للparameters، inference لا", "B": "inference يحتاج labels دائمًا", "C": "التدريب لا يستخدم بيانات", "D": "لا يوجد فرق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "training loss ينخفض لكن validation loss يرتفع باستمرار. ماذا تفعل؟", "options": {"A": "زيادة epochs بلا حدود", "B": "معالجة overfitting مثل augmentation/regularization/early stopping", "C": "حذف validation", "D": "زيادة learning rate دائمًا"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا نستخدم GPU في Deep Learning؟", "options": {"A": "لتنفيذ عمليات tensor المتوازية بكفاءة", "B": "لأنها ضرورية لكل Python", "C": "لأنها تخزن labels فقط", "D": "لأنها تستبدل optimizer"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا نسيت optimizer.zero_grad() في training loop التقليدي، ماذا قد يحدث؟", "options": {"A": "تتراكم gradients من خطوات سابقة", "B": "تختفي البيانات", "C": "يتوقف Python", "D": "تتحول الصور إلى grayscale"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك model مدرب على GPU وتحاول inference على CPU دون نقل model/data. ما المشكلة؟", "options": {"A": "Device mismatch", "B": "Overfitting", "C": "Class imbalance", "D": "Augmentation"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5: CNNs & Image Classification
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ CNNs وتصنيف الصور",
                "description": "إتقان CNNs وتصنيف الصور باستخدام Transfer Learning بدل تدريب شبكات ضخمة من الصفر.",
                "objectives": [
                    "Convolution / Kernels / Feature maps",
                    "Padding / Stride",
                    "Pooling / ReLU / Fully connected layers",
                    "CNN architecture",
                    "Data augmentation",
                    "Transfer learning / Fine-tuning",
                    "Class imbalance",
                    "Image classification metrics",
                    "Confusion matrix",
                    "Grad-CAM basics"
                ],
                "practical_task": "ابنِ Image Classification System: Dataset → Augmentation → Pretrained CNN → Fine-tuning → Evaluation → Confusion Matrix → Inference. استخدام dataset من فئتين إلى خمس فئات.",
                "youtube_ar": "https://academy.hsoub.com/learn/artificial-intelligence/",
                "youtube_en": "https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html",
                "questions": [
                    {"text": "ما الوظيفة الأساسية لـConvolution في CNN؟", "options": {"A": "استخراج features", "B": "إنشاء database", "C": "تشغيل API", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة ReLU؟", "options": {"A": "Activation function", "B": "Optimizer", "C": "Dataset", "D": "Metric"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Pooling؟", "options": {"A": "تقليل الأبعاد المكانية واستخراج تمثيل أكثر ثباتًا", "B": "زيادة labels", "C": "حفظ النموذج", "D": "إنشاء API"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يعني Transfer Learning؟", "options": {"A": "استخدام معرفة من نموذج pretrained لمهمة جديدة", "B": "نقل الملفات بين الحواسيب", "C": "تغيير Python", "D": "حذف layers"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Data Augmentation؟", "options": {"A": "إنشاء تنوع إضافي في training data", "B": "حذف validation", "C": "تقليل classes", "D": "زيادة labels يدويًا"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يحدث غالبًا عند زيادة stride في convolution؟", "options": {"A": "يقل spatial resolution", "B": "تزيد الصورة دائمًا", "C": "يزيد عدد labels", "D": "يصبح النموذج غير قابل للتدريب"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم pretrained model؟", "options": {"A": "للاستفادة من features تعلمها من dataset كبير", "B": "لأنه لا يحتاج بيانات", "C": "لأنه لا يحتاج validation", "D": "لأنه لا يحتاج inference"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت الصور 224×224×3، ماذا يمثل 3؟", "options": {"A": "RGB channels", "B": "classes", "C": "epochs", "D": "filters"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما خطر augmentation غير المناسب؟", "options": {"A": "قد يغير معنى الصورة أو يخلق بيانات غير واقعية", "B": "يحسن دائمًا الأداء", "C": "يلغي الحاجة إلى labels", "D": "يجعل CNN تعمل بدون training"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهدف من fine-tuning؟", "options": {"A": "تكييف pretrained model مع المهمة الجديدة", "B": "حذف optimizer", "C": "تغيير GPU", "D": "ضغط الصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم confusion matrix؟", "options": {"A": "لمعرفة أخطاء classification بين classes", "B": "لحفظ weights", "C": "لزيادة resolution", "D": "لإنشاء API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك 100 صورة فقط لكل class وmodel كبير pretrained. ما الاستراتيجية الأكثر منطقية؟", "options": {"A": "Train from scratch", "B": "Transfer learning + augmentation + careful validation", "C": "حذف validation", "D": "زيادة parameters"}, "correct": "B", "difficulty": "hard"},
                    {"text": "training accuracy = 99% وvalidation = 70%. ما الإجراء الأكثر منطقية؟", "options": {"A": "معالجة overfitting", "B": "حذف pretrained weights", "C": "استخدام test أثناء التدريب", "D": "رفع epochs فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا قد يكون accuracy غير كافٍ في classification؟", "options": {"A": "لأنه لا يوضح أخطاء كل class عند imbalance", "B": "لأنه لا يمكن حسابه", "C": "لأنه خاص بـregression", "D": "لأنه لا يستخدم labels"}, "correct": "A", "difficulty": "hard"},
                                       {"text": "لماذا نستخدم Grad-CAM؟", "options": {"A": "لفهم المناطق التي أثرت في قرار CNN", "B": "لتغيير optimizer", "C": "لزيادة FPS", "D": "لإنشاء Docker image"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6: Object Detection, Segmentation & Tracking
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ Object Detection والتقسيم والتتبع",
                "description": "الانتقال من سؤال 'ما الموجود في الصورة؟' إلى 'أين يوجد؟ وما شكله؟ وكيف أتبعه عبر الفيديو؟'",
                "objectives": [
                    "Object Detection",
                    "Bounding boxes / IoU",
                    "Precision/Recall / mAP / NMS",
                    "YOLO",
                    "Dataset annotation / YOLO format",
                    "Object detection training",
                    "Instance segmentation",
                    "Semantic segmentation basics",
                    "Object tracking / Multi-object tracking",
                    "FPS/latency"
                ],
                "practical_task": "ابنِ Real-Time Object Detection: Video/Webcam → YOLO → Bounding Boxes → Confidence → FPS. اجمع Dataset صغير، Annotate 2-3 classes، Train pretrained YOLO، Evaluate، شغل inference على فيديو، احسب FPS، وثق الأخطاء.",
                "youtube_ar": "https://docs.ultralytics.com/modes/train",
                "youtube_en": "https://docs.ultralytics.com/modes/train",
                "questions": [
                    {"text": "ماذا يمثل Bounding Box؟", "options": {"A": "موقع الكائن", "B": "لون الصورة فقط", "C": "optimizer", "D": "dataset"}, "correct": "A", "difficulty": "easy"},
                    {"text": "IoU يقارن؟", "options": {"A": "تداخل bounding boxes", "B": "سرعة GPU", "C": "عدد epochs", "D": "أبعاد model"}, "correct": "A", "difficulty": "easy"},
                    {"text": "YOLO يستخدم أساسًا لـ؟", "options": {"A": "Object Detection", "B": "SQL", "C": "Text generation", "D": "Audio"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يعني confidence score؟", "options": {"A": "درجة ثقة النموذج في prediction", "B": "حجم الصورة", "C": "عدد pixels", "D": "عدد epochs"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة NMS؟", "options": {"A": "إزالة detections المتداخلة غير الضرورية", "B": "تدريب database", "C": "زيادة resolution", "D": "تغيير labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "إذا كان predicted box يتطابق تمامًا مع ground truth، فإن IoU؟", "options": {"A": "0", "B": "0.25", "C": "0.5", "D": "1"}, "correct": "D", "difficulty": "medium"},
                    {"text": "لماذا تحتاج object detection إلى annotations أكثر من classification؟", "options": {"A": "لأنها تحتاج مواقع الأجسام أيضًا", "B": "لأنها لا تستخدم images", "C": "لأنها لا تستخدم labels", "D": "لأنها لا تحتاج model"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا تنتج instance segmentation؟", "options": {"A": "Mask لكل object", "B": "Class واحدة للصورة فقط", "C": "Text فقط", "D": "Audio"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يعني mAP في detection؟", "options": {"A": "Metric لتقييم detection عبر classes/thresholds", "B": "عدد الصور", "C": "سرعة التدريب", "D": "حجم النموذج"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نقيس FPS في real-time vision؟", "options": {"A": "لمعرفة سرعة معالجة الفيديو", "B": "لمعرفة عدد classes", "C": "لحساب loss فقط", "D": "لتغيير labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما سبب شائع لفشل detector في صور لم ير مثلها؟", "options": {"A": "Domain shift", "B": "Git", "C": "Docker", "D": "SQL"}, "correct": "A", "difficulty": "medium"},
                    {"text": "detector يعطي عدة boxes لنفس الجسم. ما العملية المناسبة؟", "options": {"A": "NMS", "B": "Dropout", "C": "PCA", "D": "BatchNorm"}, "correct": "A", "difficulty": "hard"},
                    {"text": "تريد نظامًا يكتشف السيارات ويتتبع كل سيارة عبر الفيديو. ماذا تحتاج فوق detection؟", "options": {"A": "Tracking", "B": "Regression فقط", "C": "OCR فقط", "D": "Classification فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا رفعت IoU threshold في NMS، ما الأثر المحتمل؟", "options": {"A": "السماح ببقاء boxes أكثر قبل حذفها", "B": "حذف كل boxes", "C": "زيادة classes", "D": "إلغاء inference"}, "correct": "A", "difficulty": "hard"},
                    {"text": "model دقيق لكنه بطيء جدًا للتطبيق على كاميرا مباشرة. ما المشكلة الأساسية؟", "options": {"A": "Accuracy فقط", "B": "Deployment latency", "C": "Label encoding", "D": "Dataset naming"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7: Advanced Computer Vision
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ Computer Vision المتقدم (Video, OCR, Pose & ViT)",
                "description": "توسيع قدراتك بعد إتقان classification وdetection إلى مهام Vision عملية متقدمة.",
                "objectives": [
                    "Video understanding",
                    "Frame sampling",
                    "Object tracking",
                    "Optical flow basics",
                    "OCR concepts",
                    "Pose estimation / Keypoints",
                    "Instance segmentation",
                    "Vision Transformers — ViT concepts",
                    "Attention basics",
                    "Multimodal vision concepts",
                    "Model selection",
                    "Real-time constraints"
                ],
                "practical_task": "اختر مسارًا واحدًا فقط كـ Advanced Mini System — الخيار الأساسي: Video Analytics. مثال: Video → Detection → Tracking → Event Logic → Output (عدّ الأشخاص الذين يدخلون منطقة).",
                "youtube_ar": "https://docs.pytorch.org/tutorials/domains.html",
                "youtube_en": "https://docs.pytorch.org/tutorials/domains.html",
                "questions": [
                    {"text": "ماذا يمثل Keypoint في Pose Estimation؟", "options": {"A": "نقطة مهمة مثل مفصل", "B": "class فقط", "C": "optimizer", "D": "pixel عشوائي"}, "correct": "A", "difficulty": "easy"},
                    {"text": "OCR يستخدم أساسًا لـ؟", "options": {"A": "استخراج النص من الصور", "B": "اكتشاف الحركة فقط", "C": "تدريب GPU", "D": "segmentation فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Tracking يعني؟", "options": {"A": "متابعة هوية/مسار object عبر frames", "B": "تصنيف صورة واحدة فقط", "C": "ضغط الفيديو", "D": "تغيير resolution"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ViT اختصار لـ؟", "options": {"A": "Vision Transformer", "B": "Video Image Tool", "C": "Visual Input Tensor", "D": "Vector Image Training"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Frame sampling يستخدم لـ؟", "options": {"A": "اختيار frames لمعالجتها", "B": "تغيير labels", "C": "حذف model", "D": "إنشاء database"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا لا نعالج كل frame دائمًا؟", "options": {"A": "لتقليل computational cost", "B": "لأن frames لا تحتوي بيانات", "C": "لأن YOLO لا يدعم الفيديو", "D": "لأن tracking غير ممكن"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Pose Estimation يخرج عادة؟", "options": {"A": "Keypoints", "B": "SQL rows", "C": "Text embeddings فقط", "D": "Database indexes"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يميز Instance Segmentation عن Object Detection؟", "options": {"A": "يعطي mask لكل instance", "B": "لا يستخدم classes", "C": "لا يستخدم الصور", "D": "لا يحتاج model"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا ViT يستخدم Attention؟", "options": {"A": "لالتقاط العلاقات بين أجزاء الصورة", "B": "لتحويل الصورة إلى SQL", "C": "لتقليل RAM دائمًا", "D": "لحذف labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا tracking مفيد في counting؟", "options": {"A": "لمنع عدّ نفس object في كل frame ككائن جديد", "B": "لزيادة resolution", "C": "لتغيير class", "D": "لتدريب model"}, "correct": "A", "difficulty": "medium"},
                    {"text": "في OCR، preprocessing الجيد قد يساعد في؟", "options": {"A": "تحسين قابلية قراءة النص", "B": "زيادة عدد objects", "C": "تغيير GPU", "D": "إزالة model"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك فيديو 30 FPS والنظام يستطيع معالجة 10 FPS فقط. ماذا تفعل؟", "options": {"A": "معالجة كل frame مهما كان", "B": "frame skipping/sampling أو تحسين model", "C": "حذف detection", "D": "زيادة labels"}, "correct": "B", "difficulty": "hard"},
                    {"text": "في tracking، يختفي object لمدة frame ثم يظهر مجددًا. ماذا يمثل هذا؟", "options": {"A": "تحدي association/occlusion", "B": "SQL problem", "C": "normalization", "D": "augmentation فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "متى قد تختار نموذج Vision Transformer بدل CNN؟", "options": {"A": "عندما تناسب المهمة/data والموارد advantages الخاصة بالAttention", "B": "لأنه دائمًا أسرع", "C": "لأنه لا يحتاج training", "D": "لأنه لا يستخدم images"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك camera system محدود GPU. ما القرار المهني الصحيح؟", "options": {"A": "اختيار أكبر model دائمًا", "B": "قياس accuracy/latency والموازنة بينهما", "C": "تجاهل latency", "D": "تجاهل accuracy"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8: Deployment, MLOps, Docker & Cloud
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ نشر الرؤية الحاسوبية وDocker وCloud",
                "description": "تحويل النموذج من Notebook إلى خدمة حقيقية قابلة للتشغيل والتحديث والمراقبة.",
                "objectives": [
                    "Model serialization",
                    "Inference pipelines / FastAPI / REST API",
                    "Docker / Dockerfile / Environment variables",
                    "GitHub / Logging / Model versioning",
                    "Basic monitoring / CPU/GPU inference",
                    "ONNX basics / Cloud storage",
                    "AWS S3 / AWS EC2 basics / IAM basics",
                    "Deployment architecture / Latency / Throughput",
                    "Model optimization basics"
                ],
                "practical_task": "حوّل نموذج Detection من المرحلة 6 إلى: Image → FastAPI → Model Inference → JSON Response. ثم FastAPI → Docker → Container. الـAPI يعيد: class, confidence, bounding_box, inference_time.",
                "youtube_ar": "https://fastapi.tiangolo.com/deployment/docker/",
                "youtube_en": "https://fastapi.tiangolo.com/deployment/docker/",
                "questions": [
                    {"text": "ما وظيفة FastAPI هنا؟", "options": {"A": "تقديم model inference عبر API", "B": "تدريب CNN فقط", "C": "annotation", "D": "image compression"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Docker؟", "options": {"A": "تغليف التطبيق والdependencies في container", "B": "تدريب YOLO فقط", "C": "تحسين accuracy تلقائيًا", "D": "إنشاء labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "S3 يستخدم أساسًا لـ؟", "options": {"A": "Object storage", "B": "CNN training فقط", "C": "SQL query", "D": "OCR"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة environment variable؟", "options": {"A": "تخزين configuration خارج الكود", "B": "زيادة accuracy", "C": "إنشاء bounding box", "D": "تغيير resolution"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة API endpoint؟", "options": {"A": "نقطة يمكن للتطبيقات إرسال requests إليها", "B": "GPU", "C": "Dataset", "D": "optimizer"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا لا تضع API key داخل GitHub؟", "options": {"A": "لأنها secret", "B": "لأنها image", "C": "لأنها model", "D": "لأنها label"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Dockerfile؟", "options": {"A": "لتعريف كيفية بناء image", "B": "لتعريف classes", "C": "لتعريف dataset فقط", "D": "لتعريف confusion matrix"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يمثل latency؟", "options": {"A": "زمن الاستجابة", "B": "عدد classes", "C": "حجم dataset", "D": "عدد epochs"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا versioning للنموذج مهم؟", "options": {"A": "لمعرفة أي model تم استخدامه وإمكانية الرجوع إليه", "B": "لزيادة pixels", "C": "لتقليل labels", "D": "لإلغاء testing"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان API يعالج 100 request في الثانية، ماذا يمثل هذا تقريبًا؟", "options": {"A": "Throughput", "B": "Accuracy", "C": "Recall", "D": "IoU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا logging مهم في production؟", "options": {"A": "لتشخيص المشاكل ومتابعة التشغيل", "B": "لزيادة accuracy تلقائيًا", "C": "لتحويل الصور", "D": "لتدريب model"}, "correct": "A", "difficulty": "medium"},
                    {"text": "نموذج دقته ممتازة لكنه يستغرق 2 ثانية لكل صورة في تطبيق real-time. ماذا تفعل؟", "options": {"A": "تجاهل المشكلة", "B": "optimization/model compression أو model أصغر", "C": "زيادة image size", "D": "حذف API"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا فصل preprocessing عن model inference مفيد؟", "options": {"A": "يسهل الاختبار والصيانة وإعادة الاستخدام", "B": "يقلل accuracy دائمًا", "C": "يمنع deployment", "D": "يلغي الحاجة إلى Git"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك model v1 وv2. كيف تمنع نشر v2 دون اختبار؟", "options": {"A": "CI/CD + validation/testing + controlled deployment", "B": "حذف v1", "C": "تغيير filename فقط", "D": "رفعه مباشرة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا قد تحتاج GPU في production؟", "options": {"A": "إذا كان inference workload يستفيد منها وتبرر التكلفة/الزمن", "B": "لأنها مطلوبة دائمًا", "C": "لأنها تخزن API", "D": "لأنها تحل bugs"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9: Practical Projects
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية المتكاملة",
                "description": "تحويل المهارات السابقة إلى Portfolio حقيقي متدرج من مشروع مبتدئ إلى Computer Vision Capstone.",
                "objectives": [
                    "Project architecture",
                    "Dataset management",
                    "Experiment tracking",
                    "Reproducibility",
                    "Model evaluation / Error analysis",
                    "Documentation",
                    "Deployment / API integration",
                    "Docker / Git/GitHub",
                    "Production thinking"
                ],
                "practical_task": "نفذ 5 مشاريع + Capstone: (1) Image Classification (2) Custom Object Detection (3) Video Analytics (4) Production Vision API (5) Cloud Vision App + Capstone: Smart Traffic Monitoring مع GitHub كامل.",
                "youtube_ar": "https://fullstackdeeplearning.com/",
                "youtube_en": "https://fullstackdeeplearning.com/",
                "questions": [
                    {"text": "ما أول شيء يجب تحديده في مشروع حقيقي؟", "options": {"A": "Problem/requirements", "B": "YOLO version", "C": "Dockerfile", "D": "GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا README مهم؟", "options": {"A": "لشرح المشروع وتشغيله", "B": "لزيادة accuracy", "C": "لتدريب model", "D": "لتغيير labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهمية Dataset documentation؟", "options": {"A": "فهم مصدر البيانات وطبيعتها وقيودها", "B": "زيادة FPS", "C": "تشغيل API", "D": "حذف errors"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا architecture diagram؟", "options": {"A": "توضيح مكونات النظام وتدفق البيانات", "B": "تدريب CNN", "C": "ضغط images", "D": "تغيير model"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يجب تسجيله أثناء experiments؟", "options": {"A": "Model/config/metrics", "B": "اسم الكمبيوتر فقط", "C": "لون الواجهة", "D": "حجم الشاشة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لديك model جيد لكن يعمل فقط على Notebook. ما الخطوة التالية؟", "options": {"A": "تحويله إلى reproducible inference pipeline", "B": "حذف notebook", "C": "تغيير dataset", "D": "إضافة classes عشوائية"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا Error Analysis مهم؟", "options": {"A": "لمعرفة أين يفشل النموذج ولماذا", "B": "لزيادة عدد الصور تلقائيًا", "C": "لإنشاء Docker image", "D": "لحذف validation"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن يكون Capstone cumulative؟", "options": {"A": "لإثبات تكامل المهارات السابقة", "B": "لتعلم 20 تقنية جديدة", "C": "لتجنب التوثيق", "D": "لتقليل الاختبارات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت detection accuracy جيدة لكن بعض الحالات الحرجة لا تُكتشف، ماذا تفعل؟", "options": {"A": "تحليل false negatives", "B": "الاكتفاء بالaccuracy", "C": "حذف الحالات", "D": "تغيير Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Docker في المشروع؟", "options": {"A": "reproducible environment", "B": "training labels", "C": "image annotation", "D": "confusion matrix"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة API في مشروع CV؟", "options": {"A": "إتاحة model للتطبيقات الأخرى", "B": "تدريب dataset", "C": "زيادة pixels", "D": "إنشاء labels"}, "correct": "A", "difficulty": "medium"},
                    {"text": "مشروعك يعمل على جهازك فقط. ما المشكلة المهنية؟", "options": {"A": "ضعف reproducibility", "B": "زيادة accuracy", "C": "زيادة recall", "D": "زيادة FPS"}, "correct": "A", "difficulty": "hard"},
                    {"text": "model A accuracy أعلى من B لكن latency ضعف B في real-time application. ما القرار الصحيح؟", "options": {"A": "اختيار A دائمًا", "B": "مقارنة accuracy/latency وفق requirements", "C": "اختيار B دائمًا", "D": "تجاهل latency"}, "correct": "B", "difficulty": "hard"},
                    {"text": "اكتشفت أن dataset تحتوي على صور من نفس الفيديو في train وtest. ما المشكلة؟", "options": {"A": "Data leakage", "B": "Quantization", "C": "Docker bug", "D": "API bug"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أقوى دليل على جاهزية المشروع؟", "options": {"A": "Notebook جميل", "B": "README فقط", "C": "Model accuracy فقط", "D": "تشغيل النظام كاملًا مع توثيق واختبارات ونتائج قابلة لإعادة الإنتاج"}, "correct": "D", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10: Professional Preparation
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 Portfolio وProfessional Preparation وJob Ready",
                "description": "تحويل المهارات والمشاريع إلى جاهزية فعلية لوظائف Junior Computer Vision Engineer.",
                "objectives": [
                    "CV Portfolio / GitHub presentation",
                    "README writing / Architecture explanation",
                    "Technical CV / LinkedIn",
                    "Project storytelling",
                    "Computer Vision interview / Python interview",
                    "ML/DL interview / CNN questions",
                    "Detection questions / Model evaluation",
                    "Debugging / Deployment questions",
                    "System design basics",
                    "Behavioral interview / Job applications"
                ],
                "practical_task": "أنشئ Job-Ready Package: 4-6 مشاريع + Capstone كامل + CV مخصص + LinkedIn + README احترافي لكل مشروع + Architecture Diagrams + Mock Interview شامل.",
                "youtube_ar": "https://learn.microsoft.com/en-us/training/paths/insight-visual-data/",
                "youtube_en": "https://learn.microsoft.com/en-us/training/paths/insight-visual-data/",
                "questions": [
                    {"text": "ماذا يجب أن يوضح README الجيد؟", "options": {"A": "كيفية فهم وتشغيل المشروع", "B": "اسم الطالب فقط", "C": "لون الواجهة", "D": "عدد ساعات التعلم"}, "correct": "A", "difficulty": "easy"},
                    {"text": "في مقابلة CV، ما الذي يجب أن تكون قادرًا على شرحه؟", "options": {"A": "لماذا اخترت النموذج وكيف قيّمته", "B": "اسم Python فقط", "C": "اسم GPU فقط", "D": "عدد ملفات المشروع فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يثبت المهارة أكثر؟", "options": {"A": "Project يعمل وموثق", "B": "مشاهدة فيديو", "C": "شهادة فقط", "D": "حفظ تعريفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يجب أن يحتوي CV لمهندس مبتدئ؟", "options": {"A": "مشاريع ومهارات تقنية قابلة للإثبات", "B": "قائمة كورسات فقط", "C": "كلمات عامة فقط", "D": "معلومات غير مرتبطة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أفضل طريقة لعرض Capstone في المقابلة؟", "options": {"A": "Problem → Architecture → Approach → Results → Limitations", "B": "قراءة الكود كاملًا", "C": "ذكر اسم framework فقط", "D": "عرض screenshot فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "سألك interviewer: لماذا اخترت YOLO؟", "options": {"A": "لأنه مشهور فقط", "B": "لأنه مناسب لمتطلبات detection/latency والبيانات المتاحة", "C": "لأن Python يستخدمه", "D": "لأنه دائمًا أفضل model"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا سُئلت عن model failure، ماذا تفعل؟", "options": {"A": "تقول إن النموذج ممتاز", "B": "تعرض failure cases وتحلل الأسباب", "C": "تخفي النتائج", "D": "تحذف test data"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما أهم شيء عند تصميم real-time CV system؟", "options": {"A": "accuracy فقط", "B": "latency فقط", "C": "balance بين accuracy وlatency/resources حسب requirements", "D": "عدد الملفات"}, "correct": "C", "difficulty": "medium"},
                    {"text": "كيف تثبت أنك تفهم CNN؟", "options": {"A": "تستطيع شرح convolution وfeature extraction وtraining", "B": "تحفظ اسم ResNet", "C": "تعرف install PyTorch فقط", "D": "تعرف Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما السؤال المهني الأقوى عند اختيار model؟", "options": {"A": "هل هو مشهور؟", "B": "هل يحقق requirements من accuracy/latency/cost؟", "C": "هل اسمه قصير؟", "D": "هل يحتوي layers كثيرة؟"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك deployment failure. ما أول خطوة؟", "options": {"A": "تغيير model فورًا", "B": "قراءة logs وتحديد نقطة الفشل", "C": "حذف Docker", "D": "إعادة كتابة المشروع كاملًا"}, "correct": "B", "difficulty": "medium"},
                    {"text": "نظامك يحقق mAP ممتازًا لكن latency لا تناسب real-time. ماذا تقترح؟", "options": {"A": "استخدام model أخف/optimization/quantization أو hardware مناسب", "B": "تجاهل latency", "C": "زيادة image resolution", "D": "حذف evaluation"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في system design، لماذا تفصل inference service عن client؟", "options": {"A": "لتحسين maintainability/scalability وإعادة الاستخدام", "B": "لأن Python لا يعمل", "C": "لزيادة labels", "D": "لإلغاء API"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا فشل الطالب في explaining Capstone architecture بوضوح، هل يعتبر Job Ready؟", "options": {"A": "نعم لأن accuracy جيدة", "B": "نعم لأن لديه GitHub", "C": "لا، لأن شرح النظام جزء أساسي من الجاهزية المهنية", "D": "نعم إذا لديه شهادة"}, "correct": "C", "difficulty": "hard"},
                    {"text": "ما التعريف الأدق لـ Strong Junior Computer Vision Engineer؟", "options": {"A": "يعرف عشرات frameworks", "B": "يستطيع بناء وفهم وتقييم ونشر نظام CV حقيقي بمستوى ابتدائي مهني", "C": "يستطيع تدريب أكبر model فقط", "D": "يعرف Deep Learning نظريًا فقط"}, "correct": "B", "difficulty": "hard"}
                ]
            }
        ]
    }
]