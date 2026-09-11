# data/career_content_security.py
# بنك محتوى مسار "محلل الأمن السيبراني (Security Analyst)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

SECURITY_ANALYST_PATHS = [
    {
        "major_key": "cyber",
        "slug": "security-analyst",
        "title": "محلل أمن سيبراني (Security Analyst / SOC L1)",
        "description": "مسار متكامل: Networking + Windows/Linux + SIEM + MITRE ATT&CK + Incident Response + Threat Hunting + Cloud Security.",
        "icon": "🛡️",
        "difficulty": "متقدم",
        "estimated_hours": 240,
        "order_index": 1,
        "stages": [
            # ==========================================
            # المرحلة 1
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات الأمن السيبراني وتقنية المعلومات",
                "description": "بناء الأساس التقني الذي يحتاجه محلل الأمن لفهم الأنظمة والشبكات والأحداث الأمنية.",
                "objectives": [
                    "CIA Triad",
                    "Authentication vs Authorization",
                    "Networking fundamentals",
                    "TCP/IP و OSI Model",
                    "IPv4 / IPv6 / TCP / UDP",
                    "DNS / DHCP / HTTP / HTTPS / SSH / SMTP",
                    "Common ports",
                    "Windows & Linux fundamentals",
                    "File systems / Processes / Users",
                    "CLI / Bash / PowerShell basics",
                    "Virtualization",
                    "Basic Git & Python"
                ],
                "practical_task": "أنشئ مختبراً بـ VirtualBox/VMware يحتوي Windows + Kali Linux، أنشئ مستخدمين وصلاحيات، نفّذ أوامر Linux، استخدم PowerShell، افحص المنافذ، نفّذ DNS lookup، والتقط حركة شبكة بـWireshark.",
                "youtube_ar": "https://www.youtube.com/watch?v=8f2Zsb89uoM",
                "youtube_en": "https://tryhackme.com/path/outline/cybersecurity101",
                "questions": [
                    {"text": "أي عنصر من CIA Triad يتعلق بمنع التعديل غير المصرح به؟", "options": {"A": "Availability", "B": "Integrity", "C": "Confidentiality", "D": "Authentication"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي بروتوكول يستخدم غالباً لترجمة أسماء النطاقات إلى IP؟", "options": {"A": "DNS", "B": "DHCP", "C": "SSH", "D": "SMTP"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي بروتوكول يعمل عادةً على المنفذ 443؟", "options": {"A": "FTP", "B": "SSH", "C": "HTTPS", "D": "DNS"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما الوظيفة الأساسية لـ DHCP؟", "options": {"A": "تشفير الاتصالات", "B": "اكتشاف البرمجيات الخبيثة", "C": "تحليل الحزم", "D": "توزيع إعدادات IP تلقائياً"}, "correct": "D", "difficulty": "easy"},
                    {"text": "أي نظام يستخدم غالباً Bash كواجهة أوامر؟", "options": {"A": "Linux", "B": "Windows فقط", "C": "Cisco IOS فقط", "D": "Android فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لديك جهاز لا يستطيع الوصول إلى اسم نطاق ولكن يستطيع الوصول إلى IP مباشرة. ما الاحتمال الأقرب؟", "options": {"A": "مشكلة DNS", "B": "مشكلة RAM", "C": "مشكلة SSH", "D": "مشكلة SMTP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين TCP وUDP؟", "options": {"A": "UDP دائماً مشفر", "B": "TCP يعتمد على اتصال وموثوقية أعلى", "C": "TCP لا يستخدم المنافذ", "D": "UDP يعمل فقط داخل LAN"}, "correct": "B", "difficulty": "medium"},
                    {"text": "تريد معرفة العمليات التي تعمل على Linux. أي أمر مناسب؟", "options": {"A": "mkdir", "B": "ps", "C": "chmod", "D": "touch"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الغرض من Wireshark؟", "options": {"A": "إدارة المستخدمين", "B": "إنشاء VM", "C": "تحليل حركة الشبكة والحزم", "D": "تشفير القرص"}, "correct": "C", "difficulty": "medium"},
                    {"text": "مستخدم يستطيع قراءة ملف لكنه لا يستطيع تعديله. أي مفهوم يرتبط بذلك مباشرة؟", "options": {"A": "Permissions", "B": "DNS", "C": "Routing", "D": "DHCP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل سبب لتعلم PowerShell لمحلل أمن؟", "options": {"A": "لأنه بديل لـ Wireshark", "B": "لأنه يستخدم فقط في Linux", "C": "لأنه يختص بالتشفير", "D": "لأنه يسمح بفحص وإدارة Windows وأتمتة المهام"}, "correct": "D", "difficulty": "medium"},
                    {"text": "جهاز يرسل DNS requests كثيرة إلى نطاقات عشوائية، ثم يبدأ اتصالاً خارجياً غير معتاد. ما أفضل إجراء أولي؟", "options": {"A": "حذف DNS", "B": "إيقاف جميع أجهزة الشبكة", "C": "جمع وتحليل السجلات وحركة الجهاز", "D": "تغيير كلمة مرور المستخدم فقط"}, "correct": "C", "difficulty": "hard"},
                    {"text": "أثناء تحليل اتصال TCP، ما الذي يساعد أكثر على تحديد الطرفين؟", "options": {"A": "MAC vendor فقط", "B": "Source/Destination IP والـports", "C": "اسم المستخدم فقط", "D": "حجم القرص"}, "correct": "B", "difficulty": "hard"},
                    {"text": "جهاز Windows لديه PowerShell process غير معتاد بدأ من Office application. لماذا يستحق التحقيق؟", "options": {"A": "PowerShell لا يعمل على Windows", "B": "Office لا يستطيع تشغيل عمليات", "C": "PowerShell دائماً ضار", "D": "قد يكون مؤشراً على تنفيذ أوامر من ملف Office خبيث"}, "correct": "D", "difficulty": "hard"},
                    {"text": "ما أفضل تسلسل لتحليل حادثة شبكية أولية؟", "options": {"A": "Identify → Collect Evidence → Analyze → Contain/Escalate", "B": "Delete → Reinstall → Analyze", "C": "Block everything → Ignore logs", "D": "Change DNS → Restart"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ الشبكات وأمن الشبكات",
                "description": "قراءة حركة الشبكة وفهم الاتصالات والبروتوكولات واكتشاف المؤشرات الشبكية للهجمات.",
                "objectives": [
                    "TCP/IP و OSI",
                    "IPv4 / IPv6 / Subnetting",
                    "ARP / ICMP / DNS / DHCP",
                    "HTTP/HTTPS / SSH / FTP / SMTP",
                    "TCP handshake / Ports / NAT",
                    "VLAN / Routing basics",
                    "Firewalls / IDS/IPS",
                    "VPN / Proxy / Segmentation",
                    "Wireshark / Nmap basics"
                ],
                "practical_task": "باستخدام Wireshark: التقط DNS، حدد query/response، التقط TCP handshake، حدد Source/Destination، افحص HTTP request، استخدم Nmap على مختبر تملكه، واكتب تقريراً بـ5 مؤشرات يمكن لمحلل SOC مراقبتها.",
                "youtube_ar": "https://www.youtube.com/watch?v=_TnDypWebbc",
                "youtube_en": "https://tryhackme.com/path/outline/cybersecurity101",
                "questions": [
                    {"text": "ما وظيفة ARP؟", "options": {"A": "ربط IP بعنوان MAC", "B": "تشفير DNS", "C": "إرسال البريد", "D": "إنشاء VPN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي بروتوكول يستخدم Echo Request/Reply؟", "options": {"A": "FTP", "B": "ICMP", "C": "SMTP", "D": "SSH"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المنفذ الافتراضي لـ SSH؟", "options": {"A": "21", "B": "25", "C": "22", "D": "53"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما وظيفة Firewall الأساسية؟", "options": {"A": "تحليل الصور", "B": "إنشاء كلمات مرور", "C": "تشغيل SIEM", "D": "التحكم في الاتصالات وفق قواعد"}, "correct": "D", "difficulty": "easy"},
                    {"text": "ماذا يعرض Wireshark؟", "options": {"A": "حزم الشبكة", "B": "ملفات Word", "C": "BIOS", "D": "RAM فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي مؤشر قد يدل على DNS tunneling؟", "options": {"A": "استعلامات DNS طبيعية قليلة", "B": "عدد كبير من أسماء نطاقات طويلة وغير معتادة", "C": "استخدام HTTPS", "D": "DHCP renewal"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة Network Segmentation؟", "options": {"A": "زيادة حجم القرص", "B": "منع جميع الاتصالات", "C": "تقليل نطاق انتشار الحوادث", "D": "تعطيل DNS"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما الذي يحدث في TCP three-way handshake؟", "options": {"A": "SYN → SYN/ACK → ACK", "B": "ACK → FIN → SYN", "C": "DNS → DHCP → ARP", "D": "GET → POST → PUT"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل استخدام أساسي لـ Nmap لمحلل SOC؟", "options": {"A": "كتابة malware", "B": "اكتشاف المنافذ والخدمات في مختبر مصرح به", "C": "تشفير الملفات", "D": "تحليل البريد"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا ظهر اتصال صادر من جهاز داخلي إلى IP خارجي عبر منفذ غير معتاد، ما أفضل خطوة؟", "options": {"A": "تجاهله", "B": "حذف الجهاز", "C": "تغيير MAC", "D": "فحص السياق والسجلات وحركة الاتصال"}, "correct": "D", "difficulty": "medium"},
                    {"text": "ما وظيفة IDS؟", "options": {"A": "اكتشاف أنماط أو أحداث مشبوهة", "B": "توزيع IP", "C": "تخزين النسخ الاحتياطية", "D": "إدارة المستخدمين"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك جهاز يقوم بإنشاء اتصالات قصيرة متكررة إلى نفس IP خارجي كل 60 ثانية. ما الاحتمال الذي يستحق التحقيق؟", "options": {"A": "NTP فقط", "B": "DHCP", "C": "Beaconing/C2", "D": "ARP"}, "correct": "C", "difficulty": "hard"},
                    {"text": "في Wireshark ترى عدداً كبيراً من SYN بدون اكتمال handshake. ما السيناريو المحتمل؟", "options": {"A": "SYN scan أو SYN flood", "B": "DNS failure فقط", "C": "DHCP lease", "D": "SMTP relay"}, "correct": "A", "difficulty": "hard"},
                    {"text": "جهاز داخلي يتصل بعنوان IP خارجي عبر 443، لكن SNI/DNS والسلوك لا يتطابق مع الخدمة المعتادة. ما الأفضل؟", "options": {"A": "اعتباره آمناً بسبب 443", "B": "التحقيق في TLS metadata وDNS وendpoint logs", "C": "حذف Wireshark", "D": "إيقاف DNS"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا لا يكفي رقم المنفذ وحده لتحديد نوع النشاط؟", "options": {"A": "لأن جميع المنافذ عشوائية", "B": "لأن المنافذ لا تظهر في TCP", "C": "لأن التطبيقات يمكنها استخدام منافذ غير قياسية", "D": "لأن IP غير مهم"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ Windows وLinux وأمن الأجهزة الطرفية",
                "description": "تحليل الأجهزة الطرفية واكتشاف العمليات والمستخدمين والخدمات والأنشطة المشبوهة.",
                "objectives": [
                    "Windows architecture & Event Logs",
                    "Security logs / Sysmon",
                    "Processes / Services / Registry",
                    "PowerShell / Scheduled Tasks",
                    "Windows Defender",
                    "Linux processes / logs / systemd",
                    "Authentication logs / File permissions",
                    "SSH logs",
                    "Endpoint Detection",
                    "Malware indicators",
                    "Persistence basics",
                    "IOC"
                ],
                "practical_task": "أنشئ مختبر Windows: فعّل Event Logging، ثبّت Sysmon، أنشئ حساب تجريبي، نفّذ PowerShell، راقب process creation وfailed logins وnetwork connections، ثم نفذ نفس التحليل على Linux عبر auth.log/journalctl، واكتب 10 IOCs.",
                "youtube_ar": "https://www.youtube.com/watch?v=8f2Zsb89uoM",
                "youtube_en": "https://tryhackme.com/path/outline/blueteam",
                "questions": [
                    {"text": "أين توجد أحداث تسجيل الدخول في Windows عادةً؟", "options": {"A": "Security Log", "B": "DNS Log", "C": "Browser Cache فقط", "D": "BIOS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Sysmon؟", "options": {"A": "تشفير القرص", "B": "توفير telemetry تفصيلية عن نشاط Windows", "C": "إنشاء مستخدمين فقط", "D": "إدارة DNS"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي أمر Linux يعرض العمليات؟", "options": {"A": "pwd", "B": "ps", "C": "cd", "D": "touch"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المقصود بـ IOC؟", "options": {"A": "مؤشر يدل على نشاط اختراق أو compromise", "B": "بروتوكول شبكي", "C": "نظام تشغيل", "D": "نوع Firewall"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Windows Defender؟", "options": {"A": "معالجة النصوص", "B": "حماية الجهاز من التهديدات", "C": "إدارة DHCP", "D": "إنشاء VLAN"}, "correct": "B", "difficulty": "easy"},
                    {"text": "كثرة failed logins على حساب واحد قد تشير إلى؟", "options": {"A": "Brute-force/password spraying", "B": "DHCP", "C": "DNS caching", "D": "Disk fragmentation"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يعتبر PowerShell مهماً في التحقيقات؟", "options": {"A": "لأنه لا يسجل أي نشاط", "B": "لأنه يمكن استخدامه للإدارة وكذلك لتنفيذ أوامر خبيثة", "C": "لأنه يعمل على routers فقط", "D": "لأنه يمنع malware"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة process tree؟", "options": {"A": "معرفة مساحة القرص", "B": "رؤية علاقة العمليات بالأب والابن", "C": "معرفة MAC", "D": "تغيير DNS"}, "correct": "B", "difficulty": "medium"},
                    {"text": "عملية غير معروفة تعمل من %TEMP% وتنفذ PowerShell. ما الأفضل؟", "options": {"A": "تجاهلها", "B": "التحقيق في parent process وcommand line والملف", "C": "حذف Windows", "D": "تغيير IP"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما فائدة Linux journalctl؟", "options": {"A": "قراءة سجلات systemd", "B": "فحص MAC", "C": "إنشاء VLAN", "D": "تعديل BIOS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود بـ Persistence؟", "options": {"A": "آلية تسمح للتهديد بالبقاء بعد إعادة التشغيل أو تسجيل الدخول", "B": "ضغط الملفات", "C": "تغيير IP", "D": "DNS resolution"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Word → PowerShell → encoded command ظهر في telemetry. ما مستوى الاشتباه؟", "options": {"A": "منخفض دائماً", "B": "لا يمكن تحليله", "C": "مرتفع ويحتاج تحقيقاً", "D": "طبيعي دائماً"}, "correct": "C", "difficulty": "hard"},
                    {"text": "ظهر sshd ثم shell غير معتاد لمستخدم لا يعمل عادةً عبر SSH. ماذا تفعل؟", "options": {"A": "تجاهله", "B": "تحقق من مصدر الاتصال والوقت والأوامر وسجل المصادقة", "C": "أعد تشغيل الجهاز فقط", "D": "احذف سجل SSH"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا تعتبر parent-child relationships مهمة؟", "options": {"A": "تساعد على كشف سلاسل تنفيذ غير معتادة", "B": "تغير IP", "C": "تشفر الملفات", "D": "تمنع DNS"}, "correct": "A", "difficulty": "hard"},
                    {"text": "اكتشفت Scheduled Task جديدة تشغل ملفاً من مجلد مستخدم عند تسجيل الدخول. ما الاحتمال؟", "options": {"A": "Persistence", "B": "DHCP", "C": "VLAN", "D": "ARP"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ السجلات وSIEM ومراقبة الأمن",
                "description": "تحويل السجلات الخام إلى معلومات أمنية، واستخدام SIEM لمراقبة الأحداث واكتشاف الأنشطة المشبوهة.",
                "objectives": [
                    "Logs & Events",
                    "SIEM / Log sources",
                    "Parsing / Normalization / Correlation",
                    "Alerts / Dashboards / Search",
                    "Splunk / Elastic Security / Wazuh",
                    "Sigma basics",
                    "Alert triage",
                    "False positives",
                    "Detection rules"
                ],
                "practical_task": "أنشئ SIEM Lab باستخدام Wazuh أو Elastic Security: Windows → Sysmon → Agent → SIEM، ثم اجمع Windows logs، نفذ failed login، نفذ PowerShell command، أنشئ alert، ابحث عن الحدث، اربط الأحداث بالـIP/user/host، أنشئ Dashboard، ووثق التحقيق.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://tryhackme.com/path/outline/blueteam",
                "questions": [
                    {"text": "ما وظيفة SIEM؟", "options": {"A": "تجميع وتحليل وربط الأحداث الأمنية", "B": "استبدال Firewall", "C": "إنشاء VM", "D": "إدارة الطابعات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ Alert؟", "options": {"A": "حدث تم تحديده كشيء يستحق الانتباه", "B": "ملف مضغوط", "C": "مستخدم", "D": "عنوان MAC"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Dashboard في SIEM؟", "options": {"A": "عرض مؤشرات وأحداث بشكل مرئي", "B": "تشفير الملفات", "C": "تثبيت Windows", "D": "إنشاء VLAN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـ False Positive؟", "options": {"A": "تهديد حقيقي لم يتم اكتشافه", "B": "تنبيه يبدو ضاراً لكنه ليس تهديداً حقيقياً", "C": "malware مؤكد", "D": "مستخدم جديد"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن يحتويه Log جيد للتحقيق؟", "options": {"A": "Timestamp وسياق الحدث", "B": "لون الجهاز", "C": "حجم الشاشة", "D": "اسم الشركة المصنعة فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لديك 1000 failed login من IP واحد خلال 5 دقائق. ما أفضل استخدام للـSIEM؟", "options": {"A": "Correlation/threshold detection", "B": "حذف السجلات", "C": "تعطيل DNS", "D": "تغيير MAC"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا تحتاج logs إلى normalization؟", "options": {"A": "لتوحيد شكل البيانات وتحليلها", "B": "لتشفيرها", "C": "لتغيير IP", "D": "لمنع Windows"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل Alert أكثر قيمة للمحلل؟", "options": {"A": "Context وseverity وrelated entities", "B": "لون مختلف", "C": "اسم طويل", "D": "حجم كبير"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان Alert يتكرر كثيراً بسبب نشاط شرعي، ماذا يمكن عمله؟", "options": {"A": "tuning/suppression وفق سياسة مناسبة", "B": "إيقاف SIEM", "C": "حذف كل logs", "D": "تجاهل كل alerts"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب ربط user + host + IP + timestamp؟", "options": {"A": "لبناء سياق للتحقيق", "B": "لتقليل RAM", "C": "لتغيير subnet", "D": "لتشفير HTTP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق الأساسي بين SIEM وEDR؟", "options": {"A": "SIEM يركز على تجميع وربط بيانات متعددة، EDR على telemetry واستجابة endpoint", "B": "لا يوجد فرق", "C": "EDR خاص بالـrouters فقط", "D": "SIEM خاص بالـprinters"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Alert يكتشف PowerShell، لكن بدون command line أو parent process. ما المشكلة؟", "options": {"A": "لا توجد أي مشكلة", "B": "نقص context يجعل التحقق أصعب", "C": "PowerShell آمن دائماً", "D": "SIEM لا يحتاج context"}, "correct": "B", "difficulty": "hard"},
                    {"text": "خمسة أجهزة تظهر نفس الاتصال الخارجي خلال دقيقة واحدة بعد تنفيذ ملف واحد على جهاز واحد. ما الأفضل؟", "options": {"A": "التحقيق في الجهاز الأصلي والـtimeline والعلاقات", "B": "حذف الأجهزة الخمسة", "C": "تجاهل الحدث", "D": "تعطيل الإنترنت بالكامل"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا correlation مهم في SIEM؟", "options": {"A": "يربط عدة أحداث منفصلة لتكوين صورة تهديد", "B": "يضغط logs فقط", "C": "يحذف alerts", "D": "يغير DNS"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Alert عالي الخطورة بدون evidence إضافي. ما التصرف الأفضل؟", "options": {"A": "اعتباره اختراقاً مؤكداً", "B": "إغلاقه مباشرة", "C": "بدء triage والتحقق من الأدلة قبل القرار", "D": "حذف الجهاز"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ كشف التهديدات وMITRE ATT&CK وThreat Hunting",
                "description": "الانتقال من مجرد استقبال Alerts إلى فهم سلوك المهاجم والبحث الاستباقي عن التهديدات.",
                "objectives": [
                    "Threat Intelligence",
                    "IOC / IOA / TTPs",
                    "MITRE ATT&CK",
                    "Attack lifecycle / Cyber Kill Chain",
                    "Threat Hunting",
                    "Hypothesis-driven hunting",
                    "Detection logic / Sigma / YARA basics",
                    "KQL basics / SPL basics",
                    "IOC enrichment"
                ],
                "practical_task": "اختر فرضية: 'هل يوجد PowerShell-based execution داخل الشبكة؟'، حدد MITRE Technique، حدد مصادر البيانات، ابحث في SIEM، حدد suspicious hosts، اربط المستخدم والعملية والـIP، أنشئ Detection Rule، ووثق النتيجة.",
                "youtube_ar": "https://attack.mitre.org/",
                "youtube_en": "https://tryhackme.com/path/outline/blueteam",
                "questions": [
                    {"text": "ما وظيفة MITRE ATT&CK؟", "options": {"A": "تصنيف سلوكيات وتقنيات المهاجمين", "B": "إدارة DHCP", "C": "تشفير القرص", "D": "إدارة البريد"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما IOC؟", "options": {"A": "دليل يمكن استخدامه للإشارة إلى compromise", "B": "نوع Firewall", "C": "نظام تشغيل", "D": "بروتوكول"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود Threat Hunting؟", "options": {"A": "البحث الاستباقي عن نشاط ضار", "B": "انتظار Alert فقط", "C": "حذف logs", "D": "تحديث Windows فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الفرق بين IOC وTTP؟", "options": {"A": "IOC دليل محدد، TTP يصف أسلوب/سلوك المهاجم", "B": "لا فرق", "C": "TTP عنوان IP فقط", "D": "IOC هو OS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Sigma؟", "options": {"A": "صياغة Detection Rules بصورة قابلة للنقل بين SIEMs", "B": "تشفير DNS", "C": "إدارة المستخدمين", "D": "تشغيل VM"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي مثال أقرب إلى TTP؟", "options": {"A": "IP محدد", "B": "Hash محدد", "C": "استخدام PowerShell لتنفيذ أوامر", "D": "Domain محدد"}, "correct": "C", "difficulty": "medium"},
                    {"text": "ما أفضل نقطة بداية لـThreat Hunt؟", "options": {"A": "فرضية واضحة", "B": "حذف logs", "C": "إغلاق Firewall", "D": "تغيير جميع كلمات المرور"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا لم تجد IOC معروفاً، هل يعني عدم وجود هجوم؟", "options": {"A": "نعم", "B": "لا", "C": "فقط في Linux", "D": "فقط في Windows"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا نستخدم MITRE ATT&CK في التقارير؟", "options": {"A": "لوصف سلوك المهاجم بطريقة معيارية", "B": "لتغيير IP", "C": "لإنشاء VM", "D": "لتشفير التقرير"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة KQL في Microsoft Sentinel/Defender؟", "options": {"A": "الاستعلام عن بيانات الأمن والتحقيق فيها", "B": "إدارة BIOS", "C": "إنشاء VLAN", "D": "تثبيت Linux"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Threat Intelligence؟", "options": {"A": "إضافة سياق حول التهديدات والمؤشرات", "B": "زيادة RAM", "C": "تغيير MAC", "D": "تعطيل SIEM"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك IOC قديم جداً لكنه يظهر على جهاز حديث. ما أفضل طريقة؟", "options": {"A": "اعتباره اختراقاً مؤكداً", "B": "تجاهله تماماً", "C": "التحقق من freshness والسياق والـtelemetry", "D": "حذف IOC"}, "correct": "C", "difficulty": "hard"},
                    {"text": "Hunt وجد PowerShell، لكن النشاط مرتبط بإدارة شرعية. ما الاستنتاج؟", "options": {"A": "PowerShell = malware", "B": "يجب استخدام context لتقليل false positives", "C": "الجهاز مخترق مؤكداً", "D": "يجب إيقاف PowerShell لكل الشبكة"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ما أفضل Hunt لاكتشاف lateral movement؟", "options": {"A": "البحث عن أنماط authentication/network connections غير المعتادة بين الأجهزة", "B": "فحص wallpaper", "C": "فحص مساحة القرص", "D": "قراءة DNS فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما الفرق بين Detection وHunt؟", "options": {"A": "Detection غالباً يبحث آلياً عن نمط معروف، Hunt يبحث استباقياً وفق فرضية", "B": "لا فرق", "C": "Hunt يستخدم فقط Wireshark", "D": "Detection لا يستخدم logs"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ الاستجابة للحوادث والتحقيق الرقمي",
                "description": "التعامل المنهجي مع الحوادث من التحقق الأولي حتى الاحتواء والتعافي والتقرير.",
                "objectives": [
                    "Incident lifecycle",
                    "Preparation / Detection / Triage",
                    "Analysis / Containment / Eradication",
                    "Recovery / Lessons learned",
                    "Evidence / Chain of custody",
                    "Timeline analysis",
                    "Malware triage / Phishing investigation",
                    "Account compromise / Ransomware basics",
                    "Documentation / Escalation"
                ],
                "practical_task": "سيناريو: موظف فتح ملف Phishing ثم ظهرت PowerShell connection خارجية. نفذ: Triage، حدد الحساب والجهاز، اجمع logs، حدد process tree، افحص network connections، حدد IOCs، حدد MITRE techniques، اقترح containment، واكتب Incident Report من صفحة واحدة.",
                "youtube_ar": "https://www.cisa.gov/",
                "youtube_en": "https://www.cisa.gov/",
                "questions": [
                    {"text": "ما أول هدف من Incident Response؟", "options": {"A": "فهم الحادث والسيطرة عليه وتقليل الضرر", "B": "حذف جميع الأجهزة", "C": "تغيير DNS", "D": "إيقاف الشركة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود Triage؟", "options": {"A": "تحديد الأولوية والنطاق والخطورة مبدئياً", "B": "حذف malware", "C": "إنشاء VPN", "D": "تشفير logs"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما Chain of Custody؟", "options": {"A": "توثيق التعامل مع الأدلة ومن استلمها ومتى", "B": "Firewall rule", "C": "DNS record", "D": "Password policy"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود Containment؟", "options": {"A": "الحد من انتشار أو تأثير الحادث", "B": "حذف التقرير", "C": "تحليل RAM فقط", "D": "تحديث المتصفح"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Lessons Learned؟", "options": {"A": "تحسين الدفاع بعد الحادث", "B": "حذف evidence", "C": "تغيير IP", "D": "إغلاق SIEM"}, "correct": "A", "difficulty": "easy"},
                    {"text": "جهاز مصاب يتصل بـC2. ما الإجراء الأقرب للـcontainment؟", "options": {"A": "عزله من الشبكة وفق الإجراء المعتمد", "B": "تجاهله", "C": "حذف SIEM", "D": "تغيير خلفية الجهاز"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا لا يجب حذف malware فوراً قبل جمع الأدلة؟", "options": {"A": "قد تفقد evidence مهمة", "B": "لأن malware آمن", "C": "لأن Windows يمنع الحذف", "D": "لأن SIEM يحتاج malware"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما فائدة Timeline؟", "options": {"A": "ترتيب الأحداث زمنياً وربطها", "B": "تغيير IP", "C": "تشفير البيانات", "D": "إنشاء مستخدم"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Phishing investigation يجب أن يفحص؟", "options": {"A": "Sender, headers, URLs, attachments, user activity", "B": "حجم الشاشة فقط", "C": "RAM فقط", "D": "DNS server فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفرق بين Containment وEradication؟", "options": {"A": "Containment يحد من الحادث، Eradication يزيل سبب/أثر التهديد", "B": "لا فرق", "C": "كلاهما نسخ احتياطي", "D": "كلاهما DNS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "متى يتم Escalation؟", "options": {"A": "عندما يتجاوز الحادث صلاحيات/خطورة/نطاق المحلل", "B": "دائماً بعد أي log", "C": "فقط عند DNS", "D": "لا يحدث في SOC"}, "correct": "A", "difficulty": "medium"},
                    {"text": "حساب إداري compromised ويستخدم حالياً في lateral movement. ما الأولوية؟", "options": {"A": "تغيير wallpaper", "B": "containment للحساب والأجهزة المتأثرة والتحقيق في النشاط", "C": "حذف جميع logs", "D": "تجاهل الحساب"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا يجب تسجيل timestamp دقيق في التحقيق؟", "options": {"A": "لربط الأحداث عبر مصادر متعددة", "B": "لتغيير MAC", "C": "لمنع malware", "D": "لتشفير البريد"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا تعارضت سجلات جهازين بسبب اختلاف الوقت، ما المشكلة؟", "options": {"A": "صعوبة بناء timeline موحد", "B": "لا مشكلة", "C": "يعني أن الجهازين مصابان", "D": "يعني DNS failure"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أفضل مبدأ عند التعامل مع evidence؟", "options": {"A": "Preserve → Document → Analyze", "B": "Delete → Analyze", "C": "Modify → Upload", "D": "Restart → Ignore"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ البرمجيات الخبيثة والتصيد والتحليل الأمني",
                "description": "تحليل البريد والملفات والروابط والـIOCs وفهم السلوك الأساسي للبرمجيات الخبيثة.",
                "objectives": [
                    "Malware types",
                    "Phishing / Spear phishing",
                    "Email headers / URLs / Domains / Attachments",
                    "Hashes / VirusTotal / Sandboxing concepts",
                    "Static analysis basics",
                    "Behavioral analysis",
                    "PowerShell threats",
                    "Office attacks / Ransomware / C2",
                    "Persistence / Malware IOCs"
                ],
                "practical_task": "خذ رسالة phishing تدريبية آمنة: افحص headers، حدد sender، افحص domain، افحص URL دون فتحه مباشرة، احسب SHA-256، افحص hash في VirusTotal، استخرج IOCs، اكتب verdict، ووثق الأدلة.",
                "youtube_ar": "https://www.youtube.com/watch?v=_TnDypWebbc",
                "youtube_en": "https://tryhackme.com/path/outline/blueteam",
                "questions": [
                    {"text": "ما المقصود Phishing؟", "options": {"A": "محاولة خداع المستخدم للحصول على معلومات أو تنفيذ فعل ضار", "B": "تحديث Windows", "C": "نسخ احتياطي", "D": "VPN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما SHA-256؟", "options": {"A": "Hash function", "B": "Firewall", "C": "Protocol", "D": "SIEM"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Email Headers؟", "options": {"A": "تتبع معلومات مسار الرسالة ومصادرها", "B": "تشفير القرص", "C": "إدارة DHCP", "D": "إنشاء VLAN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود C2؟", "options": {"A": "قناة Command and Control", "B": "نوع DNS", "C": "نظام ملفات", "D": "Antivirus"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة VirusTotal للمحلل؟", "options": {"A": "الاستفادة من معلومات وفحوص متعددة حول الملفات/المؤشرات", "B": "إنشاء SIEM", "C": "إدارة الشبكة", "D": "تشغيل VM"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Domain يشبه اسم شركة حقيقية بحرف واحد مختلف. ما الاحتمال؟", "options": {"A": "Typosquatting", "B": "DHCP", "C": "VLAN", "D": "NAT"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا hash مفيد في التحقيق؟", "options": {"A": "يساعد في تحديد الملف ومقارنته بمؤشرات معروفة", "B": "يحدد IP", "C": "يمنع DNS", "D": "يحدد المستخدم دائماً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ملف Office يحتوي Macro غير متوقع. ما التصرف؟", "options": {"A": "التحقيق في المصدر والسلوك وعدم تشغيله على جهاز حقيقي", "B": "تشغيله مباشرة", "C": "إرساله للجميع", "D": "تعطيل SIEM"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما معنى C2 beaconing؟", "options": {"A": "اتصالات دورية مع بنية تحكم", "B": "DHCP renewal", "C": "DNS فقط", "D": "تحديث Windows"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل مؤشر على phishing؟", "options": {"A": "رابط/مرسل/طلب غير معتاد مع ضغط زمني", "B": "البريد من زميل دائماً", "C": "استخدام HTML", "D": "وجود توقيع"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا لا يكفي اسم الملف لتحديد malware؟", "options": {"A": "يمكن تغييره بسهولة", "B": "لأنه لا توجد أسماء ملفات", "C": "Windows يمنعه", "D": "SIEM لا يقرأه"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ملف اسمه invoice.pdf.exe ويظهر كـPDF للمستخدم. ما المؤشر؟", "options": {"A": "Double extension", "B": "DNS poisoning", "C": "ARP", "D": "DHCP"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Hash معروف بأنه malicious لكن الملف تغير قليلاً. ماذا تفعل؟", "options": {"A": "لا تعتمد على hash وحده؛ حلل السلوك والـmetadata والاتصالات", "B": "اعتبره آمناً", "C": "احذف SIEM", "D": "غير DNS"}, "correct": "A", "difficulty": "hard"},
                    {"text": "رسالة phishing تحتوي رابطاً إلى domain جديد عمره يومان. ما قيمة هذا المؤشر؟", "options": {"A": "Context مهم وقد يرفع الاشتباه", "B": "يثبت malware 100%", "C": "لا قيمة له", "D": "يعني أن المستخدم مخترق"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يعتبر behavioral analysis مهماً؟", "options": {"A": "لأن المهاجم قد يغير hash/file name بينما يبقى السلوك مشبوهاً", "B": "لأن hashes غير موجودة", "C": "لأنه يلغي الحاجة للـlogs", "D": "لأنه يمنع phishing"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ إدارة الثغرات والضوابط الأمنية وأساسيات أمن السحابة",
                "description": "فهم الثغرات والـsecurity controls والـcloud basics حتى يستطيع المحلل ربط التنبيهات بالمخاطر الفعلية.",
                "objectives": [
                    "Vulnerability vs Threat vs Risk",
                    "CVE / CVSS",
                    "Vulnerability scanning / Patch management",
                    "Misconfiguration / Security hardening",
                    "EDR / Antivirus / Firewall / MFA",
                    "IAM / Least privilege",
                    "Cloud fundamentals / AWS/Azure basics",
                    "Cloud logs / Identity security",
                    "Security baselines"
                ],
                "practical_task": "في مختبرك: شغّل Nessus Essentials أو OpenVAS/GVM على أجهزة تملكها، نفذ vulnerability scan، صنّف CVEs حسب الخطورة، حدد false positives، اربط vulnerability بالأصل المتأثر، اقترح remediation، وأنشئ جدول Risk → Evidence → Remediation.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/",
                "questions": [
                    {"text": "ما CVE؟", "options": {"A": "معرف قياسي لثغرة أمنية", "B": "نوع SIEM", "C": "بروتوكول", "D": "Firewall"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما CVSS؟", "options": {"A": "نظام لتقييم شدة الثغرات", "B": "نظام تشغيل", "C": "IDS", "D": "SIEM"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما MFA؟", "options": {"A": "استخدام أكثر من عامل للمصادقة", "B": "تشفير DNS", "C": "Network scan", "D": "Backup"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما Least Privilege؟", "options": {"A": "إعطاء المستخدم أقل صلاحيات لازمة", "B": "إعطاء الجميع Admin", "C": "منع الجميع", "D": "تغيير IP"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما IAM؟", "options": {"A": "Identity and Access Management", "B": "Intrusion Analysis Malware", "C": "Internet Attack Monitor", "D": "Internal Audit Machine"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ثغرة Critical على جهاز غير متصل بالإنترنت، وأخرى High على خادم Internet-facing. هل يجب دائماً معالجة Critical أولاً؟", "options": {"A": "نعم دائماً", "B": "ليس بالضرورة؛ يجب تقييم السياق والخطر", "C": "لا نعالج أياً منهما", "D": "نعالج الأقل دائماً"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الفرق بين Vulnerability وRisk؟", "options": {"A": "Vulnerability ضعف، Risk احتمال وتأثير استغلاله", "B": "لا فرق", "C": "Risk هو IP", "D": "Vulnerability هي malware"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا patch management مهم؟", "options": {"A": "يقلل فرص استغلال الثغرات المعروفة", "B": "يزيد false positives", "C": "يلغي SIEM", "D": "يغير MAC"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة EDR؟", "options": {"A": "مراقبة endpoint وتوفير detection/response", "B": "إدارة DNS فقط", "C": "تخزين النسخ", "D": "إنشاء VLAN"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما المقصود Misconfiguration؟", "options": {"A": "إعداد غير آمن أو غير مناسب", "B": "Malware مؤكد", "C": "CVE دائماً", "D": "Hash"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا IAM مهم في Cloud؟", "options": {"A": "للتحكم في من يستطيع الوصول إلى الموارد وما يستطيع فعله", "B": "لتغيير DNS فقط", "C": "لفحص malware", "D": "لتسجيل الحزم"}, "correct": "A", "difficulty": "medium"},
                    {"text": "مستخدم لديه صلاحيات Admin كاملة لكنه يحتاج قراءة S3 فقط. ما المشكلة؟", "options": {"A": "Excessive privileges", "B": "DNS", "C": "IDS", "D": "Hash"}, "correct": "A", "difficulty": "hard"},
                    {"text": "Vulnerability Scanner يعطي Critical على برنامج غير مستخدم. ما الأفضل؟", "options": {"A": "حذف التقرير", "B": "التحقق من asset exposure والسياق ثم تحديد الأولوية", "C": "تجاهله دائماً", "D": "إيقاف scanner"}, "correct": "B", "difficulty": "hard"},
                    {"text": "حساب Cloud يظهر login من بلد غير معتاد ثم API calls كثيرة. ما أفضل تحقيق؟", "options": {"A": "مراجعة identity logs وAPI activity ومصدر الدخول", "B": "تغيير DNS", "C": "فحص RAM", "D": "حذف الحساب مباشرة"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب ربط vulnerability management بالـasset inventory؟", "options": {"A": "لمعرفة الأنظمة المتأثرة وأولوية المعالجة", "B": "لتغيير MAC", "C": "لتشغيل SIEM", "D": "لتشفير الملفات"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية لمحلل الأمن",
                "description": "دمج المهارات السابقة في مشاريع حقيقية قابلة للعرض في GitHub وPortfolio بدل الاكتفاء بالكورسات.",
                "objectives": [
                    "SOC workflow",
                    "Log collection / SIEM",
                    "Alert triage / Investigation",
                    "Threat hunting / Incident response",
                    "Detection engineering",
                    "Endpoint monitoring / Network analysis",
                    "Documentation / Reporting",
                    "Architecture / Portfolio building"
                ],
                "practical_task": "نفذ 6 مشاريع: (1) Network Investigation (2) Windows SOC Monitoring (3) Phishing Investigation (4) SIEM Detection Project بـ5 Rules (5) Incident Response Scenario (6) Capstone SOC Lab مع GitHub كامل.",
                "youtube_ar": "https://tryhackme.com/path/outline/blueteam",
                "youtube_en": "https://tryhackme.com/path/outline/blueteam",
                "questions": [
                    {"text": "ما أول خطوة عند وصول Alert؟", "options": {"A": "Triage", "B": "حذف الجهاز", "C": "تغيير DNS", "D": "إعادة تثبيت Windows"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من Incident Report؟", "options": {"A": "توثيق الحادث والأدلة والإجراءات والنتائج", "B": "زيادة RAM", "C": "تغيير IP", "D": "إنشاء حساب"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يمثل Architecture Diagram؟", "options": {"A": "مكونات النظام وعلاقاتها", "B": "Password list", "C": "Malware hash فقط", "D": "DNS records فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم شيء في GitHub Security Project؟", "options": {"A": "README + evidence + reproducibility", "B": "اسم جذاب فقط", "C": "عدد الملفات", "D": "صورة واحدة"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود Detection Rule؟", "options": {"A": "منطق لاكتشاف نمط نشاط مشبوه", "B": "Backup", "C": "Firewall hardware", "D": "User account"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لديك Detection Rule كثيرة false positives. ما الأفضل؟", "options": {"A": "Tune rule باستخدام context", "B": "حذف SIEM", "C": "إيقاف logs", "D": "جعل كل alerts Critical"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا MITRE mapping مهم في المشروع؟", "options": {"A": "يوضح سلوك المهاجم والتقنية المرتبطة", "B": "يزيد RAM", "C": "يغير IP", "D": "يمنع DNS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل Capstone قوياً؟", "options": {"A": "Integration + Evidence + Documentation", "B": "كثرة الأدوات", "C": "اسم المشروع", "D": "عدد الصور فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل دليل على مهارة Security Analyst؟", "options": {"A": "القدرة على التحقيق في حادث حقيقي/تدريبي وشرح القرار", "B": "مشاهدة 20 كورس", "C": "شهادة فقط", "D": "معرفة أسماء الأدوات"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجب تضمينه في Alert investigation؟", "options": {"A": "Who/What/When/Where/How", "B": "لون الجهاز", "C": "حجم الشاشة", "D": "نوع الكيبورد"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا لم تجد evidence كافية، ماذا تفعل؟", "options": {"A": "تذكر حدود التحقيق وتجمع أدلة إضافية", "B": "تخترع النتيجة", "C": "تقول malware مؤكد", "D": "تحذف alert"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Alert منفرد يبدو خطيراً، لكن endpoint telemetry طبيعي تماماً. ما القرار الأفضل؟", "options": {"A": "التحقيق في السياق قبل التصعيد", "B": "تأكيد breach", "C": "حذف endpoint", "D": "إغلاق SIEM"}, "correct": "A", "difficulty": "hard"},
                    {"text": "مشروعك يكتشف Brute Force لكنه لا يوضح كيفية التحقيق بعد Alert. ما النقص؟", "options": {"A": "Detection فقط دون Response/Investigation workflow", "B": "نقص RAM", "C": "نقص DNS", "D": "نقص Windows"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا يجب أن تحتوي المشاريع على False Positive analysis؟", "options": {"A": "لإظهار قدرة المحلل على تحسين detection وتقليل الضوضاء", "B": "لأنها مطلوبة للـnetworking", "C": "لأنها تغير IP", "D": "لأنها تمنع malware"}, "correct": "A", "difficulty": "hard"},
                    {"text": "في Capstone اكتشفت compromise. ما أفضل ترتيب؟", "options": {"A": "Evidence → Timeline → Scope → Containment → Eradication → Recovery → Report", "B": "Delete → Restart → Report", "C": "Shutdown all → Ignore evidence", "D": "Change DNS → Finish"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 التحضير المهني وJob Ready",
                "description": "تحويل المهارات والمشاريع إلى جاهزية فعلية لوظيفة Junior Security Analyst / SOC L1.",
                "objectives": [
                    "Security Analyst CV",
                    "GitHub Portfolio / LinkedIn",
                    "Incident reports",
                    "Technical interview / SOC scenarios",
                    "SIEM questions / Networking questions",
                    "Windows/Linux questions",
                    "MITRE ATT&CK / Incident Response",
                    "Threat Hunting / Detection",
                    "Security communication / Reporting",
                    "System thinking / Final assessment",
                    "Job applications"
                ],
                "practical_task": "نفذ Final Junior Security Analyst Assessment: Networking (PCAP analysis) + Windows (Event/Sysmon/PowerShell) + SIEM (3 queries + 3 alerts + 1 dashboard + 1 investigation) + Incident Response (Phishing → Credential Theft → PowerShell → C2) + Interview Simulation.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200",
                "questions": [
                    {"text": "ما الوظيفة الأقرب لمسارنا؟", "options": {"A": "Junior Security Analyst", "B": "Database Administrator", "C": "Frontend Developer", "D": "Data Engineer"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم عنصر في Security Portfolio؟", "options": {"A": "مشاريع عملية موثقة", "B": "عدد المتابعين", "C": "صورة شخصية", "D": "عدد الشهادات فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يجب أن يوضح CV؟", "options": {"A": "Skills + Projects + Evidence of practical ability", "B": "أسماء الأدوات فقط", "C": "الهوايات فقط", "D": "عدد صفحات كبير"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم مهارة في مقابلة SOC؟", "options": {"A": "القدرة على التفكير والتحقيق وشرح القرار", "B": "حفظ أسماء malware", "C": "كتابة HTML", "D": "تصميم PowerPoint"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود Job Ready؟", "options": {"A": "القدرة على أداء مهام Junior الأساسية عملياً", "B": "معرفة كل شيء في cybersecurity", "C": "Senior level", "D": "امتلاك شهادة فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "في مقابلة سألك المحاور عن Alert مشبوه، ماذا يجب أن تشرح؟", "options": {"A": "منهجية التحقيق خطوة بخطوة", "B": "اسم أداة فقط", "C": "أنك ستعيد تشغيل الجهاز", "D": "أنك ستغلق SIEM"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجعل GitHub project احترافياً؟", "options": {"A": "README + Architecture + Evidence + Results", "B": "اسم repository فقط", "C": "100 ملف", "D": "ألوان كثيرة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة لشرح مشروع SOC؟", "options": {"A": "Problem → Architecture → Detection → Investigation → Result", "B": "أسماء الأدوات فقط", "C": "عدد الأسطر", "D": "screenshots فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الذي يجب أن يفعله Junior Analyst عند عدم التأكد؟", "options": {"A": "جمع أدلة إضافية والتصعيد عند الحاجة", "B": "اختراع الإجابة", "C": "إغلاق الحادث", "D": "حذف logs"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أهم شيء في Incident Report؟", "options": {"A": "Facts, evidence, timeline, impact, actions", "B": "رأي المحلل فقط", "C": "صورة فقط", "D": "اسم الشركة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أي مهارة ترفع قيمة Security Analyst بشكل واضح؟", "options": {"A": "SIEM + Networking + Incident Response + Threat Hunting", "B": "Photoshop", "C": "تصميم مواقع", "D": "Excel فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "أثناء مقابلة طلب منك تصميم SOC workflow. ما التسلسل الأفضل؟", "options": {"A": "Telemetry → Detection → Alert → Triage → Investigation → Response → Lessons Learned", "B": "Alert → Delete Logs → Restart", "C": "Firewall → Photoshop → Report", "D": "DNS → DHCP → Finish"}, "correct": "A", "difficulty": "hard"},
                    {"text": "إذا لم تستطع تفسير Alert بدون الرجوع للمصادر، ما أفضل موقف؟", "options": {"A": "اشرح منهجية التحقيق وكيف ستتحقق بدل اختراع إجابة", "B": "ادعِ أنك تعرف", "C": "أغلق Alert", "D": "احذف evidence"}, "correct": "A", "difficulty": "hard"},
                    {"text": "شركة تسألك: 'هل هذا النشاط Malicious؟' ما أفضل إجابة محلل؟", "options": {"A": "'سأحتاج إلى evidence/context قبل تحديد verdict'", "B": "'نعم دائماً'", "C": "'لا يمكن معرفة ذلك أبداً'", "D": "'كل PowerShell malicious'"}, "correct": "A", "difficulty": "hard"},
                    {"text": "متى تستحق لقب Strong Junior Security Analyst؟", "options": {"A": "عندما تستطيع مراقبة وتحليل وتنفيذ triage والاستجابة الأساسية وتوثيق الحوادث", "B": "عندما تحفظ 1000 CVE", "C": "عندما تستخدم Kali فقط", "D": "عندما تحصل على شهادة واحدة"}, "correct": "A", "difficulty": "hard"}
                ]
            }
        ]
    }
]