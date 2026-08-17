---
layout: default
title: "Bygga kalkylartiklar med JSON"
parent: "För avancerade användare"
nav_order: 1
permalink: /avancerat/json-oversikt/
description: "När det lönar sig att skriva en kalkylartikel som JSON istället för i editorn, och vilka vägar som finns in i Kalkyldata."
category: "reference"
tags: ["json", "kalkylartikel", "import", "github", "avancerat"]
audience: "advanced"
---

# Bygga kalkylartiklar med JSON

En kalkylartikel i Kalkyldata är i grunden ett JSON-objekt med en benämning, sökord och en lista med uppgifter. Varje uppgift kan innehålla både arbete och material.

Du kan skapa och redigera kalkylartiklar direkt i Kalkyldata, men du kan också arbeta med JSON. JSON är särskilt användbart när du bygger många artiklar av samma typ, vill kopiera en befintlig artikel eller vill versionshantera innehållet.

Du behöver inte kunna JSON för att använda Kalkyldata. För de flesta användare är editorn i appen det enklaste alternativet.

## När JSON lönar sig

| Situation | Rekommendation |
| --- | --- |
| Du skapar en enstaka kalkylartikel | Använd editorn under **Mina kalkylartiklar** |
| Du skapar många varianter av samma artikel | Skriv JSON och importera |
| Du vill kopiera en befintlig artikel och ändra exempelvis artikelnummer eller benämning | Använd JSON |
| Du vill versionshantera och granska ändringar | Använd JSON och GitHub |
| Du vill att artikeln ska finnas i det gemensamma artikelbiblioteket | Bidra via GitHub-repot |
| Du vill flytta kalkyldata mellan kalkyler | Använd export och import i appen med `kdx/1` |

## Två vägar in i systemet

JSON kan användas på två olika sätt beroende på vad du vill göra.

### 1. Importera JSON i appen

När du importerar JSON till en kalkyl läggs innehållet in i den aktuella kalkylen.

Du kan också använda JSON när du skapar en egen kalkylartikel under **Mina kalkylartiklar**. Den sparade kalkylartikeln hanteras sedan som en vanlig egen kalkylartikel och kan användas i dina kalkyler.

Kalkylartiklar under **Mina kalkylartiklar** kan vara privata eller publiceras så att andra användare kan hitta och använda dem. Det är alltså inte själva JSON-importen som avgör om en kalkylartikel är privat eller publik, utan artikelns synlighetsinställning.

### 2. Bidra via GitHub

Vill du bidra med en kalkylartikel till Kalkyldatas gemensamma artikelbibliotek kan du lägga JSON-filen i artikelrepot via GitHub.

Ett automatiskt flöde läser in filen och kompletterar kalkylartikeln med metadata som behövs för sökning och publicering. Efter granskning och publicering kan alla användare hitta artikeln i snabbsök och AI-agenten kan föreslå den.

Läs mer på [Bidra till artikelbiblioteket via GitHub](/avancerat/github-bidrag/).

## Det du skriver och det systemet fyller i

I JSON-filen beskriver du kalkylartikelns innehåll:

- **Benämning och beskrivning** förklarar vad artikeln avser.
- **Sökord och kategori** hjälper användaren att hitta artikeln.
- **Uppgifter** beskriver arbetet och materialet som ingår.
- **Arbetskoder** anger vilket arbete som ska slås upp när `tsk_work_type` är `SV-ATL`.
- **Artikelnummer** anger vilket material som ska slås upp när `tsk_material_type` är `SV-ENR`.
- **Antal och mängder** anger hur mycket arbete och material som ingår.
- **Tid, materialbenämning och pris** kan anges som värden i JSON-filen och fungerar som underlag om ett uppslag inte ger någon träff.

Kalkyldata använder sedan uppgifterna för att komplettera kalkylartikeln:

- **Arbetstid** slås upp från arbetskoden när `tsk_work_type` är `SV-ATL`.
- **Materialpris, materialbenämning och leverantör** slås upp från artikelnumret när `tsk_material_type` är `SV-ENR`, med dina rabattbrev inräknade.
- **Sökord, kategori och beskrivning** kan kompletteras automatiskt när en artikel publiceras i det gemensamma biblioteket.
- **Total tid och materialkostnad** räknas fram av systemet.

## Uppslag och reservvärden

Det är ofta en bra idé att ange både en uppslagskod och ett värde i JSON-filen.

När `tsk_work_type` är `SV-ATL` försöker Kalkyldata slå upp `tsk_work_code` i arbetstidslistan. Om koden hittas används uppgifterna från uppslaget. Om koden inte hittas kan de värden som redan finns angivna i kalkylartikeln användas som reserv.

Samma princip gäller material. När `tsk_material_type` är `SV-ENR` försöker Kalkyldata slå upp `tsk_material_number` i prislistan. Om artikelnumret hittas används det aktuella uppslaget. Om det inte finns någon träff kan de angivna värdena i kalkylartikeln användas som reserv.

Det gör kalkylartikeln mer robust. Den kan fortfarande innehålla en användbar tid eller materialkostnad även om en arbetskod eller ett artikelnummer saknas i det aktuella uppslaget.

Det är därför inte fel att ange exempelvis:

```json
{
  "tsk_work_type": "SV-ATL",
  "tsk_work_code": "206501112",
  "tsk_work_task_duration": 0.06,
  "tsk_work_description": "Montage VP-RÖR",
  "tsk_material_type": "SV-ENR",
  "tsk_material_number": "1416753",
  "tsk_material_name": "VP-RÖR 20MM 750N HF, 3M",
  "tsk_material_user_price": 55.0
}
```

Om arbetskoden eller artikelnumret ger en träff kan Kalkyldata ersätta reservvärdena med aktuella uppgifter från uppslaget.

## En JSON-fil är inte samma sak som `kdx/1`

Det finns två olika JSON-format i Kalkyldata som har olika syften.

**En kalkylartikel i JSON** används för att beskriva en återanvändbar kalkylartikel, exempelvis en kabelinstallation med tillhörande arbete och material.

**`kdx/1`** används för import och export av befintlig kalkyldata mellan kalkyler och systemets olika nivåer.

Blanda därför inte ihop formaten. Läs [JSON-formatet för en kalkylartikel](/avancerat/json-format/) när du bygger en artikel och [Utbytesformatet kdx/1](/avancerat/kdx-format/) när du arbetar med import och export av kalkyldata.

## Nästa steg

Om du vill börja skriva en egen kalkylartikel går du vidare till [JSON-formatet för en kalkylartikel](/avancerat/json-format/).

Där finns en komplett fältreferens med exempel på hur arbete, material, tidsuppslag och prisuppslag definieras.
