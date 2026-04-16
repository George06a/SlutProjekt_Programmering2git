import requests

API_key = "5f5b549f759c10516a85f32b"

def hamta_valutakurs(fran="SEK", till="USD"):
    url = f"https://v6.exchangerate-api.com/v6/{API_key}/latest/{fran}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("result") == "success":
            return data["conversion_rates"].get(till)
        
        else:
            print("Fel från API.")
            return None
    except Exception as e:
        print("API-fel:", e)
        return None