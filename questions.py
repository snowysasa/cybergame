import json

questions = [
    {
        "question": "What is the primary goal of a phishing attack?",
        "options": ["To steal sensitive information", "To infect with malware", "To take down a website"],
        "answer": "To steal sensitive information"
    },
    {
        "question": "What does HTTPS stand for?",
        "options": ["Hyper Transfer Text Service", "Hypertext Transfer Protocol Secure", "Highly Tracked Payment System"],
        "answer": "Hypertext Transfer Protocol Secure"
    },
    {
        "question": "Which of the following is a strong password?",
        "options": ["password123", "Pa$$w0rd!2023", "123456"],
        "answer": "Pa$$w0rd!2023"
    },
    {
        "question": "What is the purpose of a firewall?",
        "options": ["To block incoming traffic", "To allow outgoing traffic", "To scan for malware"],
        "answer": "To block incoming traffic"
    },
    {
        "question": "What is the difference between a virus and a worm?",
        "options": ["A virus requires user interaction, while a worm does not", "A worm requires user interaction, while a virus does not", "A virus is a type of worm"],
        "answer": "A virus requires user interaction, while a worm does not"
    },
    # More questions
    {
        "question": "What is a common sign of a phishing email?",
        "options": ["Personalized greetings", "Generic greetings", "Correct grammar"],
        "answer": "Generic greetings"
    },
    {
        "question": "What is the function of two-factor authentication?",
        "options": ["To provide an additional layer of security", "To replace passwords", "To encrypt data"],
        "answer": "To provide an additional layer of security"
    },
    {
        "question": "Which of the following is a social engineering attack?",
        "options": ["Malware installation", "Pretexting", "SQL Injection"],
        "answer": "Pretexting"
    },
    {
        "question": "What does VPN stand for?",
        "options": ["Virtual Private Network", "Virtual Public Network", "Very Protected Network"],
        "answer": "Virtual Private Network"
    },
    {
        "question": "Which of the following is NOT a characteristic of a strong password?",
        "options": ["At least 12 characters", "Contains both upper and lower case letters", "Uses easily guessable words"],
        "answer": "Uses easily guessable words"
    },
    {
        "question": "What is ransomware?",
        "options": ["Malware that encrypts files and demands payment", "Software to block viruses", "A type of phishing attack"],
        "answer": "Malware that encrypts files and demands payment"
    },
    {
        "question": "What is the purpose of encryption?",
        "options": ["To make data unreadable without a key", "To speed up data transmission", "To store data in the cloud"],
        "answer": "To make data unreadable without a key"
    },
    {
        "question": "What is the main risk of using public Wi-Fi?",
        "options": ["Slow connection speeds", "Data interception by attackers", "Limited access to websites"],
        "answer": "Data interception by attackers"
    },
    {
        "question": "What is an example of malware?",
        "options": ["Antivirus software", "Web browser", "Trojan horse"],
        "answer": "Trojan horse"
    },
    {
        "question": "What should you do if you receive an email from an unknown sender?",
        "options": ["Open the email immediately", "Delete the email without opening", "Respond to the email"],
        "answer": "Delete the email without opening"
    },
    {
        "question": "What does phishing involve?",
        "options": ["Sending fraudulent emails", "Creating strong passwords", "Using secure websites"],
        "answer": "Sending fraudulent emails"
    },
    {
        "question": "What is a brute force attack?",
        "options": ["A method to guess passwords by trying many combinations", "An attack that uses social engineering", "A type of malware"],
        "answer": "A method to guess passwords by trying many combinations"
    },
    {
        "question": "What is the purpose of antivirus software?",
        "options": ["To protect against malware", "To improve internet speed", "To create backups"],
        "answer": "To protect against malware"
    },
    {
        "question": "What is data encryption?",
        "options": ["The process of converting data into a code", "A method of speeding up data transfer", "A way to store data on the cloud"],
        "answer": "The process of converting data into a code"
    },
    {
        "question": "What is social engineering?",
        "options": ["Manipulating people into divulging confidential information", "Creating software vulnerabilities", "Developing strong passwords"],
        "answer": "Manipulating people into divulging confidential information"
    },
    {
        "question": "What is the primary purpose of a VPN?",
        "options": ["To encrypt internet traffic", "To increase download speed", "To allow access to blocked websites"],
        "answer": "To encrypt internet traffic"
    },
    {
        "question": "What is a zero-day exploit?",
        "options": ["An attack that occurs before a vulnerability is known", "A type of phishing attack", "A form of ransomware"],
        "answer": "An attack that occurs before a vulnerability is known"
    },
    {
        "question": "What does the term 'malware' encompass?",
        "options": ["All types of malicious software", "Only viruses", "Only spyware"],
        "answer": "All types of malicious software"
    },
    {
        "question": "Which of the following is a common method of data breach?",
        "options": ["Weak passwords", "Strong encryption", "Regular software updates"],
        "answer": "Weak passwords"
    },
    {
        "question": "What is phishing?",
        "options": ["An attempt to steal sensitive information", "A type of firewall", "A method to encrypt data"],
        "answer": "An attempt to steal sensitive information"
    },
    {
        "question": "What is the best way to protect your online accounts?",
        "options": ["Use the same password for all accounts", "Use a password manager and unique passwords", "Avoid using any passwords"],
        "answer": "Use a password manager and unique passwords"
    },
    {
        "question": "What is the function of a security patch?",
        "options": ["To fix vulnerabilities in software", "To improve internet speed", "To add new features"],
        "answer": "To fix vulnerabilities in software"
    },
    {
        "question": "What is the main purpose of firewalls?",
        "options": ["To block unauthorized access", "To speed up internet connections", "To store data securely"],
        "answer": "To block unauthorized access"
    },
    {
        "question": "What is a strong password composed of?",
        "options": ["Only letters", "Letters, numbers, and symbols", "Only numbers"],
        "answer": "Letters, numbers, and symbols"
    },
    {
        "question": "What is the first step in responding to a data breach?",
        "options": ["Notify affected individuals", "Assess the damage", "Determine the cause"],
        "answer": "Determine the cause"
    },
    {
        "question": "Which of the following is NOT a type of malware?",
        "options": ["Trojan", "Worm", "Firewall"],
        "answer": "Firewall"
    },
    {
        "question": "What is the purpose of a password manager?",
        "options": ["To store passwords securely", "To generate random passwords", "Both of the above"],
        "answer": "Both of the above"
    },
    {
        "question": "What does the term 'hacking' refer to?",
        "options": ["Gaining unauthorized access to systems", "Improving system security", "Creating software"],
        "answer": "Gaining unauthorized access to systems"
    },
    {
        "question": "What is identity theft?",
        "options": ["Stealing someone's personal information to impersonate them", "Creating a false identity online", "Hacking into someone's bank account"],
        "answer": "Stealing someone's personal information to impersonate them"
    },
    {
        "question": "What does 'DDoS' stand for?",
        "options": ["Distributed Denial of Service", "Direct Denial of Service", "Dynamic Denial of Service"],
        "answer": "Distributed Denial of Service"
    },
    {
        "question": "What is the purpose of security awareness training?",
        "options": ["To teach employees about security threats", "To improve company productivity", "To create a strong password policy"],
        "answer": "To teach employees about security threats"
    },
    {
        "question": "What should you do if you suspect a data breach?",
        "options": ["Ignore it", "Report it to the IT department", "Post about it on social media"],
        "answer": "Report it to the IT department"
    },
    {
        "question": "What is a common tactic used in social engineering attacks?",
        "options": ["Using technical jargon", "Creating a sense of urgency", "Providing detailed information"],
        "answer": "Creating a sense of urgency"
    },
    {
        "question": "What does the acronym 'SQL' stand for?",
        "options": ["Structured Query Language", "Simple Query Language", "Sequential Query Language"],
        "answer": "Structured Query Language"
    },
    {
        "question": "What is a common method of protecting sensitive data?",
        "options": ["Storing it in plain text", "Using encryption", "Sharing it with everyone"],
        "answer": "Using encryption"
    },
    {
        "question": "What is a 'man-in-the-middle' attack?",
        "options": ["Interception of communication between two parties", "A phishing attack", "A type of virus"],
        "answer": "Interception of communication between two parties"
    },
    {
        "question": "What is spear phishing?",
        "options": ["A targeted phishing attack", "A general phishing attack", "A form of malware"],
        "answer": "A targeted phishing attack"
    },
    {
        "question": "What is the purpose of a security policy?",
        "options": ["To outline security procedures and responsibilities", "To enhance productivity", "To increase profits"],
        "answer": "To outline security procedures and responsibilities"
    },
    {
        "question": "What is the role of encryption in data protection?",
        "options": ["To make data unreadable to unauthorized users", "To speed up data transfer", "To improve system performance"],
        "answer": "To make data unreadable to unauthorized users"
    },
    {
        "question": "What should you do before clicking on a link in an email?",
        "options": ["Check the URL carefully", "Click immediately", "Delete the email"],
        "answer": "Check the URL carefully"
    },
    {
        "question": "What is the purpose of a security audit?",
        "options": ["To assess an organization's security posture", "To improve employee productivity", "To increase revenue"],
        "answer": "To assess an organization's security posture"
    },
    {
        "question": "What is the most effective way to prevent malware infections?",
        "options": ["Avoid downloading software", "Use antivirus software and keep it updated", "Disable firewalls"],
        "answer": "Use antivirus software and keep it updated"
    },
    {
        "question": "What is the role of a security analyst?",
        "options": ["To monitor and protect an organization's networks", "To develop software", "To manage databases"],
        "answer": "To monitor and protect an organization's networks"
    },
    {
        "question": "What does 'zero trust' mean in cybersecurity?",
        "options": ["Trust no one by default", "Trust all users within a network", "Trust based on user reputation"],
        "answer": "Trust no one by default"
    },
    {
        "question": "What is a keylogger?",
        "options": ["A type of malware that records keystrokes", "A method to encrypt data", "A firewall feature"],
        "answer": "A type of malware that records keystrokes"
    },
    {
        "question": "What does GDPR stand for?",
        "options": ["General Data Protection Regulation", "Global Data Privacy Regulation", "General Data Privacy Rules"],
        "answer": "General Data Protection Regulation"
    },
    {
        "question": "What is a security token?",
        "options": ["A physical or digital device used to gain access", "A type of password", "An encryption method"],
        "answer": "A physical or digital device used to gain access"
    },
    {
        "question": "What is the main goal of penetration testing?",
        "options": ["To find and exploit vulnerabilities", "To create software", "To train employees"],
        "answer": "To find and exploit vulnerabilities"
    },
    {
        "question": "What is phishing email designed to do?",
        "options": ["Trick the recipient into revealing personal information", "Provide helpful information", "Offer a product"],
        "answer": "Trick the recipient into revealing personal information"
    },
    {
        "question": "What does the term 'patch management' refer to?",
        "options": ["The process of updating software to fix vulnerabilities", "The process of securing a network", "The process of training employees"],
        "answer": "The process of updating software to fix vulnerabilities"
    },
    {
        "question": "What is the main purpose of cybersecurity?",
        "options": ["To protect systems and data from cyber threats", "To improve internet speed", "To increase profits"],
        "answer": "To protect systems and data from cyber threats"
    },
    {
        "question": "What is a common characteristic of a successful phishing attempt?",
        "options": ["Professional appearance and urgent tone", "Spelling errors", "Generic greetings"],
        "answer": "Professional appearance and urgent tone"
    },
    {
        "question": "What is a firewall?",
        "options": ["A security device that monitors and controls incoming and outgoing network traffic", "A type of malware", "A data storage solution"],
        "answer": "A security device that monitors and controls incoming and outgoing network traffic"
    },
    {
        "question": "What should you do if your password has been compromised?",
        "options": ["Change it immediately", "Ignore it", "Use the same password for all accounts"],
        "answer": "Change it immediately"
    },
    {
        "question": "What is a security breach?",
        "options": ["An incident where unauthorized access occurs", "A method to protect data", "A type of password"],
        "answer": "An incident where unauthorized access occurs"
    },
    {
        "question": "What is the role of encryption in communication?",
        "options": ["To secure data during transmission", "To speed up data transfer", "To create backups"],
        "answer": "To secure data during transmission"
    },
    {
        "question": "What is a common way to mitigate the risk of phishing attacks?",
        "options": ["Training employees to recognize phishing attempts", "Ignoring suspicious emails", "Using the same password for all accounts"],
        "answer": "Training employees to recognize phishing attempts"
    },
    {
        "question": "What is the purpose of a data backup?",
        "options": ["To protect against data loss", "To improve system performance", "To speed up internet access"],
        "answer": "To protect against data loss"
    },
    {
        "question": "What does 'malware' include?",
        "options": ["Viruses, worms, and Trojan horses", "Only viruses", "Only ransomware"],
        "answer": "Viruses, worms, and Trojan horses"
    },
    {
        "question": "What is an 'exploit'?",
        "options": ["A piece of software that takes advantage of a vulnerability", "A type of password", "An encryption method"],
        "answer": "A piece of software that takes advantage of a vulnerability"
    },
    {
        "question": "What is a 'denial of service' attack?",
        "options": ["An attempt to make a service unavailable", "A type of malware", "A security protocol"],
        "answer": "An attempt to make a service unavailable"
    },
    {
        "question": "What is the best practice for handling sensitive data?",
        "options": ["Store it unencrypted", "Use encryption and access controls", "Share it with everyone"],
        "answer": "Use encryption and access controls"
    },
    {
        "question": "What is a common sign of malware infection?",
        "options": ["Slow computer performance", "Fast internet speed", "Increased storage space"],
        "answer": "Slow computer performance"
    },
    {
        "question": "What does the term 'social engineering' refer to?",
        "options": ["Manipulating people to gain confidential information", "Creating software vulnerabilities", "Encrypting data"],
        "answer": "Manipulating people to gain confidential information"
    },
    {
        "question": "What is the purpose of security logging?",
        "options": ["To monitor system activity and detect anomalies", "To speed up system performance", "To store data securely"],
        "answer": "To monitor system activity and detect anomalies"
    },
    {
        "question": "What is a key difference between a virus and a worm?",
        "options": ["A virus requires user interaction; a worm does not", "Both require user interaction", "A worm is more dangerous"],
        "answer": "A virus requires user interaction; a worm does not"
    },
    {
        "question": "What should you do with outdated software?",
        "options": ["Keep it as it is", "Uninstall it and update to the latest version", "Use it for sensitive tasks"],
        "answer": "Uninstall it and update to the latest version"
    },
    {
        "question": "What does 'data breach' mean?",
        "options": ["Unauthorized access to sensitive data", "A type of virus", "A method of encryption"],
        "answer": "Unauthorized access to sensitive data"
    },
    {
        "question": "What is a strong security measure for online accounts?",
        "options": ["Two-factor authentication", "Using the same password for all accounts", "Ignoring security updates"],
        "answer": "Two-factor authentication"
    },
    {
        "question": "What is a common use for cryptography?",
        "options": ["Securing communication", "Storing passwords", "Improving internet speed"],
        "answer": "Securing communication"
    },
    {
        "question": "What should you do if you suspect a phishing attempt?",
        "options": ["Report it to your IT department", "Click the link to verify", "Ignore it"],
        "answer": "Report it to your IT department"
    },
    {
        "question": "What is a rootkit?",
        "options": ["A type of malware designed to gain unauthorized access", "A security protocol", "A method of encryption"],
        "answer": "A type of malware designed to gain unauthorized access"
    },
    {
        "question": "What is an example of a strong password?",
        "options": ["A combination of letters, numbers, and symbols", "Your name", "123456"],
        "answer": "A combination of letters, numbers, and symbols"
    },
    {
        "question": "What is a common sign of a phishing website?",
        "options": ["URL that does not match the legitimate website", "Professional design", "SSL certificate"],
        "answer": "URL that does not match the legitimate website"
    },
    {
        "question": "What is an advanced persistent threat (APT)?",
        "options": ["A prolonged cyber attack that targets a specific entity", "A type of firewall", "A malware type"],
        "answer": "A prolonged cyber attack that targets a specific entity"
    },
    {
        "question": "What is a common consequence of a data breach?",
        "options": ["Loss of customer trust", "Increased sales", "Improved security"],
        "answer": "Loss of customer trust"
    },
    {
        "question": "What is a common method for securing Wi-Fi networks?",
        "options": ["Using a strong password and WPA3 encryption", "Leaving it open", "Using WEP encryption"],
        "answer": "Using a strong password and WPA3 encryption"
    },
    {
        "question": "What is ransomware?",
        "options": ["Malware that encrypts files and demands a ransom for access", "A type of phishing", "A form of software update"],
        "answer": "Malware that encrypts files and demands a ransom for access"
    },
    {
        "question": "What is a cybersecurity framework?",
        "options": ["A structured approach to managing cybersecurity risks", "A type of software", "An antivirus program"],
        "answer": "A structured approach to managing cybersecurity risks"
    },
    {
        "question": "What is the main purpose of incident response planning?",
        "options": ["To prepare for and respond to security incidents", "To improve marketing strategies", "To enhance product development"],
        "answer": "To prepare for and respond to security incidents"
    },
    {
        "question": "What is the role of a chief information security officer (CISO)?",
        "options": ["To oversee an organization's cybersecurity strategy", "To manage financial risks", "To handle marketing"],
        "answer": "To oversee an organization's cybersecurity strategy"
    },
    {
        "question": "What is the first step in creating a security awareness program?",
        "options": ["Assessing current security posture", "Developing training materials", "Launching the program"],
        "answer": "Assessing current security posture"
    },
    {
        "question": "What does 'two-factor authentication' involve?",
        "options": ["Using two forms of verification before granting access", "Using the same password twice", "Using one form of verification"],
        "answer": "Using two forms of verification before granting access"
    },
    {
        "question": "What is a common way to protect sensitive information on a mobile device?",
        "options": ["Using encryption and strong passwords", "Leaving it unlocked", "Sharing it with everyone"],
        "answer": "Using encryption and strong passwords"
    },
    {
        "question": "What does the term 'cybersecurity posture' refer to?",
        "options": ["The overall security status of an organization's systems", "The physical security of a building", "The internet speed"],
        "answer": "The overall security status of an organization's systems"
    },
    {
        "question": "What is a common sign of an online scam?",
        "options": ["Too-good-to-be-true offers", "Discounted prices", "Urgent messages"],
        "answer": "Too-good-to-be-true offers"
    },
    {
        "question": "What is the purpose of a vulnerability assessment?",
        "options": ["To identify and evaluate security weaknesses", "To improve employee productivity", "To increase sales"],
        "answer": "To identify and evaluate security weaknesses"
    },
    {
        "question": "What is the main benefit of regular security training for employees?",
        "options": ["Increased awareness of cybersecurity threats", "Better communication", "Improved sales"],
        "answer": "Increased awareness of cybersecurity threats"
    },
    {
        "question": "What is a honeypot in cybersecurity?",
        "options": ["A decoy system used to attract and analyze attacks", "A type of malware", "A security protocol"],
        "answer": "A decoy system used to attract and analyze attacks"
    },
    {
        "question": "What is the purpose of incident reporting?",
        "options": ["To document and analyze security incidents", "To improve customer service", "To speed up system performance"],
        "answer": "To document and analyze security incidents"
    },
    {
        "question": "What does the term 'risk assessment' mean?",
        "options": ["Evaluating the potential risks to an organization's assets", "Improving employee productivity", "Enhancing customer satisfaction"],
        "answer": "Evaluating the potential risks to an organization's assets"
    },
    {
        "question": "What is a common security practice for passwords?",
        "options": ["Using complex passwords and changing them regularly", "Using the same password for everything", "Ignoring password policies"],
        "answer": "Using complex passwords and changing them regularly"
    },
    {
        "question": "What is the role of a penetration tester?",
        "options": ["To simulate attacks to identify vulnerabilities", "To develop software", "To manage databases"],
        "answer": "To simulate attacks to identify vulnerabilities"
    },
    {
        "question": "What is a common characteristic of a secure network?",
        "options": ["Properly configured firewalls and access controls", "Open access for everyone", "No encryption"],
        "answer": "Properly configured firewalls and access controls"
    },
    {
        "question": "What is an example of a DDoS attack?",
        "options": ["Overwhelming a server with traffic to disrupt services", "A type of encryption", "A phishing attempt"],
        "answer": "Overwhelming a server with traffic to disrupt services"
    },
    {
        "question": "What is a common reason for insider threats?",
        "options": ["Disgruntled employees or lack of awareness", "Employee promotions", "Positive company culture"],
        "answer": "Disgruntled employees or lack of awareness"
    },
    {
        "question": "What is the purpose of a security incident response team?",
        "options": ["To manage and respond to security incidents", "To handle customer complaints", "To improve sales"],
        "answer": "To manage and respond to security incidents"
    },
    {
        "question": "What is an example of a security policy?",
        "options": ["Acceptable use policy for technology resources", "A marketing strategy", "An employee handbook"],
        "answer": "Acceptable use policy for technology resources"
    },
    {
        "question": "What is the role of threat intelligence?",
        "options": ["To provide information about potential threats", "To develop software", "To manage databases"],
        "answer": "To provide information about potential threats"
    },
    {
        "question": "What is a common type of cyber attack?",
        "options": ["Phishing", "Positive reinforcement", "Employee training"],
        "answer": "Phishing"
    },
    {
        "question": "What does the term 'business continuity planning' refer to?",
        "options": ["Preparing for potential disruptions to operations", "Improving employee productivity", "Enhancing customer service"],
        "answer": "Preparing for potential disruptions to operations"
    },
    {
        "question": "What is a common strategy for responding to a data breach?",
        "options": ["Notifying affected individuals", "Ignoring it", "Hiding the breach"],
        "answer": "Notifying affected individuals"
    },
    {
        "question": "What is a common security measure for email?",
        "options": ["Using email filters and anti-spam measures", "Leaving the inbox open", "Ignoring phishing attempts"],
        "answer": "Using email filters and anti-spam measures"
    },
    {
        "question": "What is the role of a security champion?",
        "options": ["To advocate for security best practices within an organization", "To handle marketing", "To manage financial risks"],
        "answer": "To advocate for security best practices within an organization"
    },
    {
        "question": "What is the purpose of data loss prevention (DLP)?",
        "options": ["To protect sensitive data from unauthorized access and loss", "To speed up internet access", "To improve employee productivity"],
        "answer": "To protect sensitive data from unauthorized access and loss"
    },
    {
        "question": "What is a common characteristic of secure coding practices?",
        "options": ["Input validation and error handling", "Ignoring user input", "Hardcoding passwords"],
        "answer": "Input validation and error handling"
    },
    {
        "question": "What is a common reason for using a virtual private network (VPN)?",
        "options": ["To secure internet connections", "To speed up browsing", "To download files faster"],
        "answer": "To secure internet connections"
    },
    {
        "question": "What is the role of encryption in cybersecurity?",
        "options": ["To protect data by converting it into a secure format", "To make data accessible to everyone", "To improve internet speed"],
        "answer": "To protect data by converting it into a secure format"
    },
    {
        "question": "What is a common method for protecting against malware?",
        "options": ["Using antivirus software and regular updates", "Downloading unknown files", "Ignoring security alerts"],
        "answer": "Using antivirus software and regular updates"
    },
    {
        "question": "What is the purpose of a risk management strategy?",
        "options": ["To identify, assess, and mitigate risks", "To improve employee productivity", "To enhance marketing efforts"],
        "answer": "To identify, assess, and mitigate risks"
    },
    {
        "question": "What is the role of a security auditor?",
        "options": ["To evaluate an organization's security practices", "To develop software", "To manage customer relations"],
        "answer": "To evaluate an organization's security practices"
    },
    {
        "question": "What is a common sign of social engineering?",
        "options": ["Unusual requests for sensitive information", "Regular security training", "Strong passwords"],
        "answer": "Unusual requests for sensitive information"
    },
    {
        "question": "What is a key benefit of cybersecurity insurance?",
        "options": ["Financial protection against cyber threats", "Improved customer service", "Increased sales"],
        "answer": "Financial protection against cyber threats"
    },
    {
        "question": "What is the purpose of a firewall?",
        "options": ["To block unauthorized access to or from a private network", "To speed up internet access", "To improve employee productivity"],
        "answer": "To block unauthorized access to or from a private network"
    },
    {
        "question": "What does the term 'phishing' refer to?",
        "options": ["Fraudulent attempts to obtain sensitive information", "A type of coding", "An antivirus program"],
        "answer": "Fraudulent attempts to obtain sensitive information"
    },
    {
        "question": "What is the main goal of cybersecurity training for employees?",
        "options": ["To reduce human error and enhance awareness of threats", "To improve sales", "To increase customer satisfaction"],
        "answer": "To reduce human error and enhance awareness of threats"
    },
    {
        "question": "What is a common type of threat to mobile devices?",
        "options": ["Malware", "High battery usage", "Slow internet speed"],
        "answer": "Malware"
    },
    {
        "question": "What is the purpose of an information security policy?",
        "options": ["To outline an organization's security expectations and requirements", "To improve employee performance", "To enhance customer satisfaction"],
        "answer": "To outline an organization's security expectations and requirements"
    },
    {
        "question": "What is the significance of cybersecurity awareness campaigns?",
        "options": ["To educate employees about threats and safe practices", "To improve marketing strategies", "To increase sales"],
        "answer": "To educate employees about threats and safe practices"
    },
    {
        "question": "What is a common consequence of poor security practices?",
        "options": ["Increased risk of data breaches", "Higher employee morale", "Improved customer satisfaction"],
        "answer": "Increased risk of data breaches"
    },
    {
        "question": "What is the role of an incident response plan?",
        "options": ["To provide a structured approach to managing security incidents", "To improve sales", "To enhance employee productivity"],
        "answer": "To provide a structured approach to managing security incidents"
    },
    {
        "question": "What is a common mistake during a security incident?",
        "options": ["Failing to communicate effectively", "Improving communication", "Ignoring the issue"],
        "answer": "Failing to communicate effectively"
    },
    {
        "question": "What is the purpose of a penetration test?",
        "options": ["To identify vulnerabilities by simulating an attack", "To improve software design", "To manage customer relations"],
        "answer": "To identify vulnerabilities by simulating an attack"
    },
    {
        "question": "What is the role of a security operations center (SOC)?",
        "options": ["To monitor and respond to security incidents", "To handle customer service", "To develop software"],
        "answer": "To monitor and respond to security incidents"
    },
    {
        "question": "What is a common consequence of a successful cyber attack?",
        "options": ["Data loss or theft", "Increased profits", "Improved reputation"],
        "answer": "Data loss or theft"
    },
    {
        "question": "What is a common approach to securing web applications?",
        "options": ["Implementing security measures such as input validation", "Ignoring security flaws", "Using outdated software"],
        "answer": "Implementing security measures such as input validation"
    },
    {
        "question": "What does the term 'zero-day vulnerability' refer to?",
        "options": ["A security flaw that is unknown to the vendor", "A type of software", "A marketing strategy"],
        "answer": "A security flaw that is unknown to the vendor"
    },
    {
        "question": "What is the purpose of cybersecurity audits?",
        "options": ["To evaluate an organization's security posture and compliance", "To improve sales", "To enhance customer service"],
        "answer": "To evaluate an organization's security posture and compliance"
    },
    {
        "question": "What is a common characteristic of secure websites?",
        "options": ["HTTPS protocol", "HTTP protocol", "No security measures"],
        "answer": "HTTPS protocol"
    },
    {
        "question": "What is the significance of software updates?",
        "options": ["To patch vulnerabilities and improve security", "To slow down devices", "To complicate user experience"],
        "answer": "To patch vulnerabilities and improve security"
    },
    {
        "question": "What is a common sign of a compromised account?",
        "options": ["Unusual login locations or activities", "Regular logins", "Consistent activity"],
        "answer": "Unusual login locations or activities"
    },
    {
        "question": "What is the role of a chief technology officer (CTO) in cybersecurity?",
        "options": ["To oversee technology and security strategies", "To handle customer complaints", "To manage financial risks"],
        "answer": "To oversee technology and security strategies"
    },
    {
        "question": "What is the importance of security patches?",
        "options": ["To fix vulnerabilities in software", "To improve aesthetics", "To reduce functionality"],
        "answer": "To fix vulnerabilities in software"
    },
    {
        "question": "What is a common feature of identity theft protection services?",
        "options": ["Monitoring personal information for unauthorized use", "Ignoring user data", "High fees"],
        "answer": "Monitoring personal information for unauthorized use"
    },
    {
        "question": "What is the purpose of a security awareness training program?",
        "options": ["To educate employees on recognizing and responding to threats", "To improve sales", "To enhance product quality"],
        "answer": "To educate employees on recognizing and responding to threats"
    },
    {
        "question": "What is a common characteristic of a secure network?",
        "options": ["Strong access controls and encryption", "Open access for everyone", "Ignoring security alerts"],
        "answer": "Strong access controls and encryption"
    },
    {
        "question": "What is the significance of cybersecurity insurance?",
        "options": ["Financial protection against cyber incidents", "Increased sales", "Improved employee morale"],
        "answer": "Financial protection against cyber incidents"
    },
    {
        "question": "What is the primary purpose of a security policy?",
        "options": ["To set guidelines for maintaining security", "To improve marketing", "To enhance product features"],
        "answer": "To set guidelines for maintaining security"
    },
    {
        "question": "What is a common sign of malware infection?",
        "options": ["Slow performance or unexpected behavior", "Faster loading times", "Improved battery life"],
        "answer": "Slow performance or unexpected behavior"
    },
    {
        "question": "What is the role of security monitoring?",
        "options": ["To detect and respond to security incidents", "To increase internet speed", "To improve user experience"],
        "answer": "To detect and respond to security incidents"
    },
    {
        "question": "What is the significance of physical security in cybersecurity?",
        "options": ["To protect against unauthorized physical access to systems", "To improve employee morale", "To enhance marketing strategies"],
        "answer": "To protect against unauthorized physical access to systems"
    },
    {
        "question": "What is the purpose of digital forensics?",
        "options": ["To investigate and analyze cyber incidents", "To improve software performance", "To develop new technologies"],
        "answer": "To investigate and analyze cyber incidents"
    },
    {
        "question": "What is a common strategy for responding to a cyber attack?",
        "options": ["Implementing an incident response plan", "Ignoring the attack", "Downplaying its significance"],
        "answer": "Implementing an incident response plan"
    },
    {
        "question": "What is the role of a security engineer?",
        "options": ["To design and implement security systems", "To handle customer service", "To improve marketing"],
        "answer": "To design and implement security systems"
    },
    {
        "question": "What is a common feature of secure passwords?",
        "options": ["A mix of letters, numbers, and symbols", "Only lowercase letters", "Only numbers"],
        "answer": "A mix of letters, numbers, and symbols"
    },
    {
        "question": "What is the importance of multi-factor authentication?",
        "options": ["To add an extra layer of security", "To simplify the login process", "To reduce the number of passwords"],
        "answer": "To add an extra layer of security"
    },
    {
        "question": "What is the purpose of data loss prevention (DLP)?",
        "options": ["To prevent unauthorized access and data leaks", "To improve software performance", "To increase sales"],
        "answer": "To prevent unauthorized access and data leaks"
    },
    {
        "question": "What is a common sign of a phishing attempt?",
        "options": ["Suspicious emails with links or attachments", "Clear communication", "Regular updates"],
        "answer": "Suspicious emails with links or attachments"
    },
    {
        "question": "What is the role of a cybersecurity analyst?",
        "options": ["To monitor and protect an organization's networks", "To handle marketing", "To develop software"],
        "answer": "To monitor and protect an organization's networks"
    },
    {
        "question": "What is the significance of user access controls?",
        "options": ["To restrict access to sensitive information", "To improve user experience", "To increase sales"],
        "answer": "To restrict access to sensitive information"
    },
    {
        "question": "What is a common approach to securing sensitive data?",
        "options": ["Data encryption", "Ignoring data", "Keeping data publicly accessible"],
        "answer": "Data encryption"
    },
    {
        "question": "What is the purpose of network segmentation?",
        "options": ["To isolate different parts of a network for security", "To increase internet speed", "To enhance marketing efforts"],
        "answer": "To isolate different parts of a network for security"
    },
    {
        "question": "What is the role of a chief information security officer (CISO)?",
        "options": ["To oversee an organization's information security strategy", "To manage customer relations", "To improve sales"],
        "answer": "To oversee an organization's information security strategy"
    },
    {
        "question": "What is a common sign of system vulnerabilities?",
        "options": ["Unpatched software or outdated systems", "Regular updates", "Consistent performance"],
        "answer": "Unpatched software or outdated systems"
    },
    {
        "question": "What is the significance of threat intelligence?",
        "options": ["To understand potential threats and enhance security measures", "To ignore threats", "To improve marketing strategies"],
        "answer": "To understand potential threats and enhance security measures"
    },
    {
        "question": "What is the purpose of an antivirus program?",
        "options": ["To detect and remove malicious software", "To improve system performance", "To increase sales"],
        "answer": "To detect and remove malicious software"
    },
    {
        "question": "What is a common approach to securing cloud data?",
        "options": ["Using encryption and access controls", "Keeping data publicly accessible", "Ignoring security measures"],
        "answer": "Using encryption and access controls"
    },
    {
        "question": "What is the importance of regular security training?",
        "options": ["To keep employees informed about current threats", "To reduce sales", "To complicate procedures"],
        "answer": "To keep employees informed about current threats"
    },
    {
        "question": "What is a common method for managing cybersecurity risks?",
        "options": ["Conducting regular risk assessments", "Ignoring risks", "Assuming everything is secure"],
        "answer": "Conducting regular risk assessments"
    },
    {
        "question": "What is the purpose of a security incident report?",
        "options": ["To document and analyze security incidents", "To improve sales", "To enhance customer service"],
        "answer": "To document and analyze security incidents"
    },
    {
        "question": "What is a common sign of a data breach?",
        "options": ["Unexpected data changes or deletions", "Regular updates", "Consistent performance"],
        "answer": "Unexpected data changes or deletions"
    },
    {
        "question": "What is the role of a cybersecurity consultant?",
        "options": ["To advise organizations on improving their security posture", "To handle customer complaints", "To improve software performance"],
        "answer": "To advise organizations on improving their security posture"
    },
    {
        "question": "What is a common practice for securing user accounts?",
        "options": ["Using unique, strong passwords for each account", "Reusing passwords", "Using only simple passwords"],
        "answer": "Using unique, strong passwords for each account"
    },
    {
        "question": "What is the significance of security frameworks?",
        "options": ["To provide guidelines for managing cybersecurity risks", "To complicate procedures", "To improve sales"],
        "answer": "To provide guidelines for managing cybersecurity risks"
    },
    {
        "question": "What is a common characteristic of a strong cybersecurity culture?",
        "options": ["Awareness and proactive behavior among employees", "Ignoring security practices", "Only relying on technology"],
        "answer": "Awareness and proactive behavior among employees"
    },
    {
        "question": "What is the purpose of logging and monitoring in cybersecurity?",
        "options": ["To track activities and detect potential security issues", "To ignore user behavior", "To reduce performance"],
        "answer": "To track activities and detect potential security issues"
    },
    {
        "question": "What is a common sign of ransomware?",
        "options": ["Files being encrypted and held for ransom", "Faster performance", "Regular access to files"],
        "answer": "Files being encrypted and held for ransom"
    },
    {
        "question": "What is the importance of incident response training?",
        "options": ["To prepare employees for handling security incidents", "To improve sales", "To enhance product features"],
        "answer": "To prepare employees for handling security incidents"
    },
    {
        "question": "What is a common sign of insider threats?",
        "options": ["Unusual behavior or access patterns by employees", "Regular behavior", "Improved productivity"],
        "answer": "Unusual behavior or access patterns by employees"
    },
    {
        "question": "What is the role of encryption in protecting data?",
        "options": ["To convert data into a secure format that is unreadable without a key", "To make data accessible to everyone", "To improve performance"],
        "answer": "To convert data into a secure format that is unreadable without a key"
    },
    {
        "question": "What is a common method for preventing unauthorized access to systems?",
        "options": ["Implementing strong access controls and authentication measures", "Ignoring access requests", "Providing open access"],
        "answer": "Implementing strong access controls and authentication measures"
    },
    {
        "question": "What is the purpose of a security risk assessment?",
        "options": ["To identify and evaluate potential security risks", "To increase sales", "To enhance marketing strategies"],
        "answer": "To identify and evaluate potential security risks"
    },
    {
        "question": "What is a common sign of a cybersecurity breach?",
        "options": ["Unauthorized access or unusual account activity", "Regular access", "Improved user experience"],
        "answer": "Unauthorized access or unusual account activity"
    },
    {
        "question": "What is the significance of data classification?",
        "options": ["To categorize data based on sensitivity and importance", "To improve performance", "To reduce storage costs"],
        "answer": "To categorize data based on sensitivity and importance"
    },
    {
        "question": "What is a common characteristic of a secure network?",
        "options": ["Regular updates and monitoring", "Ignoring updates", "No security measures"],
        "answer": "Regular updates and monitoring"
    },
    {
        "question": "What is the role of a threat analyst?",
        "options": ["To analyze and assess potential security threats", "To improve customer service", "To develop new software"],
        "answer": "To analyze and assess potential security threats"
    },
    {
        "question": "What is the importance of backup and recovery plans?",
        "options": ["To ensure data can be restored in case of loss", "To increase data storage", "To complicate processes"],
        "answer": "To ensure data can be restored in case of loss"
    },
    {
        "question": "What is a common method for securing mobile devices?",
        "options": ["Using mobile device management (MDM) solutions", "Ignoring mobile security", "Providing open access"],
        "answer": "Using mobile device management (MDM) solutions"
    },
    {
        "question": "What is the role of a security architect?",
        "options": ["To design and build secure systems and architectures", "To handle customer complaints", "To improve sales"],
        "answer": "To design and build secure systems and architectures"
    },
    {
        "question": "What is the significance of cybersecurity laws and regulations?",
        "options": ["To ensure organizations comply with security standards", "To complicate operations", "To increase sales"],
        "answer": "To ensure organizations comply with security standards"
    },
    {
        "question": "What is a common practice for securing remote work?",
        "options": ["Implementing VPNs and secure access controls", "Ignoring remote access", "Providing open access"],
        "answer": "Implementing VPNs and secure access controls"
    },
    {
        "question": "What is the purpose of a cybersecurity framework?",
        "options": ["To provide a structured approach for managing cybersecurity risks", "To complicate security measures", "To increase sales"],
        "answer": "To provide a structured approach for managing cybersecurity risks"
    },
    {
        "question": "What is a common characteristic of effective security policies?",
        "options": ["Clear communication and guidelines", "Vague instructions", "No documentation"],
        "answer": "Clear communication and guidelines"
    },
    {
        "question": "What is the importance of monitoring network traffic?",
        "options": ["To detect potential security threats and anomalies", "To ignore traffic patterns", "To improve performance"],
        "answer": "To detect potential security threats and anomalies"
    },
    {
        "question": "What is a common sign of social engineering attacks?",
        "options": ["Manipulative communication to gain sensitive information", "Clear and direct communication", "Regular updates"],
        "answer": "Manipulative communication to gain sensitive information"
    },
    {
        "question": "What is the role of a compliance officer?",
        "options": ["To ensure adherence to laws, regulations, and policies", "To handle marketing", "To improve sales"],
        "answer": "To ensure adherence to laws, regulations, and policies"
    },
    {
        "question": "What is the purpose of a security operations center (SOC)?",
        "options": ["To monitor and respond to security incidents", "To handle customer relations", "To improve sales"],
        "answer": "To monitor and respond to security incidents"
    },
    {
        "question": "What is a common approach to securing IoT devices?",
        "options": ["Implementing strong authentication and encryption", "Ignoring IoT security", "Providing open access"],
        "answer": "Implementing strong authentication and encryption"
    },
    {
        "question": "What is the significance of vulnerability assessments?",
        "options": ["To identify and remediate security weaknesses", "To improve performance", "To increase sales"],
        "answer": "To identify and remediate security weaknesses"
    },
    {
        "question": "What is a common practice for managing cybersecurity incidents?",
        "options": ["Having a defined incident response plan", "Ignoring incidents", "Assuming everything is secure"],
        "answer": "Having a defined incident response plan"
    },
    {
        "question": "What is the role of a cybersecurity researcher?",
        "options": ["To investigate and analyze security threats and vulnerabilities", "To improve customer service", "To develop new software"],
        "answer": "To investigate and analyze security threats and vulnerabilities"
    },
    {
        "question": "What is a common sign of network attacks?",
        "options": ["Unusual traffic patterns or spikes", "Regular traffic patterns", "Improved performance"],
        "answer": "Unusual traffic patterns or spikes"
    },
    {
        "question": "What is the importance of user education in cybersecurity?",
        "options": ["To raise awareness and reduce human error", "To ignore security practices", "To complicate procedures"],
        "answer": "To raise awareness and reduce human error"
    },
    {
        "question": "What is a common characteristic of effective incident response?",
        "options": ["Timely detection and resolution of security incidents", "Ignoring incidents", "No documentation"],
        "answer": "Timely detection and resolution of security incidents"
    },
    {
        "question": "What is the role of a chief security officer (CSO)?",
        "options": ["To oversee an organization's security strategy", "To manage marketing", "To improve sales"],
        "answer": "To oversee an organization's security strategy"
    },
    {
        "question": "What is a common practice for securing APIs?",
        "options": ["Implementing authentication and rate limiting", "Ignoring API security", "Providing open access"],
        "answer": "Implementing authentication and rate limiting"
    },
    {
        "question": "What is the significance of security audits?",
        "options": ["To evaluate and improve security measures", "To complicate processes", "To increase sales"],
        "answer": "To evaluate and improve security measures"
    },
    {
        "question": "What is a common sign of compromised credentials?",
        "options": ["Unauthorized account access or changes", "Regular access", "Improved user experience"],
        "answer": "Unauthorized account access or changes"
    },
    {
        "question": "What is the role of a security engineer?",
        "options": ["To design and implement security solutions", "To improve marketing", "To handle customer complaints"],
        "answer": "To design and implement security solutions"
    },
    {
        "question": "What is a common method for preventing data breaches?",
        "options": ["Implementing strong security policies and practices", "Ignoring security", "Providing open access"],
        "answer": "Implementing strong security policies and practices"
    },
    {
        "question": "What is the importance of patch management?",
        "options": ["To keep software updated and secure", "To ignore updates", "To reduce performance"],
        "answer": "To keep software updated and secure"
    },
    {
        "question": "What is a common characteristic of effective security monitoring?",
        "options": ["Continuous monitoring and analysis of security events", "Ignoring events", "Only monitoring once a year"],
        "answer": "Continuous monitoring and analysis of security events"
    },
    {
        "question": "What is the role of a data protection officer (DPO)?",
        "options": ["To oversee data protection strategies and compliance", "To improve marketing", "To handle customer complaints"],
        "answer": "To oversee data protection strategies and compliance"
    },
    {
        "question": "What is a common practice for securing cloud environments?",
        "options": ["Implementing access controls and encryption", "Ignoring cloud security", "Providing open access"],
        "answer": "Implementing access controls and encryption"
    },
    {
        "question": "What is the significance of security incident management?",
        "options": ["To effectively respond to and manage security incidents", "To ignore incidents", "To complicate procedures"],
        "answer": "To effectively respond to and manage security incidents"
    },
    {
        "question": "What is a common sign of a cybersecurity vulnerability?",
        "options": ["Known weaknesses in software or systems", "Regular updates", "Consistent performance"],
        "answer": "Known weaknesses in software or systems"
    },
    {
        "question": "What is the role of a cybersecurity trainer?",
        "options": ["To educate employees about security best practices", "To handle marketing", "To improve sales"],
        "answer": "To educate employees about security best practices"
    },
    {
        "question": "What is a common method for securing sensitive data in transit?",
        "options": ["Using encryption protocols like TLS", "Ignoring data security", "Providing open access"],
        "answer": "Using encryption protocols like TLS"
    },
    {
        "question": "What is the importance of risk management in cybersecurity?",
        "options": ["To identify, assess, and mitigate potential risks", "To ignore risks", "To increase sales"],
        "answer": "To identify, assess, and mitigate potential risks"
    },
    {
        "question": "What is a common characteristic of a cybersecurity strategy?",
        "options": ["A comprehensive plan for protecting assets", "Ignoring security", "Assuming everything is secure"],
        "answer": "A comprehensive plan for protecting assets"
    },
    {
        "question": "What is the role of a digital forensics investigator?",
        "options": ["To collect and analyze digital evidence", "To improve marketing", "To develop new software"],
        "answer": "To collect and analyze digital evidence"
    },
    {
        "question": "What is a common practice for securing physical assets?",
        "options": ["Implementing access controls and monitoring", "Ignoring physical security", "Providing open access"],
        "answer": "Implementing access controls and monitoring"
    },
    {
        "question": "What is the significance of incident reporting?",
        "options": ["To document and communicate security incidents", "To ignore incidents", "To complicate procedures"],
        "answer": "To document and communicate security incidents"
    },
    {
        "question": "What is a common sign of an APT (Advanced Persistent Threat)?",
        "options": ["Prolonged and targeted attacks on systems", "Random attacks", "Improved user experience"],
        "answer": "Prolonged and targeted attacks on systems"
    },
    {
        "question": "What is the role of a cybersecurity policy?",
        "options": ["To provide guidelines for security practices", "To complicate procedures", "To ignore security measures"],
        "answer": "To provide guidelines for security practices"
    },
    {
        "question": "What is a common approach to securing email communications?",
        "options": ["Using encryption and secure email gateways", "Ignoring email security", "Providing open access"],
        "answer": "Using encryption and secure email gateways"
    },
    {
        "question": "What is the importance of vulnerability disclosure policies?",
        "options": ["To ensure responsible reporting of security vulnerabilities", "To ignore vulnerabilities", "To complicate procedures"],
        "answer": "To ensure responsible reporting of security vulnerabilities"
    },
    {
        "question": "What is a common characteristic of effective security awareness programs?",
        "options": ["Regular training and updates for employees", "Ignoring training", "No communication"],
        "answer": "Regular training and updates for employees"
    },
    {
        "question": "What is the role of a cybersecurity analyst?",
        "options": ["To monitor and analyze security threats", "To improve sales", "To handle customer complaints"],
        "answer": "To monitor and analyze security threats"
    },
    {
        "question": "What is a common practice for securing remote work?",
        "options": ["Implementing secure remote access solutions", "Ignoring remote work security", "Providing open access"],
        "answer": "Implementing secure remote access solutions"
    }
]

# Save the questions to a JSON file
filename = 'questions.json'

with open(filename, 'w') as json_file:
    json.dump(questions, json_file, indent=4)


print(f"Questions saved to {filename}.")
