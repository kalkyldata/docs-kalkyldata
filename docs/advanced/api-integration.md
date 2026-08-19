---
layout: default
title: "API och integrationer"
parent: "För avancerade användare"
nav_order: 7
permalink: /avancerat/api/
description: "Koppla Kalkyldata till andra system och automatisera utbyte av kalkyldata via API och webhooks."
category: "reference"
tags: ["api", "integration", "webhook", "automation"]
audience: "advanced"
---

# API och integrationer

Kalkyldata kan integreras med andra system så att data kan överföras automatiskt utan manuellt arbete. Integrationer kan till exempel användas för att skicka kalkyldata till ett affärssystem, ta emot kalkylartiklar eller koppla Kalkyldata till egna arbetsflöden.

**API-åtkomst tillhandahålls efter förfrågan.** Det finns inget självbetjäningsflöde för att skapa API-nycklar i appen. Kontakta oss och beskriv vad du vill uppnå, så bedömer vi vilken lösning som passar.

API-åtkomst och integrationsarbete kan vara förenat med en kostnad beroende på integrationens omfattning, användning och eventuella anpassningar. Vi återkommer med upplägg och pris efter att vi har gått igenom behovet.

## Vad en integration kan göra

Exempel på integrationer:

* **Läsa ut kalkyldata** — hämta en färdig kalkyl eller rapport och skicka den vidare till exempelvis ett affärssystem eller en offertportal.
* **Skicka in kalkylartiklar** — skapa eller uppdatera kalkylartiklar automatiskt från ett annat system.
* **Prisunderlag** — automatisera överföring av prislistor eller rabattbrev istället för att ladda upp filer manuellt.
* **Händelser ut** — skicka en avisering när en kalkyl uppdateras eller en rapport skapas, till exempel till ett ärendesystem eller en egen tjänst.
* **Egna arbetsflöden** — koppla Kalkyldata till ett befintligt arbetsflöde, exempelvis för att kontrollera eller överföra information innan en offert skickas.

## Så fungerar en integration

Integrationer använder HTTP-anrop och JSON. Data kan skickas både till och från Kalkyldata beroende på vad integrationen ska göra.

Det finns huvudsakligen två riktningar:

1. **Kalkyldata skickar data till dig.** Kalkyldata skickar en HTTP-POST med JSON till en webhook-adress som du anger när en relevant händelse inträffar.
2. **Du skickar data till Kalkyldata.** Ditt system skickar JSON till en adress som vi tillhandahåller, och Kalkyldata validerar och behandlar datan.

Om du använder ett integrationsverktyg som Make eller Zapier kan det ofta användas som mellanlager mellan Kalkyldata och ditt andra system. Du kan även ansluta ett eget API direkt.

Formatet bygger på samma JSON-struktur som används i Kalkyldata. Se [JSON-formatet för en kalkylartikel](/avancerat/json-format/) och [Utbytesformatet kdx/1](/avancerat/kdx-format/).

## Format och versionering

Integrationer använder dokumenterade format:

| Format               | Används till                                              |
| -------------------- | --------------------------------------------------------- |
| Artikelfil (`itm_*`) | Utbyte av enskilda kalkylartiklar                         |
| `kdx/1`              | Utbyte av en uppgift, kalkylartikel, del eller hel kalkyl |

`kdx/1` innehåller information om format och version i `_kdx`. Det gör att integrationer kan identifiera vilken version av formatet som används.

## Säkerhet

API-åtkomst sätts upp per integration. Vilken autentisering och vilka behörigheter som används beror på integrationens upplägg.

Grundprinciperna är:

* API-nycklar och andra autentiseringsuppgifter ska hanteras som hemligheter.
* Åtkomsten ska begränsas till den data och de funktioner som integrationen behöver.
* Privata kalkylartiklar ska inte exponeras för användare eller system som saknar behörighet.
* Använd HTTPS när data skickas till eller från Kalkyldata.
* Verifiera inkommande anrop innan du behandlar data från en webhook.

## Så begär du åtkomst

Skicka en förfrågan via [Kontakta support](/hjalp/kontakt/) och beskriv:

1. **Vad du vill uppnå** — beskriv behovet med vanliga ord. Exempel: "Vi vill att en färdig offert automatiskt ska skickas till vårt affärssystem."
2. **Vilket system** du vill koppla till Kalkyldata och om systemet har ett API eller kan ta emot webhooks.
3. **Riktning** — ska data skickas från Kalkyldata, till Kalkyldata eller åt båda hållen?
4. **Omfattning** — ungefär hur många kalkyler, kalkylartiklar eller anrop integrationen ska hantera.
5. **Övriga krav** — exempelvis synkronisering, schemalagda körningar eller krav på omedelbar överföring.

Vi går igenom behovet och återkommer med förslag på upplägg, format, autentisering och eventuell kostnad.

## Kostnad

API-åtkomst och integrationer prissätts utifrån omfattningen.

En enkel integration med begränsad användning kan ha andra förutsättningar än en omfattande integration med hög anropsvolym, kontinuerlig synkronisering eller särskilda anpassningar.

**Kontakta oss innan du bygger integrationen**, så kan vi först bekräfta vilket API-upplägg och vilka villkor som gäller för ditt behov.

## Begränsningar

* Det finns inget publikt, självbetjänat API idag. Åtkomst sätts upp manuellt.
* Anropstakten kan begränsas per integration för att skydda systemets stabilitet.
* API-åtkomst innebär inte automatiskt tillgång till all data i Kalkyldata. Åtkomsten styrs av integrationens upplägg och behörigheter.
* AI-agenten är inte ett API. Den är en del av Kalkyldatas användargränssnitt och kan inte användas som en maskinell datatjänst.
