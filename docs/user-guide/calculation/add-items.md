---
layout: default
title: "Lägg till kalkylartiklar"
parent: "Kalkyl"
nav_order: 3
permalink: /anvandarguide/kalkyl/lagg-till-kalkylartiklar/
description: "Lägg till kalkylartiklar med snabbsök, från AI-agentens förslag eller direkt i kalkylpanelen."
category: "guide"
tags: ["kalkylartikel", "snabbsök", "ai-agenten", "kalkyl"]
audience: "user"
---

Du kan lägga till **kalkylartiklar** på tre sätt: med **snabbsök**, från **AI-agentens förslag** eller direkt i **kalkylpanelen**. En kalkylartikel är ett återanvändbart arbetsmoment som innehåller en eller flera **uppgifter**.

## Lägg till med snabbsök

Snabbsök är det snabbaste sättet att lägga till en kalkylartikel när du redan vet vad du söker.

1. Klicka i chattrutan längst ned.
2. Skriv minst tre tecken av kalkylartikelns namn, kategori, nyckelord eller artikelnummer.
3. Välj en kalkylartikel i listan.
4. Ange **Antal** om kalkylartikeln ska användas flera gånger.
5. Klicka **Lägg till**.
6. Välj en annan del om kalkylartikeln ska placeras någon annanstans.

Snabbsök lägger till kalkylartikeln direkt utan att du behöver vänta på ett AI-svar.

> Snabbsök är inte tillgängligt i kalkylens första meddelande eftersom det används för att skapa och namnge kalkylen.

## Lägg till från AI-agentens förslag

Använd AI-agenten när du vill att systemet ska föreslå lämpliga kalkylartiklar utifrån arbetsbeskrivningen.

1. Beskriv arbetet, till exempel `Installera 12 spottar i undertak på plan 2`.
2. Vänta på AI-agentens förslag.
3. Granska uppgifter, arbetstid och material.
4. Klicka **Lägg till i kalkyl** på de kalkylartiklar du vill använda.
5. Välj del och antal om alternativen visas.

AI-agenten använder din fråga och informationen i [projektinfo](/anvandarguide/chat/projektinfo/) när den väljer kalkylartiklar.

> AI-agenten lägger aldrig till något automatiskt. Du måste alltid bekräfta genom att klicka **Lägg till i kalkyl**.

## Lägg till direkt i kalkylpanelen

Du kan även skapa en tom kalkylartikel direkt i kalkylpanelen. Det används främst när du behöver lägga till specialmaterial, leverantörsofferter, underentreprenörer eller eller skapa ett arbetsmoment som inte redan finns som kalkylartikel.

1. Öppna kalkylpanelen.
2. Expandera den del där kalkylartikeln ska ligga.
3. Klicka **Lägg till kalkylartikel** längst ned i tabellen.
4. Ange ett namn på kalkylartikeln.
5. Expandera kalkylartikeln och klicka **Lägg till uppgift**.
6. Fyll i arbetstid, material och övriga uppgifter.

I de flesta fall går det snabbare att använda en befintlig kalkylartikel och sedan anpassa den efter behov.

## Ändra en tillagd kalkylartikel

När en kalkylartikel har lagts till i kalkylen kan du ändra den utan att originalet påverkas.

Du kan bland annat ändra:

- antal,
- uppgiftens namn,
- moment,
- tid per enhet,
- material,
- materialmängd,
- arbetskod och arbetstyp,
- materialnummer och materialtyp.

Om en kalkylartikel innehåller **0,15 timmar** och **1 vägguttag** och du anger antalet till `4`, räknas både arbetstid och material fyra gånger.

Fält som hämtas automatiskt från SV-ATL eller SV-ENR är låsta tills du byter till en manuell typ. Läs mer i [Så här sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).

## Kontrollera kalkylartikeln

Expandera kalkylartikeln för att kontrollera att:

- antal är korrekt,
- uppgifterna stämmer,
- arbetstiden är rimlig,
- materialnummer och materialmängd är korrekta,
- materialets leverantör och pris ser rätt ut.

## När använder du vilket sätt?

| Arbetssätt | När passar det bäst? |
| --- | --- |
| **Snabbsök** | När du redan vet vilken kalkylartikel du vill lägga till. |
| **AI-agentens förslag** | När du vill att AI-agenten ska föreslå lämpliga kalkylartiklar utifrån arbetsbeskrivningen. |
| **Direkt i kalkylpanelen** | När du behöver lägga till specialmaterial, offerter, UE eller skapa ett eget arbetsmoment. |

## Bra att veta

- Snabbsök kräver minst tre tecken och söker i namn, nyckelord, kategori, artikelnummer och beskrivning.
- Du kan visa kalkylartikelns kort i chatten innan du lägger till den.
- Du kan markera en kalkylartikel som favorit för att hitta den snabbare nästa gång.
- Alla ändringar sparas automatiskt.
- Kontrollera alltid AI-agentens förslag innan du skapar en offert eller materiallista.
