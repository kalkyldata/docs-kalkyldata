---
layout: default
title: "Projekthandlingar"
parent: "Chat och AI-agenten"
grand_parent: "Användarguide"
nav_order: 6
permalink: /anvandarguide/chat/projekthandlingar/
description: "Ladda upp förfrågningsunderlag och tekniska beskrivningar i Kalkyldata och låt AI-agenten använda handlingarna som källa när den svarar på frågor och väljer kalkylartiklar."
category: "guide"
tags: ["projekthandlingar", "underlag", "ai-agent", "chat", "källhänvisning", "pdf"]
audience: "user"
---

# Projekthandlingar

Ladda upp förfrågningsunderlag, tekniska beskrivningar och andra projekthandlingar i Kalkyldata. AI-agenten kan sedan använda handlingarna som källa när den svarar på frågor, föreslår eller väljer kalkylartiklar och hjälper dig att bygga kalkylen.

## Ladda upp en handling

1. Öppna **Projektinfo** överst i chatten.
2. Fäll ut **Handlingar**.
3. Dra in filen i uppladdningsområdet eller klicka för att välja en fil.
4. Vänta tills statusen visar **Klar**.

Du kan också klicka på gemet i skrivrutan för att ladda upp en handling.

Handlingarna hör till den konversation du står i. När du byter konversation visas handlingarna som hör till den konversationen.

## Filer som fungerar

Du kan ladda upp följande filtyper:

| Fungerar                | Fungerar inte |
| ----------------------- | ------------- |
| PDF                     | DWG           |
| Word (`.doc`, `.docx`)  | DXF           |
| Excel (`.xls`, `.xlsx`) | IFC           |
| Textfiler               | RVT           |

En fil får vara högst **5 MB**.

Om du laddar upp samma fil igen i samma kalkyl används den redan inlästa versionen.

### Skannade PDF-filer

Skannade PDF-filer läses med textigenkänning. Resultatet kan bli sämre än för en PDF som innehåller ett riktigt textlager.

Ladda därför helst upp originalfilen när du har tillgång till den.

## Fråga om handlingarna

När en handling har status **Klar** kan AI-agenten söka i innehållet. Skriv frågan direkt i chatten, till exempel:

* `Vad säger handlingarna om belysningen?`
* `Vilka krav finns på kanalisation i kontorsdelen?`
* `Sammanfatta förfrågningsunderlaget.`
* `Vilka kalkylartiklar är relevanta utifrån kraven i underlaget?`

AI-agenten använder innehållet i de uppladdade handlingarna som underlag för svaret.

### Kalkylera utifrån handlingarna

Du kan också be AI-agenten att hjälpa dig hitta rätt kalkylartiklar utifrån kraven i handlingarna. Agenten använder då både **projekthandlingarna och Kalkyldatas katalog** som underlag.

Exempel:

* `Vilka kalkylartiklar behöver jag för belysningen enligt beskrivningen?`
* `Hitta kalkylartiklar för kanalisation enligt kraven i underlaget.`
* `Vad behöver jag ta med i kalkylen för brandlarm enligt handlingarna?`

På så sätt kan projekthandlingarna användas som projektets kravunderlag när AI-agenten hjälper dig att hitta rätt kalkylartiklar.

### Källhänvisningar

När svaret bygger på en projekthandling visas källhänvisningar med **filnamn och sida**. Klicka på en källhänvisning för att se det textstycke som svaret bygger på.

Om AI-agenten inte hittar stöd för ett påstående i de uppladdade handlingarna anger den det i stället för att gissa.

## Status för uppladdningen

När du laddar upp en handling visas aktuell status:

| Status           | Betyder                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| **Laddas upp**   | Filen skickas till Kalkyldata.                                         |
| **Läses in**     | Texten hämtas ut och görs sökbar. Det tar oftast under en minut.       |
| **Klar**         | AI-agenten kan söka i handlingen. Antalet sidor visas.                 |
| **Misslyckades** | Något gick fel vid inläsningen. Orsaken visas och du kan försöka igen. |

En vanlig orsak till att en handling inte kan läsas in är att filen saknar text, till exempel en ritning som har sparats som PDF utan textlager.

## Ta bort en handling

Klicka på **papperskorgen** bredvid handlingen och bekräfta borttagningen.

Både filen och den sökbara texten raderas. AI-agenten kan därefter inte längre använda handlingen som underlag.

## Sekretess

Uppladdade handlingar är privata. Andra användare kommer inte åt dina filer.

AI-agenten använder relevanta delar av handlingarna som underlag när den svarar på dina frågor och hjälper dig med kalkylen.

## Bra att veta

* Ladda helst upp originaldokument med ett textlager i stället för inskannade PDF-filer.
* Använd tydliga frågor när du vill att AI-agenten ska hitta krav i en specifik handling.
* När AI-agenten föreslår kalkylartiklar utgår den från både innehållet i projekthandlingarna och informationen i Kalkyldatas katalog.
* En handling måste ha status **Klar** innan AI-agenten kan söka i den.

## Relaterat

* [Projektinfo](/anvandarguide/chat/projektinfo/)
* [Skriv effektiva frågor](/anvandarguide/chat/effektiva-fragor/)
