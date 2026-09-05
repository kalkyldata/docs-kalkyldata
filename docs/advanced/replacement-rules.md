---
layout: default
title: "Ersättningsregler"
parent: "För avancerade användare"
nav_order: 7
permalink: /avancerat/ersattningsregler/
description: "Skapa egna ersättningsregler som styr vilka artiklar prisoptimeringen får byta ut och vilka alternativ som är tillåtna."
category: "reference"
tags: ["prisoptimering", "ersättningsregler", "regler", "json", "SV-ENR", "avancerat"]
audience: "advanced"
---
# Ersättningsregler
Ersättningsregler låter dig styra vilka material som får ersättas vid prisoptimering och vilka alternativ som är tillåtna. Du kan till exempel hitta billigare alternativ, standardisera material eller förbjuda vissa artiklar.

Prisoptimeringen visar alltid en diff innan något ändras. Du väljer själv vilka föreslagna byten som ska genomföras.

## Så använder du ersättningsregler

1. Öppna kalkylens meny.
2. Klicka på **Hantera ersättningsregler**.
3. Skapa en regel i **Byggare** eller klistra in en befintlig regel under **JSON**.
4. Spara regeln.
5. Kör [prisoptimering](/anvandarguide/kalkyl/prisoptimering/).
6. Granska de föreslagna bytena i diffen.
7. Godkänn de ändringar du vill genomföra.

Regler är privata som standard. Slå på **Publik regel** om andra användare ska kunna använda regeln.

## Byggare eller JSON

Du kan skapa samma ersättningsregel på två sätt.

### Byggare

**Byggare** är det visuella sättet att skapa regler.

Du kan bland annat:

* söka efter artiklar i prislistan
* lägga till flera artiklar som regeln ska leta efter
* välja vilka ersättare som är tillåtna
* ange en mängdfaktor för en ersättare
* se fel direkt medan du bygger regeln
* se hur många rader i kalkylen som regeln matchar

### JSON

Under **JSON** kan du klistra in eller kopiera en hel regeluppsättning.

Flera regler kan ligga i samma `replacement_rules`-lista.

När du växlar mellan **Byggare** och **JSON** konverteras innehållet automatiskt. Om JSON:en är ogiltig kan du inte växla förrän felen är rättade.

## Fyra vanliga sätt att använda regler

| Jag vill…                             | Så bygger du regeln                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| **Hitta det billigaste alternativet** | Lägg flera kandidater i `replace`, inklusive originalet om det ska få behållas |
| **Standardisera material**            | Lägg flera artiklar i `search` och en enda artikel i `replace`                 |
| **Förbjuda en artikel**               | Lägg inte originalet i `replace`                                               |
| **Tvinga en viss artikel**            | Lägg exakt en artikel i `replace`                                              |

## Hitta det billigaste alternativet

Använd flera kandidater i `replace` när prisoptimeringen ska välja det billigaste alternativet.

Om originalartikeln också får behållas måste den finnas med i `replace`.

```json
{
  "replacement_rules": [
    {
      "name": "Skruv M4 → billigaste",
      "description": "Väljer billigaste tillåtna M4-skruv.",
      "priority": 10,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            { "material_number": "781237266", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            {
              "material_number": "781237266",
              "material_type": "SV-ENR",
              "quantity_factor": 3
            }
          ]
        }
      ]
    }
  ]
}
```

Regeln letar efter de två artiklarna i `search`. Om någon av dem finns i kalkylen jämförs priset på alla kandidater i `replace`.

Prisoptimeringen föreslår det billigaste alternativet.

## Standardisera flera artiklar

Använd flera artiklar i `search` och en enda artikel i `replace` när flera material alltid ska ersättas med samma standardartikel.

```json
{
  "replacement_rules": [
    {
      "name": "Standardisera kopplingsdosa",
      "description": "Alla angivna kopplingsdosor byts till standardmodell.",
      "priority": 5,
      "replacements": [
        {
          "search": [
            { "material_number": "1201001", "material_type": "SV-ENR" },
            { "material_number": "1201002", "material_type": "SV-ENR" },
            { "material_number": "1201003", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "1201001", "material_type": "SV-ENR" }
          ]
        }
      ]
    }
  ]
}
```

Alla artiklar i `search` ersätts med artikeln i `replace`.

## Förbjuda en artikel

Om originalartikeln inte finns med i `replace` kan prisoptimeringen inte behålla den.

Regeln måste därför välja någon av de tillåtna ersättarna, förutsatt att minst en ersättare har ett tillgängligt pris.

```json
{
  "replacement_rules": [
    {
      "name": "Ersätt utgående kabel",
      "description": "Den gamla kabeln får inte längre användas.",
      "priority": 3,
      "replacements": [
        {
          "search": [
            { "material_number": "7101001", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "7101002", "material_type": "SV-ENR" },
            { "material_number": "7101003", "material_type": "SV-ENR" }
          ]
        }
      ]
    }
  ]
}
```

## Tvinga en viss artikel

Använd exakt en artikel i `replace` när en artikel alltid ska ersättas med ett bestämt alternativ.

```json
{
  "replacement_rules": [
    {
      "name": "Tvinga skruv M4 rostfri",
      "description": "Byter alltid till rostfri variant.",
      "priority": 2,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            { "material_number": "781237266", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237300", "material_type": "SV-ENR" }
          ]
        }
      ]
    }
  ]
}
```

Artikeln i `replace` används för alla träffar i `search`, förutsatt att artikeln har ett tillgängligt pris.

## Använd mängdfaktor vid byte

En ersättare kan behöva en annan mängd än originalartikeln.

Använd `quantity_factor` för att räkna om mängden.

```json
{
  "replacement_rules": [
    {
      "name": "Skruv 100-pack",
      "description": "Ersätter styckskruv med förpackning. En förpackning räcker till 100 skruvar.",
      "priority": 4,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            {
              "material_number": "781237500",
              "material_type": "SV-ENR",
              "quantity_factor": 0.01
            }
          ]
        }
      ]
    }
  ]
}
```

Mängdfaktorn påverkar både prisjämförelsen och mängden efter bytet.

Om originalartikeln kostar `2 kr/st` och ersättaren kostar `120 kr` med `quantity_factor: 0.01` jämförs:

* Original: `2 × 1 = 2 kr`
* Ersättare: `120 × 0.01 = 1,20 kr`

Ersättaren är billigare och mängden i kalkylen multipliceras med `0.01`.

## Använd flera regler

Du kan lägga flera regler i samma JSON.

Reglerna körs oberoende av varandra. Om flera regler matchar samma rad används den regel som har lägst `priority`.

```json
{
  "replacement_rules": [
    {
      "name": "Skruv M4 → billigaste",
      "priority": 10,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            { "material_number": "781237266", "material_type": "SV-ENR" }
          ]
        }
      ]
    },
    {
      "name": "Kabelsko → standard",
      "priority": 5,
      "replacements": [
        {
          "search": [
            { "material_number": "7301001", "material_type": "SV-ENR" },
            { "material_number": "7301002", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "7301001", "material_type": "SV-ENR" }
          ]
        }
      ]
    }
  ]
}
```

## Hantera regler som överlappar

Flera regler kan matcha samma material.

Använd `priority` för att bestämma vilken regel som ska användas.

Lägst nummer har högst prioritet.

```json
{
  "replacement_rules": [
    {
      "name": "Generell skruvoptimering",
      "priority": 20,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            { "material_number": "781237266", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237237", "material_type": "SV-ENR" },
            { "material_number": "781237266", "material_type": "SV-ENR" }
          ]
        }
      ]
    },
    {
      "name": "Projektspecifik skruv",
      "priority": 10,
      "replacements": [
        {
          "search": [
            { "material_number": "781237237", "material_type": "SV-ENR" }
          ],
          "replace": [
            { "material_number": "781237500", "material_type": "SV-ENR" }
          ]
        }
      ]
    }
  ]
}
```

`Projektspecifik skruv` har `priority: 10` och används därför för artikelnummer `781237237`.

Den generella regeln har `priority: 20` och används fortfarande för `781237266`.

## Fälten i ersättningsregler

| Fält              | Måste anges? | Beskrivning                                                                           |
| ----------------- | ------------ | ------------------------------------------------------------------------------------- |
| `name`            | Ja           | Regelns namn. Visas i diffen så att du ser vilken regel som föreslår bytet            |
| `description`     | Nej          | En beskrivning av regeln                                                              |
| `priority`        | Nej          | Avgör vilken regel som används om flera regler matchar samma rad. Lägst nummer vinner |
| `search`          | Ja           | Artiklar som regeln letar efter. Flera artiklar fungerar som ett `OR`                 |
| `replace`         | Ja           | Tillåtna ersättare. En artikel väljs för varje träff                                  |
| `material_number` | Ja           | Artikelnummer i både `search` och `replace`                                           |
| `material_type`   | Ja           | Materialtyp, till exempel `"SV-ENR"`. Måste matcha materialtypen på raden             |
| `quantity_factor` | Nej          | Räknar om mängden vid byte. Saknas värdet används `1`                                 |

## Bra att veta

* **Du godkänner alltid själv.** Prisoptimeringen visar regel, gammal artikel, ny artikel, mängd, pris och kostnadsdifferens innan något ändras.
* **Ersättare utan pris används inte.** Om ingen tillåten ersättare har ett pris lämnas raden oförändrad och visas i varningslistan.
* **Originalartikeln måste finnas i `replace` om den får behållas.** Om originalet saknas kan prisoptimeringen bara välja bland ersättarna.
* **`quantity_factor` påverkar både pris och mängd.** En faktor på `3` jämför ersättaren som `pris × 3` och multiplicerar mängden med `3` efter bytet.
* **En rad byts bara en gång per körning.** Om flera regler matchar används regeln med lägst `priority`.
* **Byten kan inte kedjas i samma körning.** Ett material som har ersatts används inte som utgångspunkt för ytterligare en ersättning under samma prisoptimering.
* **Du kan köra prisoptimeringen igen.** En redan optimerad kalkyl ger ingen ny diff om priserna och reglerna är oförändrade.
* **Materialinformationen uppdateras vid byte.** Namn, pris och leverantör hämtas för den nya artikeln. Produktlänken nollställs och en systemkommentar med regelns namn och tidigare artikelnummer läggs till på uppgiften.
* **Arbetstid påverkas inte.** Ersättningsregler ändrar bara material.

## Systemregler

Utöver dina egna regler kan Kalkyldata ha **systemregler** som underhålls centralt.

Systemregler fungerar på samma sätt som dina egna regler, men kan inte redigeras i Kalkyldata. Du kan fortfarande välja bort föreslagna byten rad för rad i diffen.

Se [Bidra med ersättningsregler via GitHub](/avancerat/github-bidrag-ersattningsregler/).
