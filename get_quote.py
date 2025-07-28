import requests, datetime

def get_random_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random/")
        response.raise_for_status()
        for quote in response.json():
            return f"\"{quote['q']}\" \n- {quote['a']}"
    except requests.exceptions.HTTPError as e:
        print("Erreur http:", e)
        return "Citation indisponible pour aujourdhui"
    except requests.exceptions.RequestException as e:
        print("Erreur http:", e)
        return "Citation indisponible pour aujourdhui"