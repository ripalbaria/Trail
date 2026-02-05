from curl_cffi import requests # Special Library for bypassing Cloudflare
import time

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
    
    print(f"🚀 STARTING CLOUDFLARE BYPASS TEST...")
    print(f"   Target: {TARGET_URL}")
    print(f"   Proxy: {ORACLE_IP}:{ORACLE_PORT}")
    print("-" * 50)
    
    # curl_cffi use kar rahe hain (requests ki jagah)
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    try:
        print("   ⏳ Connecting with Real Chrome Fingerprint...")
        
        # 'impersonate="chrome"' ye sabse bada jadu hai!
        resp = requests.get(
            TARGET_URL, 
            proxies=proxies, 
            impersonate="chrome110",  # Cloudflare ko lagega ye Chrome v110 hai
            timeout=15
        )
        
        print(f"   📡 STATUS CODE: {resp.status_code}")
        
        if resp.status_code == 200:
            data = resp.json()
            if "playback_url" in data:
                print("\n   🎉 SUCCESS! Cloudflare Bypass Ho Gaya!")
                print(f"   🔗 M3U8 Link: {data['playback_url'][:60]}...")
            else:
                print("   ⚠️ Connected but JSON key missing.")
        elif resp.status_code == 403:
            print("   ❌ STILL BLOCKED (403): Cloudflare abhi bhi pakad raha hai.")
        else:
            print(f"   ❌ FAILED with Status: {resp.status_code}")

    except Exception as e:
        print(f"\n   ❌ ERROR: {e}")

if __name__ == "__main__":
    test_github_connection()
