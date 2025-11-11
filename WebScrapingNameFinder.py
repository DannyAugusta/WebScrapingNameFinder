import requests          # pro stahování HTML stránky
from bs4 import BeautifulSoup  # pro parsování HTML
import json              # pro uložení výsledků do JSON souboru

# URL stránky, kterou chceme scrapovat
url = "https://passages.winnipegfreepress.com/passage-details/id-316772/AUGUSTA_DANIEL"

# Hlavičky HTTP requestu (User-Agent), aby stránka neblokovala požadavek
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/142.0.0.0 Safari/537.36"
}

# Stažení obsahu stránky
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Chyba při načítání stránky: {response.status_code}")
    exit()  # ukončí skript při chybě

# Parsování HTML stránky pomocí BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Varianty jména a příjmení, které hledáme
name_variants = ["Dan", "Daniel", "Danny"]
last_name = "Augusta"

# Najdeme všechny <p> tagy na stránce
tags = soup.find_all(lambda t: t.name == "p")

# Slovník pro uložení odstavců do JSON
paragraphs_dict = {}
count = 0  # počítadlo relevantních tagů

# Pro každý <p> tag zkontrolujeme, zda obsahuje jméno, příjmení nebo celé jméno dohromady
for i, tag in enumerate(tags, 1):
    text = tag.get_text(strip=True)  # získání čistého textu
    found = []  # seznam nalezených typů výskytu

    # Kontrola, zda text obsahuje některou variantu jména
    for fn in name_variants:
        if fn in text:
            found.append(f"Jméno: {fn}")

    # Kontrola, zda text obsahuje příjmení
    if last_name in text:
        found.append(f"Příjmení: {last_name}")

    # Kontrola, zda text obsahuje celé jméno dohromady
    for fn in name_variants:
        if f"{fn} {last_name}" in text:
            found.append(f"Celé jméno: {fn} {last_name}")

    # Pokud jsme něco našli, vypíšeme stručně do konzole a uložíme celý text do JSON
    if found:
        count += 1
        print(f"\n--- Tag {count} ({tag.name}) obsahuje ---")
        print(", ".join(found))
        paragraphs_dict[f"Paragraph_{count}"] = text

# Pokud nebyl nalezen žádný relevantní tag
if count == 0:
    print(f"Nebyly nalezeny žádné relevantní odstavce s jménem nebo příjmením.")

# Uložení všech relevantních odstavců do JSON souboru
with open("name_paragraphs.json", "w", encoding="utf-8") as f:
    json.dump(paragraphs_dict, f, indent=4, ensure_ascii=False)

print(f"\nRelevantní odstavce byly uloženy do souboru 'name_paragraphs.json'.")
