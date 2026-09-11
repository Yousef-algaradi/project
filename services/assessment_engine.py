# services/assessment_engine.py
"""
محرك اختبار الميول المهنية + أسئلة المواد
"""

class AssessmentEngine:
    
    # ==========================================
    # أبعاد الميول
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
    # أسئلة الميول (7 أسئلة)
    # ==========================================
    APTITUDE_QUESTIONS = [
        {
            'id': 1,
            'text': 'عندما تواجه مشكلة معقدة، ما أول شيء تفعله؟',
            'options': [
                {'id': 'A', 'text': 'أحلل المشكلة خطوة بخطوة للوصول للسبب الجذري', 'scores': {'analytical': 5, 'problem_solving': 4}},
                {'id': 'B', 'text': 'أجرب حلولاً عملية مباشرة حتى أجد الحل', 'scores': {'problem_solving': 5, 'practical': 4}},
                {'id': 'C', 'text': 'أبحث عن معلومات وتجارب مشابهة', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'D', 'text': 'أستشير الآخرين وأناقش الحل معهم', 'scores': {'communication': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 2,
            'text': 'أي بيئة عمل تجذبك أكثر؟',
            'options': [
                {'id': 'A', 'text': 'مختبر أو مركز أبحاث علمي', 'scores': {'research': 5, 'health': 3}},
                {'id': 'B', 'text': 'شركة تقنية أو بيئة برمجية', 'scores': {'technology': 5, 'problem_solving': 3}},
                {'id': 'C', 'text': 'مستشفى أو مركز صحي', 'scores': {'health': 5, 'communication': 4}},
                {'id': 'D', 'text': 'موقع مشاريع أو منشأة هندسية', 'scores': {'engineering': 5, 'practical': 4}}
            ]
        },
        {
            'id': 3,
            'text': 'أي إنجاز سيجعلك أكثر فخراً؟',
            'options': [
                {'id': 'A', 'text': 'اكتشاف علمي أو بحث جديد', 'scores': {'research': 5, 'analytical': 3}},
                {'id': 'B', 'text': 'تطوير تقنية أو تطبيق يستخدمه الناس', 'scores': {'technology': 5, 'creativity': 3}},
                {'id': 'C', 'text': 'مساعدة شخص على الشفاء أو تحسين حياته', 'scores': {'health': 5, 'communication': 4}},
                {'id': 'D', 'text': 'بناء مشروع أو نظام ناجح', 'scores': {'leadership': 5, 'engineering': 3}}
            ]
        },
        {
            'id': 4,
            'text': 'عندما تتعلم موضوعاً جديداً، ما الطريقة التي تفضلها؟',
            'options': [
                {'id': 'A', 'text': 'التجربة والتطبيق العملي المباشر', 'scores': {'practical': 5, 'engineering': 3}},
                {'id': 'B', 'text': 'القراءة والبحث والتحليل النظري', 'scores': {'research': 5, 'analytical': 4}},
                {'id': 'C', 'text': 'مشاهدة فيديوهات وشرح عملي', 'scores': {'technology': 4, 'practical': 3}},
                {'id': 'D', 'text': 'مناقشته مع الآخرين في مجموعة', 'scores': {'communication': 5, 'leadership': 3}}
            ]
        },
        {
            'id': 5,
            'text': 'عندما يُطلب منك حل مشكلة، ما أسلوبك؟',
            'options': [
                {'id': 'A', 'text': 'ابتكار فكرة جديدة تماماً', 'scores': {'creativity': 5, 'technology': 3}},
                {'id': 'B', 'text': 'تحسين حل موجود مسبقاً', 'scores': {'problem_solving': 4, 'practical': 3}},
                {'id': 'C', 'text': 'بناء حل عملي وفعّال بأقل موارد', 'scores': {'practical': 5, 'engineering': 4}},
                {'id': 'D', 'text': 'دراسة المشكلة بعمق قبل الاقتراح', 'scores': {'research': 5, 'analytical': 4}}
            ]
        },
        {
            'id': 6,
            'text': 'في فريق عمل، أي دور تفضله؟',
            'options': [
                {'id': 'A', 'text': 'قائد الفريق ومنظّم المهام', 'scores': {'leadership': 5, 'communication': 4}},
                {'id': 'B', 'text': 'المحلل الذي يضع الخطة الاستراتيجية', 'scores': {'analytical': 5, 'leadership': 3}},
                {'id': 'C', 'text': 'المنفّذ التقني للمهام', 'scores': {'technology': 5, 'practical': 4}},
                {'id': 'D', 'text': 'الباحث الذي يجمع المعلومات', 'scores': {'research': 5, 'analytical': 3}}
            ]
        },
        {
            'id': 7,
            'text': 'ما أهم شيء تبحث عنه في مهنتك المستقبلية؟',
            'options': [
                {'id': 'A', 'text': 'التأثير المباشر في حياة الناس', 'scores': {'health': 5, 'communication': 4}},
                {'id': 'B', 'text': 'الإبداع والابتكار المستمر', 'scores': {'creativity': 5, 'technology': 3}},
                {'id': 'C', 'text': 'الاستقرار المالي والمكانة الاجتماعية', 'scores': {'leadership': 4, 'analytical': 3}},
                {'id': 'D', 'text': 'التعلم المستمر وتطوير الذات', 'scores': {'research': 5, 'analytical': 3}}
            ]
        }
    ]

    # ==========================================
    # أسئلة المواد
    # ==========================================
    SUBJECT_QUESTIONS = {
        # ============ القسم العلمي ============
        'علمي': {
            'math': {
                'name': '📐 الرياضيات',
                'questions': [
                    {
                        'id': 'math_1',
                        'difficulty': 'سهل',
                        'text': 'ما ناتج 15 + 27؟',
                        'options': [
                            {'id': 'A', 'text': '32'},
                            {'id': 'B', 'text': '42'},
                            {'id': 'C', 'text': '52'},
                            {'id': 'D', 'text': '40'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'math_2',
                        'difficulty': 'متوسط',
                        'text': 'ما هو حل المعادلة 2x + 6 = 14؟',
                        'options': [
                            {'id': 'A', 'text': 'x = 3'},
                            {'id': 'B', 'text': 'x = 4'},
                            {'id': 'C', 'text': 'x = 5'},
                            {'id': 'D', 'text': 'x = 6'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'math_3',
                        'difficulty': 'صعب',
                        'text': 'ما هو مشتق الدالة f(x) = x³ + 2x² - 5x؟',
                        'options': [
                            {'id': 'A', 'text': '3x² + 4x - 5'},
                            {'id': 'B', 'text': '3x² + 2x - 5'},
                            {'id': 'C', 'text': 'x² + 4x - 5'},
                            {'id': 'D', 'text': '3x² + 4x + 5'}
                        ],
                        'correct': 'A'
                    }
                ]
            },
            'physics': {
                'name': '⚡ الفيزياء',
                'questions': [
                    {
                        'id': 'physics_1',
                        'difficulty': 'سهل',
                        'text': 'ما هي وحدة قياس القوة في النظام الدولي؟',
                        'options': [
                            {'id': 'A', 'text': 'الجول'},
                            {'id': 'B', 'text': 'الواط'},
                            {'id': 'C', 'text': 'النيوتن'},
                            {'id': 'D', 'text': 'الأمبير'}
                        ],
                        'correct': 'C'
                    },
                    {
                        'id': 'physics_2',
                        'difficulty': 'متوسط',
                        'text': 'إذا تحرك جسم بسرعة 20 م/ث لمدة 5 ثوانٍ، فما المسافة المقطوعة؟',
                        'options': [
                            {'id': 'A', 'text': '80 متر'},
                            {'id': 'B', 'text': '100 متر'},
                            {'id': 'C', 'text': '120 متر'},
                            {'id': 'D', 'text': '60 متر'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'physics_3',
                        'difficulty': 'صعب',
                        'text': 'ما هي وحدة قياس الطاقة الحركية؟',
                        'options': [
                            {'id': 'A', 'text': 'النيوتن'},
                            {'id': 'B', 'text': 'الجول'},
                            {'id': 'C', 'text': 'الواط'},
                            {'id': 'D', 'text': 'الباسكال'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'chemistry': {
                'name': '🧪 الكيمياء',
                'questions': [
                    {
                        'id': 'chemistry_1',
                        'difficulty': 'سهل',
                        'text': 'ما هو الرمز الكيميائي للماء؟',
                        'options': [
                            {'id': 'A', 'text': 'CO₂'},
                            {'id': 'B', 'text': 'H₂O'},
                            {'id': 'C', 'text': 'O₂'},
                            {'id': 'D', 'text': 'NaCl'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'chemistry_2',
                        'difficulty': 'متوسط',
                        'text': 'كم عدد الإلكترونات في ذرة الكربون؟',
                        'options': [
                            {'id': 'A', 'text': '4'},
                            {'id': 'B', 'text': '6'},
                            {'id': 'C', 'text': '8'},
                            {'id': 'D', 'text': '12'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'chemistry_3',
                        'difficulty': 'صعب',
                        'text': 'ما هو العنصر الأكثر كهروسلبية في الجدول الدوري؟',
                        'options': [
                            {'id': 'A', 'text': 'الأكسجين'},
                            {'id': 'B', 'text': 'الفلور'},
                            {'id': 'C', 'text': 'الكلور'},
                            {'id': 'D', 'text': 'النيتروجين'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'biology': {
                'name': '🧬 الأحياء',
                'questions': [
                    {
                        'id': 'biology_1',
                        'difficulty': 'سهل',
                        'text': 'ما هي وحدة بناء الجسم الأساسية؟',
                        'options': [
                            {'id': 'A', 'text': 'النسيج'},
                            {'id': 'B', 'text': 'الخلية'},
                            {'id': 'C', 'text': 'العضو'},
                            {'id': 'D', 'text': 'الجزيء'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'biology_2',
                        'difficulty': 'متوسط',
                        'text': 'ما هي العملية التي تنتج فيها النباتات الغذاء؟',
                        'options': [
                            {'id': 'A', 'text': 'التنفس'},
                            {'id': 'B', 'text': 'البناء الضوئي'},
                            {'id': 'C', 'text': 'النتح'},
                            {'id': 'D', 'text': 'الانتشار'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'biology_3',
                        'difficulty': 'صعب',
                        'text': 'ما هو العضوان المسؤولان عن تنقية الدم في جسم الإنسان؟',
                        'options': [
                            {'id': 'A', 'text': 'الكبد والقلب'},
                            {'id': 'B', 'text': 'الكلى'},
                            {'id': 'C', 'text': 'الرئتان'},
                            {'id': 'D', 'text': 'الطحال'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'english': {
                'name': '🇬🇧 اللغة الإنجليزية',
                'questions': [
                    {
                        'id': 'english_1',
                        'difficulty': 'سهل',
                        'text': 'اختر الكلمة الصحيحة: She ____ to school every day.',
                        'options': [
                            {'id': 'A', 'text': 'go'},
                            {'id': 'B', 'text': 'goes'},
                            {'id': 'C', 'text': 'going'},
                            {'id': 'D', 'text': 'gone'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'english_2',
                        'difficulty': 'متوسط',
                        'text': 'ما معنى كلمة "Innovation"؟',
                        'options': [
                            {'id': 'A', 'text': 'التعليم'},
                            {'id': 'B', 'text': 'الابتكار'},
                            {'id': 'C', 'text': 'الاختراع'},
                            {'id': 'D', 'text': 'التطوير'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'english_3',
                        'difficulty': 'صعب',
                        'text': 'اختر الصيغة الصحيحة: If I ____ rich, I would travel the world.',
                        'options': [
                            {'id': 'A', 'text': 'am'},
                            {'id': 'B', 'text': 'was'},
                            {'id': 'C', 'text': 'were'},
                            {'id': 'D', 'text': 'be'}
                        ],
                        'correct': 'C'
                    }
                ]
            }
        },
        # ============ القسم الأدبي ============
        'أدبي': {
            'arabic': {
                'name': '📖 اللغة العربية',
                'questions': [
                    {
                        'id': 'arabic_1',
                        'difficulty': 'سهل',
                        'text': 'ما هو نوع كلمة "كتاب" في اللغة العربية؟',
                        'options': [
                            {'id': 'A', 'text': 'فعل'},
                            {'id': 'B', 'text': 'اسم'},
                            {'id': 'C', 'text': 'حرف'},
                            {'id': 'D', 'text': 'ضمير'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'arabic_2',
                        'difficulty': 'متوسط',
                        'text': 'ما إعراب كلمة "المعلمُ" في جملة "المعلمُ مخلصٌ"؟',
                        'options': [
                            {'id': 'A', 'text': 'مفعول به'},
                            {'id': 'B', 'text': 'مبتدأ مرفوع'},
                            {'id': 'C', 'text': 'خبر'},
                            {'id': 'D', 'text': 'فاعل'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'arabic_3',
                        'difficulty': 'صعب',
                        'text': 'ما هو الوزن الصرفي لكلمة "استغفار"؟',
                        'options': [
                            {'id': 'A', 'text': 'افتعال'},
                            {'id': 'B', 'text': 'استفعال'},
                            {'id': 'C', 'text': 'مفاعلة'},
                            {'id': 'D', 'text': 'تفعيل'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'history': {
                'name': '📜 التاريخ',
                'questions': [
                    {
                        'id': 'history_1',
                        'difficulty': 'سهل',
                        'text': 'في أي عام انتهت الحرب العالمية الثانية؟',
                        'options': [
                            {'id': 'A', 'text': '1943'},
                            {'id': 'B', 'text': '1945'},
                            {'id': 'C', 'text': '1947'},
                            {'id': 'D', 'text': '1950'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'history_2',
                        'difficulty': 'متوسط',
                        'text': 'من هو مؤسس الدولة السعودية الثالثة؟',
                        'options': [
                            {'id': 'A', 'text': 'الملك عبدالعزيز آل سعود'},
                            {'id': 'B', 'text': 'الملك فيصل'},
                            {'id': 'C', 'text': 'الملك سعود'},
                            {'id': 'D', 'text': 'الملك فهد'}
                        ],
                        'correct': 'A'
                    },
                    {
                        'id': 'history_3',
                        'difficulty': 'صعب',
                        'text': 'في أي عام سقطت الدولة العباسية على يد المغول؟',
                        'options': [
                            {'id': 'A', 'text': '1258م'},
                            {'id': 'B', 'text': '1453م'},
                            {'id': 'C', 'text': '1187م'},
                            {'id': 'D', 'text': '1300م'}
                        ],
                        'correct': 'A'
                    }
                ]
            },
            'geography': {
                'name': '🌍 الجغرافيا',
                'questions': [
                    {
                        'id': 'geography_1',
                        'difficulty': 'سهل',
                        'text': 'ما هي أكبر قارة في العالم من حيث المساحة؟',
                        'options': [
                            {'id': 'A', 'text': 'أفريقيا'},
                            {'id': 'B', 'text': 'آسيا'},
                            {'id': 'C', 'text': 'أوروبا'},
                            {'id': 'D', 'text': 'أمريكا الشمالية'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'geography_2',
                        'difficulty': 'متوسط',
                        'text': 'ما هو أطول نهر في العالم؟',
                        'options': [
                            {'id': 'A', 'text': 'النيل'},
                            {'id': 'B', 'text': 'الأمازون'},
                            {'id': 'C', 'text': 'الفرات'},
                            {'id': 'D', 'text': 'المسيسيبي'}
                        ],
                        'correct': 'A'
                    },
                    {
                        'id': 'geography_3',
                        'difficulty': 'صعب',
                        'text': 'ما هي الدولة التي تمتلك أكبر احتياطي نفطي في العالم؟',
                        'options': [
                            {'id': 'A', 'text': 'السعودية'},
                            {'id': 'B', 'text': 'فنزويلا'},
                            {'id': 'C', 'text': 'روسيا'},
                            {'id': 'D', 'text': 'إيران'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'islamic': {
                'name': '☪️ التربية الإسلامية',
                'questions': [
                    {
                        'id': 'islamic_1',
                        'difficulty': 'سهل',
                        'text': 'كم عدد أركان الإسلام؟',
                        'options': [
                            {'id': 'A', 'text': '4'},
                            {'id': 'B', 'text': '5'},
                            {'id': 'C', 'text': '6'},
                            {'id': 'D', 'text': '7'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'islamic_2',
                        'difficulty': 'متوسط',
                        'text': 'ما هي أول سورة نزلت في القرآن الكريم؟',
                        'options': [
                            {'id': 'A', 'text': 'الفاتحة'},
                            {'id': 'B', 'text': 'العلق'},
                            {'id': 'C', 'text': 'البقرة'},
                            {'id': 'D', 'text': 'الناس'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'islamic_3',
                        'difficulty': 'صعب',
                        'text': 'في أي عام هجري وقعت غزوة بدر؟',
                        'options': [
                            {'id': 'A', 'text': '1 هـ'},
                            {'id': 'B', 'text': '2 هـ'},
                            {'id': 'C', 'text': '3 هـ'},
                            {'id': 'D', 'text': '5 هـ'}
                        ],
                        'correct': 'B'
                    }
                ]
            },
            'english': {
                'name': '🇬🇧 اللغة الإنجليزية',
                'questions': [
                    {
                        'id': 'english_1',
                        'difficulty': 'سهل',
                        'text': 'اختر الكلمة الصحيحة: They ____ playing football now.',
                        'options': [
                            {'id': 'A', 'text': 'is'},
                            {'id': 'B', 'text': 'are'},
                            {'id': 'C', 'text': 'am'},
                            {'id': 'D', 'text': 'be'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'english_2',
                        'difficulty': 'متوسط',
                        'text': 'ما معنى كلمة "Communication"؟',
                        'options': [
                            {'id': 'A', 'text': 'التعليم'},
                            {'id': 'B', 'text': 'التواصل'},
                            {'id': 'C', 'text': 'الكتابة'},
                            {'id': 'D', 'text': 'الإعلام'}
                        ],
                        'correct': 'B'
                    },
                    {
                        'id': 'english_3',
                        'difficulty': 'صعب',
                        'text': 'اختر الصيغة الصحيحة: She has been studying English ____ 2018.',
                        'options': [
                            {'id': 'A', 'text': 'for'},
                            {'id': 'B', 'text': 'since'},
                            {'id': 'C', 'text': 'from'},
                            {'id': 'D', 'text': 'in'}
                        ],
                        'correct': 'B'
                    }
                ]
            }
        }
    }

    # ==========================================
    # دالة حساب درجات أبعاد الميول
    # ==========================================
    @staticmethod
    def calculate_dimension_scores(answers):
        """
        تحسب درجات كل بُعد من إجابات الميول.
        :param answers: dict {question_id: option_id}
        :return: dict {dimension: normalized_score (0-100)}
        """
        raw_scores = {dim: 0 for dim in AssessmentEngine.APTITUDE_DIMENSIONS}
        max_possible = {dim: 0 for dim in AssessmentEngine.APTITUDE_DIMENSIONS}
        
        for question in AssessmentEngine.APTITUDE_QUESTIONS:
            qid = question['id']
            if qid not in answers:
                continue
            
            selected_option_id = answers[qid]
            selected_option = next((opt for opt in question['options'] if opt['id'] == selected_option_id), None)
            if not selected_option:
                continue
            
            for dim, score in selected_option['scores'].items():
                raw_scores[dim] += score
            
            for opt in question['options']:
                for dim, score in opt['scores'].items():
                    max_possible[dim] += score
        
        normalized = {}
        for dim in AssessmentEngine.APTITUDE_DIMENSIONS:
            if max_possible[dim] > 0:
                normalized[dim] = round((raw_scores[dim] / max_possible[dim]) * 100, 1)
            else:
                normalized[dim] = 0
        
        return normalized

    # ==========================================
    # دالة تصحيح أسئلة المواد
    # ==========================================
    @staticmethod
    def calculate_subject_scores(answers, branch):
        """
        تصحيح أسئلة المواد.
        :param answers: dict {question_id: option_id}
        :param branch: 'علمي' أو 'أدبي'
        :return: dict {subject_key: score_0_to_100} - None للـ N/A
        """
        subject_scores = {}
        
        if branch not in AssessmentEngine.SUBJECT_QUESTIONS:
            return subject_scores
        
        subjects_data = AssessmentEngine.SUBJECT_QUESTIONS[branch]
        
        for subject_key, subject_info in subjects_data.items():
            questions = subject_info['questions']
            correct_count = 0
            answered_count = 0  # عدد الأسئلة التي أجاب عليها (بدون تخطي)
            
            for q in questions:
                qid = q['id']
                if qid in answers:
                    answered_count += 1
                    if answers[qid] == q['correct']:
                        correct_count += 1
                # إذا لم يجب → لا تحسب (N/A)
            
            # إذا لم يجب على أي سؤال → N/A
            if answered_count == 0:
                subject_scores[subject_key] = None  # N/A
            else:
                # الدرجة من عدد الأسئلة التي أجاب عليها فقط
                subject_scores[subject_key] = round((correct_count / answered_count) * 100, 1)
        
        return subject_scores