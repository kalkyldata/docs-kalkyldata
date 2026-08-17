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
| Du vill att artikeln ska finnas för alla användare | Bidra via GitHub-repot |
| Du vill flytta kalkyldata mellan kalkyler | Använd export och import i appen med `kdx/1` |

## Två vägar in i systemet

Det finns två huvudsakliga sätt att använda en JSON-baserad kalkylartikel.

### 1. Import i appen

Du kan importera JSON direkt i Kalkyldata när du arbetar med kalkyldata eller skapar egna kalkylartiklar.

En importerad kalkylartikel kan användas i din egen kalkyl eller sparas bland **Mina kalkylartiklar**. Egna kalkylartiklar är privata och blir inte automatiskt synliga för andra användare.

Det här är rätt väg när du vill skapa artiklar för eget bruk utan att publicera dem i det gemensamma artikelbiblioteket.

### 2. Bidrag via GitHub

Vill du bidra med en kalkylartikel till Kalkyldatas gemensamma artikelbibliotek kan du lägga JSON-filen i artikelrepot via GitHub.

Ett automatiskt flöde läser in filen och kompletterar kalkylartikeln med metadata som behövs för sökning och publicering. Efter granskning och publicering kan alla användare hitta artikeln i snabbsök och AI-agenten kan föreslå den.

Läs mer på [Bidra till artikelbiblioteket via GitHub](/avancerat/github-bidrag/).

## Det du skriver och det systemet fyller i

Du beskriver själva kalkylartikelns innehåll i JSON:

- **Benämning och beskrivning** förklarar vad artikeln avser.
- **Sökord och kategori** hjälper användaren att hitta artikeln.
- **Uppgifter** beskriver arbetet och materialet som ingår.
- **Arbetskoder** anger vilket arbete som ska slås upp när `tsk_work_type` är `SV-ATL`.
- **Artikelnummer** anger vilket material som ska slås upp när `tsk_material_type` är `SV-ENR`.
- **Antal och mängder** anger hur mycket arbete och material som ingår.

Kalkyldata fyller eller beräknar sedan information utifrån dessa uppgifter:

- **Arbetstid** slås upp från arbetskoden när `tsk_work_type` är `SV-ATL`.
- **Materialpris, materialbenämning och leverantör** slås upp från artikelnumret när `tsk_material_type` är `SV-ENR`, med dina rabattbrev inräknade.
- **Sökord, kategori och beskrivning** kan kompletteras automatiskt när en artikel publiceras i det gemensamma biblioteket.
- **Total tid och materialkostnad** räknas fram av systemet och ska inte skrivas in som summeringar i JSON-filen.

### Skriv inte in värden som systemet ska slå upp

För rader som använder `SV-ATL` ska du normalt inte skriva in en egen tid. Ange arbetskoden och låt Kalkyldata slå upp tiden.

På samma sätt ska du normalt inte ange ett eget pris eller en egen materialbenämning på en rad som använder `SV-ENR`. Ange artikelnumret och låt Kalkyldata göra prisuppslaget.

Det är viktigt eftersom uppslagen kan ändras när underliggande arbets- eller prisdata uppdateras.

Om du i stället vill ange tid eller material manuellt använder du `Övrig tid` respektive `Övrigt material`.

## En JSON-fil är inte samma sak som `kdx/1`

Det finns två olika JSON-format i Kalkyldata som har olika syften.

**En kalkylartikel i JSON** används för att beskriva en återanvändbar kalkylartikel, exempelvis en kabelinstallation med tillhörande arbete och material.

**`kdx/1`** används för import och export av befintlig kalkyldata mellan kalkyler och systemets olika nivåer.

Blanda därför inte ihop formaten. Läs [JSON-formatet för en kalkylartikel](/avancerat/json-format/) när du bygger en artikel och [Utbytesformatet kdx/1](/avancerat/kdx-format/) när du arbetar med import och export av kalkyldata.

## Nästa steg

Om du vill börja skriva en egen kalkylartikel går du vidare till [JSON-formatet för en kalkylartikel](/avancerat/json-format/).

Där finns en komplett fältreferens med exempel på hur arbete, material, tidsuppslag och prisuppslag definieras.
