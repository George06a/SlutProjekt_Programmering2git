import html

class Fraga:
    def __init__(self, text, alternativ, korrekt):
        self.text = html.unescape(text)
        self.alternativ = [html.unescape(a) for a in alternativ]
        self.korrekt = html.unescape(korrekt)

    def visa(self):
        print("\n" + self.text)
        for i, alt in enumerate(self.alternativ, 1):
            print(f"{i}. {alt}")

    def kontrollera(self, svar):
        try:
            return self.alternativ[svar - 1] == self.korrekt
        except:
            return False