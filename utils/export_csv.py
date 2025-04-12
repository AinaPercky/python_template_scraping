import csv

def export_to_csv(data, filename="basket_matches.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Jour", "Heure", "Équipes"])
        for match in data:
            writer.writerow([match["jour"], match["heure"], match["equipes"]])

    print(f"\n✅ Données exportées vers CSV : {filename}")