---
title: n8n-integration
layout: default
parent: Referens
nav_order: 5
permalink: /referens/n8n-integration/
description: Integrera Kalkyldata med n8n för automatiserade arbetsflöden.
category: reference
tags:
  - referens
  - n8n
  - integration
audience: advanced
---

# n8n-integration

Kalkyldata kan integreras med n8n för att automatisera arbetsflöden och koppla ihop system.

## Förutsättningar
- En fungerande n8n-installation.
- API-nyckel från Kalkyldata (finns under **Administration** > **Integrationer**).

## Sätt upp anslutningen
1. I n8n, skapa en ny **HTTP Request**-nod.
2. Ange Kalkyldata API-URL och autentisera med din API-nyckel.
3. Välj metod (GET, POST, etc.) beroende på åtgärd.

## Exempel på automatiseringsflöden
- **Ny order → ny kalkyl**: skapa automatiskt en kalkyl när en order registreras i ett annat system.
- **Kalkyl klar → notis i Slack**: skicka ett meddelande när en kalkyl godkänns.
- **Prislistuppdatering → synk**: importera nya prislistor automatiskt.

## API-dokumentation
Se den fullständiga API-dokumentationen i Kalkyldata under **Administration** > **Integrationer** > **API-docs**.
