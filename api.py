import random
import time


class Quiz:
    def __init__(self, fragor):
        self.fragor = fragor
        self.poang = 0

    def starta(self):
        if not self.fragor:
            print("Inga frågor!")
            return 0, 0

        random.shuffle(self.fragor)
        start = time.time()

        for fraga in self.fragor:
            fraga.visa()

            try:
                svar = int(input("Ditt svar: "))

                if fraga.kontrollera(svar):
                    print("Rätt!")
                    self.poang += 1
                else:
                    print(f"Fel! Rätt svar: {fraga.korrekt}")

            except:
                print("Ogiltigt svar!")

        tid = round(time.time() - start, 2)

        print(f"\nPoäng: {self.poang}/{len(self.fragor)}")
        print(f"Tid: {tid} sekunder")

        return self.poang, tid