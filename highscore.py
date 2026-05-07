class Highscore:
    def __init__(self):
        # lista som sparar namn, poäng och tid
        self.scores = []

    def lagg_till(self, namn, poang, tid):
        # lägger till nytt resultat
        self.scores.append((namn, poang, tid))

        # sorterar efter högst poäng och snabbast tid
        self.scores.sort(key=lambda x: (-x[1], x[2]))

    def visa(self):
        print("\n--- HIGHSCORE ---")

        # om inga highscores finns
        if not self.scores:
            print("Inga highscores än.")
            return

        # skriver ut highscores
        for namn, poang, tid in self.scores:
            print(f"{namn}: {poang} poäng ({tid} sekunder)")