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

From your screenshot, it looks like the GitHub Markdown rendering issue is due to an incorrectly formatted section in your `README.md` file. The issue appears to be:

1. **Mixed Markdown Headers and Code Blocks**:  
   - The `### **2️⃣ Install Dependencies**` header is not correctly separating the next code block.
   - The `pip install -r requirements.txt` command might be merged improperly.

### **How to Fix It**
To correctly separate the sections and ensure proper rendering in GitHub, try formatting your `README.md` file as follows:

```md
## Installation & Usage

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
python security_scanner.py
```
```

### **Fix Explanation**
1. **Properly Close Code Blocks**: Ensure each code block is enclosed within triple backticks (```) and correctly formatted.
2. **Avoid Mixing Markdown Headers Inside Code Blocks**: The `### **2️⃣ Install Dependencies**` was previously formatted incorrectly, causing GitHub to misinterpret it.
3. **Ensure Blank Lines for Proper Separation**: GitHub's parser sometimes fails when there are no new lines between sections.

This should resolve the issue, making the README display separate code blocks correctly.

Let me know if you need further refinements! 🚀
