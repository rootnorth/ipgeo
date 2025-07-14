import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['status'] == 'success':
            print("\n📡 IP Bilgileri\n" + "-"*40)
            print(f"🆔 IP Adresi     : {data.get('query')}")
            print(f"🌍 Ülke          : {data.get('country')} ({data.get('countryCode')})")
            print(f"🏙️ Şehir         : {data.get('city')}")
            print(f"📮 Posta Kodu    : {data.get('zip')}")
            print(f"🗺️ Bölge         : {data.get('regionName')} ({data.get('region')})")
            print(f"🌐 Zaman Dilimi  : {data.get('timezone')}")
            print(f"🛰️ ISP           : {data.get('isp')}")
            print(f"💻 Organizasyon  : {data.get('org')}")
            print(f"🔧 AS Bilgisi    : {data.get('as')}")
            print(f"📍 Koordinatlar  : {data.get('lat')}, {data.get('lon')}")
            print(f"📶 Mobil Ağ mı?  : {'Evet' if data.get('mobile') else 'Hayır'}")
            print(f"🔒 VPN/Proxy?    : {'Evet' if data.get('proxy') else 'Hayır'}")
        else:
            print("❌ IP bilgisi alınamadı:", data.get('message'))

    except requests.exceptions.RequestException as e:
        print("🔌 Hata oluştu:", e)

if __name__ == "__main__":
    print("🌐 IP Adresi Sorgulayıcı\n" + "-"*40)
    ip = input("🔎 IP adresini gir: ").strip()
    get_ip_info(ip)
