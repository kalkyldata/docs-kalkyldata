---
layout: default
title: "Utbytesformatet kdx/1"
parent: "För avancerade användare"
nav_order: 4
permalink: /avancerat/kdx-format/
description: "Så fungerar kdx/1, Kalkyldatas format för import och export av uppgifter, kalkylartiklar, delar och hela kalkyler."
category: "reference"
tags: ["kdx", "json", "export", "import", "format"]
audience: "advanced"
---

# Utbytesformatet kdx/1

`kdx/1` är Kalkyldatas format för import och export av kalkyldata. Formatet kan innehålla olika nivåer av kalkylen: en **uppgift**, en **kalkylartikel**, en **del** eller en **hel kalkyl**.

Till skillnad från JSON-formatet för en kalkylartikel är `kdx/1` alltså inte främst till för att beskriva en återanvändbar artikel. Det används när befintlig kalkyldata ska flyttas, sparas eller importeras mellan kalkyler och system.

## Så ser en fil ut

Innehållet ligger direkt på JSON-filens rotnivå. Information om formatet ligger under nyckeln `_kdx`.

```json
{
  "itm_name": "Vägguttag enkel",
  "itm_quantity": 4,
  "itm_tasks": [],
  "_kdx": {
    "format": "kdx",
    "version": 1,
    "kind": "item",
    "exportedAt": "2026-08-14T10:00:00.000Z",
    "source": {
      "app": "Kalkyldata",
      "appVersion": "1.0"
    }
  }
}
```

Fälten under `_kdx` beskriver själva utbytesfilen:

| Fält | Beskrivning |
| --- | --- |
| `format` | Formatets namn. För `kdx/1` är värdet `kdx`. |
| `version` | Formatversion. Den aktuella versionen är `1`. |
| `kind` | Vilken nivå filen innehåller: `task`, `item`, `part` eller `project`. |
| `exportedAt` | Datum och tid då filen exporterades. |
| `source` | Vilken app och version som skapade filen. |

### `kind`

Värdet i `kind` anger vilken nivå som exporterats:

| `kind` | Innehåller |
| --- | --- |
| `task` | En uppgift |
| `item` | En kalkylartikel |
| `part` | En del |
| `project` | En hel kalkyl |

Det gör att Kalkyldata kan avgöra vilken typ av kalkyldata som finns i filen och hur den ska hanteras vid import.

## Identifierare skapas på nytt

Interna identifierare följer inte med vid export.

Det gäller bland annat:

- `prj_id` för kalkylen
- `prt_id` för delen
- `itm_id` för kalkylartikeln
- `tsk_id` för uppgiften

Identifierarna är interna för den ursprungliga kalkylen och har ingen betydelse i en annan kalkyl. När filen importeras skapar Kalkyldata därför nya identifierare.

Det innebär att en importerad kopia behandlas som ny kalkyldata och inte automatiskt är kopplad till originalet.

## Vad som inte följer med

`kdx/1` innehåller den kalkyldata som behövs för att återskapa innehållet, men inte tillfälliga eller rent visuella delar av den ursprungliga kalkylen.

Följande följer exempelvis inte med:

- framräknade totalsummor
- tillfälliga prisjämförelser mellan leverantörer
- visningsinställningar som kolumnval, filter och sortering
- interna identifierare

Summor räknas fram på nytt vid import.

Materialpriser beräknas också utifrån den miljö där filen importeras. Det innebär att samma `kdx/1`-fil kan ge olika materialkostnad för olika användare, beroende på deras prisunderlag och rabattbrev.

## Import utan `_kdx`

En `kdx/1`-fil innehåller normalt `_kdx`-informationen, men Kalkyldata kan även försöka läsa JSON som saknar detta omslag.

Om `_kdx` saknas identifieras innehållets nivå utifrån fälten på rotnivå:

| Fältprefix | Tolkas som |
| --- | --- |
| `tsk_` | Uppgift |
| `itm_` | Kalkylartikel |
| `prt_` | Del |
| `prj_` | Kalkyl |

Det gör det möjligt att importera JSON som exempelvis har skapats manuellt eller genererats av ett annat verktyg, utan att du först behöver lägga till `_kdx`-objektet.

## Begränsningar

Vid import gäller bland annat följande:

- Filen får vara högst `1 MB`.
- JSON-filens rot måste vara ett objekt.
- En JSON-lista som rot stöds inte.
- Filen måste innehålla giltig JSON.
- Markdown-markeringar runt ett JSON-kodblock kan rensas bort automatiskt vid inklistring.

## Filnamn vid export

Kalkyldata namnger exporterade filer utifrån innehållets nivå, namn och exportdatum.

Exempel:

```text
task-montering-2026-08-14.json
item-vagguttag-enkel-2026-08-14.json
part-kok-2026-08-14.json
kalkyl-villa-lindberg-2026-08-14.json
```

Filnamnet påverkar inte innehållet i `kdx/1` eller hur filen identifieras vid import.

## `kdx/1` jämfört med kalkylartikel-JSON

Det är lätt att blanda ihop formaten eftersom båda använder JSON.

| | Kalkylartikel-JSON | `kdx/1` |
| --- | --- | --- |
| Huvudsyfte | Skapa och beskriva en återanvändbar kalkylartikel | Import och export av befintlig kalkyldata |
| Kan innehålla | Kalkylartikel med uppgifter | Uppgift, kalkylartikel, del eller hel kalkyl |
| `_kdx` | Nej | Ja, vid normal export |
| Interna ID:n | Skapas vid import | Tas bort vid export och skapas på nytt vid import |
| Typisk användning | Artikelbibliotek, egna artiklar och GitHub | Flytta eller säkerhetskopiera kalkyldata |

Om du bygger en kalkylartikel som ska återanvändas i artikelbiblioteket ska du alltså utgå från [JSON-formatet för en kalkylartikel](/avancerat/json-format/).

Om du vill exportera eller importera befintlig kalkyldata använder du `kdx/1`.

## Import och export i appen

För den praktiska användningen behöver du normalt inte skapa eller redigera `kdx/1` manuellt.

Kalkyldata skapar formatet automatiskt när du exporterar kalkyldata och tolkar formatet när du importerar.

Se [Import och export av kalkyldata](/anvandarguide/kalkyl/import-och-export/) för steg-för-steg-instruktioner.
