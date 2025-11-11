# WebScraping Name Finder

**Autor:** Augusta Daniel  
**Popis:** Tento skript vyhledává na veřejné stránce odstavce obsahující moje jméno a příjmení, vypisuje informace do konzole a ukládá celé relevantní odstavce do JSON souboru.

---

## Cíl úkolu

- Najít veřejnou stránku, kde se vyskytuje vaše jméno a příjmení.  
- Použít webscraping k načtení dat stránky.  
- Vypsat informace o tagu, ve kterém se jméno/příjmení nachází.  
- Uložit celé odstavce obsahující jméno/příjmení do souboru JSON.

---

## Použitá stránka

[Winnipeg Free Press – Augusta Daniel](https://passages.winnipegfreepress.com/passage-details/id-316772/AUGUSTA_DANIEL)

---

## Použité knihovny

- `requests` – pro stahování HTML stránky  
- `BeautifulSoup` (bs4) – pro parsování HTML  
- `json` – pro uložení výsledků do souboru  

Instalace závislostí (pokud ještě nejsou nainstalovány):

```bash
pip install requests beautifulsoup4
```

## Popis skriptu
```Text
- Skript načte HTML stránku s použitím User-Agent, aby se předešlo blokování.
  - Vyhledá všechny <p> tagy obsahující:
  - Jméno (Dan, Daniel, Danny)
  - Příjmení (Augusta)
- Celé jméno dohromady (Dan Augusta, Daniel Augusta, Danny Augusta)
- V konzoli vypíše tagy s informací, co přesně se našlo (jméno, příjmení, celé jméno).
- Do souboru name_paragraphs.json uloží celý text odstavce, aby bylo možné s ním dále pracovat.
```

## Spuštění skriptu:
```bash
python WebScrapingNameFinder.py
```

## Příklad výstupu v konzoli:
```Text
--- Tag 1 (p) obsahuje ---
Jméno: Daniel, Příjmení: Augusta, Celé jméno: Daniel Augusta
--- Tag 2 (p) obsahuje ---
Jméno: Dan, Příjmení: Augusta, Celé jméno: Dan Augusta
...
Relevantní odstavce byly uloženy do souboru 'name_paragraphs.json'.
