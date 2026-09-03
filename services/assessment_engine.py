# services/assessment_engine.py
"""
محرك اختبار الميول المهنية
يحتوي على أسئلة الميول العشرين ومنطق حساب الدرجات للأبعاد المختلفة
"""

class AssessmentEngine:
    
    # ==========================================
    # أبعاد الميول المهنية
    # ==========================================
    APTITUDE_DIMENSIONS = {
        'analytical': 'التحليل والمنطق',
        'problem_solving': 'حل المشكلات',
        'technology': 'التكنولوجيا',
        'research': 'البحث العلمي',
        'communication': 'التواصل والعمل الجماعي',
        'creativity': 'الإبداع',
        'leadership': 'القيادة',
        'practical': 'العمل العملي',
        'health': 'الاهتمام بالصحة والإنسان',
        'engineering': 'التصميم والهندسة'
    }

    # ==========================================
    # أسئلة الميول (20 سؤال)
    # كل سؤال له خيارات وكل خيار يعطي درجات لأبعاد معينة
    # ==========================================
    QUESTIONS = [
        {
            'id': 1,
            'text': 'واجهت مشكلة معقدة ولا تعرف سببها، ماذا تفضل أن تفعل؟',
            'options': [
                {'id': 'A', 'text': 'أحلل المشكلة خطوة بخطوة وأبحث عن السبب', 'scores': {'analytical': 5, 'problem_solving': 4}},
                {'id': 'B', 'text': 'أجرب حلولًا مختلفة حتى أجد الحل المناسب', 'scores': {'problem_solving': 5, 'practical': 3}},
                {'id': 'C', 'text': 'أبحث عن معلومات وتجارب سابقة تساعدني', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'D', 'text': 'أناقش المشكلة مع الآخرين للوصول إلى حل', 'scores': {'communication': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 2,
            'text': 'أي بيئة عمل تبدو أكثر جاذبية لك؟',
            'options': [
                {'id': 'A', 'text': 'مختبر أو مركز أبحاث', 'scores': {'research': 5, 'health': 3}},
                {'id': 'B', 'text': 'شركة تقنية أو بيئة برمجية', 'scores': {'technology': 5, 'problem_solving': 3}},
                {'id': 'C', 'text': 'مستشفى أو مركز صحي', 'scores': {'health': 5, 'communication': 3}},
                {'id': 'D', 'text': 'موقع مشاريع أو منشأة هندسية', 'scores': {'engineering': 5, 'practical': 4}}
            ]
        },
        {
            'id': 3,
            'text': 'عندما يأتي شخص إليك وهو يعاني من مشكلة، ما الشيء الذي تستمتع به أكثر؟',
            'options': [
                {'id': 'A', 'text': 'فهم المشكلة ومساعدته على حلها', 'scores': {'problem_solving': 4, 'communication': 3}},
                {'id': 'B', 'text': 'الاستماع إليه ومحاولة فهم مشاعره', 'scores': {'communication': 5, 'health': 3}},
                {'id': 'C', 'text': 'البحث عن السبب العلمي للمشكلة', 'scores': {'research': 5, 'analytical': 4}},
                {'id': 'D', 'text': 'إعطاؤه خطوات عملية واضحة', 'scores': {'practical': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 4,
            'text': 'إذا حصلت على جهاز أو برنامج جديد، ماذا تفعل غالبًا؟',
            'options': [
                {'id': 'A', 'text': 'أحاول فهم كيفية عمله', 'scores': {'analytical': 4, 'research': 3}},
                {'id': 'B', 'text': 'أبحث عن طريقة لتطويره أو تحسينه', 'scores': {'technology': 5, 'creativity': 4}},
                {'id': 'C', 'text': 'أستخدمه مباشرة لإنجاز المهمة', 'scores': {'practical': 5, 'problem_solving': 2}},
                {'id': 'D', 'text': 'أفضل أن يشرح لي شخص آخر طريقة استخدامه', 'scores': {'communication': 3}}
            ]
        },
        {
            'id': 5,
            'text': 'أي نوع من الأسئلة يثير فضولك أكثر؟',
            'options': [
                {'id': 'A', 'text': 'لماذا تحدث هذه الظاهرة؟', 'scores': {'research': 5, 'analytical': 4}},
                {'id': 'B', 'text': 'كيف يمكن علاج هذه المشكلة؟', 'scores': {'health': 5, 'problem_solving': 3}},
                {'id': 'C', 'text': 'كيف يمكن بناء شيء يحل هذه المشكلة؟', 'scores': {'engineering': 5, 'practical': 4}},
                {'id': 'D', 'text': 'كيف يمكن استخدام التكنولوجيا لحلها؟', 'scores': {'technology': 5, 'problem_solving': 3}}
            ]
        },
        {
            'id': 6,
            'text': 'أي نشاط تفضله؟',
            'options': [
                {'id': 'A', 'text': 'إجراء تجربة علمية', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'B', 'text': 'بناء أو إصلاح شيء', 'scores': {'practical': 5, 'engineering': 4}},
                {'id': 'C', 'text': 'كتابة برنامج أو تحليل بيانات', 'scores': {'technology': 5, 'analytical': 4}},
                {'id': 'D', 'text': 'إجراء مقابلة أو التواصل مع أشخاص', 'scores': {'communication': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 7,
            'text': 'كيف تشعر عندما تواجه مسألة تحتاج إلى تحليل أرقام وبيانات؟',
            'options': [
                {'id': 'A', 'text': 'أستمتع بتحليلها واكتشاف الأنماط', 'scores': {'analytical': 5, 'research': 3}},
                {'id': 'B', 'text': 'لا أمانع، لكن أفضل الأمور العملية', 'scores': {'practical': 3}},
                {'id': 'C', 'text': 'أحب استخدامها لاتخاذ قرار', 'scores': {'leadership': 4, 'analytical': 3}},
                {'id': 'D', 'text': 'أفضل تجنبها قدر الإمكان', 'scores': {}}
            ]
        },
        {
            'id': 8,
            'text': 'لو أعطيتك سؤالًا لا توجد له إجابة واضحة، ماذا تفعل؟',
            'options': [
                {'id': 'A', 'text': 'أبحث وأقرأ حتى أصل إلى نتيجة', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'B', 'text': 'أجرب بنفسي', 'scores': {'practical': 5, 'problem_solving': 4}},
                {'id': 'C', 'text': 'أسأل أشخاصًا لديهم خبرة', 'scores': {'communication': 4, 'leadership': 2}},
                {'id': 'D', 'text': 'أبحث عن طريقة تقنية لحل المشكلة', 'scores': {'technology': 5, 'problem_solving': 4}}
            ]
        },
        {
            'id': 9,
            'text': 'عندما يُطلب منك تصميم حل لمشكلة، ماذا تفضل؟',
            'options': [
                {'id': 'A', 'text': 'ابتكار فكرة جديدة تمامًا', 'scores': {'creativity': 5, 'technology': 3}},
                {'id': 'B', 'text': 'تحسين حل موجود', 'scores': {'problem_solving': 4, 'practical': 3}},
                {'id': 'C', 'text': 'بناء حل عملي وفعال', 'scores': {'practical': 5, 'engineering': 4}},
                {'id': 'D', 'text': 'دراسة المشكلة أولًا بشكل عميق', 'scores': {'research': 5, 'analytical': 4}}
            ]
        },
        {
            'id': 10,
            'text': 'في موقف يحتاج إلى قرار سريع، ماذا تفعل؟',
            'options': [
                {'id': 'A', 'text': 'أحلل المعلومات المتاحة بسرعة', 'scores': {'analytical': 5, 'problem_solving': 3}},
                {'id': 'B', 'text': 'أركز على الشخص المتضرر وأتصرف لمساعدته', 'scores': {'health': 5, 'communication': 4}},
                {'id': 'C', 'text': 'أعتمد على خبرتي وأتخذ القرار', 'scores': {'leadership': 5, 'practical': 3}},
                {'id': 'D', 'text': 'أفضل أخذ وقت كافٍ قبل القرار', 'scores': {'research': 3, 'analytical': 3}}
            ]
        },
        {
            'id': 11,
            'text': 'أي وصف أقرب لك؟',
            'options': [
                {'id': 'A', 'text': 'ألاحظ التفاصيل الصغيرة بسرعة', 'scores': {'analytical': 5, 'research': 3}},
                {'id': 'B', 'text': 'أهتم بالصورة الكبيرة أكثر', 'scores': {'leadership': 3, 'creativity': 3}},
                {'id': 'C', 'text': 'أهتم بالنتيجة النهائية', 'scores': {'practical': 4, 'problem_solving': 2}},
                {'id': 'D', 'text': 'أهتم بكيفية تنفيذ العمل', 'scores': {'practical': 5, 'engineering': 3}}
            ]
        },
        {
            'id': 12,
            'text': 'لو كان لديك مختبر ومجموعة أدوات علمية لمدة يوم كامل، ماذا ستفعل؟',
            'options': [
                {'id': 'A', 'text': 'أجرب وأختبر فرضيات مختلفة', 'scores': {'research': 5, 'analytical': 4}},
                {'id': 'B', 'text': 'أتعلم كيفية استخدام الأدوات', 'scores': {'practical': 4, 'technology': 3}},
                {'id': 'C', 'text': 'أحاول اكتشاف شيء جديد', 'scores': {'creativity': 5, 'research': 4}},
                {'id': 'D', 'text': 'أفضل استخدام الوقت في مشروع عملي', 'scores': {'practical': 5, 'engineering': 3}}
            ]
        },
        {
            'id': 13,
            'text': 'أي نشاط يبدو ممتعًا أكثر؟',
            'options': [
                {'id': 'A', 'text': 'كتابة برنامج لحل مشكلة', 'scores': {'technology': 5, 'problem_solving': 4}},
                {'id': 'B', 'text': 'تحليل البيانات واستخراج النتائج', 'scores': {'analytical': 5, 'research': 3}},
                {'id': 'C', 'text': 'تصميم جهاز أو نظام', 'scores': {'engineering': 5, 'practical': 4}},
                {'id': 'D', 'text': 'دراسة مشكلة علمية', 'scores': {'research': 5, 'analytical': 4}}
            ]
        },
        {
            'id': 14,
            'text': 'أي موضوع يثير اهتمامك أكثر؟',
            'options': [
                {'id': 'A', 'text': 'كيفية عمل جسم الإنسان', 'scores': {'health': 5, 'research': 4}},
                {'id': 'B', 'text': 'أسباب الأمراض وكيفية علاجها', 'scores': {'health': 5, 'problem_solving': 3}},
                {'id': 'C', 'text': 'كيفية تطوير أجهزة تساعد المرضى', 'scores': {'engineering': 4, 'health': 4, 'technology': 3}},
                {'id': 'D', 'text': 'دراسة الكائنات الحية والبيئة', 'scores': {'research': 5, 'health': 3}}
            ]
        },
        {
            'id': 15,
            'text': 'لو طُلب منك تصميم جسر، ما الجانب الذي يجذبك؟',
            'options': [
                {'id': 'A', 'text': 'حساب القوة والأحمال', 'scores': {'engineering': 5, 'analytical': 4}},
                {'id': 'B', 'text': 'تصميم الشكل', 'scores': {'creativity': 5, 'engineering': 3}},
                {'id': 'C', 'text': 'اختيار المواد المناسبة', 'scores': {'practical': 4, 'engineering': 4}},
                {'id': 'D', 'text': 'استخدام التكنولوجيا لمراقبته وتحسينه', 'scores': {'technology': 5, 'engineering': 3}}
            ]
        },
        {
            'id': 16,
            'text': 'أي مهمة تفضل؟',
            'options': [
                {'id': 'A', 'text': 'تقديم فكرة أمام مجموعة', 'scores': {'communication': 5, 'leadership': 4}},
                {'id': 'B', 'text': 'العمل بمفردي على مشكلة', 'scores': {'analytical': 4, 'problem_solving': 3}},
                {'id': 'C', 'text': 'قيادة فريق لإنجاز مشروع', 'scores': {'leadership': 5, 'communication': 3}},
                {'id': 'D', 'text': 'إجراء بحث وتحليل النتائج', 'scores': {'research': 5, 'analytical': 4}}
            ]
        },
        {
            'id': 17,
            'text': 'أي إنجاز سيجعلك أكثر فخرًا؟',
            'options': [
                {'id': 'A', 'text': 'اكتشاف علمي جديد', 'scores': {'research': 5, 'creativity': 3}},
                {'id': 'B', 'text': 'تطوير تقنية يستخدمها الناس', 'scores': {'technology': 5, 'practical': 3}},
                {'id': 'C', 'text': 'مساعدة الناس وتحسين حياتهم', 'scores': {'health': 5, 'communication': 4}},
                {'id': 'D', 'text': 'بناء مشروع أو نظام ناجح', 'scores': {'engineering': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 18,
            'text': 'عندما تتعلم موضوعًا جديدًا، ما الطريقة التي تفضلها؟',
            'options': [
                {'id': 'A', 'text': 'التجربة والتطبيق', 'scores': {'practical': 5, 'problem_solving': 3}},
                {'id': 'B', 'text': 'القراءة والبحث', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'C', 'text': 'مشاهدة شرح عملي', 'scores': {'practical': 4, 'communication': 2}},
                {'id': 'D', 'text': 'مناقشته مع الآخرين', 'scores': {'communication': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 19,
            'text': 'لو كنت ضمن فريق لإنجاز مشروع، أي دور تفضل؟',
            'options': [
                {'id': 'A', 'text': 'تحليل المشكلة ووضع الخطة', 'scores': {'analytical': 5, 'leadership': 3}},
                {'id': 'B', 'text': 'تنفيذ الجزء التقني', 'scores': {'technology': 5, 'practical': 4}},
                {'id': 'C', 'text': 'البحث وجمع المعلومات', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'D', 'text': 'تنظيم الفريق والتواصل', 'scores': {'communication': 5, 'leadership': 4}}
            ]
        },
        {
            'id': 20,
            'text': 'أي نوع من الإنجازات يجذبك أكثر؟',
            'options': [
                {'id': 'A', 'text': 'تطوير برنامج أو تقنية جديدة', 'scores': {'technology': 5, 'creativity': 4}},
                {'id': 'B', 'text': 'اكتشاف علمي أو إجراء بحث', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'C', 'text': 'تشخيص مشكلة ومساعدة شخص على علاجها', 'scores': {'health': 5, 'communication': 3}},
                {'id': 'D', 'text': 'تصميم وبناء حل هندسي', 'scores': {'engineering': 5, 'practical': 4}}
            ]
        }
    ]

    # ==========================================
    # دالة حساب درجات الأبعاد من الإجابات
    # ==========================================
    @staticmethod
    def calculate_dimension_scores(answers):
        """
        تحسب درجات كل بُعد من إجابات المستخدم.
        
        :param answers: dict بصيغة {question_id: option_id}
                        مثال: {1: 'A', 2: 'B', ...}
        :return: dict بصيغة {dimension: normalized_score (0-100)}
        """
        # قاموس لتجميع الدرجات الخام لكل بُعد
        raw_scores = {dim: 0 for dim in AssessmentEngine.APTITUDE_DIMENSIONS}
        max_possible = {dim: 0 for dim in AssessmentEngine.APTITUDE_DIMENSIONS}
        
        # لكل سؤال، نضيف درجات الخيار المختار
        for question in AssessmentEngine.QUESTIONS:
            qid = question['id']
            if qid not in answers:
                continue  # سؤال تم تخطيه
            
            selected_option_id = answers[qid]
            selected_option = next((opt for opt in question['options'] if opt['id'] == selected_option_id), None)
            if not selected_option:
                continue
            
            for dim, score in selected_option['scores'].items():
                raw_scores[dim] += score
            
            # حساب أقصى درجة ممكنة لكل بُعد من هذا السؤال
            for opt in question['options']:
                for dim, score in opt['scores'].items():
                    max_possible[dim] += score
        
        # تحويل الدرجات الخام إلى نسبة مئوية (0-100)
        normalized = {}
        for dim in AssessmentEngine.APTITUDE_DIMENSIONS:
            if max_possible[dim] > 0:
                normalized[dim] = round((raw_scores[dim] / max_possible[dim]) * 100, 1)
            else:
                normalized[dim] = 0
        
        return normalized