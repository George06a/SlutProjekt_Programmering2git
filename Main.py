from quiz import Quiz
from api import hamta_API_fragor
from highscore import Highscore
from Offlinefragor import Fragbank


def meny():
    highscore = Highscore()
    fragbank = Fragbank()

    kategori_map = {
        "1": 21,
        "2": 22,
        "3": 23,
        "4": 18,
        "5": None
    }

    while True:
        print("\n--- QUIZMASTER ---")
        print("1. Starta quiz (API)")
        print("2. Starta quiz (lokal frågebank)")
        print("3. Visa highscore")
        print("0. Avsluta")

        val = input("Val: ")

        # API QUIZ
        if val == "1":
            print("\nKategori:")
            print("1. Sport")
            print("2. Geografi")
            print("3. Historia")
            print("4. Datorer")
            print("5. Random")

            kat_val = input("Val: ")
            kategori = kategori_map.get(kat_val)

            # antal frågor
            try:
                antal = int(input("Hur många frågor vill du ha? "))

                if antal <= 0:
                    print("Ogiltigt antal, använder 5 frågor.")
                    antal = 5

            except ValueError:
                print("Ogiltigt antal, använder 5 frågor.")
                antal = 5

            diff = input("Svårighet (easy/medium/hard): ").lower()

            fragor = hamta_API_fragor(antal, kategori, diff)

            if not fragor:
                print("Kunde inte hämta frågor från API.")
                continue

            quiz = Quiz(fragor)
            poang, tid = quiz.starta()

            # poängsystem
            multiplikator = {
                "easy": 1,
                "medium": 2,
                "hard": 3
            }.get(diff, 1)

            slutpoang = poang * multiplikator

            print("\n--- RESULTAT ---")
            print(f"Rätt: {poang}/{antal}")
            print(f"Svårighet: {diff}")
            print(f"Slutpoäng: {slutpoang}")
            print(f"Tid: {tid} sekunder")

            namn = input("Namn: ")
            highscore.lagg_till(namn, slutpoang, tid)

        # LOKAL FRÅGEBANK
        elif val == "2":
            kategorier = fragbank.kategorier()

            print("\nKategori:")
            for i, kategori in enumerate(kategorier, 1):
                print(f"{i}. {kategori}")

            try:
                val_k = int(input("Val: "))
                kategori = kategorier[val_k - 1]

                fragor = fragbank.hamta(kategori)

                quiz = Quiz(fragor)
                poang, tid = quiz.starta()

                print("\n--- RESULTAT ---")
                print(f"Rätt: {poang}/{len(fragor)}")
                print(f"Tid: {tid} sekunder")

                namn = input("Namn: ")
                highscore.lagg_till(namn, poang, tid)

            except:
                print("Fel val!")

        # VISA HIGHSCORE
        elif val == "3":
            highscore.visa()

        # AVSLUTA
        elif val == "0":
            print("Hejdå!")
            break

        else:
            print("Ogiltigt val!")


if __name__ == "__main__":
    meny()