# data/career_content_nlp.py
# بنك محتوى مسار "مهندس معالجة اللغة الطبيعية (NLP Engineer)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

NLP_ENGINEER_PATHS = [
    {
        "major_key": "ai",
        "slug": "nlp-engineer",
        "title": "مهندس معالجة لغة طبيعية (NLP Engineer)",
        "description": "مسار متكامل: Python + ML + NLP + PyTorch + Transformers + LLMs + RAG + Fine-tuning + Deployment.",
        "icon": "💬",
        "difficulty": "متقدم",
        "estimated_hours": 280,
        "order_index": 3,
        "stages": [
            # ==========================================
            # المرحلة 1: Programming, Math & ML Foundations
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات البرمجة والرياضيات وML",
                "description": "بناء الأساس البرمجي والرياضي والتعلم الآلي الذي يحتاجه مهندس NLP قبل الانتقال إلى Deep Learning وTransformers.",
                "objectives": [
                    "Python fundamentals",
                    "Functions & data structures",
                    "OOP basics / Exceptions",
                    "Virtual environments",
                    "NumPy / Pandas",
                    "Git & GitHub",
                    "Probability / Statistics",
                    "Linear algebra basics",
                    "ML fundamentals",
                    "Train/validation/test",
                    "Classification & regression",
                    "Model evaluation"
                ],
                "practical_task": "Text Classification Baseline: CSV → Cleaning → Feature Extraction → ML Model → Evaluation باستخدام Scikit-learn، وقارن Logistic Regression مع Naive Bayes ووثّق Precision/Recall/F1.",
                "youtube_ar": "https://academy.hsoub.com/",
                "youtube_en": "https://www.deeplearning.ai/courses/machine-learning-specialization/",
                "questions": [
                    {"text": "أي نوع بيانات مناسب لتخزين مجموعة عناصر مرتبة وقابلة للتغيير في Python؟", "options": {"A": "Tuple", "B": "List", "C": "Set", "D": "String"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة try/except؟", "options": {"A": "إنشاء Class", "B": "تكرار الكود", "C": "التعامل مع الأخطاء", "D": "تثبيت المكتبات"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الهدف الأساسي من Train/Test Split؟", "options": {"A": "حذف البيانات", "B": "تقييم النموذج على بيانات لم يتدرب عليها", "C": "زيادة حجم البيانات", "D": "تسريع Python"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي مكتبة تستخدم عادة للتعامل مع DataFrames؟", "options": {"A": "Pandas", "B": "Flask", "C": "Requests", "D": "Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يخزن عادة في Git؟", "options": {"A": "تغييرات المشروع", "B": "كلمات المرور", "C": "RAM", "D": "GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Validation Set؟", "options": {"A": "لتخزين النسخة النهائية فقط", "B": "لاختيار وضبط النموذج قبل الاختبار النهائي", "C": "لحذف Outliers دائماً", "D": "لاستبدال Training Set"}, "correct": "B", "difficulty": "medium"},
                    {"text": "في مشكلة تصنيف غير متوازنة، أي Metric قد يكون أكثر فائدة من Accuracy وحدها؟", "options": {"A": "File size", "B": "F1-score", "C": "Number of columns", "D": "Runtime فقط"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ماذا يعني Overfitting؟", "options": {"A": "النموذج لا يتعلم إطلاقاً", "B": "النموذج يعمل جيداً على التدريب وضعيف على بيانات جديدة", "C": "البيانات كلها مفقودة", "D": "النموذج لا يحتوي Parameters"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Virtual Environment؟", "options": {"A": "لتشغيل GPU", "B": "لعزل Dependencies الخاصة بالمشروع", "C": "لتشفير البيانات", "D": "لتغيير نظام التشغيل"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة Feature Scaling لبعض نماذج ML؟", "options": {"A": "حذف Labels", "B": "جعل المقاييس العددية أكثر اتساقاً", "C": "زيادة عدد الصفوف", "D": "تحويل النص إلى صوت"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كانت Precision عالية وRecall منخفضة، فهذا يعني غالباً أن النموذج:", "options": {"A": "يفوّت عدداً من الحالات الإيجابية", "B": "يصنف كل شيء إيجابياً", "C": "لا يستخدم Features", "D": "لا يحتوي Validation Set"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك Dataset صغيرة جداً. ما المشكلة الأكبر عند تقسيمها بشكل عشوائي دون مراعاة توزيع الفئات؟", "options": {"A": "قد تصبح بعض الفئات ممثلة بشكل سيئ في Train/Test", "B": "Python سيتوقف", "C": "Git لن يعمل", "D": "Pandas يحذف البيانات"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب عدم استخدام Test Set لضبط Hyperparameters؟", "options": {"A": "لأنها بطيئة", "B": "لأنها ستصبح جزءاً من عملية الاختيار وتفقد استقلاليتها", "C": "لأنها لا تحتوي Labels", "D": "لأنها لا يمكن قراءتها"}, "correct": "B", "difficulty": "hard"},
                    {"text": "نموذج يعطي Accuracy = 95% على Dataset تحتوي 95% من العينات من فئة واحدة. ما الاستنتاج الصحيح؟", "options": {"A": "النموذج ممتاز بالضرورة", "B": "Accuracy وحدها غير كافية", "C": "النموذج يحتاج GPU", "D": "Dataset مثالية"}, "correct": "B", "difficulty": "hard"},
                    {"text": "في Text Classification، لماذا يجب تنفيذ بعض خطوات preprocessing بطريقة تمنع تسرب معلومات Test إلى Training؟", "options": {"A": "لمنع Data Leakage", "B": "لتقليل حجم Git", "C": "لتغيير اللغة", "D": "لتشغيل CUDA"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2: NLP Fundamentals & Text Processing
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ أساسيات NLP ومعالجة النصوص",
                "description": "فهم كيفية تمثيل اللغة ومعالجة النصوص وبناء أنظمة NLP تقليدية قبل الانتقال إلى Deep Learning.",
                "objectives": [
                    "NLP pipeline",
                    "Text normalization",
                    "Tokenization / Stopwords",
                    "Stemming / Lemmatization",
                    "N-grams",
                    "Bag of Words / TF-IDF",
                    "Word embeddings",
                    "Text classification",
                    "NER basics",
                    "Sentiment analysis",
                    "Arabic text preprocessing",
                    "Unicode & evaluation metrics"
                ],
                "practical_task": "Arabic Sentiment Analysis System: Text → Normalization → Tokenization → TF-IDF → Classifier → Precision/Recall/F1، مع اختبار تأثير إزالة التشكيل والتطبيع وإزالة Stopwords.",
                "youtube_ar": "https://academy.hsoub.com/",
                "youtube_en": "https://www.deeplearning.ai/courses/natural-language-processing-specialization/",
                "questions": [
                    {"text": "ما الهدف من Tokenization؟", "options": {"A": "تقسيم النص إلى وحدات", "B": "تدريب GPU", "C": "ضغط الصور", "D": "حذف Labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "TF-IDF يستخدم أساساً من أجل:", "options": {"A": "تمثيل أهمية الكلمات", "B": "ترجمة النص", "C": "إنشاء صوت", "D": "تدريب Transformer مباشرة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ N-gram؟", "options": {"A": "مجموعة متتابعة من N وحدات", "B": "نوع قاعدة بيانات", "C": "نموذج GPU", "D": "ملف JSON"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Stemming يهدف إلى:", "options": {"A": "تقليل الكلمات إلى جذور تقريبية", "B": "ترجمة الكلمات", "C": "توليد نص", "D": "تصنيف الصور"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Sentiment Analysis يحدد عادة:", "options": {"A": "لغة البرمجة", "B": "مشاعر أو قطبية النص", "C": "حجم الملف", "D": "نوع GPU"}, "correct": "B", "difficulty": "easy"},
                    {"text": "لماذا قد يكون Stopword Removal غير مناسب لبعض المهام؟", "options": {"A": "بعض الكلمات الشائعة تحمل معنى مهماً في السياق", "B": "لأنه يزيد RAM دائماً", "C": "لأنه يمنع Python", "D": "لأنه يحذف الصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين Stemming وLemmatization؟", "options": {"A": "Lemmatization تعتمد عادة على التحليل اللغوي للوصول إلى صيغة أساسية", "B": "لا فرق", "C": "Stemming يستخدم GPU فقط", "D": "Lemmatization خاصة بالصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Word Embeddings؟", "options": {"A": "تمثيل الكلمات كمتجهات رقمية تحمل علاقات دلالية", "B": "تخزين الملفات", "C": "ضغط الفيديو", "D": "إنشاء قواعد البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المشكلة المحتملة عند استخدام Bag of Words؟", "options": {"A": "لا يمثل ترتيب الكلمات والسياق جيداً", "B": "لا يستطيع قراءة CSV", "C": "يحتاج دائماً GPU", "D": "لا يعمل مع Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا تحتاج Arabic NLP إلى معالجة خاصة أحياناً؟", "options": {"A": "بسبب اختلافات الكتابة والصرف والتشكيل واللهجات", "B": "لأن Python لا يدعم العربية", "C": "لأن NLP لا يدعم Unicode", "D": "لأن النص العربي ليس بيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقياس الذي يمثل التوازن بين Precision وRecall؟", "options": {"A": "Accuracy", "B": "F1-score", "C": "MSE", "D": "R²"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كانت كلمة تظهر في جميع الوثائق تقريباً، فماذا يحدث عادة لقيمتها في TF-IDF؟", "options": {"A": "ترتفع جداً", "B": "تنخفض أهميتها", "C": "تتحول إلى Label", "D": "تختفي من Dataset"}, "correct": "B", "difficulty": "hard"},
                    {"text": "في تصنيف النصوص، لماذا يجب أن يتم تعلم Vocabulary/Statistics من Training Set فقط؟", "options": {"A": "لمنع Data Leakage", "B": "لتقليل عدد الكلمات", "C": "لزيادة GPU", "D": "لتغيير اللغة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا قد يفشل نموذج يعتمد على الكلمات المنفردة في فهم 'ليس جيداً'؟", "options": {"A": "لأنه قد لا يمثل تركيب النفي والعلاقة بين الكلمات جيداً", "B": "لأن TF-IDF لا يعمل", "C": "لأن النص قصير", "D": "لأن Python لا يدعم النفي"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك نموذج عربي ممتاز على نصوص الأخبار لكنه ضعيف على لهجة يمنية. ما التفسير الأقوى؟", "options": {"A": "Domain/Language Variety Shift", "B": "مشكلة Git", "C": "نقص RAM فقط", "D": "خطأ في CSV"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3: Deep Learning for NLP
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ التعلم العميق لـ NLP",
                "description": "فهم الشبكات العصبية المستخدمة في NLP وبناء نماذج Deep Learning بسيطة باستخدام PyTorch.",
                "objectives": [
                    "Neural networks / Tensors",
                    "PyTorch / Forward-backward pass",
                    "Loss functions / Optimizers",
                    "Embedding layers",
                    "RNN / LSTM / GRU",
                    "Sequence classification",
                    "Attention concept",
                    "Training loops",
                    "GPU basics / Regularization",
                    "Early stopping"
                ],
                "practical_task": "Arabic Text Classification Neural Network باستخدام PyTorch: Text → Vocabulary/Tokenizer → Embedding → BiLSTM/GRU → Linear → Prediction، ومقارنته مع نموذج المرحلة 2.",
                "youtube_ar": "https://academy.hsoub.com/",
                "youtube_en": "https://web.stanford.edu/class/cs224n/",
                "questions": [
                    {"text": "ما وظيفة Embedding Layer؟", "options": {"A": "تحويل Tokens إلى متجهات قابلة للتعلم", "B": "تحويل النص إلى صورة", "C": "حذف Dataset", "D": "تشغيل Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المكتبة الرئيسية المستخدمة في هذا المسار؟", "options": {"A": "PyTorch", "B": "Flask فقط", "C": "Selenium", "D": "BeautifulSoup فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Loss Function؟", "options": {"A": "قياس خطأ النموذج", "B": "تحميل البيانات", "C": "حفظ Git", "D": "تنظيف القرص"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Optimizer؟", "options": {"A": "تحديث Parameters", "B": "قراءة CSV فقط", "C": "إنشاء Labels", "D": "ترجمة النص"}, "correct": "A", "difficulty": "easy"},
                    {"text": "RNN صممت أساساً للتعامل مع:", "options": {"A": "البيانات المتسلسلة", "B": "الصور فقط", "C": "قواعد البيانات", "D": "ملفات PDF فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا تستخدم LSTM بدل RNN التقليدية أحياناً؟", "options": {"A": "للتعامل بشكل أفضل مع الاعتماديات طويلة المدى", "B": "لأنها لا تحتاج Training", "C": "لأنها لا تحتوي Parameters", "D": "لأنها ليست Neural Network"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يحدث أثناء Backpropagation؟", "options": {"A": "حساب Gradients لتحديث Parameters", "B": "حذف البيانات", "C": "تغيير Labels يدوياً", "D": "إنشاء Tokenizer"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Dropout؟", "options": {"A": "تقليل Overfitting", "B": "زيادة حجم Dataset", "C": "ترجمة النص", "D": "حذف Vocabulary"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Batch Training؟", "options": {"A": "لمعالجة مجموعات من العينات في كل خطوة", "B": "لمنع GPU", "C": "لتحويل النص إلى JSON", "D": "لإزالة Embeddings"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Epoch؟", "options": {"A": "مرور كامل على Training Dataset", "B": "عينة واحدة", "C": "Token واحد", "D": "Layer واحدة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا انخفض Training Loss بينما ارتفع Validation Loss، فما الاحتمال الأكبر؟", "options": {"A": "Overfitting", "B": "Underfitting", "C": "Tokenization ناجح", "D": "Dataset فارغة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يصعب على RNN التقليدية الاحتفاظ بمعلومات بعيدة جداً في التسلسل؟", "options": {"A": "بسبب مشاكل مثل Vanishing Gradients", "B": "لأنها لا تستخدم Tokens", "C": "لأنها لا تحتوي Loss", "D": "لأنها تعمل على الصور"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الفائدة الأساسية من Attention؟", "options": {"A": "السماح للنموذج بالتركيز على أجزاء مهمة من السياق", "B": "حذف الكلمات", "C": "تقليل عدد Labels", "D": "إلغاء Training"}, "correct": "A", "difficulty": "hard"},
                    {"text": "عند مقارنة نموذجين، لماذا يجب استخدام نفس Test Set؟", "options": {"A": "لضمان عدالة المقارنة", "B": "لزيادة Accuracy", "C": "لتغيير Hyperparameters", "D": "لمنع استخدام PyTorch"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج لديه Training F1 = 0.99 وValidation F1 = 0.62. أفضل إجراء أولي؟", "options": {"A": "فحص Overfitting والبيانات والـregularization", "B": "حذف Validation", "C": "استخدام Test Set للتدريب", "D": "زيادة Epochs بلا حدود"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4: Transformers & Modern NLP
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ Transformers وNLP الحديث",
                "description": "إتقان البنية الأساسية للـTransformers واستخدام النماذج الحديثة مثل BERT وT5 وGPT عبر Hugging Face.",
                "objectives": [
                    "Attention / Self-attention",
                    "Multi-head attention",
                    "Positional encoding",
                    "Encoder / Decoder",
                    "Transformer architecture",
                    "BERT / RoBERTa / T5 / GPT",
                    "Tokenizers",
                    "Hugging Face Transformers & Datasets",
                    "Model Hub",
                    "Fine-tuning concepts"
                ],
                "practical_task": "استخدم BERT أو نموذج عربي مناسب: Dataset → Tokenizer → Pretrained Transformer → Fine-tuning → Evaluation على مهمة Arabic Text Classification أو NER.",
                "youtube_ar": "https://huggingface.co/",
                "youtube_en": "https://huggingface.co/learn/nlp-course/",
                "questions": [
                    {"text": "ما الفكرة الأساسية في Self-Attention؟", "options": {"A": "حساب علاقات بين Tokens داخل التسلسل", "B": "حذف Tokens", "C": "تحويل النص إلى صورة", "D": "تشغيل Docker"}, "correct": "A", "difficulty": "easy"},
                    {"text": "BERT يعتمد أساساً على:", "options": {"A": "Transformer Encoder", "B": "CNN فقط", "C": "Database", "D": "RNN فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Tokenizer؟", "options": {"A": "تحويل النص إلى Tokens/IDs يفهمها النموذج", "B": "تدريب GPU", "C": "حفظ Git", "D": "إنشاء API"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Hugging Face Transformers توفر:", "options": {"A": "نماذج وأدوات NLP جاهزة", "B": "نظام تشغيل", "C": "قاعدة بيانات", "D": "Compiler"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Pretrained Model؟", "options": {"A": "البدء من نموذج تعلم من بيانات كبيرة سابقاً", "B": "عدم الحاجة إلى بيانات أبداً", "C": "عدم الحاجة إلى تقييم", "D": "إلغاء التدريب دائماً"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا تحتاج Transformers إلى Positional Information؟", "options": {"A": "لأن Attention وحده لا يفرض ترتيب Tokens بنفس طريقة RNN", "B": "لأن Python لا يدعم النص", "C": "لأن BERT لا يستخدم Tokens", "D": "لتخزين الصور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين Encoder وDecoder في Transformer؟", "options": {"A": "الاستخدام والبنية المتعلقة بفهم المدخلات مقابل التوليد", "B": "لا يوجد فرق", "C": "Encoder للصور فقط", "D": "Decoder لقواعد البيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة Attention Mask؟", "options": {"A": "منع النموذج من الانتباه إلى Tokens غير المرغوبة مثل Padding", "B": "حذف النموذج", "C": "زيادة Dataset", "D": "تشفير API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم max_length؟", "options": {"A": "للتحكم في طول التسلسل المعالج", "B": "لتحديد حجم GPU", "C": "لتحديد عدد Labels", "D": "لتغيير اللغة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Hugging Face Datasets؟", "options": {"A": "تحميل ومعالجة وإدارة Datasets للتعلم الآلي", "B": "تشغيل Web Server", "C": "إنشاء GPU", "D": "إدارة Git فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا لا يكفي اختيار Transformer كبير لمشكلة صغيرة؟", "options": {"A": "قد يزيد التكلفة والكمون واحتمال الإفراط في التعقيد", "B": "لأن Transformers لا تعمل على النصوص", "C": "لأن BERT لا يحتوي Parameters", "D": "لأن النماذج الكبيرة لا يمكن تقييمها"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان Tokenizer للنموذج لا يطابق Tokenizer المستخدم أثناء التدريب، فما المشكلة؟", "options": {"A": "اختلاف تمثيل المدخلات قد يؤدي إلى نتائج خاطئة", "B": "زيادة Accuracy", "C": "تحسن الأداء تلقائياً", "D": "لا توجد مشكلة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب الاحتفاظ بنسخة من Model وTokenizer المستخدمين في Production؟", "options": {"A": "لضمان إعادة إنتاج نفس المعالجة والنموذج", "B": "لتقليل عدد Tokens", "C": "لمنع Git", "D": "لزيادة حجم Dataset"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج NER يعطي نتائج سيئة رغم أن Loss منخفض. ما الذي يجب فحصه أولاً؟", "options": {"A": "Alignment بين Tokens وLabels وطريقة التقييم", "B": "حذف النموذج", "C": "زيادة حجم الشاشة", "D": "تغيير نظام التشغيل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "عند اختيار نموذج NLP لمهمة إنتاجية، ما القرار الصحيح؟", "options": {"A": "الموازنة بين الجودة والحجم والكمون والتكلفة ومتطلبات المهمة", "B": "اختيار أكبر نموذج دائماً", "C": "اختيار أحدث نموذج فقط", "D": "تجاهل latency"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5: LLMs, Prompting & Generative NLP
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ LLMs وPrompting وNLP التوليدي",
                "description": "الانتقال من NLP التقليدي إلى بناء تطبيقات LLM عملية وفهم كيفية استخدام النماذج اللغوية الكبيرة بكفاءة.",
                "objectives": [
                    "LLM fundamentals",
                    "Causal language modeling",
                    "Context window",
                    "Prompt engineering",
                    "System/user instructions",
                    "Few-shot prompting",
                    "Structured output",
                    "Function/tool calling concepts",
                    "Temperature / Top-p",
                    "Hallucination / LLM APIs",
                    "Open-source LLMs",
                    "Local inference / Token cost / Safety"
                ],
                "practical_task": "LLM Text Assistant API: User Input → Prompt Template → LLM → Structured Response → Validation، مع 3 مهام: Summarization, Classification, Information extraction إلى JSON، ومقارنة على مجموعة Test ثابتة.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://huggingface.co/learn/nlp-course/",
                "questions": [
                    {"text": "ما المقصود بـ LLM؟", "options": {"A": "Large Language Model", "B": "Local Linux Machine", "C": "Linear Learning Module", "D": "Language Loading Manager"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Prompt؟", "options": {"A": "إعطاء تعليمات ومدخلات للنموذج", "B": "تدريب GPU فقط", "C": "تخزين Dataset", "D": "إنشاء Database"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Hallucination؟", "options": {"A": "توليد معلومات غير صحيحة أو غير مدعومة", "B": "بطء الإنترنت", "C": "خطأ Python", "D": "حذف Tokenizer"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Temperature تؤثر عادة في:", "options": {"A": "عشوائية/تنوع التوليد", "B": "حجم GPU", "C": "حجم Dataset", "D": "عدد Layers في النموذج"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Context Window تعني:", "options": {"A": "مقدار النص/التوكنات التي يستطيع النموذج التعامل معها ضمن سياق الطلب", "B": "سرعة الإنترنت", "C": "حجم RAM فقط", "D": "عدد المستخدمين"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Few-shot Prompting؟", "options": {"A": "إعطاء أمثلة للنموذج لتوضيح المطلوب", "B": "حذف بيانات التدريب", "C": "زيادة GPU", "D": "ضغط النص"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Structured Output؟", "options": {"A": "الحصول على نتائج بتنسيق محدد يمكن للبرنامج التعامل معه", "B": "زيادة حجم النموذج", "C": "إلغاء التقييم", "D": "حذف Prompt"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا زادت Temperature كثيراً، ماذا قد يحدث؟", "options": {"A": "يصبح التوليد أكثر تنوعاً وأقل حتمية", "B": "يصبح النموذج أصغر", "C": "تختفي Tokens", "D": "يتوقف API دائماً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب ألا تعتمد على LLM في معلومة حرجة دون تحقق؟", "options": {"A": "احتمال Hallucination وعدم الموثوقية", "B": "لأن LLM لا يستخدم Tokens", "C": "لأن JSON لا يعمل", "D": "لأن Python يمنع ذلك"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم System Prompt؟", "options": {"A": "لتحديد سلوك وتعليمات عامة للنموذج", "B": "لحذف User Prompt", "C": "لتدريب النموذج من الصفر", "D": "لإنشاء GPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك مهمة تتطلب استخراج أسماء الأشخاص من نص وإرجاع JSON. ما الأفضل؟", "options": {"A": "تحديد Schema وتعليمات واضحة ثم التحقق من الناتج برمجياً", "B": "الاعتماد على النص دون تحقق", "C": "زيادة Temperature", "D": "حذف الأمثلة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نموذج يعطي إجابات صحيحة غالباً لكنه يستهلك Tokens كثيرة جداً. ما أول شيء تراجعه؟", "options": {"A": "Prompt/context length وطريقة الطلب", "B": "حجم الشاشة", "C": "Git branches", "D": "اسم المشروع"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب أن تكون تعليمات Prompt غير متعارضة؟", "options": {"A": "لتقليل ambiguity وتحسين قابلية التنبؤ", "B": "لزيادة عدد Parameters", "C": "لمنع Tokenization", "D": "لتغيير Model Architecture"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان LLM يقدم إجابة مقنعة لكنها غير موجودة في الوثائق التي أعطيته إياها، ما المشكلة؟", "options": {"A": "Hallucination / lack of grounding", "B": "Overfitting في SQL", "C": "Database deadlock", "D": "Git conflict"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أفضل طريقة لمقارنة Prompt جديد بقديم؟", "options": {"A": "استخدام Evaluation Dataset ثابت وقياس النتائج", "B": "الحكم على إجابة واحدة", "C": "اختيار الأطول", "D": "اختيار الأحدث"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6: RAG, Embeddings & Vector Search
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ RAG وEmbeddings وVector Search",
                "description": "تعلم بناء أنظمة NLP/LLM تعتمد على المعرفة الخارجية بدل الاعتماد على معلومات النموذج وحدها.",
                "objectives": [
                    "Embeddings / Semantic similarity",
                    "Vector databases / FAISS",
                    "Chunking / Document ingestion",
                    "Metadata / Retrieval / Top-k",
                    "RAG architecture",
                    "Retrieval quality",
                    "Reranking basics",
                    "Grounding / Citation"
                ],
                "practical_task": "Arabic RAG Assistant: PDF/Text → Chunking → Embeddings → Vector Search → Retrieved Context → LLM → Answer + Sources، واختبر النظام على 30 سؤالاً مع تسجيل Retrieval relevance وAnswer correctness وHallucinations وLatency.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://huggingface.co/learn/nlp-course/",
                "questions": [
                    {"text": "ما وظيفة Embedding؟", "options": {"A": "تمثيل النص كمتجه رقمي", "B": "حذف النص", "C": "ضغط PDF", "D": "تدريب GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Vector Database؟", "options": {"A": "تخزين والبحث في المتجهات", "B": "تشغيل Python", "C": "إدارة Git", "D": "إنشاء صور"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ RAG؟", "options": {"A": "Retrieval-Augmented Generation", "B": "Random AI Generator", "C": "Rapid API Gateway", "D": "Retrieval Algorithm Group"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نقسم الوثائق إلى Chunks؟", "options": {"A": "لتسهيل الاسترجاع وإدارة السياق", "B": "لتغيير اللغة", "C": "لتقليل عدد الملفات فقط", "D": "لإلغاء Embeddings"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Top-k تعني عادة:", "options": {"A": "عدد النتائج الأعلى التي يتم استرجاعها", "B": "عدد GPUs", "C": "عدد Labels", "D": "عدد Users"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا Semantic Search أفضل أحياناً من Keyword Search؟", "options": {"A": "يمكنه التقاط التشابه في المعنى", "B": "لأنه لا يحتاج بيانات", "C": "لأنه لا يستخدم Embeddings", "D": "لأنه دائماً أدق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المشكلة في Chunks الكبيرة جداً؟", "options": {"A": "قد تحتوي معلومات غير مرتبطة وتستهلك Context", "B": "لا يمكن تخزينها", "C": "تمنع Python", "D": "تمنع Vector Search"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المشكلة في Chunks الصغيرة جداً؟", "options": {"A": "قد تفقد السياق المطلوب للإجابة", "B": "تزيد جودة كل شيء دائماً", "C": "تمنع Embeddings", "D": "توقف LLM"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة Metadata؟", "options": {"A": "حفظ معلومات مثل المصدر والعنوان والصفحة", "B": "استبدال Embedding", "C": "تدريب النموذج", "D": "حذف الوثائق"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما معنى Grounding؟", "options": {"A": "ربط إجابة النموذج بمعلومات مصدرية متاحة", "B": "تغيير GPU", "C": "حذف Prompt", "D": "ضغط النص"}, "correct": "A", "difficulty": "medium"},
                    {"text": "RAG يعيد وثائق غير مرتبطة بالسؤال. ما أول شيء يجب فحصه؟", "options": {"A": "Chunking/Embedding/Retrieval configuration", "B": "Temperature فقط", "C": "حجم الشاشة", "D": "Git"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا قد لا يؤدي رفع Top-k دائماً إلى تحسين RAG؟", "options": {"A": "قد يضيف سياقاً غير ذي صلة ويزيد الضوضاء", "B": "لأنه يحذف Embeddings", "C": "لأنه يمنع LLM", "D": "لأنه يلغي Retrieval"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما فائدة Reranking؟", "options": {"A": "إعادة ترتيب النتائج المسترجعة لتحسين الصلة", "B": "تدريب Python", "C": "حذف Vector DB", "D": "إنشاء Tokenizer"}, "correct": "A", "difficulty": "hard"},
                    {"text": "نظام RAG يجيب بشكل ممتاز عندما يجد الوثيقة الصحيحة، لكنه يفشل في استرجاعها. المشكلة الأساسية هي:", "options": {"A": "Retrieval", "B": "Generation فقط", "C": "UI", "D": "Temperature"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أفضل تقييم لنظام RAG يجب أن يفصل بين:", "options": {"A": "جودة Retrieval وجودة الإجابة", "B": "لون الواجهة وحجم الخط", "C": "Python وGit", "D": "CPU وKeyboard"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7: Fine-Tuning, PEFT & Advanced NLP
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ Fine-Tuning وPEFT وNLP المتقدم",
                "description": "تعلم متى وكيف يتم تخصيص النماذج المدربة مسبقاً باستخدام Fine-tuning وPEFT/LoRA دون محاولة تدريب LLM من الصفر.",
                "objectives": [
                    "Fine-tuning",
                    "Instruction tuning concepts",
                    "Supervised fine-tuning",
                    "Dataset preparation",
                    "Train/validation split",
                    "LoRA / PEFT / QLoRA concept",
                    "Quantization basics",
                    "Hyperparameters",
                    "Checkpoints / Model cards",
                    "Overfitting / Catastrophic forgetting",
                    "Arabic model adaptation"
                ],
                "practical_task": "استخدم نموذجاً صغيراً مفتوح المصدر وطبّق LoRA Fine-tuning لمهمة NLP محددة، ثم قارن Base Model vs Fine-tuned Model من حيث F1، حجم النموذج، وقت inference، وعدد Parameters المدربة.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://huggingface.co/docs/peft/",
                "questions": [
                    {"text": "ما الهدف من Fine-tuning؟", "options": {"A": "تكييف نموذج pretrained لمهمة أو مجال محدد", "B": "حذف النموذج", "C": "إنشاء GPU", "D": "ضغط Dataset"}, "correct": "A", "difficulty": "easy"},
                    {"text": "LoRA هي:", "options": {"A": "طريقة PEFT", "B": "Database", "C": "Tokenizer", "D": "Operating System"}, "correct": "A", "difficulty": "easy"},
                    {"text": "PEFT يهدف إلى:", "options": {"A": "تقليل عدد Parameters التي يتم تدريبها", "B": "زيادة كل Parameters", "C": "حذف النموذج", "D": "منع التدريب"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نحتاج Validation Dataset؟", "options": {"A": "لمراقبة الأداء أثناء التطوير", "B": "لتخزين Logs فقط", "C": "لتغيير اللغة", "D": "لحذف Labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Model Card توثق:", "options": {"A": "معلومات عن النموذج واستخدامه وحدوده", "B": "Passwords", "C": "GPU drivers", "D": "Git commits فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة LoRA مقارنة بـ Full Fine-tuning؟", "options": {"A": "تكلفة وذاكرة تدريب أقل عادة", "B": "لا يحتاج Dataset", "C": "لا يحتاج Model", "D": "يضمن أفضل نتيجة دائماً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب تنظيف Dataset قبل Fine-tuning؟", "options": {"A": "جودة البيانات تؤثر مباشرة على جودة النموذج", "B": "لأن GPU لا يقرأ النص", "C": "لأن Transformers لا تقرأ JSON", "D": "لتغيير Python"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما خطر وجود Labels خاطئة بكثرة؟", "options": {"A": "تعلم النموذج أنماطاً خاطئة", "B": "زيادة Accuracy بالضرورة", "C": "تقليل حجم Model", "D": "منع Tokenization"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Quantization؟", "options": {"A": "تمثيل Parameters بدقة عددية أقل لتقليل الذاكرة/الحساب", "B": "زيادة Dataset", "C": "ترجمة النص", "D": "تغيير اللغة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نحتفظ بـ Checkpoints؟", "options": {"A": "لحفظ حالات النموذج أثناء التدريب", "B": "لتخزين كلمات المرور", "C": "لمنع Evaluation", "D": "لتغيير Tokenizer"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Catastrophic Forgetting؟", "options": {"A": "فقدان النموذج بعض قدراته السابقة أثناء التكيف", "B": "حذف Dataset يدوياً", "C": "توقف GPU", "D": "خطأ Git"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Fine-tuning يعطي نتيجة أسوأ من Base Model. ما أول شيء تفحصه؟", "options": {"A": "Dataset quality/format, labels, hyperparameters, evaluation", "B": "لون الواجهة", "C": "اسم GitHub", "D": "سرعة الإنترنت فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا لا ينبغي Fine-tune نموذج كبير لمجرد وجود Dataset صغيرة؟", "options": {"A": "خطر Overfitting والتكلفة قد لا تبرر النتيجة", "B": "لأن النماذج الكبيرة لا تعمل", "C": "لأن LoRA ممنوع", "D": "لأن NLP لا يستخدم Training"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا كان هدفك إضافة معرفة خاصة تتغير باستمرار إلى LLM، فما الحل الذي ينبغي تقييمه قبل Fine-tuning؟", "options": {"A": "RAG", "B": "إعادة تدريب النموذج من الصفر", "C": "حذف البيانات", "D": "زيادة Temperature"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أفضل مقارنة بعد LoRA Fine-tuning؟", "options": {"A": "Base vs Fine-tuned على Test Set ثابت", "B": "Training loss فقط", "C": "Prompt واحد", "D": "حجم الملف فقط"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8: NLP Deployment, APIs, Evaluation & LLMOps
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ النشر وAPIs وEvaluation وLLMOps",
                "description": "تحويل نموذج NLP من Notebook إلى خدمة قابلة للاستخدام والمراقبة والتقييم في بيئة عملية.",
                "objectives": [
                    "FastAPI / REST APIs",
                    "Docker",
                    "Model serving",
                    "Hugging Face Hub",
                    "Authentication basics",
                    "Environment variables / Logging",
                    "Latency / Throughput",
                    "Model evaluation",
                    "Regression testing",
                    "LLM evaluation",
                    "Monitoring / MLflow basics",
                    "Safety / Prompt injection basics",
                    "PII awareness",
                    "Production debugging"
                ],
                "practical_task": "حوّل نموذج NLP السابق إلى: Client → FastAPI → NLP Model → JSON Response، ثم: Docker → API → Logging → Evaluation Dataset → Monitoring. أنشئ 30 Test Cases ثابتة لاكتشاف Regression.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://mlflow.org/docs/latest/genai/eval-monitor/",
                "questions": [
                    {"text": "FastAPI تستخدم لبناء:", "options": {"A": "APIs", "B": "Databases فقط", "C": "GPUs", "D": "Tokenizers فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Docker يستخدم أساساً لـ:", "options": {"A": "Packaging وتشغيل التطبيق في بيئة معزولة", "B": "تدريب النموذج فقط", "C": "إنشاء Dataset", "D": "كتابة SQL"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Logging؟", "options": {"A": "تتبع ما يحدث داخل التطبيق", "B": "زيادة Accuracy", "C": "تدريب Model", "D": "حذف Errors"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Latency تعني:", "options": {"A": "زمن الاستجابة", "B": "حجم Dataset", "C": "عدد Parameters", "D": "عدد Labels"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Evaluation Dataset؟", "options": {"A": "قياس جودة النظام بشكل متكرر", "B": "تشغيل Docker", "C": "حذف النموذج", "D": "تغيير Prompt عشوائياً"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم Environment Variables للمفاتيح السرية؟", "options": {"A": "لتجنب وضعها مباشرة في Source Code", "B": "لزيادة Accuracy", "C": "لتغيير Tokenizer", "D": "لتقليل Context"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق بين Training وInference؟", "options": {"A": "Training يتعلم Parameters، Inference يستخدم النموذج للتنبؤ", "B": "لا فرق", "C": "Inference يدرب النموذج", "D": "Training لا يحتاج بيانات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Regression Testing في LLM؟", "options": {"A": "التأكد أن التغييرات لم تكسر السلوك السابق", "B": "زيادة Parameters", "C": "حذف Prompts", "D": "تغيير اللغة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نراقب Token Usage؟", "options": {"A": "للتكلفة والأداء", "B": "لمنع Python", "C": "لإنشاء Database", "D": "لتدريب CNN"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة Health Check للـAPI؟", "options": {"A": "التحقق من أن الخدمة تعمل", "B": "تقييم Accuracy", "C": "تدريب النموذج", "D": "إنشاء Embeddings"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Throughput؟", "options": {"A": "مقدار العمل الذي تتم معالجته خلال فترة", "B": "حجم النموذج", "C": "عدد Tokens في Prompt فقط", "D": "حجم GPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "API تعمل محلياً لكنها تفشل في Docker بسبب Model Path. ما أول شيء تفحصه؟", "options": {"A": "Paths/volumes/configuration داخل container", "B": "Temperature", "C": "Dataset labels", "D": "Prompt length فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "LLM application أصبحت أبطأ بعد إضافة RAG. ما الذي يجب قياسه؟", "options": {"A": "Retrieval latency + embedding latency + generation latency", "B": "لون الواجهة", "C": "Git branches", "D": "عدد ملفات المشروع"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا نستخدم Golden Evaluation Set؟", "options": {"A": "لمقارنة إصدارات النظام بشكل ثابت", "B": "لتدريب LLM دائماً", "C": "لحذف Retrieval", "D": "لتقليل RAM"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا حسّن Prompt جديد الجودة لكنه زاد تكلفة Tokens 5 مرات، ما القرار المهني؟", "options": {"A": "مقارنة جودة التحسن مع التكلفة والـlatency ومتطلبات المنتج", "B": "استخدامه دائماً", "C": "رفضه دائماً", "D": "تجاهل التكلفة"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9: Practical Projects
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية المتكاملة",
                "description": "تحويل المهارات السابقة إلى Portfolio حقيقي متدرج يثبت قدرة الطالب على بناء أنظمة NLP من البداية إلى Production.",
                "objectives": [
                    "Project architecture",
                    "Dataset preparation",
                    "NLP pipelines",
                    "Model training",
                    "Transformers",
                    "LLM applications",
                    "RAG",
                    "Fine-tuning",
                    "Evaluation",
                    "APIs / Docker / GitHub",
                    "Documentation / Deployment / Troubleshooting"
                ],
                "practical_task": "نفذ 6 مشاريع: (1) Arabic Sentiment Analysis (2) Arabic Text Classification/NER بـ BERT (3) LLM Application (4) Production-style Arabic RAG (5) Fine-Tuned NLP Model بـ LoRA (6) NLP API + Capstone: Arabic Knowledge Intelligence Platform مع GitHub كامل.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://huggingface.co/learn/nlp-course/",
                "questions": [
                    {"text": "ما أول خطوة صحيحة في مشروع NLP؟", "options": {"A": "تحديد المشكلة والمتطلبات", "B": "اختيار أكبر LLM", "C": "كتابة Dockerfile", "D": "شراء GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "README مهم لأنه:", "options": {"A": "يشرح المشروع وطريقة تشغيله", "B": "يزيد Accuracy", "C": "يدرب النموذج", "D": "يخزن Embeddings"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Architecture Diagram؟", "options": {"A": "توضيح مكونات النظام وعلاقاتها", "B": "زيادة Tokens", "C": "حذف Bugs", "D": "تدريب Model"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن يحتويه Capstone؟", "options": {"A": "تكامل المهارات السابقة", "B": "مهارة واحدة فقط", "C": "Prompt واحد", "D": "Notebook فارغ"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا نستخدم GitHub؟", "options": {"A": "Version control وPortfolio", "B": "GPU", "C": "Vector Search فقط", "D": "LLM inference فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "مشروع RAG لا يحتوي Evaluation Dataset. ما المشكلة؟", "options": {"A": "لا يوجد معيار ثابت لقياس التحسين", "B": "لا يمكن تشغيل Python", "C": "لا يمكن استخدام Embeddings", "D": "Docker لن يعمل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب توثيق Limitations؟", "options": {"A": "لإظهار فهم حدود النظام ومخاطره", "B": "لتقليل Accuracy", "C": "لحذف المشروع", "D": "لمنع الاستخدام"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب استخدام Test Dataset منفصل؟", "options": {"A": "لتقييم نهائي غير متحيز", "B": "لتدريب النموذج", "C": "لزيادة Parameters", "D": "لإنشاء API"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل المشروع Job-ready أكثر؟", "options": {"A": "Documentation + testing + deployment + measurable results", "B": "عدد كبير من المكتبات", "C": "Notebook طويل فقط", "D": "واجهة جميلة فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة لإظهار مقارنة نموذجين؟", "options": {"A": "Metrics على نفس Test Set", "B": "رأي شخصي", "C": "Screenshot فقط", "D": "حجم الملفات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب حفظ Dataset/version المستخدمة؟", "options": {"A": "لإعادة إنتاج النتائج", "B": "لزيادة Tokens", "C": "لتغيير Model", "D": "لتقليل GPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Capstone يعمل لكنه لا يحتوي Tests أو Evaluation. هل هو Production-ready؟", "options": {"A": "لا", "B": "نعم دائماً", "C": "فقط إذا كان LLM كبيراً", "D": "إذا كان README طويلاً"}, "correct": "A", "difficulty": "hard"},
                    {"text": "RAG يعطي نتائج جيدة في 8 أسئلة من 10 لكنه يفشل في سؤالين بسبب Retrieval. ماذا توثق؟", "options": {"A": "Failure cases وتحليل سببها", "B": "تحذف السؤالين", "C": "تقول 100% accuracy", "D": "تغير النتائج"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب ألا تستخدم بيانات Test أثناء تطوير Prompt؟", "options": {"A": "لمنع overfitting على Test Set", "B": "لزيادة Tokens", "C": "لمنع Embeddings", "D": "لأن Prompt لا يعمل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "أي مشروع أقوى Portfolio لوظيفة Junior NLP Engineer؟", "options": {"A": "نظام RAG كامل مع Evaluation وAPI وDocker وتوثيق", "B": "Notebook يطبع Hello World", "C": "Screenshot لـChatGPT", "D": "قائمة كورسات"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10: Professional Preparation & Job Ready
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 التحضير المهني وJob Ready",
                "description": "تحويل المهارات والمشاريع إلى جاهزية فعلية لوظيفة Junior / Entry-Level NLP Engineer واجتياز المقابلات والتقييمات التقنية.",
                "objectives": [
                    "NLP interview preparation",
                    "Python interview",
                    "ML/DL interview",
                    "Transformers / LLMs / RAG",
                    "Fine-tuning",
                    "Model evaluation",
                    "System design basics",
                    "API design / Docker basics",
                    "Git/GitHub / Portfolio",
                    "CV / LinkedIn",
                    "Technical presentation",
                    "Behavioral interview / Job applications"
                ],
                "practical_task": "نفّذ Final NLP Engineer Assessment: Python + NLP + ML + Deep Learning + Transformers + LLM + RAG + Fine-tuning + Engineering + Evaluation + System Design + Interview + Portfolio.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://web.stanford.edu/class/cs224n/",
                "questions": [
                    {"text": "ما المستوى المستهدف من هذا المسار؟", "options": {"A": "Junior / Entry-Level NLP Engineer", "B": "Senior AI Architect", "C": "Research Scientist فقط", "D": "CTO"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم عنصر في Portfolio؟", "options": {"A": "مشاريع عملية موثقة", "B": "عدد Followers", "C": "عدد الصور", "D": "طول CV فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن يظهر في CV؟", "options": {"A": "Skills + Projects + measurable achievements", "B": "قائمة أفلام", "C": "Passwords", "D": "جميع الكورسات دون مشاريع"}, "correct": "A", "difficulty": "easy"},
                    {"text": "GitHub يستخدم في Portfolio لإظهار:", "options": {"A": "العمل البرمجي والتوثيق", "B": "الراتب", "C": "عدد ساعات النوم", "D": "GPU"}, "correct": "A", "difficulty": "easy"},
                    {"text": "المقابلة التقنية تقيس:", "options": {"A": "المعرفة والتطبيق وحل المشكلات", "B": "سرعة الكتابة فقط", "C": "عدد الشهادات فقط", "D": "عدد المتابعين"}, "correct": "A", "difficulty": "easy"},
                    {"text": "في مقابلة NLP، لماذا قد يسألك interviewer عن Precision وRecall؟", "options": {"A": "لفهم قدرتك على اختيار Metrics المناسبة", "B": "لأنها أوامر Git", "C": "لأنها تخص Docker", "D": "لأنها تخص HTML"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا سُئلت: لماذا استخدمت RAG بدل Fine-tuning؟", "options": {"A": "تشرح ثبات المعرفة وتحديثها وتكلفة التدريب وطبيعة المشكلة", "B": "تقول لأن RAG مشهور", "C": "تقول لأن Fine-tuning ممنوع", "D": "لا تجيب"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا سُئلت عن مشروعك، ما الأفضل؟", "options": {"A": "شرح المشكلة والـarchitecture والقرارات والنتائج والقيود", "B": "قراءة README فقط", "C": "ذكر أسماء المكتبات", "D": "عرض Screenshot فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل مشروعاً أقوى في المقابلة؟", "options": {"A": "القدرة على شرح trade-offs والنتائج", "B": "عدد ملفات المشروع", "C": "عدد الألوان", "D": "حجم README فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن تعرف أساسيات Docker؟", "options": {"A": "لتشغيل ونقل تطبيق NLP بشكل متسق", "B": "لتدريب كل LLM", "C": "لإنشاء Tokens", "D": "لتقييم Accuracy"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة System Design في مقابلة NLP Engineer؟", "options": {"A": "إظهار القدرة على تحويل نموذج إلى نظام متكامل", "B": "اختبار HTML", "C": "اختبار Photoshop", "D": "قياس سرعة الكتابة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "شركة تطلب NLP Engineer لبناء Chatbot على وثائق داخلية تتغير أسبوعياً. ما التصميم الأولي الأنسب؟", "options": {"A": "RAG مع ingestion/update pipeline وevaluation", "B": "Fine-tune كل أسبوع بالضرورة", "C": "تدريب LLM من الصفر", "D": "استخدام Prompt فقط دون الوثائق"}, "correct": "A", "difficulty": "hard"},
                    {"text": "النموذج ممتاز على Benchmark لكنه ضعيف على بيانات الشركة. ماذا تستنتج؟", "options": {"A": "يوجد Domain/Data mismatch ويجب تقييم بيانات المجال", "B": "Benchmark يثبت أن المشكلة ليست في البيانات", "C": "يجب حذف Test Set", "D": "يجب اختيار أكبر LLM مباشرة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك نموذج دقيق لكنه بطيء جداً للإنتاج. ما القرار الهندسي الصحيح؟", "options": {"A": "دراسة model size, quantization, batching, caching, serving وتحقيق trade-off", "B": "تجاهل latency", "C": "زيادة حجم النموذج", "D": "حذف Evaluation"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أفضل معيار لإعلان الطالب Job Ready؟", "options": {"A": "اجتياز التقييم النهائي + تنفيذ مشاريع حقيقية + القدرة على شرحها وحل المشكلات", "B": "إنهاء 10 كورسات", "C": "الحصول على شهادة واحدة", "D": "معرفة أسماء 100 مكتبة"}, "correct": "A", "difficulty": "hard"}
                ]
            }
        ]
    }
]