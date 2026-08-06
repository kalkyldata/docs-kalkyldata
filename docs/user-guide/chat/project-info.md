---
layout: default
title: "Projektinfo"
parent: "Chat och AI-agenten"
grand_parent: "Användarguide"
nav_order: 5
permalink: /anvandarguide/chat/projektinfo/
description: "Fyll i projektinfo i Kalkyldata så att AI-agenten känner till projekttyp, omfattning, segment, beställare och standardavtal och kan ge mer relevanta förslag."
category: "guide"
tags: ["projektinfo", "ai-agent", "chat", "kontext", "standardavtal", "rot"]
audience: "user"
---

# Projektinfo

Projektinfo är den korta beskrivningen av projektet som AI-agenten läser innan den svarar. När du fyllt i den vet agenten om det gäller nybyggnad eller renovering, villa eller kontor, och vilket standardavtal som gäller — och förslagen träffar mycket bättre. Du fyller i projektinfo en gång per kalkyl.

## Så använder du projektinfo

1. Öppna **Projektinfo** överst i kalkylpanelen, eller skriv `Öppna projektinfo` i chatten.
2. Välj **Projekttyp** och **Omfattning**.
3. Välj **Segment / Byggtyp**, **Beställartyp** och **Status**.
4. Välj **Standardavtal** om ett avtal gäller.
5. Fyll i **Kund** och **Ort**.
6. Skriv en kort **Projektbeskrivning** med det som är speciellt för jobbet, till exempel `Renovering av 1970-talsvilla, befintlig elcentral byts`.
7. Stäng panelen. Uppgifterna sparas direkt och följer med i varje fråga du ställer.

## Fälten och vad de påverkar

| Fält | Val | Varför det spelar roll |
| --- | --- | --- |
| Projekttyp | `Nybyggnad`, `Renovering`, `Tillbyggnad`, `Underhåll` | Renovering ger normalt mer rivning, håltagning och tidspåslag än nybyggnad |
| Omfattning | `Liten`, `Medel`, `Stor` | Styr detaljnivån i förslagen |
| Segment / Byggtyp | `Villa`, `Flerbostadshus`, `Kontor`, `Industri`, `Infrastruktur` | Avgör materialval och installationsstandard |
| Beställartyp | `Privat`, `Kommun`, `BRF`, `Entreprenör`, `Fastighetsbolag` | Privatperson kan innebära ROT; offentlig beställare andra krav |
| Status | `Offert`, `Pågående`, `Vunnen`, `Förlorad` | Håller ordning på dina kalkyler i listan |
| Standardavtal | `AB 04`, `ABT 06`, `ABS 18`, `Hantverkarformuläret 17` med flera | Följer med till offerten och styr villkorstexten |
| Kund och Ort | Fritext | Följer med till rapporten och ger agenten sammanhang |
| Projektbeskrivning | Fritext | Det du inte får plats med i valen: förutsättningar, begränsningar, önskemål |

Fälten du inte fyller i lämnas tomma — agenten gissar inte.

## Exempel på skillnaden

Utan projektinfo tolkar agenten `Byt elcentral` som ett generellt moment.

Med **Projekttyp: Renovering**, **Segment: Villa** och beskrivningen `Befintlig central från 1972, ny jordfelsbrytare krävs` föreslår agenten i stället rivning av gammal central, ny normcentral med jordfelsbrytare och rimlig arbetstid för trång utrymme.

## Bra att veta

- Projektinfo gäller per kalkyl. Varje konversation i sidopanelen har sin egen projektinfo.
- Du kan ändra uppgifterna när som helst under arbetet. Ändringen påverkar kommande svar, inte de kalkylartiklar du redan lagt till.
- Kund, ort och avtal återanvänds när du skapar en offert, så du slipper skriva in dem två gånger.
- Skriv aldrig personuppgifter du inte behöver. Kundens namn och ort räcker.
