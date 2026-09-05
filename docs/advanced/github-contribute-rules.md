---
layout: default
title: "Bidra med ersättningsregler via GitHub"
parent: "För avancerade användare"
nav_order: 8
permalink: /avancerat/github-bidrag-ersattningsregler/
description: "Så bidrar du med gemensamma ersättningsregler via GitHub och gör dem tillgängliga som systemregler för alla användare."
category: "reference"
tags: ["github", "bidrag", "ersättningsregler", "prisoptimering", "systemregel"]
audience: "advanced"
---
# Bidra med ersättningsregler via GitHub
Du kan bidra med gemensamma ersättningsregler genom GitHub. Regler som har granskats och lagts till i regel-repot blir **systemregler** och kan användas av alla användare i Kalkyldata.

Systemregler är skrivskyddade i appen för att alla användare ska utgå från samma version. Om du vill ändra en systemregel kan du kopiera den till en egen regel eller föreslå en ändring via GitHub.

## Så fungerar systemregler

Systemregler visas tillsammans med andra tillgängliga regler under **System- och publika regler** i **Ersättningsregler**.

En systemregel:

* är tillgänglig för alla användare
* kan användas i prisoptimeringen
* kan inte redigeras direkt i appen
* kan kopieras till en egen regel och ändras
* ändrar aldrig något automatiskt

Precis som med andra ersättningsregler granskar och godkänner du alltid föreslagna byten i diffen.

## Så bidrar du med en regel

1. Skapa och testa regeln i Kalkyldata under **Ersättningsregler**.
2. Kör [prisoptimering](/anvandarguide/kalkyl/prisoptimering/) på en relevant kalkyl och kontrollera resultatet.
3. Kontrollera att artiklarna och ersättarna fungerar som avsett.
4. Växla till fliken **JSON** och kopiera hela regeluppsättningen.
5. Skapa en JSON-fil i regel-repot under rätt kategori.
6. Döp filen efter regeln med ett tydligt och beskrivande filnamn.
7. Öppna en pull request och beskriv vad regeln löser och varför ersättarna är likvärdiga.
8. När ändringen har granskats och slagits samman synkas regeln automatiskt till Kalkyldata.

Den godkända regeln blir därefter tillgänglig som en **systemregel**.

## Filstruktur

Använd ett tydligt filnamn baserat på regelns innehåll.

Filens innehåll ska använda samma JSON-format som fliken **JSON** i regelbyggaren.

```json
{
  "replacement_rules": [
    {
      "name": "Standardisera installationskabel",
      "description": "Ersätter angivna kabeltyper med vald standardkabel.",
      "priority": 10,
      "replacements": [
        {
          "search": [
            {
              "material_number": "1234567",
              "material_type": "SV-ENR"
            }
          ],
          "replace": [
            {
              "material_number": "7654321",
              "material_type": "SV-ENR"
            }
          ]
        }
      ]
    }
  ]
}
```

## Krav på regeln

| Krav                | Beskrivning                                                          |
| ------------------- | -------------------------------------------------------------------- |
| `replacement_rules` | Ska innehålla regeluppsättningen                                     |
| `name`              | Ska vara tydligt och unikt                                           |
| `description`       | Ska förklara vad regeln gör och varför bytet är lämpligt             |
| `priority`          | Avgör vilken regel som används om flera regler matchar samma artikel |
| `material_type`     | Använd `SV-ENR` för material som hämtas från prislistan              |
| Artikelnummer       | Använd giltiga artikelnummer för de material som regeln ska hantera  |

## Vad ska beskrivas i pull requesten?

Beskriv kort:

* vilket problem regeln löser
* vilka artiklar regeln letar efter
* vilka ersättare som är tillåtna
* varför ersättarna är likvärdiga eller lämpliga
* om regeln har testats i prisoptimeringen

En tydlig beskrivning gör det enklare att granska regeln och förstå syftet med den längre fram.

## Bra att veta

* **Dina egna regler påverkar inte regel-repot.** Egna regler sparas separat och kan vara privata eller publika.
* **Systemregler kan inte redigeras i appen.** Vill du ändra en systemregel gör du ändringen via regel-repot.
* **Du kan kopiera en systemregel.** Den kopierade regeln blir en egen regel som du kan ändra utan att påverka originalet.
* **Prisoptimeringen är alltid manuell.** En systemregel ändrar ingenting förrän du godkänner bytet i diffen.
* **Regler behöver testas innan de föreslås som systemregler.** Kontrollera både träffar, priser och mängdfaktorer innan du öppnar en pull request.

## Relaterade guider

* [Ersättningsregler](/avancerat/ersattningsregler/)
* [Prisoptimering](/anvandarguide/kalkyl/prisoptimering/)
