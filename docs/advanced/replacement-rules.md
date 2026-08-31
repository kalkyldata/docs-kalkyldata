---
layout: default
title: "Ersättningsregler"
parent: "För avancerade användare"
nav_order: 7
permalink: /avancerat/ersattningsregler/
description: "Skapa egna ersättningsregler som styr vilka materialartiklar som kan ersätta varandra vid prisoptimering."
category: "advanced"
tags: ["prisoptimering", "ersättningsregler", "json", "sv-enr", "avancerat"]
audience: "advanced"
---

# Ersättningsregler

Med ersättningsregler bestämmer du vilka materialartiklar som får ersätta varandra vid prisoptimering. En regel anger vilka artiklar Kalkyldata ska leta efter och vilka artiklar som får användas som ersättare.

Reglerna används av [Prisoptimering](/anvandarguide/kalkyl/prisoptimering/). Prisoptimeringen visar alltid föreslagna byten innan något ändras, och du väljer själv vilka byten du vill genomföra.

Du skapar och hanterar regler från kalkylens meny:

1. Klicka på **⋯** uppe till höger i kalkyltabellen.
2. Välj **Hantera ersättningsregler…**.

Egna regler är privata som standard. Aktivera **Publik regel** om andra användare ska kunna använda regeln.

## Så fungerar en ersättningsregel

Varje ersättningsregel består av två delar:

* `search` anger vilka artiklar regeln ska leta efter i kalkylen.
* `replace` anger vilka artiklar som får användas som ersättare.

När en artikel matchar `search` jämför prisoptimeringen de tillåtna alternativen i `replace`. Vilket alternativ som föreslås beror på regelns uppbyggnad och vilka alternativ som kan prissättas.

## Fyra vanliga sätt att använda regler

| Jag vill…                          | Så bygger du regeln                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| **Hitta billigaste alternativ**    | Lägg flera kandidater i `replace`, inklusive originalartikeln om den ska få behållas. |
| **Standardisera**                  | Lägg flera artiklar i `search` och en enda kandidat i `replace`.                      |
| **Ersätta en artikel**             | Lämna originalartikeln utanför `replace` och ange de tillåtna ersättarna.             |
| **Alltid föreslå en viss artikel** | Ange exakt en kandidat i `replace`.                                                   |

## Ett komplett exempel

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
            { "material_number": "781237266", "material_type": "SV-ENR", "quantity_factor": 3 }
          ]
        }
      ]
    }
  ]
}
```

Regeln letar efter artikelnummer `781237237` och `781237266`. Om någon av artiklarna finns i kalkylen jämför prisoptimeringen de tillåtna alternativen i `replace`.

Eftersom den andra artikeln har `quantity_factor: 3` räknas dess pris med en faktor på 3 vid jämförelsen.

## Fler exempel

### Standardisera flera artiklar till en

Använd flera artiklar i `search` och en enda kandidat i `replace` när flera artiklar ska ersättas med samma standardartikel.

```json
{
  "replacement_rules": [
    {
      "name": "Standardisera kopplingsdosa",
      "description": "Alla typer av kopplingsdosor byts till standardmodell.",
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

### Ersätta en artikel med ett tillåtet alternativ

Om originalartikeln inte finns med i `replace` kan den inte väljas som alternativ. Prisoptimeringen kan då föreslå någon av de artiklar som finns i `replace`, förutsatt att minst en av dem kan prissättas.

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

### Alltid föreslå ett visst material

En enda kandidat i `replace` innebär att samma artikel alltid föreslås när regeln träffar, förutsatt att artikeln kan prissättas.

```json
{
  "replacement_rules": [
    {
      "name": "Tvinga skruv M4 rostfri",
      "description": "Byter alltid till rostfri variant oavsett tidigare val.",
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

Prisoptimeringen genomför inte bytet automatiskt. Du granskar och godkänner fortfarande förslaget innan artikeln ändras i kalkylen.

## Mängdfaktor vid byte

En ersättningsartikel kan kräva en annan mängd än originalartikeln. Använd `quantity_factor` för att ange hur mängden ska räknas om.

Faktorn används både när alternativen jämförs och när ett byte genomförs.

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
            { "material_number": "781237500", "material_type": "SV-ENR", "quantity_factor": 0.01 }
          ]
        }
      ]
    }
  ]
}
```

### Exempel på prisjämförelse

Om originalartikeln kostar `2 kr/st` och ersättaren kostar `120 kr` per förpackning jämförs kostnaden så här:

* Originalartikel: `2 × 1 = 2 kr`
* Ersättare: `120 × 0,01 = 1,20 kr`

Ersättaren är billigare och kan därför föreslås som byte. När bytet genomförs multipliceras mängden i kalkylen med `0,01`.

## Flera regler i samma fil

Du kan lägga flera regler i samma JSON. Reglerna körs oberoende av varandra.

Om flera regler träffar samma rad används regeln med lägst `priority`.

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

## Hantera överlappande regler

Samma artikel kan förekomma i flera `search`-listor. Använd `priority` för att styra vilken regel som ska användas när flera regler träffar samma rad.

Lägre nummer har högre prioritet.

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

För artikelnummer `781237237` används `Projektspecifik skruv` eftersom regeln har `priority: 10`. Den generella regeln kan fortfarande användas för artikelnummer `781237266`.

## Fälten i korthet

| Fält              | Måste anges? | Vad det gör                                                                                         |
| ----------------- | ------------ | --------------------------------------------------------------------------------------------------- |
| `name`            | Ja           | Regelns namn. Visas i prisoptimeringen så att du ser vilken regel som föreslår bytet.               |
| `description`     | Nej          | En beskrivning av regelns syfte.                                                                    |
| `priority`        | Nej          | Avgör vilken regel som används om flera regler träffar samma rad. Lägre nummer har högre prioritet. |
| `search`          | Ja           | Artiklarna som regeln letar efter. Flera poster fungerar som `OR`.                                  |
| `replace`         | Ja           | De artiklar som får användas som ersättare. Ett alternativ väljs per träffad rad.                   |
| `material_number` | Ja           | Artikelnummer. Används både i `search` och `replace`.                                               |
| `material_type`   | Ja           | Materialtyp, till exempel `"SV-ENR"`. Måste matcha materialtypen på uppgiften.                      |
| `quantity_factor` | Nej          | Räknar om mängden vid byte. Om fältet saknas används faktorn `1`.                                   |

## Bra att veta

* **Du godkänner alltid bytet själv.** Prisoptimeringen visar regel, gammalt och nytt artikelnummer, mängd, pris och kostnadsdifferens innan något ändras.
* **Ett alternativ utan pris kan inte väljas.** Om ingen tillåten ersättare kan prissättas lämnas raden oförändrad och visas i varningslistan.
* **Originalartikeln kan bara behållas om den finns i `replace`.** Lägg därför alltid till originalet i `replace` om det ska få vara kvar när det är billigast.
* **`quantity_factor` påverkar både pris och mängd.** En faktor på `3` innebär att priset jämförs som `pris × 3` och att mängden multipliceras med `3` när bytet genomförs.
* **En rad byts bara en gång per körning.** Om flera regler träffar samma rad används regeln med högst prioritet, alltså lägst `priority`.
* **Regler kan inte kedjas i samma körning.** Ett artikelbyte leder inte till att nästa ersättningsregel körs på den nya artikeln.
* **Du kan köra prisoptimeringen igen.** Om kalkylen redan är optimerad visas normalt inga nya byten om priser och regler är oförändrade.
* **Materialinformationen uppdateras vid byte.** Namn, pris och leverantör hämtas på nytt. En eventuell produktlänk tas bort och en systemkommentar läggs till på uppgiften. Arbetstid påverkas inte.

## Systemregler

Utöver egna ersättningsregler kan Kalkyldata innehålla systemregler. De fungerar på samma sätt som egna regler och används vid prisoptimering.

Du granskar alltid de föreslagna bytena och väljer själv vilka rader som ska ändras.
