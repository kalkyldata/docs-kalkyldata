---
title: AI-actions
layout: default
parent: Referens
nav_order: 2
permalink: /referens/ai-actions/
description: Referens för tillgängliga AI-actions i Kalkyldata.
category: reference
tags:
  - referens
  - ai-actions
audience: advanced
---

# AI-actions

AI-agenten i Kalkyldata kan utföra ett antal fördefinierade actions via chatten.

## Tillgängliga actions

| Action | Beskrivning |
|---|---|
| `search_items` | Söker efter kalkylartiklar baserat på sökterm. |
| `add_item` | Lägger till en kalkylartikel i aktiv del. |
| `create_part` | Skapar en ny del i kalkylen. |
| `calculate_total` | Beräknar totalkostnad för del eller hela kalkylen. |
| `generate_report` | Genererar en rapport eller offert. |
| `set_quantity` | Sätter mängd för en specifik artikel. |

## Använda actions via chatten
Actions aktiveras automatiskt när AI-agenten tolkar din förfrågan. Du kan också anropa dem explicit med `/action`-syntax, t.ex. `/search_items kabel 2,5`.
