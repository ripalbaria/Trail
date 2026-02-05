from curl_cffi import requests
import time

# --- CONFIGURATION (NO PROXY) ---
TARGET_URL = "https://kick.com/api/v2/channels/65656576"

def test_direct_connection():
    print(f"🚀 STARTING DIRECT TEST (NO PROXY)...")
    print(f"   Target: {TARGET_URL}")
    print(f"   Technique: curl_cffi (Fake Chrome 110)")
    print("-" * 50)
    
    try:
        print("   ⏳ Connecting directly from GitHub Server...")
        
        # Sirf 'impersonate' use kar rahe hain, proxies hata diya hai
        resp = requests.get(
            TARGET_URL, 
            impersonate="chrome110",  # Cloudflare ko dhoka dene ke liye
            timeout=15
        )
        
        print(f"   📡 STATUS CODE: {resp.status_code}")
        
        if resp.status_code == 200:
            data = resp.json()
            if "playback_url" in data:
                print("\n   🎉 SUCCESS! Proxy ki zarurat nahi hai!")
                print(f"   🔗 Link: {data['playback_url'][:60]}...")
            else:
                print("   ⚠️ Connected but JSON key missing.")
        elif resp.status_code == 403:
            print("   ❌ BLOCKED (403): GitHub IP Blacklisted hai. Proxy lagani padegi.")
        else:
            print(f"   ❌ FAILED with Status: {resp.status_code}")

    except Exception as e:
        print(f"\n   ❌ ERROR: {e}")

if __name__ == "__main__":
    test_direct_connection()
