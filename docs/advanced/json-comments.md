---
layout: default
title: "Kommentarer och noteringar i JSON"
parent: "För avancerade användare"
nav_order: 3
permalink: /avancerat/json-kommentarer/
description: "Så fungerar kommentarer och noteringar i en kalkylartikel och hur itm_comments används."
category: "reference"
tags: ["json", "kommentarer", "itm_comments", "kalkylartikel"]
audience: "advanced"
---

# Kommentarer och noteringar i JSON

Kommentarer är fritext som följer med kalkylartikeln in i kalkylen. De kan användas för att förklara exempelvis var en tid eller kostnad kommer ifrån, vilka moment som är summerade eller vilka förutsättningar som gäller.

I JSON-formatet stöds kommentarer på **kalkylartikelnivå** genom fältet `itm_comments`.

## itm_comments — kommentarer på kalkylartikeln

`itm_comments` är en lista med objekt. Fältet `text` är det enda som krävs:

```json
{
  "itm_comments": [
    {
      "text": "Summerad tid enligt ackordstidslistan 2020759 moment 1+2+7: 0,03+0,02+0,06 = 0,11 tim."
    },
    {
      "text": "Kontrollmätning räknas som halv tid eftersom mätning görs i länkens båda ändar.",
      "kind": "system",
      "source": "Ackordstidslistan 2020759"
    }
  ]
}
```

| Fält | Krav | Beskrivning |
| --- | --- | --- |
| `text` | Ja | Själva kommentaren. |
| `kind` | Nej | `system` för fakta som följer med artikeln, `user` för egna anteckningar. Om fältet utelämnas används `system`. |
| `source` | Nej | Varifrån uppgiften kommer, till exempel en tidslista. |
| `createdAt` | Nej | Tidsstämpel. Sätts automatiskt om den saknas. |

Kommentarerna visas i kolumnen **Kommentarer** på kalkylartikelns rad, både i kalkyltabellen och i kortet som AI-agenten visar i chatten.

Systemkommentarer och egna kommentarer hålls isär. Egna anteckningar skrivs inte över när kalkylartikeln uppdateras.

## Kommentarer på uppgifter stöds inte

Det finns inget stött `tsk_comments`-fält i kalkylartikelns JSON-format.

Lägg därför inte kommentarer på enskilda uppgifter genom att lägga till egna `tsk_comments`-fält. Om en förklaring behöver följa med kalkylartikeln ska den i stället läggas i `itm_comments`.

Det gör också JSON-formatet enklare och säkerställer att kommentarer som är viktiga för användaren hamnar på en plats där de faktiskt visas i appen.

## Skriv kommentarer som stämmer med fälten

En kommentar som säger en sak medan fälten säger en annan skapar mer förvirring än den löser.

Kontrollera därför innan du publicerar en kalkylartikel:

1. Arbetskoden i kommentaren är samma kod som står i `tsk_work_code`.
2. Den tid som anges i kommentaren stämmer med den tid som uppslaget ger.
3. Avrundningar anges som avrundningar, till exempel `0,11 / 2 ≈ 0,06 tim`.

## När är en kommentar användbar?

Använd kommentarer när informationen hjälper en annan användare att förstå eller kontrollera kalkylartikeln.

Bra användning är till exempel:

- förklara hur en summerad tid har räknats fram
- ange vilket underlag som använts
- beskriva särskilda förutsättningar
- förklara varför en viss mängd eller tid används
- dokumentera en avvikelse från ett normalt arbetssätt

Undvik kommentarer som bara upprepar information som redan finns i benämningen eller i uppgifterna.

## Om kommentarerna inte syns

Kontrollera först att `itm_comments` ligger på kalkylartikelns rotnivå och att varje kommentar innehåller fältet `text`.

Exempel:

```json
{
  "itm_name": "EXQ 3G1,5 I RÖR",
  "itm_comments": [
    {
      "text": "Tiden bygger på summering av flera moment i arbetstidslistan."
    }
  ],
  "itm_tasks": []
}
```

Kommentarer som ligger under en enskild uppgift eller i ett eget, icke-stött fält visas inte som kalkylartikelns kommentarer.
