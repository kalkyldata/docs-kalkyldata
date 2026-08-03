---
title: Beräkningsregler
layout: default
parent: Referens
nav_order: 3
permalink: /referens/berakningsregler/
description: Teknisk referens för beräkningsregler i Kalkyldata.
category: reference
tags:
  - referens
  - beräkningsregler
audience: advanced
---

# Beräkningsregler

Dokumentation av hur Kalkyldata beräknar priser, mängder och totaler.

## Grundläggande beräkning

```
Artikelpris = Listpris × (1 - Rabatt%) × (1 + Pålägg%)
Deltotal = Σ (Artikelpris × Mängd) per del
Kalkyltotal = Σ Deltotaler
```

## Avrundningsregler
- Priser avrundas till 2 decimaler.
- Mängder avrundas till konfigurerat antal decimaler per enhet (standard: 2).

## Prisprofiler
En prisprofil kan åsidosätta rabatt och pålägg per artikelgrupp. Prisprofilen appliceras efter grundberäkning.

## Valutahantering
Alla priser lagras i systemvaluta. Valutaomräkning sker vid export med dagskurs.
