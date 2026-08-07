---
layout: default
title: "Import och export av kalkyldata"
parent: "Kalkyl"
nav_order: 8
permalink: /anvandarguide/kalkyl/import-export/
description: "Exportera och importera kalkyldata för att återanvända eller flytta uppgifter, kalkylartiklar, delar och hela kalkyler."
category: "guide"
tags: ["import", "export", "json", "kalkyl"]
audience: "user"
---

Du kan exportera och importera kalkyldata i JSON-format. Det gör det enkelt att återanvända uppgifter, kalkylartiklar, delar eller hela kalkyler mellan olika projekt eller installationer av Kalkyldata.

## Exportera kalkyldata

1. Öppna kalkylpanelen.
2. Klicka på de tre vertikala punkterna (**⋮**) längst upp till höger i kalkyltabellen.
3. Se under menyn **IMPORTERA OCH EXPORTERA**.
4. Välj **Ladda ner som JSON** eller **Kopiera JSON till urklipp**.

Du kan exportera hela kalkylen från menyn. Om kolumnen **Export** är synlig kan du även exportera en enskild uppgift, kalkylartikel eller del direkt från tabellen.

Exportfilen får automatiskt ett namn med kalkylens namn och dagens datum, till exempel:

`kalkyl-garage-2026-08-07.json`

## Importera kalkyldata

1. Öppna kalkylpanelen.
2. Klicka på de tre vertikala punkterna (**⋮**) längst upp till höger i kalkyltabellen.
3. Öppna menyn **IMPORTERA OCH EXPORTERA**.
4. Välj **Importera kalkyldata**.
5. Ladda upp en JSON-fil eller klistra in JSON-text.
6. Kontrollera vilket innehåll som hittades.
7. Välj var innehållet ska importeras.
8. Klicka **Importera**.

Du kan importera:

- en uppgift,
- en kalkylartikel,
- en del,
- en hel kalkyl.

När du importerar en hel kalkyl kan du välja:

- **Slå ihop** – lägger till den importerade kalkylen i den aktuella.
- **Ersätt** – ersätter den aktuella kalkylen helt.

{: .warning }
> Kontrollera alltid att du har valt rätt alternativ innan du använder **Ersätt**. Den aktuella kalkylen ersätts av den importerade.

## Välj rätt importmål

| Du importerar | Importeras till | Resultat |
| --- | --- | --- |
| Uppgift | En kalkylartikel | Uppgiften läggs till i kalkylartikeln. |
| Kalkylartikel | En del eller **Ny del** | Kalkylartikeln läggs till i den valda delen. |
| Del | Den aktuella kalkylen | Delen läggs till som en ny del. |
| Kalkyl | **Slå ihop** eller **Ersätt** | Kalkylerna slås ihop eller ersätts. |

## Begränsningar

- Endast JSON-filer kan importeras.
- En fil får vara högst `1 MB`.
- Ogiltiga eller ofullständiga filer stoppas innan något importeras.
- Totalsummor beräknas om automatiskt efter import.

## Bra att veta

- Exporten innehåller kalkylens innehåll och kommentarer.
- Kolumnval, filter och sortering exporteras inte.
- Efter en import kan materialpriser behöva uppdateras. Kör **Prisuppdatering** om du vill använda aktuella prislistor och rabattbrev.
- Spara gärna en export innan du använder **Ersätt**.
- JSON-filer kan innehålla kund- och projektuppgifter. Dela dem bara med personer som ska ha tillgång till informationen.
