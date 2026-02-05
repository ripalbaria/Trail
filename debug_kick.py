import requests
import json
import urllib3

# SSL Warnings disable
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
TARGET_URL = "https://kick.com/api/v2/channels/65656576"
USER_PROXY = "http://115.114.77.133:9090"  # Aapki Indian Proxy

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

def test_request(url, proxy=None, name="DIRECT"):
    print(f"\n👉 TESTING MODE: {name}")
    print(f"   URL: {url}")
    if proxy:
        print(f"   Proxy: {proxy}")
    
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        
        # Timeout kam rakha hai taaki jaldi result aaye
        resp = requests.get(url, headers=HEADERS, proxies=proxies, timeout=10, verify=False)
        
        print(f"   📡 Status Code: {resp.status_code}")
        
        if resp.status_code == 200:
            data = resp.json()
            if "playback_url" in data:
                print("   ✅ SUCCESS! 'playback_url' found.")
                print(f"   🔗 Link: {data['playback_url'][:50]}...")
                return True
            else:
                print("   ⚠️ JSON received but 'playback_url' missing.")
        elif resp.status_code == 403:
            print("   ❌ BLOCKED (403 Forbidden) - Cloudflare/Server rejected request.")
        else:
            print(f"   ❌ FAILED with Status: {resp.status_code}")
            print(f"   Response: {resp.text[:100]}")

    except Exception as e:
        print(f"   ❌ EXCEPTION: {e}")
    
    return False

def main():
    print("🚀 STARTING KICK DEBUGGER...")
    
    # 1. STEP: DIRECT TEST
    success = test_request(TARGET_URL, proxy=None, name="DIRECT (No Proxy)")
    
    if success:
        print("\n🎉 RESULT: Direct connection working! No proxy needed.")
    else:
        print("\n⚠️ Direct failed. Now trying your Indian Proxy...")
        
        # 2. STEP: INDIAN PROXY TEST
        success_proxy = test_request(TARGET_URL, proxy=USER_PROXY, name="INDIAN PROXY")
        
        if success_proxy:
            print("\n🎉 RESULT: Your Proxy is WORKING!")
        else:
            print("\n💀 RESULT: Both Direct and Proxy failed.")

if __name__ == "__main__":
    main()

