import requests
import time
import urllib3

# SSL Warnings disable
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
TARGET_URL = "https://kick.com/api/v2/channels/65656576"

# --- SUPER FAKE HEADERS (Browser ki nakal) ---
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"'
}

def test_lightweight_connection():
    print(f"🚀 STARTING LIGHTWEIGHT TEST (Standard Requests)...")
    print(f"   Target: {TARGET_URL}")
    print(f"   Library: Standard 'requests' (No curl_cffi)")
    print("-" * 50)
    
    try:
        print("   ⏳ Connecting with Heavy Headers...")
        
        # Simple requests.get call
        resp = requests.get(TARGET_URL, headers=HEADERS, timeout=15, verify=False)
        
        print(f"   📡 STATUS CODE: {resp.status_code}")
        
        if resp.status_code == 200:
            data = resp.json()
            if "playback_url" in data:
                print("\n   🎉 MAGIC! Simple Request kaam kar gayi!")
                print(f"   🔗 Link: {data['playback_url'][:60]}...")
            else:
                print("   ⚠️ 200 OK, but Data Missing.")
        elif resp.status_code == 403:
            print("   ❌ BLOCKED (403): User-Agent kaam nahi kiya. TLS Fingerprint pakda gaya.")
            print("   (Conclusion: Hame 'curl_cffi' ki zarurat hai)")
        else:
            print(f"   ❌ FAILED: {resp.status_code}")

    except Exception as e:
        print(f"\n   ❌ ERROR: {e}")

if __name__ == "__main__":
    test_lightweight_connection()
