import requests
from bs4 import BeautifulSoup
import json

url = "https://passages.winnipegfreepress.com/passage-details/id-316772/AUGUSTA_DANIEL"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/142.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Chyba při načítání stránky: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

name_variants = ["Dan", "Daniel", "Danny"]
last_name = "Augusta"

tags = soup.find_all(lambda t: t.name == "p")

paragraphs_dict = {}
count = 0

for i, tag in enumerate(tags, 1):
    text = tag.get_text(strip=True)
    found = []
    
    # Kontrola jména
    for fn in name_variants:
        if fn in text:
            found.append(f"Jméno: {fn}")
    
    # Kontrola příjmení
    if last_name in text:
        found.append(f"Příjmení: {last_name}")
    
    # Kontrola celého jména dohromady
    for fn in name_variants:
        if f"{fn} {last_name}" in text:
            found.append(f"Celé jméno: {fn} {last_name}")
    
    # Pokud něco z toho platí, vypíšeme do konzole a uložíme do JSON
    if found:
        count += 1
        print(f"\n--- Tag {count} ({tag.name}) obsahuje ---")
        print(", ".join(found))
        paragraphs_dict[f"Paragraph_{count}"] = text

if count == 0:
    print(f"Nebyly nalezeny žádné relevantní odstavce s jménem nebo příjmením.")

# Uložení do JSON
with open("name_paragraphs.json", "w", encoding="utf-8") as f:
    json.dump(paragraphs_dict, f, indent=4, ensure_ascii=False)

print(f"\nRelevantní odstavce byly uloženy do souboru 'name_paragraphs.json'.")
