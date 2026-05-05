from fraga import Fraga

class Fragbank:
    def __init__(self):
        self.fragor = {
            "sport": [
                Fraga(
                    "Hur många spelare har ett fotbollslag på planen?",
                    ["9", "10", "11", "12"],
                    "11"
                ),
                Fraga(
                    "Vilken sport använder en puck?",
                    ["Fotboll", "Ishockey", "Tennis", "Basket"],
                    "Ishockey"
                )
            ],

            "geografi": [
                Fraga(
                    "Vad är Sveriges huvudstad?",
                    ["Göteborg", "Stockholm", "Malmö", "Uppsala"],
                    "Stockholm"
                ),
                Fraga(
                    "Vilket land ligger norr om Sverige?",
                    ["Danmark", "Finland", "Tyskland", "Polen"],
                    "Finland"
                )
            ],

            "historia": [
                Fraga(
                    "När började andra världskriget?",
                    ["1914", "1939", "1945", "1950"],
                    "1939"
                ),
                Fraga(
                    "Vem var första presidenten i USA?",
                    ["Lincoln", "Washington", "Obama", "Jefferson"],
                    "Washington"
                )
            ]
        }

    def kategorier(self):
        return list(self.fragor.keys())

    def hamta(self, kategori):
        return self.fragor.get(kategori, [])