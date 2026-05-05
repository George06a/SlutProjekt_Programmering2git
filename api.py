import random
import time


class Quiz:
    def __init__(self, frågor):
        self.frågor = frågor
        self.poäng = 0

    def starta(self):
        if not self.frågor:
            print("Inga frågor!")
            return 0, 0

        random.shuffle(self.frågor)
        start = time.time()

        for fråga in self.frågor:
            fråga.visa()

            try:
                svar = int(input("Ditt svar: "))

                if fråga.kontrollera(svar):
                    print("Rätt!")
                    self.poang += 1
                else:
                    print(f"Fel! Rätt svar: {fråga.korrekt}")

            except:
                print("Ogiltigt svar!")

        tid = round(time.time() - start, 2)

        print(f"\nPoäng: {self.poang}/{len(self.frågor)}")
        print(f"Tid: {tid} sekunder")

        return self.poang, tid