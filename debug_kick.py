import requests
import urllib3
import time

# SSL Warnings disable (Clean logs)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- ✅ WORKING ORACLE PROXY DETAILS ---
ORACLE_IP = "161.118.179.243"
ORACLE_PORT = "48923"
ORACLE_USER = "sony"
ORACLE_PASS = "bypass123"

# --- KICK URL ---
TARGET_URL = "https://kick.com/api/v2/channels/65656576"

def get_proxy_string():
    # Format: http://user:pass@ip:port
    return f"http://{ORACLE_USER}:{ORACLE_PASS}@{ORACLE_IP}:{ORACLE_PORT}"

def test_github_connection():
    proxy_url = get_proxy_string()
    
    print(f"🚀 STARTING GITHUB PROXY TEST...")
    print(f"   Target: {TARGET_URL}")
    print(f"   Proxy IP: {ORACLE_IP}:{ORACLE_PORT}")
    print("-" * 50)
    
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }

    try:
        print("   ⏳ Connecting to Kick via Proxy...")
        
        # 15 second timeout diya hai taaki connection establish ho sake
        resp = requests.get(TARGET_URL, headers=headers, proxies=proxies, timeout=15, verify=False)
        
        print(f"   📡 STATUS CODE: {resp.status_code}")
        
        if resp.status_code == 200:
            data = resp.json()
            if "playback_url" in data:
                print("\n   🎉 SUCCESS! GitHub ne Kick ka data khinch liya!")
                print(f"   🔗 M3U8 Link: {data['playback_url'][:60]}...")
                print("   ✅ Proxy is WORKING perfectly on GitHub Actions.")
            else:
                print("   ⚠️ Connected (200 OK), but 'playback_url' not found in JSON.")
                print(f"   Response Preview: {str(data)[:100]}")
                
        elif resp.status_code == 403:
            print("   ❌ BLOCKED (403): Kick ne request reject kar di (Cloudflare).")
        elif resp.status_code == 407:
            print("   ❌ AUTH FAIL (407): Username/Password galat hai.")
        else:
            print(f"   ❌ FAILED with Status: {resp.status_code}")
            print(f"   Response: {resp.text[:200]}")

    except Exception as e:
        print(f"\n   ❌ CONNECTION ERROR: {e}")
        print("   (Check if Proxy Server is running and Port 48923 is Open)")

if __name__ == "__main__":
    test_github_connection()
