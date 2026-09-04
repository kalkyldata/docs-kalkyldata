---
layout: default
title: "Grundbegrepp: del, uppgift och kalkylartikel"
parent: "Kom igång"
nav_order: 4
permalink: /kom-igang/grundbegrepp/
description: "Lär dig hur en kalkyl är uppbyggd med delar, kalkylartiklar och uppgifter."
category: "guide"
tags: ["grundbegrepp", "del", "uppgift", "kalkylartikel"]
audience: "user"
---

# Grundbegrepp: del, uppgift och kalkylartikel

Kalkyldata bygger på några få grundbegrepp. När du förstår hur de hänger ihop blir det enklare att använda både chatten, kalkylpanelen och rapporterna.

## Begreppen i korthet

| Begrepp | Beskrivning |
| --- | --- |
| **Kalkyl** <!-- AI_KEYWORDS: projekt, jobb, arbete, uppdrag --> | Hela projektet eller jobbet du räknar på. Varje kalkyl har en egen konversation med AI-agenten. |
| **Del** <!-- AI_KEYWORDS: delprojekt, sektion, område, etapp, byggnadsdel --> | En gruppering av kalkylartiklar, till exempel `Källare`, `Plan 2` eller `Utomhus`. |
| **Kalkylartikel** <!-- AI_KEYWORDS: recept, arbetsmoment, artikel, moment, kod, receptkod --> | Ett arbetsmoment som innehåller en eller flera uppgifter med material och arbetstid. |
| **Uppgift** <!-- AI_KEYWORDS: arbetsuppgift, moment, rad, arbetsrad, aktivitet --> | Den minsta delen i en kalkylartikel. En uppgift beskriver ett arbetsmoment och kan innehålla material, arbetstid eller båda. |

## Så hänger begreppen ihop

```text
Kalkyl
├── Del
│   ├── Kalkylartikel
│   │   ├── Uppgift
│   │   └── Uppgift
│   └── Kalkylartikel
└── Del
    └── Kalkylartikel
```

Exempel:

```text
Kalkyl: Villa Ekbacken
├── Del: Källare
│   ├── Kalkylartikel: Uttag infälld
│   │   ├── Uppgift: Vägguttag 1-fas
│   │   └── Uppgift: Montage och inkoppling
│   └── Kalkylartikel: Belysningspunkt tak
└── Del: Plan 2
    └── Kalkylartikel: Spotlight undertak
```

Varje uppgift innehåller material, arbetstid eller båda. Summorna räknas sedan ihop stegvis: uppgifter blir kalkylartiklar, kalkylartiklar blir delar och delar blir hela kalkylen.

## Varför är uppdelningen viktig?

- **Delar** gör kalkylen lättare att läsa och används för att gruppera innehållet i rapporter.
- **Kalkylartiklar** gör att du kan återanvända vanliga arbetsmoment istället för att skapa dem från början varje gång.
- **Uppgifter** ger dig kontroll över detaljerna. Du kan ändra material, arbetstid, antal eller pris utan att påverka övriga uppgifter i kalkylartikeln.

## Egna kalkylartiklar

Förutom systemets kalkylartiklar kan du skapa egna för arbeten som du återkommer till.

Du kan också **forka** en befintlig kalkylartikel. Det innebär att du skapar en egen kopia som du kan ändra fritt utan att originalet påverkas.

Egna kalkylartiklar hittar du under **Mina kalkylartiklar** i profilmenyn.

## Bra att veta

- Varje uppgift tillhör en **etapp**, till exempel **Elkanalisation** eller **Elinstallation**. Etappen används för att gruppera och analysera arbetet men är inte en egen nivå i kalkylens struktur.
- Kalkylartiklar från systemets katalog är märkta med källa så att du ser var innehållet kommer ifrån.
- En kalkylartikel som du stjärnmarkerar blir en favorit och prioriteras i snabbsök. Du kan också be AI-agenten att **Visa mina favoriter**.
- AI-agenten använder samma begrepp som visas i kalkylpanelen och rapporterna. Om du till exempel ber AI-agenten skapa en ny **del** eller lägga till en **kalkylartikel** används samma struktur i hela kalkylen.
