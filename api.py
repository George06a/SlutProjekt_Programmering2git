import requests
import random
from fraga import Fraga


def hamta_API_fragor(antal=5, kategori=None, svarighet=None):
    url = "https://opentdb.com/api.php"

    params = {
        "amount": antal,
        "type": "multiple"
    }

    if kategori:
        params["category"] = kategori

    if svarighet:
        params["difficulty"] = svarighet

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data["response_code"] != 0:
            print("Inga frågor hittades!")
            return []

        fragor = []

        for item in data["results"]:
            alternativ = item["incorrect_answers"] + [item["correct_answer"]]
            random.shuffle(alternativ)

            fragor.append(
                Fraga(item["question"], alternativ, item["correct_answer"])
            )

        return fragor

    except:
        print("Kunde inte hämta frågor från API!")
        return []