# 🛡️ Uniks Security Scanner 🕵️‍♂️

![Security Scanner](https://img.shields.io/badge/Security-Scanner-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Made%20with-Python-ff69b4?style=for-the-badge)

🚀 **Uniks Security Scanner** is an **automated web security tool** to detect:
- ✅ **SQL Injection (SQLi)**
- ✅ **Cross-Site Scripting (XSS)**
- ✅ **CSRF vulnerabilities**
- ✅ **HTML Injection flaws**

It helps **pentesters and developers** identify security weaknesses in web applications.

---

## 🔥 Features
✔️ Detects **SQL Injection** (Bypasses authentication, extracts data)  
✔️ Tests for **Cross-Site Scripting (XSS)** (Reflected & Stored XSS)  
✔️ Scans for **CSRF vulnerabilities** (Unauthenticated actions)  
✔️ Finds **HTML Injection** (Malicious HTML tags in forms)  
✔️ **Fast & Automated!**

---

## **⚒️ Installation & Usage**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Krich21/Uniks.git
cd Uniks
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Scanner
```bash
python3 security_scanner.py
```

---

## **🎯 Example Output**
```bash
===== Starting Advanced Security Scanner =====

[*] Testing for SQL Injection...
[+] SQL Injection vulnerability detected using: ' OR 1=1 --

[*] Testing for CSRF Vulnerabilities...
[+] Possible CSRF vulnerability detected! Password changed without a CSRF token.

[*] Testing for XSS Vulnerabilities...
[+] Found 3 forms for XSS testing.
[+] XSS vulnerability detected on /feedback

[*] Testing for HTML Injection Vulnerabilities...
[+] HTML Injection vulnerability detected on /comments

===== Security Scan Completed =====
```
---

## **📚 Additional Resources**

- [🔗 OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [📖 Juice Shop Documentation](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/)
- [🐍 Python requests library](https://docs.python-requests.org/en/latest/)
- [🔍 BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [📖 BASH Docs](https://devdocs.io/bash/)


