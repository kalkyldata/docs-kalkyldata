---
title: Rapportkonfiguration
layout: default
parent: Referens
nav_order: 4
permalink: /referens/rapportkonfiguration/
description: Teknisk referens för konfiguration av rapporter i Kalkyldata.
category: reference
tags:
  - referens
  - rapportkonfiguration
audience: advanced
---

# Rapportkonfiguration

Detaljerad referens för rapportinställningar och konfigurationsalternativ.

## Tillgängliga rapporttyper
- **Offert** – kundinriktad prissammanställning.
- **Internt underlag** – detaljerad kalkyl för internt bruk.
- **Sammanfattning** – förenklad rapport med totaler per del.

## Konfigurationsalternativ

| Fält | Typ | Beskrivning |
|---|---|---|
| `show_unit_price` | Boolean | Visa à-pris per artikel. |
| `show_quantities` | Boolean | Visa mängder. |
| `group_by_part` | Boolean | Gruppera artiklar per del. |
| `include_terms` | Boolean | Inkludera villkorstext. |
| `logo_url` | String | URL till logotyp. |
| `header_text` | String | Text i sidhuvud. |
| `footer_text` | String | Text i sidfot. |

## PDF-inställningar
- Sidformat: A4 (standard) eller Letter.
- Orientering: Stående eller liggande.
