# data/career_content_netsec.py
# بنك محتوى مسار "مهندس أمن الشبكات (Network Security Engineer)"
# 10 مراحل × 15 سؤال = 150 سؤال
# ==========================================

NETWORK_SECURITY_PATHS = [
    {
        "major_key": "cyber",
        "slug": "network-security-engineer",
        "title": "مهندس أمن شبكات (Network Security Engineer)",
        "description": "مسار متكامل: Networking + Routing/Switching + Segmentation + Firewall/NAT/VPN + IDS/IPS + Cloud Network Security + Automation.",
        "icon": "🌐",
        "difficulty": "متقدم",
        "estimated_hours": 260,
        "order_index": 3,
        "stages": [
            # ==========================================
            # المرحلة 1
            # ==========================================
            {
                "stage_number": 1,
                "title": "1️⃣ أساسيات IT والشبكات والأمن",
                "description": "بناء أساس قوي في الشبكات وأنظمة التشغيل والأمن حتى يستطيع المتعلم فهم حركة البيانات والمخاطر الأمنية.",
                "objectives": [
                    "OSI & TCP/IP",
                    "IPv4 / IPv6",
                    "MAC / IP / ARP",
                    "TCP / UDP",
                    "Ports & Protocols",
                    "DNS / DHCP",
                    "HTTP / HTTPS / SSH",
                    "Linux CLI basics",
                    "Windows networking basics",
                    "CIA Triad",
                    "Authentication / Authorization",
                    "Least Privilege",
                    "Threats & Attack Surface",
                    "Virtualization / Basic Git"
                ],
                "practical_task": "أنشئ Lab بسيط: Linux VM + Windows VM، حدد IP لكل جهاز، اختبر ping، استخدم ipconfig/ip addr، استخدم nslookup، افحص المنافذ بـnetstat/ss، اتصل عبر SSH، أنشئ مستخدماً وصلاحيات، التقط DNS/TCP traffic بـWireshark، واكتب تقريراً من صفحة واحدة.",
                "youtube_ar": "https://www.youtube.com/watch?v=8f2Zsb89uoM",
                "youtube_en": "https://learn.microsoft.com/en-us/training/modules/network-fundamentals/",
                "questions": [
                    {"text": "أي عنصر يستخدم لتحديد جهاز داخل شبكة IP؟", "options": {"A": "MAC Address", "B": "IP Address", "C": "Port Number", "D": "Protocol"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أي بروتوكول يستخدم عادة للحصول على IP تلقائياً؟", "options": {"A": "DNS", "B": "SSH", "C": "DHCP", "D": "FTP"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما وظيفة DNS الأساسية؟", "options": {"A": "تحويل أسماء النطاقات إلى عناوين IP", "B": "تشفير الملفات", "C": "توزيع IP", "D": "فحص المنافذ"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي بروتوكول يستخدم عادة للاتصال الآمن بسطر الأوامر؟", "options": {"A": "FTP", "B": "Telnet", "C": "HTTP", "D": "SSH"}, "correct": "D", "difficulty": "easy"},
                    {"text": "أي عنصر يمثل Confidentiality في CIA Triad؟", "options": {"A": "منع تعديل البيانات", "B": "ضمان توفر الخدمة", "C": "منع الوصول غير المصرح", "D": "تسجيل الأحداث"}, "correct": "C", "difficulty": "easy"},
                    {"text": "جهاز يستطيع الوصول إلى IP داخلي لكنه لا يستطيع الوصول إلى اسم موقع، ما المشكلة المحتملة؟", "options": {"A": "DNS", "B": "DHCP", "C": "MAC", "D": "ARP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كان جهازان في نفس الشبكة المحلية، فما الآلية المهمة لمعرفة MAC المرتبط بعنوان IPv4؟", "options": {"A": "DNS", "B": "ARP", "C": "DHCP", "D": "NAT"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك خدمة Web تعمل على TCP/443. ماذا يمثل الرقم 443؟", "options": {"A": "IP", "B": "MAC", "C": "Subnet", "D": "Port"}, "correct": "D", "difficulty": "medium"},
                    {"text": "أي أمر Linux يعرض عناوين الشبكة والواجهات في الأنظمة الحديثة؟", "options": {"A": "ip addr", "B": "pwd", "C": "whoami", "D": "cat"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يعتبر Least Privilege مهماً؟", "options": {"A": "يزيد سرعة الشبكة", "B": "يقلل حجم البيانات", "C": "يقلل صلاحيات الحساب إلى ما يحتاجه فقط", "D": "يمنع DNS"}, "correct": "C", "difficulty": "medium"},
                    {"text": "جهاز يستطيع تنفيذ ping 8.8.8.8 لكنه لا يستطيع ping google.com. ما الاحتمال الأقوى؟", "options": {"A": "مشكلة DNS", "B": "مشكلة RAM", "C": "مشكلة MAC", "D": "مشكلة SSH"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك جهاز يحصل على IP من DHCP لكنه لا يستطيع الوصول إلى شبكة أخرى. ما أول شيء منطقي لفحصه؟", "options": {"A": "Browser cache", "B": "Default Gateway", "C": "Username", "D": "File permissions"}, "correct": "B", "difficulty": "hard"},
                    {"text": "أثناء تحليل اتصال وجدت TCP SYN يخرج من جهاز داخلي ولا يظهر SYN/ACK من الخادم. ماذا يدل ذلك غالباً؟", "options": {"A": "الاتصال اكتمل", "B": "DNS نجح", "C": "لا يوجد رد على محاولة إنشاء الاتصال", "D": "HTTP تم تشفيره"}, "correct": "C", "difficulty": "hard"},
                    {"text": "مستخدم عادي يستطيع تعديل إعدادات Firewall الخاصة بالخادم. أي مبدأ أمني تم انتهاكه بوضوح؟", "options": {"A": "Defense in Depth", "B": "Availability", "C": "Least Privilege", "D": "Redundancy"}, "correct": "C", "difficulty": "hard"},
                    {"text": "تريد تحديد ما إذا كانت مشكلة الاتصال في Layer 3 أم أعلى. ما الاختبار الأنسب أولاً؟", "options": {"A": "فتح HTTPS", "B": "اختبار الوصول إلى IP باستخدام ping", "C": "تغيير كلمة المرور", "D": "حذف Browser Cookies"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 2
            # ==========================================
            {
                "stage_number": 2,
                "title": "2️⃣ التوجيه والتحويل والبنية التحتية للشبكات",
                "description": "إتقان البنية التي يعمل فوقها أمن الشبكات: Switching، Routing، VLANs، Subnetting، ACLs وIPv6.",
                "objectives": [
                    "Ethernet / Switching / VLAN",
                    "Access / Trunk Ports",
                    "STP concepts",
                    "IPv4 Subnetting / IPv6 basics",
                    "Static Routing / Dynamic Routing concepts",
                    "Default Route / Inter-VLAN Routing",
                    "ACL concepts / NAT concepts",
                    "Routing Tables",
                    "Network Troubleshooting",
                    "Broadcast / Collision Domains"
                ],
                "practical_task": "باستخدام Packet Tracer: أنشئ شبكة 2 Switches + 2 Routers + 4 PCs، أنشئ VLAN 10 و20، استخدم Trunk بين Switches، طبّق Inter-VLAN Routing، أضف Static Routes، اختبر الاتصال، اكسر Route عمداً وشخّص، أضف ACL تمنع VLAN 10 من خدمة معينة، ووثق Topology وIP addressing.",
                "youtube_ar": "https://eg.stjegypt.com/course/n/772",
                "youtube_en": "https://learn.microsoft.com/en-us/training/modules/network-fundamentals/",
                "questions": [
                    {"text": "ما وظيفة VLAN؟", "options": {"A": "تقسيم الشبكة منطقياً", "B": "تشفير البيانات", "C": "توزيع DNS", "D": "فحص الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الجهاز المسؤول أساساً عن Forwarding بين شبكات IP مختلفة؟", "options": {"A": "Hub", "B": "Router", "C": "Access Point فقط", "D": "Printer"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الذي يحدد الشبكة والـHost في IPv4؟", "options": {"A": "MAC", "B": "Port", "C": "Subnet Mask", "D": "DNS"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ما استخدام Trunk Port؟", "options": {"A": "حمل VLANs متعددة", "B": "تشفير VPN", "C": "تعيين DHCP فقط", "D": "منع ARP"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا تفعل Default Route؟", "options": {"A": "تمنع كل Traffic", "B": "تستخدم عندما لا يوجد Route أكثر تحديداً", "C": "تحول DNS", "D": "تنشئ VLAN"}, "correct": "B", "difficulty": "easy"},
                    {"text": "لديك 192.168.10.0/24 وتحتاج 4 شبكات متساوية. ما Prefix المناسب؟", "options": {"A": "/25", "B": "/26", "C": "/27", "D": "/28"}, "correct": "B", "difficulty": "medium"},
                    {"text": "جهازان في VLAN مختلفة لا يستطيعان التواصل. ما المطلوب عادة؟", "options": {"A": "DNS", "B": "Inter-VLAN Routing", "C": "تغيير MAC", "D": "FTP"}, "correct": "B", "difficulty": "medium"},
                    {"text": "إذا كان Switch يستقبل Frame لوجهة موجودة في MAC table، ماذا يفعل عادة؟", "options": {"A": "يرسلها إلى المنفذ المناسب", "B": "يرسلها إلى جميع المنافذ", "C": "يحذفها دائماً", "D": "يحولها إلى IP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يستخدم STP؟", "options": {"A": "منع Layer 2 loops", "B": "تشفير VLAN", "C": "تعيين IP", "D": "فحص Malware"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ACL تسمح بـTCP/443 من شبكة الإدارة فقط. ما الهدف الأساسي؟", "options": {"A": "تقليل Broadcast", "B": "تقييد الوصول إلى الخدمة", "C": "زيادة MTU", "D": "تغيير DNS"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك Route إلى 10.10.10.0/24 وDefault Route. أيهما يستخدم للوصول إلى 10.10.10.5؟", "options": {"A": "Default Route", "B": "Route الأكثر تحديداً", "C": "DNS Route", "D": "ARP Route"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك VLAN 10 و20، والـTrunk يعمل، لكن الأجهزة في VLAN 20 لا تتواصل مع Gateway. ما أول شيء تفحصه؟", "options": {"A": "VLAN membership وGateway configuration", "B": "DNS record", "C": "Browser", "D": "SSH key"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك شبكة 10.0.0.0/24 وتحتاج 30 جهازاً في كل subnet. أي Prefix هو الأنسب؟", "options": {"A": "/26", "B": "/27", "C": "/28", "D": "/29"}, "correct": "B", "difficulty": "hard"},
                    {"text": "بعد إضافة Link ثانية بين Switchين بدأت الشبكة تعاني من Broadcast storm. ما السبب المحتمل؟", "options": {"A": "DNS failure", "B": "Layer 2 loop", "C": "DHCP lease", "D": "Wrong gateway only"}, "correct": "B", "difficulty": "hard"},
                    {"text": "ACL تمنع Traffic صحيحاً لأن Rule عامة جاءت قبل Rule الخاصة بالسماح. ما المشكلة؟", "options": {"A": "DNS cache", "B": "Rule ordering", "C": "MTU", "D": "STP priority"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 3
            # ==========================================
            {
                "stage_number": 3,
                "title": "3️⃣ معمارية أمن الشبكات والتقسيم",
                "description": "الانتقال من إدارة الشبكة إلى تصميم شبكة آمنة باستخدام Defense in Depth، Segmentation، DMZ وZero Trust.",
                "objectives": [
                    "Defense in Depth",
                    "Security Zones / DMZ",
                    "Network Segmentation / Micro-segmentation",
                    "Zero Trust",
                    "Trust Boundaries",
                    "East-West / North-South Traffic",
                    "Security Policies / ACL Design",
                    "Firewall Zones / Bastion Hosts",
                    "Management Networks",
                    "Secure Network Architecture",
                    "Attack Surface Reduction"
                ],
                "practical_task": "صمم Network Architecture لشركة لديها Users, Servers, Database, Public Web Server, Admin Network, Guest Network. قسّمها إلى Internet → Firewall → DMZ → Internal → Database → Management، حدد Security Zones، اكتب 15 Firewall/ACL Rules، امنع Guest من Internal، اسمح Web → Database بالمنفذ المطلوب فقط، امنع Users من Management، وأنشئ Architecture Diagram.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://learn.microsoft.com/en-us/azure/networking/security/",
                "questions": [
                    {"text": "ما الهدف الأساسي من Network Segmentation؟", "options": {"A": "زيادة سرعة الإنترنت فقط", "B": "تقليل الحركة الجانبية وتحسين التحكم", "C": "زيادة DNS", "D": "إلغاء Firewall"}, "correct": "B", "difficulty": "easy"},
                    {"text": "أين يوضع Web Server المتاح من الإنترنت غالباً؟", "options": {"A": "Database VLAN", "B": "Management VLAN", "C": "DMZ", "D": "Guest Printer VLAN"}, "correct": "C", "difficulty": "easy"},
                    {"text": "ماذا يعني Defense in Depth؟", "options": {"A": "الاعتماد على Firewall واحد", "B": "استخدام طبقات متعددة من الحماية", "C": "منع كل الإنترنت", "D": "استخدام VPN فقط"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المبدأ الأساسي في Zero Trust؟", "options": {"A": "الثقة بكل الأجهزة الداخلية", "B": "Never trust, always verify", "C": "الثقة بالـIP الداخلي", "D": "السماح لكل VLAN"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما المقصود بـEast-West Traffic؟", "options": {"A": "Internet إلى المؤسسة", "B": "حركة داخلية بين الأنظمة", "C": "DNS فقط", "D": "VPN فقط"}, "correct": "B", "difficulty": "easy"},
                    {"text": "لماذا يجب عزل شبكة الإدارة؟", "options": {"A": "لتقليل مساحة الوصول إلى أجهزة الإدارة", "B": "لتسريع DNS", "C": "لإلغاء Logging", "D": "لزيادة Broadcast"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Server في DMZ يحتاج الاتصال بقاعدة البيانات. ما السياسة الأفضل؟", "options": {"A": "السماح بكل المنافذ", "B": "السماح بالمنفذ المطلوب فقط", "C": "السماح لكل Internal", "D": "السماح من Guest"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما الخطر من شبكة Flat Network؟", "options": {"A": "انخفاض DNS", "B": "سهولة الحركة الجانبية للمهاجم", "C": "عدم وجود IP", "D": "عدم وجود MAC"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي تصميم أكثر أماناً؟", "options": {"A": "Users → Database مباشرة", "B": "Internet → Database", "C": "Internet → DMZ → Controlled Internal Access", "D": "Guest → Management"}, "correct": "C", "difficulty": "medium"},
                    {"text": "لماذا لا يعتبر وجود الجهاز داخل LAN سبباً كافياً للثقة؟", "options": {"A": "لأن الأجهزة الداخلية قد تُخترق", "B": "لأن LAN لا تستخدم IP", "C": "لأن DNS يمنعها", "D": "لأن VLAN لا تعمل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "تريد منع Workstations من الاتصال مباشرة بـDatabase. ما الحل الأنسب؟", "options": {"A": "Segmentation + Firewall Policy", "B": "DNS", "C": "DHCP", "D": "زيادة MTU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "مهاجم اخترق Web Server في DMZ ويحاول الاتصال بـSMB على عشرات الأجهزة الداخلية. ما التحكم الأهم؟", "options": {"A": "زيادة سرعة Internet", "B": "East-West segmentation", "C": "تغيير DNS فقط", "D": "إضافة Public IP"}, "correct": "B", "difficulty": "hard"},
                    {"text": "في تصميم Zero Trust، جهاز موثوق سابقاً أصبح مصاباً. ما الفكرة التي تحد من الضرر؟", "options": {"A": "الثقة الدائمة", "B": "Continuous verification + least privilege", "C": "السماح الداخلي", "D": "إلغاء Authentication"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لماذا يجب عدم وضع Firewall Management Interface على شبكة المستخدمين؟", "options": {"A": "لأنها تزيد سرعة الشبكة", "B": "لأنها تقلل MTU", "C": "لأنها تزيد خطر الوصول الإداري غير المصرح", "D": "لأنها تمنع DHCP"}, "correct": "C", "difficulty": "hard"},
                    {"text": "مؤسسة لديها Web وAPI وDatabase. أي تصميم يوفر أفضل فصل؟", "options": {"A": "الثلاثة في VLAN واحدة", "B": "Web وDatabase على الإنترنت", "C": "Security Zones متعددة مع قواعد محددة بين الطبقات", "D": "السماح بكل Traffic بين الجميع"}, "correct": "C", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 4
            # ==========================================
            {
                "stage_number": 4,
                "title": "4️⃣ جدران الحماية وNAT وVPN",
                "description": "إتقان أهم وظيفة عملية لمهندس أمن الشبكات: Firewall Policies، NAT، VPN، Routing.",
                "objectives": [
                    "Stateful Firewalls",
                    "Firewall Policies / Zones / Objects",
                    "Services / NAT / SNAT / DNAT",
                    "Port Forwarding / Security Policies",
                    "Logging",
                    "Site-to-Site VPN / IPsec",
                    "SSL VPN concepts / Remote Access VPN",
                    "Authentication",
                    "Firewall Troubleshooting",
                    "FortiGate CLI/GUI"
                ],
                "practical_task": "أنشئ FortiGate Lab: Internet/WAN → FortiGate → LAN، Configure Interfaces وLAN DHCP، Create Address/Service Objects وFirewall Policies، Configure SNAT وPort Forwarding، Enable Logging، أنشئ Site-to-Site IPsec VPN بين شبكتين، اختبر VPN، استخدم Packet Capture لتشخيص مشكلة مصطنعة، ووثق جميع Rules.",
                "youtube_ar": "https://it-sharks.com/ar/course/FortiGate-firewall-course7",
                "youtube_en": "https://training.fortinet.com/",
                "questions": [
                    {"text": "ما وظيفة Stateful Firewall؟", "options": {"A": "تتبع حالة الاتصالات واتخاذ قرارات بناءً عليها", "B": "توزيع DNS", "C": "إنشاء VLAN فقط", "D": "ضغط الملفات"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة SNAT غالباً؟", "options": {"A": "تغيير Source Address", "B": "تغيير Destination Port فقط", "C": "تشفير DNS", "D": "إنشاء VLAN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما استخدام DNAT؟", "options": {"A": "تغيير Source MAC", "B": "تحويل Destination إلى عنوان داخلي", "C": "توزيع DHCP", "D": "إنشاء مستخدم"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الهدف من VPN؟", "options": {"A": "إنشاء اتصال محمي عبر شبكة غير موثوقة", "B": "إلغاء Firewall", "C": "زيادة Broadcast", "D": "استبدال DNS"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي بروتوكول يرتبط بشكل شائع بـSite-to-Site VPN؟", "options": {"A": "ARP", "B": "IPsec", "C": "DHCP", "D": "ICMP"}, "correct": "B", "difficulty": "easy"},
                    {"text": "لديك Web Server داخلي وتريد نشره على الإنترنت. ما الوظيفة المطلوبة عادة؟", "options": {"A": "DNAT/Port Forwarding + Firewall Policy", "B": "DHCP فقط", "C": "STP", "D": "ARP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Rule تسمح من LAN إلى Internet لكن المستخدم لا يستطيع الوصول للإنترنت. ما أول شيء تتحقق منه؟", "options": {"A": "Policy + NAT + Routing", "B": "Keyboard", "C": "DNS فقط دائماً", "D": "VLAN name فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب وضع قواعد Firewall محددة؟", "options": {"A": "لتقليل الوصول غير الضروري", "B": "لتسمح بكل شيء", "C": "لتلغي Logging", "D": "لزيادة Broadcast"}, "correct": "A", "difficulty": "medium"},
                    {"text": "إذا كانت Firewall Policy تسمح TCP/443 فقط، ماذا يحدث لمحاولة TCP/22؟", "options": {"A": "تُسمح دائماً", "B": "تعتمد على قاعدة أخرى، وإلا تُرفض حسب السياسة الافتراضية", "C": "تتحول إلى UDP", "D": "تصبح DNS"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة للسماح Web Server بالوصول إلى Database؟", "options": {"A": "Allow All", "B": "السماح بالـIP/Port المطلوب فقط", "C": "فتح كل Internal Ports", "D": "السماح من Internet"}, "correct": "B", "difficulty": "medium"},
                    {"text": "Site-to-Site IPsec يعمل من جهة واحدة فقط. ما أحد أهم الأشياء التي تفحصها؟", "options": {"A": "Phase parameters / routing / policies", "B": "Browser cookies", "C": "Printer driver", "D": "Keyboard"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Firewall Policy صحيحة لكن الـTraffic لا يصل. Routing table لا تحتوي Route للـDestination. ما النتيجة؟", "options": {"A": "سيعمل بسبب DNS", "B": "لن يعمل لأن Firewall ليست Router بديلة تلقائياً", "C": "سيتحول إلى Broadcast", "D": "سيستخدم MAC فقط"}, "correct": "B", "difficulty": "hard"},
                    {"text": "Port Forwarding يعمل من خارج الشبكة لكن السيرفر لا يرد. ما المجموعة الأكثر منطقية للفحص؟", "options": {"A": "Server Gateway + Firewall Policy + Return Routing", "B": "Wallpaper", "C": "DNS TXT فقط", "D": "USB"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك VPN Tunnel Up لكن لا يوجد Ping بين الشبكتين. ما السبب المحتمل؟", "options": {"A": "Encryption نجح إذن كل شيء صحيح", "B": "Routing أو Firewall Policy أو Phase 2 selectors", "C": "DHCP على جهاز المستخدم فقط", "D": "Browser"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لديك Rule تسمح Any → Any. ما المشكلة الأساسية؟", "options": {"A": "ضعف مبدأ Least Privilege وارتفاع Attack Surface", "B": "أنها تمنع كل Traffic", "C": "أنها تمنع DNS", "D": "أنها تقلل Bandwidth"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 5
            # ==========================================
            {
                "stage_number": 5,
                "title": "5️⃣ مراقبة الشبكة وWireshark وIDS/IPS",
                "description": "القدرة على رؤية ما يحدث داخل الشبكة، تحليل Packets، اكتشاف الأنماط المشبوهة واستخدام IDS/IPS.",
                "objectives": [
                    "Packet Capture / Wireshark",
                    "Display Filters",
                    "TCP Handshake / DNS Analysis",
                    "HTTP/HTTPS / TLS basics",
                    "ARP Analysis / ICMP",
                    "Network Baselines",
                    "Syslog / SNMP concepts / NetFlow concepts",
                    "IDS / IPS",
                    "Signature Detection",
                    "Suricata / Alert Analysis / False Positives"
                ],
                "practical_task": "استخدم Wireshark وSuricata في Lab: Capture DNS traffic، Capture TCP 3-way handshake، حلل HTTP request، استخدم Filters (dns, tcp, http, icmp)، حلل ARP traffic، شغّل Suricata، راقب Alerts، صنّف كل Alert (True Positive / False Positive / Informational)، واكتب Incident Note لكل Alert مهم.",
                "youtube_ar": "https://www.wireshark.org/docs/wsug_html_chunked/",
                "youtube_en": "https://www.wireshark.org/docs/wsug_html_chunked/",
                "questions": [
                    {"text": "ما وظيفة Wireshark الأساسية؟", "options": {"A": "Packet Analysis", "B": "Password Management", "C": "Database Management", "D": "Email Hosting"}, "correct": "A", "difficulty": "easy"},
                    {"text": "كم مرحلة أساسية في TCP Three-Way Handshake؟", "options": {"A": "1", "B": "2", "C": "3", "D": "4"}, "correct": "C", "difficulty": "easy"},
                    {"text": "أي Filter يعرض DNS traffic؟", "options": {"A": "http", "B": "dns", "C": "ssh", "D": "arp"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما وظيفة IDS؟", "options": {"A": "اكتشاف النشاط المشبوه", "B": "توزيع IP", "C": "تشفير القرص", "D": "إدارة المستخدمين"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الفرق الأساسي بين IDS وIPS؟", "options": {"A": "IPS يمكنه منع Traffic", "B": "IDS يوزع DHCP", "C": "IDS يقوم دائماً بالتشفير", "D": "لا يوجد فرق"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ظهر SYN من Client ولا يوجد SYN/ACK. ماذا تحقق أولاً؟", "options": {"A": "هل الخادم/Firewall يرد أم يتم حجب Traffic", "B": "DNS TXT", "C": "MAC Printer", "D": "Username"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نستخدم Network Baseline؟", "options": {"A": "معرفة النشاط الطبيعي ومقارنته بالشذوذ", "B": "حذف Logs", "C": "إلغاء Firewall", "D": "إنشاء VLAN"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Alert IDS ظهر لكن النشاط طبيعي ومصرح به. كيف يصنف غالباً؟", "options": {"A": "True Positive", "B": "False Positive", "C": "Critical Incident دائماً", "D": "Malware مؤكد"}, "correct": "B", "difficulty": "medium"},
                    {"text": "أي بروتوكول يستخدم غالباً لتجميع Logs مركزياً؟", "options": {"A": "Syslog", "B": "ARP", "C": "DHCP", "D": "ICMP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الفائدة الأمنية من Packet Capture؟", "options": {"A": "رؤية تفاصيل الاتصال الفعلي", "B": "تغيير Password", "C": "إنشاء User", "D": "توزيع IP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "حركة DNS ضخمة وغير معتادة من جهاز واحد قد تشير إلى ماذا؟", "options": {"A": "احتمال DNS tunneling أو نشاط غير طبيعي", "B": "نجاح DHCP", "C": "VLAN trunk", "D": "STP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "جهاز يرسل عدداً كبيراً من TCP SYN إلى منافذ كثيرة في نفس الخادم. ما الاحتمال الأقوى؟", "options": {"A": "Port scanning / SYN-based activity", "B": "DHCP renewal", "C": "DNS normal traffic", "D": "ARP cache refresh فقط"}, "correct": "A", "difficulty": "hard"},
                    {"text": "IDS ينبه عن Attack Signature معروفة، لكن Packet Capture يظهر أن الـTraffic جزء من اختبار مصرح. ماذا تفعل؟", "options": {"A": "تعتبره Malware فوراً", "B": "تتحقق من السياق وتوثق False Positive إن ثبت", "C": "تحذف IDS", "D": "تمنع الإنترنت بالكامل"}, "correct": "B", "difficulty": "hard"},
                    {"text": "تريد معرفة الأجهزة التي تتصل بخادم محدد على TCP/443. ما أفضل مصدر؟", "options": {"A": "Packet capture أو network flow data", "B": "Keyboard logs", "C": "DHCP فقط", "D": "Wallpaper"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك Alert عن HTTP إلى IP مشبوه، لكن HTTPS traffic لا يظهر في المحتوى. لماذا؟", "options": {"A": "TLS يخفي محتوى التطبيق أثناء النقل", "B": "TCP لا يعمل", "C": "IP غير موجود", "D": "DNS يمنع HTTPS"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 6
            # ==========================================
            {
                "stage_number": 6,
                "title": "6️⃣ الوصول الآمن والهوية واللاسلكي وتقوية الشبكة",
                "description": "تأمين نقاط الوصول إلى الشبكة والأجهزة والخدمات، وربط Network Security بالهوية وAAA وWireless.",
                "objectives": [
                    "AAA / RADIUS / TACACS+",
                    "Authentication / Authorization / Accounting",
                    "MFA",
                    "Network Device Hardening / SSH",
                    "Secure Management / SNMPv3",
                    "Wireless Security / WPA2/WPA3",
                    "Guest Networks / NAC concepts",
                    "DHCP Security / ARP Spoofing",
                    "DHCP Snooping / Dynamic ARP Inspection",
                    "Port Security / Configuration Backup"
                ],
                "practical_task": "في Packet Tracer/GNS3: Configure SSH بدل Telnet، أنشئ Admin user، طبّق privilege levels وPort Security، أنشئ Guest VLAN وافصلها عن Internal، صمم AAA Architecture concept، وثق Hardening Checklist، أنشئ Backup للـconfiguration، واختبر محاولة وصول غير مصرح بها.",
                "youtube_ar": "https://eg.stjegypt.com/course/n/772",
                "youtube_en": "https://learn.microsoft.com/en-us/azure/security/fundamentals/",
                "questions": [
                    {"text": "ماذا تعني AAA؟", "options": {"A": "Authentication, Authorization, Accounting", "B": "Access, Address, ARP", "C": "Authentication, Address, ARP", "D": "Authorization, ARP, Accounting"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أي بروتوكول يستخدم عادة للإدارة الآمنة بدل Telnet؟", "options": {"A": "FTP", "B": "SSH", "C": "HTTP", "D": "TFTP"}, "correct": "B", "difficulty": "easy"},
                    {"text": "WPA3 يتعلق بأمن ماذا؟", "options": {"A": "Wireless", "B": "DNS", "C": "Routing", "D": "VPN فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من MFA؟", "options": {"A": "إضافة عامل تحقق إضافي", "B": "تغيير IP", "C": "زيادة Bandwidth", "D": "إلغاء Password"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الخطر من استخدام Telnet لإدارة جهاز؟", "options": {"A": "البيانات غير مشفرة", "B": "يمنع Routing", "C": "يمنع VLAN", "D": "يغير MAC"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة RADIUS؟", "options": {"A": "AAA للشبكة", "B": "Routing فقط", "C": "DNS فقط", "D": "Packet Capture"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يتم فصل Guest Wi-Fi؟", "options": {"A": "لمنع الضيوف من الوصول إلى الشبكات الداخلية", "B": "لزيادة DHCP", "C": "لإلغاء Encryption", "D": "لتسريع DNS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الهجوم الذي يستغل ARP لإيهام الأجهزة بعنوان MAC مزيف؟", "options": {"A": "ARP Spoofing", "B": "DNS poisoning فقط", "C": "SYN Flood فقط", "D": "DHCP starvation فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما وظيفة DHCP Snooping؟", "options": {"A": "الحد من DHCP servers غير الموثوقة", "B": "تشفير HTTP", "C": "إدارة VPN", "D": "إنشاء DNS"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يستخدم SNMPv3 بدل SNMP القديم عندما يكون الأمان مهماً؟", "options": {"A": "يوفر آليات أمنية أفضل", "B": "لأنه أسرع دائماً", "C": "لأنه يمنع Routing", "D": "لأنه يلغي IP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل وسيلة لإدارة Router عن بُعد في بيئة آمنة؟", "options": {"A": "Telnet من أي مكان", "B": "SSH مع Access Control", "C": "HTTP بدون TLS", "D": "FTP"}, "correct": "B", "difficulty": "medium"},
                    {"text": "مهاجم يستطيع توصيل جهازه بأي Port في Switch والوصول للشبكة. ما التحكم الذي يمكن أن يقلل الخطر؟", "options": {"A": "Port Security / NAC", "B": "DNS", "C": "NTP فقط", "D": "HTTP"}, "correct": "A", "difficulty": "hard"},
                    {"text": "موظف يستخدم حساباً إدارياً كامل الصلاحيات لكل المهام اليومية. ما المشكلة؟", "options": {"A": "Violation of Least Privilege", "B": "مشكلة MTU", "C": "مشكلة DNS", "D": "مشكلة VLAN"}, "correct": "A", "difficulty": "hard"},
                    {"text": "جهاز ضيف يحصل على IP صحيح لكنه يستطيع الوصول إلى Server VLAN. ما الذي يجب فحصه أولاً؟", "options": {"A": "Segmentation/ACL/Firewall policy", "B": "Browser", "C": "DNS TTL", "D": "CPU"}, "correct": "A", "difficulty": "hard"},
                    {"text": "تريد منع جهاز مصاب من استخدام عنوان IP لجهاز آخر عبر ARP spoofing. أي مجموعة مفاهيم مناسبة؟", "options": {"A": "DHCP Snooping + Dynamic ARP Inspection", "B": "DNS + HTTP", "C": "NAT + FTP", "D": "STP + SMTP"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 7
            # ==========================================
            {
                "stage_number": 7,
                "title": "7️⃣ إدارة الثغرات والبروتوكولات الآمنة والدفاع المتقدم",
                "description": "القدرة على اكتشاف نقاط الضعف والمخاطر في الشبكة، تأمين البروتوكولات والخدمات، وفهم الدفاع.",
                "objectives": [
                    "Vulnerability Management",
                    "CVE / CVSS concepts",
                    "Network Scanning / Nmap",
                    "Service Enumeration",
                    "Secure Protocols / TLS / PKI",
                    "Certificates / SSH Hardening",
                    "DNS Security / DoH/DoT concepts",
                    "DDoS / Rate Limiting",
                    "Network Attacks / Rogue Services",
                    "Patch Management / Configuration Auditing",
                    "Risk Prioritization"
                ],
                "practical_task": "أنشئ شبكة Lab مقصودة: شغّل خدمات داخلية، استخدم Nmap لاكتشاف Hosts، نفذ Service Enumeration، سجل الخدمات المفتوحة، صنفها (Required / Unnecessary / High Risk)، عطّل خدمة غير ضرورية، استبدل Telnet بـSSH، تحقق من TLS Certificate، أنشئ Vulnerability Report، ورتب المخاطر حسب Impact × Likelihood × Exposure.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices",
                "questions": [
                    {"text": "ما وظيفة Nmap الأساسية؟", "options": {"A": "Network discovery and scanning", "B": "Email encryption", "C": "Word processing", "D": "Backup"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ماذا يعني CVE؟", "options": {"A": "معرف قياسي لثغرة أمنية", "B": "نوع Firewall", "C": "بروتوكول VPN", "D": "DNS server"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الهدف من TLS؟", "options": {"A": "حماية الاتصال أثناء النقل", "B": "توزيع IP", "C": "إنشاء VLAN", "D": "إدارة Switch"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما المقصود بـAttack Surface؟", "options": {"A": "مجموعة نقاط التعرض التي يمكن مهاجمتها", "B": "سرعة الإنترنت", "C": "عدد المستخدمين فقط", "D": "مساحة القرص"}, "correct": "A", "difficulty": "easy"},
                    {"text": "لماذا يتم تعطيل الخدمات غير الضرورية؟", "options": {"A": "تقليل Attack Surface", "B": "زيادة Broadcast", "C": "زيادة Ports", "D": "منع DHCP"}, "correct": "A", "difficulty": "easy"},
                    {"text": "Nmap يظهر Port 23 مفتوحاً على جهاز. لماذا يستحق التحقيق؟", "options": {"A": "Telnet قد يكون غير آمن", "B": "لأنه DNS", "C": "لأنه HTTPS", "D": "لأنه DHCP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك ثغرة Critical على جهاز غير مكشوف للإنترنت لكنها تؤثر على Domain Controller. ما الأولوية؟", "options": {"A": "تجاهلها", "B": "تقييم Impact وExposure ثم معالجتها بسرعة", "C": "حذف DNS", "D": "تغيير MAC"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا لا يكفي CVSS وحده لاتخاذ قرار الإصلاح؟", "options": {"A": "لأن السياق والـExposure وBusiness Impact مهمون", "B": "لأنه لا يحتوي رقماً", "C": "لأنه خاص بـDNS", "D": "لأنه لا يقيس أي شيء"}, "correct": "A", "difficulty": "medium"},
                    {"text": "شهادة TLS غير صالحة. ما الخطر المحتمل؟", "options": {"A": "فقدان الثقة في هوية الطرف الآخر واحتمال MITM", "B": "زيادة DHCP", "C": "تغيير VLAN", "D": "زيادة MTU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل إجراء ضد خدمة غير مستخدمة؟", "options": {"A": "إبقاؤها مفتوحة", "B": "تعطيلها أو تقييد الوصول إليها", "C": "نشرها على الإنترنت", "D": "السماح لـAny"}, "correct": "B", "difficulty": "medium"},
                    {"text": "DDoS يستهدف Availability. ما التحكم الذي قد يساعد؟", "options": {"A": "DDoS protection/rate limiting/filtering", "B": "تغيير Username", "C": "DNS cache فقط", "D": "زيادة Ports"}, "correct": "A", "difficulty": "medium"},
                    {"text": "Scan يظهر 20 خدمة على Server لا يحتاج إلا 3. ما الاستنتاج الأمني الأفضل؟", "options": {"A": "Attack Surface أكبر من المطلوب", "B": "الجهاز آمن", "C": "DNS خاطئ", "D": "يجب فتح المزيد"}, "correct": "A", "difficulty": "hard"},
                    {"text": "جهاز يحتوي على خدمة قديمة عالية الخطورة لكنها مطلوبة للعمل. ما أفضل نهج؟", "options": {"A": "تجاهلها", "B": "تعويضها بـSegmentation + ACL + Monitoring + Patch Plan", "C": "نشرها للإنترنت", "D": "تعطيل Firewall"}, "correct": "B", "difficulty": "hard"},
                    {"text": "تريد اكتشاف خدمات غير متوقعة في شبكة كبيرة دون فحص كل شيء عشوائياً. ما النهج الأفضل؟", "options": {"A": "Asset inventory + controlled scanning", "B": "إيقاف الشبكة", "C": "حذف DNS", "D": "فتح كل Ports"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لديك ثغرة منخفضة CVSS على جهاز Public-facing وخطورة أعلى على جهاز داخلي حساس. كيف تقرر؟", "options": {"A": "تختار دائماً الأعلى CVSS فقط", "B": "تستخدم Risk Context الذي يجمع Severity وExposure وAsset Criticality", "C": "تختار الأقدم فقط", "D": "لا تصلح أي شيء"}, "correct": "B", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 8
            # ==========================================
            {
                "stage_number": 8,
                "title": "8️⃣ أمن شبكات السحابة والأتمتة والعمليات الإنتاجية",
                "description": "نقل مهارات Network Security إلى البيئات الحديثة Hybrid/Cloud، مع أساسيات Automation وMonitoring.",
                "objectives": [
                    "Cloud Networking",
                    "Azure Virtual Network / Subnets",
                    "NSG / Azure Firewall",
                    "VPN Gateway / Private Endpoints",
                    "Network Watcher / Hybrid Connectivity",
                    "Zero Trust / IAM basics",
                    "Logging / Monitoring",
                    "Python Networking Automation",
                    "REST APIs / Ansible concepts",
                    "Configuration Management / Git",
                    "Change Management / Backup / Rollback"
                ],
                "practical_task": "أنشئ تصميم Azure Security: Internet → Azure Firewall → DMZ/Web Subnet → Application Subnet → Private Database. أنشئ VNet وSubnets، طبّق NSGs، صمم Azure Firewall rules، امنع الوصول المباشر إلى Database، صمم VPN connectivity، فعّل Logging/Monitoring، اكتب Python script بسيطاً، استخدم Git لحفظ configuration/documentation، ووثق Architecture.",
                "youtube_ar": "https://learn.microsoft.com/ar-sa/training/",
                "youtube_en": "https://learn.microsoft.com/en-us/training/paths/implement-network-security-controls-azure/",
                "questions": [
                    {"text": "ما وظيفة Azure VNet؟", "options": {"A": "شبكة افتراضية للموارد", "B": "نظام ملفات", "C": "Email server", "D": "Antivirus فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة NSG؟", "options": {"A": "التحكم في Network Traffic", "B": "إنشاء User فقط", "C": "تشغيل Python", "D": "Backup"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما وظيفة Azure Firewall؟", "options": {"A": "Network traffic inspection/control", "B": "DNS registration فقط", "C": "Code compilation", "D": "File compression"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Git؟", "options": {"A": "Version Control", "B": "Packet Capture", "C": "DNS", "D": "VPN"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما فائدة Automation في Network Security؟", "options": {"A": "تقليل العمل اليدوي وتحسين الاتساق", "B": "إلغاء Security", "C": "فتح كل Ports", "D": "تعطيل Logging"}, "correct": "A", "difficulty": "easy"},
                    {"text": "تريد Database لا تملك Public IP. ما المبدأ المناسب؟", "options": {"A": "Private connectivity", "B": "Public exposure", "C": "Any/Any", "D": "Open FTP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "تريد منع Web subnet من الوصول إلى Management subnet. ما الأداة المناسبة؟", "options": {"A": "Network security controls/ACL/NSG/Firewall", "B": "DNS", "C": "NTP", "D": "DHCP"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب استخدام Git مع Network Configurations؟", "options": {"A": "Version history وChange tracking", "B": "زيادة MTU", "C": "منع ARP", "D": "تشفير VPN تلقائياً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما الخطر من تنفيذ Configuration يدوياً على 100 جهاز؟", "options": {"A": "Inconsistency and human error", "B": "زيادة DNS", "C": "تحسين الأمن تلقائياً", "D": "تقليل Attack Surface دائماً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ماذا يعني Hybrid Network؟", "options": {"A": "ربط بيئات On-Premises وCloud", "B": "شبكة بدون IP", "C": "شبكة Wi-Fi فقط", "D": "LAN فقط"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا نحتاج Logging في Cloud Network Security؟", "options": {"A": "Detection + Troubleshooting + Auditing", "B": "زيادة Bandwidth", "C": "حذف Routes", "D": "إلغاء Authentication"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك Azure Web VM public-facing وقاعدة بيانات تحتوي بيانات حساسة. أي تصميم أفضل؟", "options": {"A": "Public IP لكليهما", "B": "Web public + Database private + controlled traffic", "C": "Database public فقط", "D": "Allow Any"}, "correct": "B", "difficulty": "hard"},
                    {"text": "Automation script يطبق Firewall Rule خاطئة على 200 جهاز. ما أفضل ممارسة لتقليل الخطر؟", "options": {"A": "تنفيذها مباشرة دائماً", "B": "Test + Review + Versioning + Rollback", "C": "حذف Logs", "D": "تعطيل Git"}, "correct": "B", "difficulty": "hard"},
                    {"text": "لديك VPN بين On-Prem وAzure لكنه لا يصل إلى Subnet معينة. ما الذي تفحصه؟", "options": {"A": "Routing + NSG/Firewall + VPN configuration", "B": "Browser cache", "C": "Printer", "D": "Keyboard"}, "correct": "A", "difficulty": "hard"},
                    {"text": "لماذا تعتبر Private Endpoint مفيدة؟", "options": {"A": "تقلل الحاجة إلى Public Network Exposure لبعض الخدمات", "B": "تجعل كل شيء Public", "C": "تلغي Authentication", "D": "تمنع كل Routing"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 9
            # ==========================================
            {
                "stage_number": 9,
                "title": "9️⃣ المشاريع العملية لأمن الشبكات",
                "description": "دمج المهارات السابقة في مشاريع تشبه العمل الحقيقي لمهندس أمن شبكات، من Network Lab بسيط إلى Capstone متكامل.",
                "objectives": [
                    "Network Security Design",
                    "Firewall Engineering",
                    "Network Segmentation",
                    "VPN",
                    "IDS/IPS",
                    "Traffic Analysis",
                    "Vulnerability Assessment",
                    "Monitoring / Troubleshooting",
                    "Cloud Security / Automation",
                    "Documentation / Architecture / Incident Analysis"
                ],
                "practical_task": "نفذ 6 مشاريع: (1) Secure Small Office Network (2) Enterprise Segmented Network (3) Site-to-Site VPN (4) Network Monitoring & IDS (5) Network Vulnerability Assessment (6) Secure Cloud Network + Capstone: Enterprise Network Security Platform مع GitHub Repository كامل.",
                "youtube_ar": "https://it-sharks.com/ar/course/FortiGate-firewall-course7",
                "youtube_en": "https://training.fortinet.com/",
                "questions": [
                    {"text": "أول شيء يجب تحديده في مشروع Network Security حقيقي؟", "options": {"A": "Requirements and assets", "B": "Wallpaper", "C": "Username", "D": "Browser"}, "correct": "A", "difficulty": "easy"},
                    {"text": "أين يوضع Public Web Server عادة؟", "options": {"A": "Management", "B": "DMZ", "C": "Database", "D": "Admin PC"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الأداة المناسبة لتحليل PCAP؟", "options": {"A": "Wireshark", "B": "Excel فقط", "C": "Word", "D": "Git"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الأداة المناسبة لاكتشاف المنافذ؟", "options": {"A": "Nmap", "B": "Photoshop", "C": "DHCP", "D": "SSH فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن يحتويه README احترافي؟", "options": {"A": "Project purpose/setup/architecture/usage", "B": "Passwords", "C": "Private keys", "D": "Random screenshots فقط"}, "correct": "A", "difficulty": "easy"},
                    {"text": "مشروع VPN يعمل لكن Users لا يصلون إلى Remote LAN. ماذا تفحص؟", "options": {"A": "Routing + Policies + VPN selectors", "B": "Browser", "C": "Wallpaper", "D": "CPU"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن تكون Firewall Rules في المشروع موثقة؟", "options": {"A": "لتوضيح intent وتسهيل الإدارة والتدقيق", "B": "لتزيد Bandwidth", "C": "لتمنع DNS", "D": "لتلغي Logs"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك 50 Alerts من IDS. ما أول خطوة؟", "options": {"A": "تصنيف الأولوية والتحقق من السياق", "B": "حذف كل Alerts", "C": "إيقاف IDS", "D": "إعادة تشغيل الشبكة"}, "correct": "A", "difficulty": "medium"},
                    {"text": "اكتشفت خدمة غير ضرورية على Server. ماذا تفعل؟", "options": {"A": "تعطيلها أو تقييدها", "B": "نشرها للإنترنت", "C": "فتح جميع Ports", "D": "تجاهلها"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لماذا يجب أن يتضمن Capstone Troubleshooting؟", "options": {"A": "لأن العمل الحقيقي يتطلب تشخيص الأعطال", "B": "لأنه يضيف صفحات README", "C": "لأنه يلغي Security", "D": "لأنه ليس مهماً"}, "correct": "A", "difficulty": "medium"},
                    {"text": "ما أفضل دليل على أن Firewall Rule تعمل؟", "options": {"A": "اختبار Traffic فعلي + Logs", "B": "صورة للواجهة فقط", "C": "اسم Rule", "D": "كتابة أنها تعمل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "لديك Architecture ممتازة لكن Guest VLAN تستطيع الوصول إلى Database. ما المشكلة؟", "options": {"A": "Security policy implementation failure", "B": "README problem", "C": "DNS issue فقط", "D": "Git issue"}, "correct": "A", "difficulty": "hard"},
                    {"text": "IDS reports Port Scan لكن Nmap كان جزءاً من الاختبار المصرح. كيف توثق النتيجة؟", "options": {"A": "Malicious attack مؤكد", "B": "Authorized security testing / expected alert", "C": "Delete alert", "D": "Disable IDS"}, "correct": "B", "difficulty": "hard"},
                    {"text": "Capstone يعمل، لكن لا يوجد Version Control أو Documentation. هل هو Production-style؟", "options": {"A": "نعم بالكامل", "B": "لا، توجد فجوة Engineering/operational readiness", "C": "نعم لأن Firewall تعمل", "D": "نعم إذا كان Ping يعمل"}, "correct": "B", "difficulty": "hard"},
                    {"text": "تريد إثبات أن التغييرات الأمنية حسنت الشبكة. ما أفضل طريقة؟", "options": {"A": "Before/after tests + logs + measurable controls", "B": "Screenshot واحدة", "C": "رأي شخصي", "D": "حذف الاختبارات"}, "correct": "A", "difficulty": "hard"}
                ]
            },
            # ==========================================
            # المرحلة 10
            # ==========================================
            {
                "stage_number": 10,
                "title": "🔟 التحضير المهني وJob Ready",
                "description": "تحويل المهارات والمشاريع إلى جاهزية فعلية لوظيفة Junior Network Security Engineer.",
                "objectives": [
                    "Network Security CV",
                    "GitHub Portfolio",
                    "Technical Documentation",
                    "Architecture Presentation",
                    "Troubleshooting Interviews",
                    "Firewall Interviews / Networking Interviews",
                    "Security Scenarios / System Design Basics",
                    "Incident Scenarios / Change Management",
                    "Professional Communication",
                    "Job Applications / Technical Assessment"
                ],
                "practical_task": "نفذ Final Job Readiness Assessment: بيئة Network Lab (Router + Switch + Firewall + Linux Server + Windows Client + Web Server + DMZ + Monitoring)، ثم سيناريو: 'تم اكتشاف اتصال غير طبيعي من جهاز داخلي إلى Server خارجي، وبعض المستخدمين لا يستطيعون الوصول لخدمة داخلية'. المطلوب: Network Troubleshooting + Firewall Analysis + Traffic Analysis + IDS Alert + Vulnerability + Architecture + Hardening + Documentation.",
                "youtube_ar": "https://www.nist.gov/itl/applied-cybersecurity/nice",
                "youtube_en": "https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/resources/occupations-jobs-and-work",
                "questions": [
                    {"text": "ما الوظيفة الأقرب لهذا المسار؟", "options": {"A": "Junior Network Security Engineer", "B": "Database Administrator", "C": "Data Engineer", "D": "Graphic Designer"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أهم عنصر في Portfolio؟", "options": {"A": "عدد الأدوات", "B": "مشاريع موثقة تثبت المهارة", "C": "عدد الصور", "D": "Wallpaper"}, "correct": "B", "difficulty": "easy"},
                    {"text": "ما الذي يجب أن يوضحه Architecture Diagram؟", "options": {"A": "المكونات والزones وتدفق Traffic", "B": "اسم الموظفين", "C": "رواتب", "D": "هوايات الفريق"}, "correct": "A", "difficulty": "easy"},
                    {"text": "ما أول خطوة عند Troubleshooting مشكلة اتصال؟", "options": {"A": "تحديد النطاق والطبقة المتأثرة", "B": "حذف Firewall", "C": "إعادة تشغيل كل شيء", "D": "تغيير كلمات المرور"}, "correct": "A", "difficulty": "easy"},
                    {"text": "هل الشهادة وحدها تكفي لـJob Ready؟", "options": {"A": "نعم", "B": "لا", "C": "فقط Fortinet", "D": "فقط CCNA"}, "correct": "B", "difficulty": "easy"},
                    {"text": "في مقابلة سُئلت: 'كيف تبدأ تصميم شبكة آمنة؟' ما الإجابة الأفضل؟", "options": {"A": "أشغّل Firewall", "B": "أحدد Requirements وAssets ثم Security Zones ثم Policies", "C": "أفتح كل شيء", "D": "أبدأ بـVPN"}, "correct": "B", "difficulty": "medium"},
                    {"text": "كيف تشرح Firewall Rule لمدير غير تقني؟", "options": {"A": "تستخدم مصطلحات تقنية فقط", "B": "تشرح الفائدة الأمنية وBusiness Impact بلغة واضحة", "C": "تعطي رقم Policy فقط", "D": "تعرض Terminal"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لديك Rule تسمح كل شيء مؤقتاً. ماذا تفعل؟", "options": {"A": "تتركها", "B": "توثقها كمخاطرة وتُخطط لتقييدها حسب Least Privilege", "C": "تحذفها مباشرة", "D": "توسعها أكثر"}, "correct": "B", "difficulty": "medium"},
                    {"text": "لماذا يجب أن يحتوي Portfolio مشروع Cloud Network Security؟", "options": {"A": "لأن البيئات الحديثة Hybrid/Cloud", "B": "لأنه مطلوب دائماً", "C": "لأنه بديل للـNetworking", "D": "لأنه أسهل"}, "correct": "A", "difficulty": "medium"},
                    {"text": "سأل interviewer: 'لماذا FortiGate وليس Cisco؟'", "options": {"A": "لأن Cisco غير آمن", "B": "لأن المفاهيم Network Security تنقل بين المنتجات، وFortiGate يمثل بيئة عملية شائعة", "C": "لأن FortiGate أسرع", "D": "لأن Cisco يمنع VPN"}, "correct": "B", "difficulty": "medium"},
                    {"text": "ما أفضل طريقة للإجابة عن سؤال لم تعرفه؟", "options": {"A": "اختراع إجابة", "B": "توضيح ما تعرفه ثم شرح كيف ستبحث وتتحقق", "C": "تغيير الموضوع", "D": "استخدام AI دون تفكير"}, "correct": "B", "difficulty": "medium"},
                    {"text": "في Final Assessment اكتشفت مخاطرة خارج Scope. ماذا تفعل؟", "options": {"A": "تختبرها", "B": "لا تختبرها وتوثق الملاحظة للإدارة", "C": "تنشرها", "D": "تتجاهلها"}, "correct": "B", "difficulty": "hard"},
                    {"text": "Final Assessment نجح في Technical لكنه فشل في Documentation. هل تعلن Job Ready؟", "options": {"A": "نعم", "B": "لا؛ Documentation والتواصل جزء من المهنة", "C": "نعم إذا استخدم FortiGate", "D": "نعم إذا كان Ping يعمل"}, "correct": "B", "difficulty": "hard"},
                    {"text": "مشروعك يثبت Networking فقط، بينما الوظيفة تتطلب Firewall + Cloud + Automation. ما المشكلة؟", "options": {"A": "يجب أن تغطي Portfolio المهارات الأساسية المطلوبة للدور", "B": "Networking يكفي دائماً", "C": "Cloud غير مهم", "D": "Firewall غير مهم"}, "correct": "A", "difficulty": "hard"},
                    {"text": "ما أقوى مؤشر على Strong Junior Network Security Engineer؟", "options": {"A": "حفظ 100 Command", "B": "معرفة أسماء أدوات كثيرة", "C": "القدرة على تصميم وتشغيل وتشخيص وتوثيق شبكة آمنة بمستوى عملي", "D": "امتلاك أكبر عدد شهادات"}, "correct": "C", "difficulty": "hard"}
                ]
            }
        ]
    }
]
