---
layout: default
title: "För avancerade användare"
nav_order: 6
permalink: /avancerat/
description: "Arbeta med Kalkyldatas JSON-format, kdx/1, ersättningsregler och andra avancerade funktioner."
category: "reference"
tags: ["json", "kalkylartikel", "uppgift", "kdx", "ersättningsregler", "prisoptimering"]
audience: "advanced"
has_children: true
---

# För avancerade användare

Den här delen är för dig som vill arbeta direkt med Kalkyldatas dataformat, skapa många kalkylartiklar, använda ersättningsregler eller bidra till artikelbiblioteket. Du behöver inte använda dessa funktioner för att skapa vanliga kalkyler i gränssnittet.

## Sidor i den här delen

* [Bygga kalkylartiklar med JSON](/avancerat/json-oversikt/) — när JSON är användbart och hur du skapar kalkylartiklar från JSON.
* [JSON-formatet för en kalkylartikel](/avancerat/json-format/) — fält för kalkylartiklar och uppgifter med exempel.
* [Kommentarer och noteringar i JSON](/avancerat/json-kommentarer/) — hur `itm_comments` och `tsk_comments` används.
* [Utbytesformatet kdx/1](/avancerat/kdx-format/) — formatet som används vid import och export av kalkyldata.
* [Bidra till artikelbiblioteket via GitHub](/avancerat/github-bidrag/) — mappstruktur, filnamn och hur kalkylartiklar blir sökbara.
* [Validera och felsök din JSON](/avancerat/validera-json/) — kontrollpunkter och vanliga fel.
* [Ersättningsregler](/avancerat/ersattningsregler/) — skapa regler som styr vilka materialartiklar som får ersätta varandra vid prisoptimering.
* [API och integrationer](/avancerat/api/) — koppla Kalkyldata till andra system via webhooks. API tillhandahålls efter förfrågan.

## Två JSON-format

Kalkyldata använder två JSON-format med olika syften. En **artikelfil** beskriver en återanvändbar kalkylartikel, medan `kdx/1` används för att importera och exportera kalkyldata.

| Format     | Används till                        | Innehåller                                                               |
| ---------- | ----------------------------------- | ------------------------------------------------------------------------ |
| Artikelfil | Kalkylartiklar i artikelbiblioteket | Ett `itm_*`-objekt med en eller flera `itm_tasks`                        |
| `kdx/1`    | Import och export av kalkyldata     | Kalkylens domänfält tillsammans med `_kdx`, som anger format och version |

### Artikelfil

En artikelfil beskriver en återanvändbar **kalkylartikel**. Kalkylartikeln innehåller en eller flera **uppgifter**, där varje uppgift beskriver ett arbetsmoment och kan innehålla arbetstid och material.

Artikelfiler används bland annat när du bygger kalkylartiklar med JSON eller bidrar med kalkylartiklar till artikelbiblioteket.

En kalkylartikel använder `itm_*`-fält. Uppgifterna i `itm_tasks` använder `tsk_*`-fält. Prefixen visar vilken nivå varje fält tillhör.

### `kdx/1`

`kdx/1` är Kalkyldatas utbytesformat för import och export. Formatet kan användas för en **uppgift**, **kalkylartikel**, **del** eller en hel **kalkyl**.

Formatet använder samma domänfält som Kalkyldata använder internt. En `_kdx`-sektion på JSON-objektets toppnivå anger att filen använder kdx-formatet och vilken version den har.

Det betyder att du inte behöver översätta fältnamn när du arbetar med `kdx/1`. Exempelvis används `itm_name` för kalkylartikelns namn och `tsk_material_number` för uppgiftens artikelnummer.

## När ska du använda JSON?

Använd JSON när du behöver arbeta med kalkylartiklar eller kalkyldata utanför det vanliga arbetsflödet i gränssnittet.

JSON är särskilt användbart när du:

* skapar eller ändrar många kalkylartiklar samtidigt
* vill bygga kalkylartiklar från befintliga data
* behöver kontrollera enskilda fält och uppgifter
* bidrar med kalkylartiklar till artikelbiblioteket
* behöver exportera eller importera kalkyldata med `kdx/1`

För vanligt kalkylarbete behöver du inte arbeta med JSON. Du kan skapa och ändra kalkyler och kalkylartiklar direkt i Kalkyldata.

## Kalkylens struktur

Kalkyldata bygger kalkylen i fyra nivåer:

```text
Kalkyl
└── Del
    └── Kalkylartikel
        └── Uppgift
```

En **kalkyl** innehåller delar. En **del** innehåller kalkylartiklar. En **kalkylartikel** innehåller en eller flera uppgifter. En **uppgift** är det minsta arbetsmomentet och kan innehålla arbetstid, material eller båda.

I JSON motsvaras nivåerna av följande prefix:

| Nivå          | Prefix  |
| ------------- | ------- |
| Kalkyl        | `prj_*` |
| Del           | `prt_*` |
| Kalkylartikel | `itm_*` |
| Uppgift       | `tsk_*` |

De tekniska prefixen ska behållas när du arbetar med JSON. De är en del av Kalkyldatas dataformat och ska inte översättas.

## Beräkningar i JSON

Mängden på en kalkylartikel fungerar som en multiplikator för alla uppgifter i kalkylartikeln.

Exempel:

```json
{
  "itm_name": "Vägguttag enkel",
  "itm_quantity": 4
}
```

Om kalkylartikeln innehåller en uppgift med `0,15` timmars arbetstid per enhet blir den totala arbetstiden `0,60` timmar när `itm_quantity` är `4`.

Materialkostnaden beräknas på motsvarande sätt utifrån uppgiftens antal, materialmängd och materialpris.

## Bra att veta

* `itm_*` används för kalkylartikelns fält och `tsk_*` för uppgiftens fält.
* `itm_quantity` multiplicerar arbetstid och materialkostnad för hela kalkylartikeln.
* `SV-ATL` används för standardiserade arbetstidsuppslag. `Övrig tid` används när arbetstiden ska anges manuellt.
* `SV-ENR` används för material med prisuppslag. `Övrigt material` används när materialet hanteras manuellt.
* `kdx/1` innehåller inte interna UUID:n för kalkyl, del, kalkylartikel eller uppgift. Dessa skapas på nytt vid import.
* Här används tekniska fältnamn som `itm_*` och `tsk_*` medvetet. I vanlig användartext används i stället **kalkylartikel** och **uppgift**.
