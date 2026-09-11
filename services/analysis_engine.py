# services/analysis_engine.py
import json
import re


class AnalysisEngine:
    MAJORS_DB = [
        # ==========================================
        # الفرع العلمي (6 تخصصات)
        # ==========================================
        {
            "title": "الطب والعلوم الصحية (Medicine & Health Sciences)",
            "branch": "علمي",
            "min_percentage": 82.0,
            "subject_weights": {"biology": 0.45, "chemistry": 0.35, "english": 0.20},
            "keywords": ["طب", "صحة", "أحياء", "كيمياء", "علاج", "تشخيص", "إنسان"],
            "aptitude_profile": {
                "analytical": 0.6, "technology": 0.3, "research": 0.7, "problem_solving": 0.7,
                "practical": 0.7, "creativity": 0.2, "communication": 0.85, "leadership": 0.4,
                "health": 1.0, "engineering": 0.1
            },
            "career_paths": [
                {
                    "title": "طبيب بشري (Physician)",
                    "description": "تشخيص الأمراض وعلاجها ومتابعة المرضى في المستشفيات والمراكز الصحية.",
                    "salary": "18,000 - 45,000 ريال سعودي",
                    "skills": ["التشخيص", "التواصل", "التفكير السريري", "الطب الباطني", "الإسعافات الأولية"],
                    "benefits": "مكانة اجتماعية مرموقة، تأثير مباشر في حياة الناس، رواتب مرتفعة، فرص في كل مكان."
                },
                {
                    "title": "طبيب أسنان (Dentist)",
                    "description": "تشخيص وعلاج أمراض الفم والأسنان واللثة، مع إمكانية التخصص في التقويم أو الجراحة.",
                    "salary": "15,000 - 40,000 ريال سعودي",
                    "skills": ["تشخيص الأسنان", "الحشو", "التقويم", "الجراحة الفموية", "الدقة اليدوية"],
                    "benefits": "عمل مستقل، دخل مرتفع، ساعات عمل مرنة، إمكانية عيادة خاصة."
                },
                {
                    "title": "صيدلي (Pharmacist)",
                    "description": "صرف الأدوية والاستشارات الدوائية والعمل في المستشفيات أو الصناعات الدوائية.",
                    "salary": "10,000 - 22,000 ريال سعودي",
                    "skills": ["علم الأدوية", "الاستشارات", "التواصل", "إدارة الصيدلية", "الجرعات"],
                    "benefits": "عمل مستقر، فرص في كل مكان، تأثير على صحة المرضى."
                },
                {
                    "title": "ممرض (Registered Nurse)",
                    "description": "تقديم الرعاية الصحية المباشرة للمرضى ومتابعة حالاتهم في المستشفيات.",
                    "salary": "8,000 - 15,000 ريال سعودي",
                    "skills": ["الرعاية", "التواصل", "الملاحظة", "الإسعافات", "العمل الجماعي"],
                    "benefits": "طلب مستمر، فرص واسعة، عمل إنساني."
                },
                {
                    "title": "أخصائي مختبرات طبية (Medical Lab Specialist)",
                    "description": "إجراء التحاليل المخبرية والفحوصات التي تساعد في التشخيص الدقيق.",
                    "salary": "8,000 - 16,000 ريال سعودي",
                    "skills": ["التحاليل", "الأجهزة المخبرية", "الدقة", "الكيمياء الحيوية", "الدم"],
                    "benefits": "عمل مخبري تقني، دقة علمية، طلب مرتفع."
                }
            ]
        },
        {
            "title": "الذكاء الاصطناعي (Artificial Intelligence)",
            "branch": "علمي",
            "min_percentage": 75.0,
            "subject_weights": {"math": 0.50, "physics": 0.25, "english": 0.25},
            "keywords": ["ذكاء اصطناعي", "تعلم آلة", "روبوتات", "خوارزميات", "رياضيات", "برمجة"],
            "aptitude_profile": {
                "analytical": 0.95, "technology": 0.9, "research": 0.8, "problem_solving": 0.85,
                "practical": 0.6, "creativity": 0.7, "communication": 0.2, "leadership": 0.1,
                "health": 0.05, "engineering": 0.4
            },
            "career_paths": [
                {
                    "title": "مهندس تعلم آلة (Machine Learning Engineer)",
                    "description": "يصمم ويطور نماذج التعلم الآلي ويضبطها لتعمل بكفاءة في التطبيقات الواقعية.",
                    "salary": "15,000 - 30,000 ريال سعودي",
                    "skills": ["Python", "TensorFlow/PyTorch", "ML Algorithms", "Data Preprocessing", "Deployment", "SQL"],
                    "benefits": "مجال ساخن جداً، رواتب عالية، إمكانية العمل في الشركات الناشئة والكبيرة."
                },
                {
                    "title": "باحث في الذكاء الاصطناعي (AI Researcher)",
                    "description": "يبتكر خوارزميات ونماذج جديدة للذكاء الاصطناعي، وينشر أبحاثاً في المجلات العلمية.",
                    "salary": "20,000 - 40,000 ريال سعودي",
                    "skills": ["Python", "رياضيات متقدمة", "إحصاء", "Deep Learning", "قراءة الأبحاث", "الكتابة العلمية"],
                    "benefits": "فرص أكاديمية وبحثية، مكانة مرموقة، إمكانية العمل في جامعات ومراكز بحثية."
                },
                {
                    "title": "مهندس روبوتات (Robotics Engineer)",
                    "description": "يبرمج ويصمم الروبوتات الذكية التي تتفاعل مع البيئة، باستخدام الذكاء الاصطناعي والتحكم الآلي.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["Python/C++", "ROS", "Control Systems", "Computer Vision", "Sensors", "Embedded Systems"],
                    "benefits": "عمل مشوق وملموس، تطبيقات في الصناعة والطب والخدمات."
                }
            ]
        },
        {
            "title": "الأمن السيبراني (Cyber Security)",
            "branch": "علمي",
            "min_percentage": 70.0,
            "subject_weights": {"math": 0.30, "physics": 0.20, "english": 0.50},
            "keywords": ["أمن", "شبكات", "حماية", "اختراق", "سيبراني"],
            "aptitude_profile": {
                "analytical": 0.85, "technology": 0.9, "research": 0.6, "problem_solving": 0.9,
                "practical": 0.75, "creativity": 0.3, "communication": 0.2, "leadership": 0.1,
                "health": 0.05, "engineering": 0.6
            },
            "career_paths": [
                {
                    "title": "محلل أمن سيبراني (Security Analyst)",
                    "description": "يراقب الأنظمة والشبكات للكشف عن التهديدات والهجمات، ويستجيب للحوادث الأمنية ويعزز الحماية.",
                    "salary": "10,000 - 20,000 ريال سعودي",
                    "skills": ["Networking", "Firewalls", "SIEM", "Vulnerability Assessment", "Python", "Linux"],
                    "benefits": "طلب متزايد جداً، فرص في كل القطاعات، عمل حيوي ومهم."
                },
                {
                    "title": "مهندس اختبار الاختراق (Penetration Tester)",
                    "description": "يحاكي هجمات القراصنة لاختبار نقاط الضعف في الأنظمة، ويقدم تقارير لإصلاح الثغرات.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["Kali Linux", "Metasploit", "Python/Bash", "OWASP", "Networking", "Cryptography"],
                    "benefits": "عمل مثير وتحدي، رواتب جيدة، إمكانية العمل الحر (Freelance)."
                },
                {
                    "title": "مهندس أمن الشبكات (Network Security Engineer)",
                    "description": "يصمم ويطبق حلول أمن الشبكات مثل الجدران النارية والتشفير، ويضمن أمن البنية التحتية للاتصالات.",
                    "salary": "10,000 - 22,000 ريال سعودي",
                    "skills": ["Cisco/Juniper", "Firewalls", "VPN", "IDS/IPS", "Linux", "Scripting"],
                    "benefits": "استقرار وظيفي، طلب مستمر، فرص في الشركات الكبرى."
                }
            ]
        },
        {
            "title": "هندسة البرمجيات وعلوم الحاسب (Software Engineering / CS)",
            "branch": "علمي",
            "min_percentage": 70.0,
            "subject_weights": {"math": 0.40, "english": 0.60},
            "keywords": ["برمجة", "تطوير", "خوارزميات", "تصميم", "هندسة", "تطبيقات", "حاسوب"],
            "aptitude_profile": {
                "analytical": 0.85, "technology": 0.9, "research": 0.4, "problem_solving": 0.85,
                "practical": 0.75, "creativity": 0.55, "communication": 0.3, "leadership": 0.2,
                "health": 0.0, "engineering": 0.85
            },
            "career_paths": [
                {
                    "title": "مطور برمجيات (Software Developer)",
                    "description": "يصمم ويطور ويختبر تطبيقات وبرامج تلبي احتياجات المستخدمين والشركات.",
                    "salary": "10,000 - 20,000 ريال سعودي",
                    "skills": ["Java/C#/Python", "Git", "Agile", "قواعد البيانات", "تصميم واجهات", "حل المشكلات"],
                    "benefits": "طلب هائل، فرص في كل القطاعات، إمكانية العمل الحر والريادة."
                },
                {
                    "title": "مهندس برمجيات (Software Engineer)",
                    "description": "يطبق مبادئ الهندسة في تطوير البرمجيات، مع التركيز على التصميم المعماري والجودة والأداء.",
                    "salary": "15,000 - 28,000 ريال سعودي",
                    "skills": ["Design Patterns", "Microservices", "Cloud (AWS/Azure)", "CI/CD", "Testing", "System Design"],
                    "benefits": "رواتب مرتفعة، مكانة مرموقة، فرص في الشركات العالمية."
                },
                {
                    "title": "مطور تطبيقات الهواتف (Mobile App Developer)",
                    "description": "يطور تطبيقات للأجهزة المحمولة على أنظمة iOS و Android، مع التركيز على تجربة المستخدم.",
                    "salary": "12,000 - 22,000 ريال سعودي",
                    "skills": ["Flutter/Swift/Kotlin", "UI/UX", "APIs", "Firebase", "التطبيقات الأصلية"],
                    "benefits": "طلب متزايد، عمل إبداعي، فرص في الشركات الناشئة والكبيرة."
                }
            ]
        },
        {
            "title": "علوم البيانات (Data Science)",
            "branch": "علمي",
            "min_percentage": 70.0,
            "subject_weights": {"math": 0.60, "english": 0.40},
            "keywords": ["بيانات", "تحليل", "إحصاء", "رياضيات", "ذكاء اصطناعي"],
            "aptitude_profile": {
                "analytical": 0.9, "technology": 0.8, "research": 0.75, "problem_solving": 0.8,
                "practical": 0.5, "creativity": 0.4, "communication": 0.3, "leadership": 0.2,
                "health": 0.1, "engineering": 0.2
            },
            "career_paths": [
                {
                    "title": "محلل بيانات (Data Analyst)",
                    "description": "يقوم بجمع البيانات وتنظيفها وتحليلها واستخراج رؤى قيمة تساعد الشركات في اتخاذ القرارات.",
                    "salary": "8,000 - 15,000 ريال سعودي",
                    "skills": ["SQL", "Python", "Excel", "Tableau/Power BI", "الإحصاء", "التفكير التحليلي"],
                    "benefits": "فرص عمل واسعة في جميع القطاعات، إمكانية التطور إلى عالم بيانات، عمل مكتبي مستقر."
                },
                {
                    "title": "عالم بيانات (Data Scientist)",
                    "description": "يستخدم النماذج الرياضية والتعلم الآلي لتحليل البيانات الضخمة والتنبؤ بالاتجاهات المستقبلية.",
                    "salary": "15,000 - 30,000 ريال سعودي",
                    "skills": ["Python", "R", "Machine Learning", "Deep Learning", "الإحصاء المتقدم", "SQL", "Big Data"],
                    "benefits": "راتب مرتفع، طلب كبير في السوق، فرص للعمل في شركات عالمية، إمكانية البحث العلمي."
                },
                {
                    "title": "مهندس بيانات (Data Engineer)",
                    "description": "يبني البنية التحتية للبيانات، وينشئ قواعد البيانات وأنابيب نقل البيانات لضمان تدفقها بسلاسة.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["Python", "SQL", "Spark", "Hadoop", "Cloud (AWS/GCP/Azure)", "ETL", "قواعد البيانات"],
                    "benefits": "طلب مرتفع جداً، فرص في شركات التقنية الكبرى، عمل مشوق مع أنظمة ضخمة."
                }
            ]
        },
        {
            "title": "الهندسة (Engineering)",
            "branch": "علمي",
            "min_percentage": 75.0,
            "subject_weights": {"math": 0.40, "physics": 0.45, "english": 0.15},
            "keywords": ["هندسة", "تصميم", "بناء", "آلات", "كهرباء", "ميكانيكا", "مدني"],
            "aptitude_profile": {
                "analytical": 0.85, "technology": 0.7, "research": 0.4, "problem_solving": 0.85,
                "practical": 0.95, "creativity": 0.5, "communication": 0.3, "leadership": 0.3,
                "health": 0.0, "engineering": 1.0
            },
            "career_paths": [
                {
                    "title": "مهندس مدني (Civil Engineer)",
                    "description": "تصميم والإشراف على بناء الجسور والمباني والبنية التحتية.",
                    "salary": "10,000 - 20,000 ريال سعودي",
                    "skills": ["AutoCAD", "التحليل الإنشائي", "إدارة المشاريع", "مواد البناء", "المساحة"],
                    "benefits": "طلب مستمر، مشاريع ضخمة، فرص في القطاعين العام والخاص."
                },
                {
                    "title": "مهندس كهرباء (Electrical Engineer)",
                    "description": "تصميم وتطوير الأنظمة الكهربائية والإلكترونية وأنظمة الطاقة.",
                    "salary": "10,000 - 22,000 ريال سعودي",
                    "skills": ["الدوائر الكهربائية", "أنظمة الطاقة", "MATLAB", "PLC", "الإلكترونيات"],
                    "benefits": "طلب مرتفع، عمل تقني متقدم، فرص في الطاقة والصناعة."
                },
                {
                    "title": "مهندس ميكانيكا (Mechanical Engineer)",
                    "description": "تصميم وتطوير الآلات والأنظمة الميكانيكية وأنظمة التبريد والتكييف.",
                    "salary": "10,000 - 20,000 ريال سعودي",
                    "skills": ["SolidWorks", "الديناميكا الحرارية", "ميكانيكا الموائع", "التصنيع", "الصيانة"],
                    "benefits": "أساس لكل الصناعات، طلب دائم، تطبيقات متنوعة."
                }
            ]
        },

        # ==========================================
        # الفرع الأدبي (5 تخصصات)
        # ==========================================
        {
            "title": "إدارة الأعمال والمحاسبة (Business & Accounting)",
            "branch": "أدبي",
            "min_percentage": 65.0,
            "subject_weights": {"math": 0.40, "english": 0.30, "arabic": 0.30},
            "keywords": ["إدارة", "أعمال", "محاسبة", "تجارة", "مال", "قيادة", "تسويق", "استثمار"],
            "aptitude_profile": {
                "analytical": 0.7, "technology": 0.3, "research": 0.3, "problem_solving": 0.7,
                "practical": 0.7, "creativity": 0.5, "communication": 0.9, "leadership": 0.9,
                "health": 0.0, "engineering": 0.1
            },
            "career_paths": [
                {
                    "title": "محاسب (Accountant)",
                    "description": "تسجيل وتحليل المعاملات المالية وإعداد التقارير المحاسبية.",
                    "salary": "8,000 - 18,000 ريال سعودي",
                    "skills": ["المحاسبة", "Excel", "التقارير المالية", "الضرائب", "التدقيق"],
                    "benefits": "طلب مستمر في كل القطاعات، استقرار وظيفي، فرص في الشركات الكبرى."
                },
                {
                    "title": "مدير أعمال (Business Manager)",
                    "description": "إدارة الفرق والموارد لتحقيق أهداف المؤسسة.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["القيادة", "التخطيط", "إدارة الفرق", "التحليل المالي", "اتخاذ القرار"],
                    "benefits": "مسار وظيفي واضح، مكانة مرموقة، فرص في كل القطاعات."
                },
                {
                    "title": "أخصائي تسويق (Marketing Specialist)",
                    "description": "تطوير الحملات التسويقية وإدارة العلامات التجارية.",
                    "salary": "8,000 - 20,000 ريال سعودي",
                    "skills": ["التسويق الرقمي", "SEO", "وسائل التواصل", "تحليل السوق", "الإبداع"],
                    "benefits": "مجال ديناميكي، فرص في الشركات والوكالات، إبداع مستمر."
                }
            ]
        },
        {
            "title": "اللغات والترجمة (Languages & Translation)",
            "branch": "أدبي",
            "min_percentage": 70.0,
            "subject_weights": {"english": 0.60, "arabic": 0.40},
            "keywords": ["لغة", "ترجمة", "إنجليزي", "لغات", "ثقافة", "تواصل"],
            "aptitude_profile": {
                "analytical": 0.6, "technology": 0.2, "research": 0.6, "problem_solving": 0.5,
                "practical": 0.4, "creativity": 0.7, "communication": 0.95, "leadership": 0.3,
                "health": 0.0, "engineering": 0.0
            },
            "career_paths": [
                {
                    "title": "مترجم (Translator)",
                    "description": "ترجمة النصوص والوثائق بين اللغات مع الحفاظ على المعنى والأسلوب.",
                    "salary": "8,000 - 18,000 ريال سعودي",
                    "skills": ["الترجمة", "اللغات", "الدقة", "الأسلوب", "المصطلحات"],
                    "benefits": "عمل مرن، إمكانية العمل الحر، فرص في المنظمات الدولية."
                },
                {
                    "title": "مترجم فوري (Interpreter)",
                    "description": "الترجمة الفورية في المؤتمرات والاجتماعات رفيعة المستوى.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["الترجمة الفورية", "التركيز", "سرعة البديهة", "المصطلحات المتخصصة"],
                    "benefits": "رواتب مرتفعة، فرص سفر، مكانة مميزة."
                },
                {
                    "title": "مدرس لغة (Language Teacher)",
                    "description": "تدريس اللغات الأجنبية في المدارس والمعاهد والجامعات.",
                    "salary": "7,000 - 15,000 ريال سعودي",
                    "skills": ["التدريس", "التواصل", "الصبر", "طرق التعليم الحديثة", "التقييم"],
                    "benefits": "عمل مستقر، تأثير تربوي، فرص في المدارس الدولية."
                }
            ]
        },
        {
            "title": "الإعلام والاتصال (Media & Communication)",
            "branch": "أدبي",
            "min_percentage": 65.0,
            "subject_weights": {"arabic": 0.55, "english": 0.45},
            "keywords": ["إعلام", "صحافة", "اتصال", "كتابة", "تلفزيون", "إذاعة", "رقمي"],
            "aptitude_profile": {
                "analytical": 0.5, "technology": 0.5, "research": 0.6, "problem_solving": 0.5,
                "practical": 0.6, "creativity": 0.95, "communication": 0.95, "leadership": 0.6,
                "health": 0.0, "engineering": 0.0
            },
            "career_paths": [
                {
                    "title": "صحفي (Journalist)",
                    "description": "جمع الأخبار والتحقيق فيها وكتابة التقارير الصحفية.",
                    "salary": "8,000 - 18,000 ريال سعودي",
                    "skills": ["الكتابة", "البحث", "المقابلات", "التحقيق", "الأخلاقيات"],
                    "benefits": "عمل مثير، تأثير اجتماعي، لقاءات متعددة."
                },
                {
                    "title": "مذيع / مقدم برامج (Broadcaster)",
                    "description": "تقديم البرامج التلفزيونية أو الإذاعية والتواصل مع الجمهور.",
                    "salary": "10,000 - 25,000 ريال سعودي",
                    "skills": ["الإلقاء", "الحضور", "الارتجال", "التواصل", "الثقة"],
                    "benefits": "شهرة، دخل مرتفع للمتميزين، عمل متنوع."
                },
                {
                    "title": "أخصائي تسويق رقمي (Digital Marketer)",
                    "description": "إدارة المحتوى والحملات على منصات التواصل الاجتماعي.",
                    "salary": "8,000 - 20,000 ريال سعودي",
                    "skills": ["السوشال ميديا", "المحتوى", "التحليلات", "الإعلانات", "SEO"],
                    "benefits": "مجال حيوي ومتجدد، فرص عمل حرة، إبداع مستمر."
                }
            ]
        },
        {
            "title": "التربية والتعليم (Education)",
            "branch": "أدبي",
            "min_percentage": 60.0,
            "subject_weights": {"arabic": 0.50, "english": 0.30, "islamic": 0.20},
            "keywords": ["تربية", "تعليم", "تدريس", "معلم", "طلاب", "مدرسة"],
            "aptitude_profile": {
                "analytical": 0.5, "technology": 0.3, "research": 0.5, "problem_solving": 0.6,
                "practical": 0.7, "creativity": 0.7, "communication": 0.95, "leadership": 0.7,
                "health": 0.2, "engineering": 0.0
            },
            "career_paths": [
                {
                    "title": "معلم (Teacher)",
                    "description": "تدريس المواد الدراسية للطلاب في المدارس وإعداد المناهج.",
                    "salary": "7,000 - 14,000 ريال سعودي",
                    "skills": ["التدريس", "التواصل", "الصبر", "التقييم", "إدارة الفصل"],
                    "benefits": "عمل مستقر، تأثير تربوي مباشر، إجازات طويلة."
                },
                {
                    "title": "أخصائي تعليم إلكتروني (E-Learning Specialist)",
                    "description": "تصميم وتطوير المناهج الإلكترونية والمنصات التعليمية.",
                    "salary": "9,000 - 18,000 ريال سعودي",
                    "skills": ["التعليم الإلكتروني", "تصميم المناهج", "LMS", "المحتوى الرقمي"],
                    "benefits": "مجال حديث ومتنامي، فرص في التعليم والشركات."
                },
                {
                    "title": "مرشد طلابي (Student Counselor)",
                    "description": "مساعدة الطلاب على التخطيط لمستقبلهم الأكاديمي والمهني.",
                    "salary": "8,000 - 15,000 ريال سعودي",
                    "skills": ["الإرشاد", "التخطيط", "التواصل", "تحليل الشخصية", "الدعم النفسي"],
                    "benefits": "تأثير إيجابي، عمل إنساني، فرص في المدارس والجامعات."
                }
            ]
        },
        {
            "title": "الشريعة والقانون (Sharia & Law)",
            "branch": "أدبي",
            "min_percentage": 70.0,
            "subject_weights": {"arabic": 0.55, "islamic": 0.45},
            "keywords": ["شريعة", "قانون", "حقوق", "قضاء", "محاماة", "عدالة", "فتوى"],
            "aptitude_profile": {
                "analytical": 0.8, "technology": 0.2, "research": 0.9, "problem_solving": 0.7,
                "practical": 0.5, "creativity": 0.3, "communication": 0.85, "leadership": 0.6,
                "health": 0.0, "engineering": 0.0
            },
            "career_paths": [
                {
                    "title": "محامي (Lawyer)",
                    "description": "الدفاع عن الحقوق وتمثيل العملاء أمام المحاكم.",
                    "salary": "10,000 - 30,000 ريال سعودي",
                    "skills": ["المرافعة", "التحليل القانوني", "الكتابة القانونية", "البحث", "الإقناع"],
                    "benefits": "مكانة مرموقة، دخل مرتفع، تأثير اجتماعي."
                },
                {
                    "title": "قاضي (Judge)",
                    "description": "الفصل في القضايا وإصدار الأحكام بناءً على الشريعة والقانون.",
                    "salary": "15,000 - 30,000 ريال سعودي",
                    "skills": ["القضاء", "التحليل", "النزاهة", "الحكمة", "الفقه"],
                    "benefits": "مكانة عالية، استقرار وظيفي، احترام المجتمع."
                },
                {
                    "title": "مستشار قانوني (Legal Advisor)",
                    "description": "تقديم الاستشارات القانونية للشركات والمؤسسات.",
                    "salary": "12,000 - 25,000 ريال سعودي",
                    "skills": ["العقود", "الاستشارات", "الصياغة القانونية", "الامتثال", "التحليل"],
                    "benefits": "طلب مرتفع، فرص في القطاع الخاص، دخل جيد."
                }
            ]
        }
    ]

    SUBJECT_NAMES_AR = {
        'math': 'الرياضيات', 'physics': 'الفيزياء', 'chemistry': 'الكيمياء',
        'biology': 'الأحياء', 'english': 'الإنجليزية', 'arabic': 'العربية',
        'history': 'التاريخ', 'geography': 'الجغرافيا', 'islamic': 'التربية الإسلامية'
    }

    DIM_NAMES_AR = {
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

    # نصائح مخصصة لكل تخصص (للأدبي)
    MAJOR_SPECIFIC_TIPS = {
        "الطب والعلوم الصحية": "تطوير مهارات التواصل مع المرضى — مهم لمهنة طبية",
        "الذكاء الاصطناعي": "تعلم أساسيات Python — مطلوبة لمعظم وظائف AI",
        "الأمن السيبراني": "التدرب على أنظمة Linux — أساسية في الأمن السيبراني",
        "هندسة البرمجيات وعلوم الحاسب": "تعلم Git وإدارة الإصدارات — ضرورية للمطورين",
        "علوم البيانات": "التدرب على SQL — لغة تحليل البيانات الأولى",
        "الهندسة": "تعلم AutoCAD — أساسية للمهندسين",
        "إدارة الأعمال والمحاسبة": "تطوير مهارات Excel المتقدمة — مطلوبة في المحاسبة",
        "اللغات والترجمة": "قراءة الأدب الإنجليزي لتحسين المفردات — مهم للمترجمين",
        "الإعلام والاتصال": "التدرب على الكتابة الصحفية — أساسية للإعلامي",
        "التربية والتعليم": "تطوير مهارات إدارة الفصل — مهمة للمعلم",
        "الشريعة والقانون": "قراءة الفقه المقارن — يوسع أفق القانوني"
    }

    @staticmethod
    def analyze_student(user_id, hs_profile, assessment_scores=None, subject_test_scores=None):
        branch = hs_profile.branch or 'علمي'
        overall = hs_profile.overall_percentage if hs_profile.overall_percentage else 0.0

        grades = {}
        if hs_profile.subject_grades:
            try:
                grades = json.loads(hs_profile.subject_grades)
            except:
                grades = {}

        interests_list = []
        if hs_profile.interests:
            interests_list = re.split(r'[،,;\s]+', hs_profile.interests.strip())
            interests_list = [i.strip() for i in interests_list if i.strip()]

        recommendations = []

        for major in AnalysisEngine.MAJORS_DB:
            # تصفية حسب القسم
            if major["branch"] != branch:
                continue

            # تصفية حسب الحد الأدنى
            if overall < major["min_percentage"]:
                continue

            # ========== 1. الأكاديمي (30%) ==========
            subject_weights = major.get("subject_weights", {})
            weighted_sum = 0
            total_weight_used = 0
            subject_details = []

            for sub, weight in subject_weights.items():
                if sub in grades and grades[sub] is not None:
                    weighted_sum += grades[sub] * weight
                    total_weight_used += weight
                    subject_details.append((sub, grades[sub], weight))

            if total_weight_used > 0:
                weighted_avg = weighted_sum / total_weight_used
                academic_score = (weighted_avg / 100) * 30
            else:
                weighted_avg = 0
                academic_score = 0

            # ========== 2. الاهتمامات (30%) ==========
            match_keywords = major["keywords"]
            matched_interests = []
            if interests_list and match_keywords:
                for interest in interests_list:
                    for keyword in match_keywords:
                        if keyword in interest or interest in keyword:
                            matched_interests.append(interest)
                            break

            if interests_list:
                keyword_interest_score = (len(matched_interests) / len(interests_list)) * 30
            else:
                keyword_interest_score = 0

            # ========== 3. اختبار الميول ==========
            aptitude_score = 0
            top_aptitude_dims = []
            if assessment_scores and "aptitude_profile" in major:
                profile = major["aptitude_profile"]
                weighted_sum_apt = 0
                total_weight_apt = 0
                for dim, weight in profile.items():
                    if dim in assessment_scores:
                        weighted_sum_apt += assessment_scores[dim] * weight
                        total_weight_apt += weight
                        if weight >= 0.7 and assessment_scores[dim] >= 70:
                            top_aptitude_dims.append(dim)
                if total_weight_apt > 0:
                    aptitude_score = (weighted_sum_apt / total_weight_apt) * 0.30

            interest_score = aptitude_score if assessment_scores else keyword_interest_score

            # ========== 4. النسبة (40%) ==========
            gpa_score = (overall / 100) * 40

            # ========== 5. Bonus من أسئلة المواد ==========
            subject_bonus = 0
            subject_bonus_details = []

            if subject_test_scores:
                for sub_key, sub_score in subject_test_scores.items():
                    if sub_score is None:
                        continue
                    if sub_key in subject_weights:
                        weight = subject_weights[sub_key]
                        if weight >= 0.3:
                            if sub_score == 100:
                                subject_bonus += 5
                                subject_bonus_details.append((sub_key, 100))
                            elif sub_score >= 66:
                                subject_bonus += 3
                                subject_bonus_details.append((sub_key, sub_score))
                            elif sub_score >= 33:
                                subject_bonus += 1
                                subject_bonus_details.append((sub_key, sub_score))

            # ========== 6. Specific Bonus ==========
            specific_bonus = 0
            for sub, grade, weight in subject_details:
                if weight >= 0.4 and grade >= 90:
                    specific_bonus += 3
                elif weight >= 0.4 and grade >= 80:
                    specific_bonus += 1.5

            if assessment_scores and "aptitude_profile" in major:
                profile = major["aptitude_profile"]
                for dim, weight in profile.items():
                    if dim in assessment_scores and weight >= 0.8 and assessment_scores[dim] >= 75:
                        specific_bonus += 2

            total_score = min(100.0, academic_score + interest_score + gpa_score + specific_bonus + subject_bonus)

            # ==========================================
            # بناء الأسباب
            # ==========================================
            reasons_list = []

            if subject_details:
                top_subjects = sorted(subject_details, key=lambda x: x[2], reverse=True)
                top_subject_names = [
                    AnalysisEngine.SUBJECT_NAMES_AR.get(s[0], s[0])
                    for s in top_subjects[:2]
                    if s[1] >= 75
                ]
                if top_subject_names:
                    if weighted_avg >= 85:
                        reasons_list.append(f"تميزك اللافت في {', '.join(top_subject_names)} بمتوسط مرجح {round(weighted_avg, 1)}%")
                    elif weighted_avg >= 75:
                        reasons_list.append(f"مستواك الجيد في {', '.join(top_subject_names)} بمتوسط مرجح {round(weighted_avg, 1)}%")
                    else:
                        reasons_list.append(f"أساسك الأكاديمي في {', '.join(top_subject_names)} يدعم هذا التخصص")

            if matched_interests:
                interests_str = '، '.join(matched_interests[:2])
                reasons_list.append(f"اهتماماتك في {interests_str} تتوافق مع متطلبات هذا المجال")

            if assessment_scores and aptitude_score >= 18 and top_aptitude_dims:
                top_dims_ar = [AnalysisEngine.DIM_NAMES_AR.get(d, d) for d in top_aptitude_dims[:2]]
                reasons_list.append(f"اختبار الميول أظهر قدراتك العالية في {', '.join(top_dims_ar)}")
            elif assessment_scores and aptitude_score >= 18:
                reasons_list.append("نتائج اختبار الميول تدعم توجهك لهذا المجال")

            if subject_bonus_details:
                top_bonus_subjects = sorted(subject_bonus_details, key=lambda x: x[1], reverse=True)[:2]
                bonus_names = [AnalysisEngine.SUBJECT_NAMES_AR.get(s[0], s[0]) for s in top_bonus_subjects]
                reasons_list.append(f"أداؤك المتميز في اختبار {', '.join(bonus_names)} يعزز هذا التخصص")

            if overall >= 90:
                reasons_list.append(f"نسبتك العامة المتميزة ({overall}%) تفتح لك آفاقاً واسعة في هذا المجال")
            elif overall >= 80:
                reasons_list.append(f"نسبتك العامة الجيدة ({overall}%) تؤهلك للنجاح في هذا التخصص")

            if not reasons_list:
                reasons_list.append(f"ملفك الأكاديمي يتوافق مع متطلبات هذا التخصص بنسبة {round(total_score, 1)}%")

            # ==========================================
            # نقاط تحتاج تطويرها (مخصصة لكل تخصص)
            # ==========================================
            weaknesses_set = set()

            # 1) من المواد الأساسية — أعلى مادة وزناً فقط
            subject_candidates = []
            for sub, weight in subject_weights.items():
                if weight >= 0.3 and sub in grades and grades[sub] is not None:
                    subject_candidates.append((weight, sub, grades[sub]))
            subject_candidates.sort(key=lambda x: x[0], reverse=True)

            for weight, sub, grade in subject_candidates[:1]:
                sub_name = AnalysisEngine.SUBJECT_NAMES_AR.get(sub, sub)
                if grade < 60:
                    weaknesses_set.add(f"تحسين مستواك في {sub_name} ({grade}%) — مادة أساسية لهذا التخصص")
                elif grade < 80:
                    weaknesses_set.add(f"تطوير مهاراتك في {sub_name} ({grade}%) لتعزيز فرصك في هذا المجال")
                elif grade < 92:
                    weaknesses_set.add(f"رفع مستواك في {sub_name} ({grade}%) إلى مستوى التميز (92%+)")

            # 2) من اختبار الميول — بعد واحد فقط (الأعلى وزناً والأقل قيمة)
            if assessment_scores and "aptitude_profile" in major:
                profile = major["aptitude_profile"]
                has_real_answers = any(v > 0 for v in assessment_scores.values())

                if has_real_answers:
                    dim_candidates = []
                    for dim, weight in profile.items():
                        if dim in assessment_scores:
                            dim_score = assessment_scores[dim]
                            if weight >= 0.6 and 0 < dim_score < 70:
                                dim_candidates.append((weight, dim, dim_score))
                    dim_candidates.sort(key=lambda x: x[0], reverse=True)

                    for weight, dim, dim_score in dim_candidates[:1]:
                        dim_name = AnalysisEngine.DIM_NAMES_AR.get(dim, dim)
                        weaknesses_set.add(f"تطوير مهاراتك في {dim_name} ({dim_score}%) — ركيزة أساسية في هذا المجال")

            # 3) نصيحة مخصصة إذا لم توجد أي نقطة
            if not weaknesses_set:
                for key, tip in AnalysisEngine.MAJOR_SPECIFIC_TIPS.items():
                    if key in major["title"]:
                        weaknesses_set.add(tip)
                        break

            weaknesses_list = list(weaknesses_set)[:2]

            recommendations.append({
                "major_title": major["title"],
                "match_percentage": round(total_score, 2),
                "reasons_list": reasons_list,
                "weaknesses_list": weaknesses_list,
                "career_paths": major["career_paths"]
            })

        recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
        return recommendations