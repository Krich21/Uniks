# 🛡️ Uniks Security Scanner 🕵️‍♂️

![Security Scanner](https://img.shields.io/badge/Security-Scanner-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Made%20with-Python-ff69b4?style=for-the-badge)

🚀 **Automated Security Scanner** to detect **SQL Injection, XSS, CSRF, and HTML Injection vulnerabilities** in web applications.

---

## 🔥 Features
✅ Detects **SQL Injection (SQLi)**  
✅ Tests for **Cross-Site Scripting (XSS)**  
✅ Scans for **CSRF vulnerabilities**  
✅ Finds **HTML Injection flaws**  
✅ **Automated and easy-to-use!**

---

## 🛠️ Installation & Usage

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/OleksandrBaranenko/Uniks.git
cd Uniks

### **2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

### **3️⃣ Run the Scanner
```bash
python security_scanner.py


🎯 Example Output
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


## 🏆 Contributing
Want to improve the scanner? Open a Pull Request!

## 📜 License
This project is open-source under the MIT License.

✅ **What this does:**
- Adds **badges** for a cool look.
- Includes a **screenshot of usage**.
- Provides **clear steps to install & run**.
- Makes it **easy for others to contribute**.

---

## **2️⃣ Create a Cool GitHub Wiki**
- Go to your repo → Click **Wiki** → **Create a New Page**.
- Add **separate guides** for:
  - How the scanner works.
  - How to extend it.
  - How to contribute.

Example:
- **[🔗 How to Use](https://github.com/OleksandrBaranenko/Uniks/wiki/How-to-Use)**
- **[🔗 How It Works](https://github.com/OleksandrBaranenko/Uniks/wiki/How-It-Works)**

---

## **3️⃣ Add an Issues & Pull Request Template**
**Issues** help track bugs, while **Pull Request Templates** guide contributors.

### **📌 Issue Template (`.github/ISSUE_TEMPLATE.md`)**
Create a `.github/ISSUE_TEMPLATE.md` file:
```md
### 🐛 Bug Report
**Describe the issue**
A clear and concise description of the problem.

**Steps to Reproduce**
1. Run `python security_scanner.py`
2. Enter "..."
3. See error

**Expected behavior**
Explain what should happen.

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.10]


