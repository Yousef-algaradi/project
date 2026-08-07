# services/analysis_engine.py
import json
import re

class AnalysisEngine:
    MAJORS_DB = [
        {
            "title": "علوم البيانات (Data Science)",
            "branch": "علمي",
            "min_percentage": 70.0,
            "key_subjects": ["math", "english"],
            "keywords": ["بيانات", "تحليل", "إحصاء", "برمجة", "رياضيات", "ذكاء اصطناعي"],
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
            "title": "الذكاء الاصطناعي (AI)",
            "branch": "علمي",
            "min_percentage": 75.0,
            "key_subjects": ["math", "english"],
            "keywords": ["ذكاء اصطناعي", "تعلم آلة", "روبوتات", "خوارزميات", "برمجة", "رياضيات"],
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
            "key_subjects": ["math", "english"],
            "keywords": ["أمن", "شبكات", "برمجة", "حماية", "اختراق", "سيبراني"],
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
            "title": "تقنية المعلومات (IT)",
            "branch": "علمي",
            "min_percentage": 65.0,
            "key_subjects": ["math", "english"],
            "keywords": ["شبكات", "أنظمة", "قواعد بيانات", "برمجة", "حاسوب", "دعم فني"],
            "career_paths": [
                {
                    "title": "أخصائي دعم فني (IT Support Specialist)",
                    "description": "يقدم الدعم الفني للمستخدمين، يحل مشكلات الأجهزة والبرامج، ويضمن سير العمل بشكل سلس.",
                    "salary": "6,000 - 12,000 ريال سعودي",
                    "skills": ["Windows/Linux", "Active Directory", "الشبكات الأساسية", "حل المشكلات", "التواصل"],
                    "benefits": "طلب مستمر في كل المؤسسات، فرص للترقية إلى إدارة الأنظمة، عمل مكتبي مستقر."
                },
                {
                    "title": "مسؤول أنظمة (System Administrator)",
                    "description": "يدير ويراقب أنظمة الخوادم والتطبيقات، ويضمن أداءها واستمراريتها وأمنها.",
                    "salary": "10,000 - 18,000 ريال سعودي",
                    "skills": ["Linux/Windows Server", "Virtualization", "Scripting (Bash/PowerShell)", "التشغيل الآلي", "أمن الأنظمة"],
                    "benefits": "رواتب جيدة، فرص في شركات التقنية والبنوك، عمل مهم وحساس."
                },
                {
                    "title": "مهندس شبكات (Network Engineer)",
                    "description": "يصمم وينشر ويدير البنية التحتية للشبكات، ويضمن أدائها وأمنها واستمراريتها.",
                    "salary": "12,000 - 22,000 ريال سعودي",
                    "skills": ["Cisco/Juniper", "Routing & Switching", "Firewalls", "Network Security", "SD-WAN"],
                    "benefits": "طلب مرتفع، فرص في شركات الاتصالات والشركات الكبرى، عمل تقني متقدم."
                }
            ]
        },
        {
            "title": "هندسة البرمجيات (Software Engineering)",
            "branch": "علمي",
            "min_percentage": 70.0,
            "key_subjects": ["math", "english"],
            "keywords": ["برمجة", "تطوير", "خوارزميات", "تصميم", "هندسة", "تطبيقات"],
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
            "title": "الطب والعلوم الصحية (Medicine & Health Sciences)",
            "branch": "علمي",
            "min_percentage": 80.0,
            "key_subjects": ["biology", "chemistry", "english"],
            "keywords": ["طب", "صحة", "أحياء", "كيمياء", "علاج", "تشخيص", "إنسان", "مختبر"],
            "career_paths": [
                {
                    "title": "الطب البشري (Human Medicine)",
                    "description": "تشخيص الأمراض وعلاجها والوقاية منها، مع إمكانية التخصص لاحقاً في مجالات طبية دقيقة.",
                    "salary": "20,000 - 45,000 ريال سعودي",
                    "skills": ["الأحياء", "الكيمياء", "التفكير السريري", "التواصل", "حل المشكلات", "القدرة على تحمل الضغط"],
                    "benefits": "مجال واسع وتأثير مباشر في حياة الناس، مع عدد كبير من التخصصات الطبية."
                },
                {
                    "title": "طب الأسنان (Dentistry)",
                    "description": "تشخيص وعلاج أمراض الفم والأسنان واللثة، ويجمع بين المعرفة الطبية والمهارات اليدوية الدقيقة.",
                    "salary": "15,000 - 30,000 ريال سعودي",
                    "skills": ["الأحياء", "الكيمياء", "الدقة اليدوية", "التشخيص", "التواصل", "العمل تحت الضغط"],
                    "benefits": "مسار صحي واضح يجمع بين الجانب الطبي والعمل العملي، مع إمكانية التخصص الدقيق."
                },
                {
                    "title": "الصيدلة (Pharmacy)",
                    "description": "دراسة الأدوية وتركيبها وتأثيراتها واستخدامها الآمن، مع إمكانية التخصص في الصيدلة السريرية أو الصناعات الدوائية.",
                    "salary": "12,000 - 22,000 ريال سعودي",
                    "skills": ["الكيمياء", "الأحياء", "علم الأدوية", "الدقة", "التحليل", "التواصل"],
                    "benefits": "يجمع بين العلوم الصحية والكيمياء، مع فرص في المستشفيات والصناعة الدوائية والبحث."
                },
                {
                    "title": "التمريض (Nursing)",
                    "description": "تقديم الرعاية الصحية المباشرة للمرضى ومتابعة حالاتهم والمساهمة في خطط العلاج والرعاية.",
                    "salary": "8,000 - 15,000 ريال سعودي",
                    "skills": ["الأحياء", "التواصل", "الرعاية", "العمل الجماعي", "تحمل الضغط", "التعاطف"],
                    "benefits": "طلب مستمر في القطاع الصحي وفرص واسعة في المستشفيات والمراكز الصحية."
                },
                {
                    "title": "العلوم الطبية والمختبرات (Medical Laboratory Sciences)",
                    "description": "تحليل العينات الطبية وإجراء الفحوصات المخبرية التي تساعد في تشخيص الأمراض ومتابعة الحالات.",
                    "salary": "8,000 - 16,000 ريال سعودي",
                    "skills": ["الأحياء", "الكيمياء", "التحليل", "الدقة", "العمل المخبري", "التفسير العلمي"],
                    "benefits": "مناسب لمن يحب العلوم والتجارب والعمل المخبري أكثر من التعامل السريري المباشر."
                }
            ]
        },
        {
            "title": "الأعمال والإدارة والاقتصاد (Business, Management & Economics)",
            "branch": "أدبي",
            "min_percentage": 60.0,
            "key_subjects": ["math", "english"],
            "keywords": ["إدارة", "أعمال", "اقتصاد", "تجارة", "مال", "قيادة", "تسويق", "استثمار", "مشاريع"],
            "career_paths": [
                {
                    "title": "إدارة الأعمال (Business Administration)",
                    "description": "دراسة إدارة المؤسسات والموارد والعمليات واتخاذ القرارات، مع إمكانية التخصص في الإدارة أو التسويق أو الموارد البشرية.",
                    "salary": "10,000 - 25,000 ريال سعودي",
                    "skills": ["Management", "Communication", "Leadership", "Business Analysis", "Planning", "Decision Making"],
                    "benefits": "تخصص مرن يمكن تطبيقه في معظم القطاعات، مع إمكانية التخصص في مجالات إدارية متعددة."
                },
                {
                    "title": "الاقتصاد (Economics)",
                    "description": "تحليل الأسواق والموارد والسياسات الاقتصادية والعوامل المؤثرة في النمو والتضخم والبطالة.",
                    "salary": "12,000 - 20,000 ريال سعودي",
                    "skills": ["تحليل بيانات", "إحصاء", "نظريات اقتصادية", "سياسات مالية", "تفكير استراتيجي"],
                    "benefits": "فرص في البنوك والمؤسسات المالية والحكومات ومراكز الأبحاث."
                },
                {
                    "title": "المحاسبة (Accounting)",
                    "description": "تسجيل وتحليل وتدقيق المعاملات المالية للشركات والمؤسسات، وإعداد التقارير المالية.",
                    "salary": "8,000 - 18,000 ريال سعودي",
                    "skills": ["محاسبة", "تحليل مالي", "تقارير مالية", "برامج محاسبية", "دقة", "تنظيم"],
                    "benefits": "طلب مستمر في كل القطاعات، استقرار وظيفي، فرص في الشركات الكبرى والبنوك."
                },
                {
                    "title": "التسويق (Marketing)",
                    "description": "دراسة سلوك المستهلك وتطوير استراتيجيات تسويقية للترويج للمنتجات والخدمات وبناء العلامات التجارية.",
                    "salary": "8,000 - 20,000 ريال سعودي",
                    "skills": ["تسويق رقمي", "تحليل سوق", "إبداع", "تواصل", "وسائل التواصل الاجتماعي", "تحليل بيانات"],
                    "benefits": "مجال ديناميكي ومتغير، فرص في الشركات الكبرى والوكالات الإعلانية والشركات الناشئة."
                },
                {
                    "title": "ريادة الأعمال (Entrepreneurship)",
                    "description": "دراسة كيفية إنشاء وإدارة المشاريع الناشئة، وتطوير الأفكار الإبداعية إلى مشاريع قابلة للاستمرار.",
                    "salary": "متغير حسب نجاح المشروع",
                    "skills": ["إدارة مشاريع", "تخطيط استراتيجي", "تسويق", "تمويل", "قيادة", "إبداع", "تحمل المخاطر"],
                    "benefits": "إمكانية بناء ثروة، استقلالية، تحقيق الذات، فرص في مجالات متعددة."
                }
            ]
        }
    ]

    @staticmethod
    def analyze_student(user_id, hs_profile):
        branch = hs_profile.branch
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
            # تصفية حسب الفرع
            major_branches = [b.strip() for b in major["branch"].split('/')]
            if branch not in major_branches:
                continue
            
            if overall < major["min_percentage"]:
                continue

            key_subjects = major["key_subjects"]
            subject_scores = []
            for sub in key_subjects:
                if sub in grades:
                    subject_scores.append(grades[sub])
            
            if subject_scores:
                avg_subject = sum(subject_scores) / len(subject_scores)
                subject_score = (avg_subject / 100) * 30
            else:
                subject_score = 0

            match_keywords = major["keywords"]
            if interests_list and match_keywords:
                matches = 0
                for interest in interests_list:
                    for keyword in match_keywords:
                        if keyword in interest or interest in keyword:
                            matches += 1
                            break
                max_possible = len(interests_list)
                if max_possible > 0:
                    interest_score = (matches / max_possible) * 30
                else:
                    interest_score = 0
            else:
                interest_score = 0

            gpa_score = (overall / 100) * 40

            total_score = subject_score + interest_score + gpa_score
            total_score = min(100.0, total_score)

            reason_parts = []
            if subject_score > 20:
                reason_parts.append(f"تميزك في مواد {', '.join(key_subjects)}")
            if interest_score > 15:
                reason_parts.append(f"توافق اهتماماتك مع المجال")
            if gpa_score > 30:
                reason_parts.append(f"نسبتك العامة مرتفعة")
            
            reason = "، ".join(reason_parts) if reason_parts else "ملفك متناسب مع هذا التخصص"
            reason = f"تم اقتراح هذا المجال لـ {reason}."

            recommendations.append({
                "major_title": major["title"],
                "match_percentage": round(total_score, 2),
                "reason": reason,
                "career_paths": major["career_paths"]
            })

        recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
        return recommendations