---
layout: default
title: "Prisstrategier och profiler"
parent: "Rapporter"
grand_parent: "Användarguide"
nav_order: 2
permalink: /anvandarguide/rapporter/prisstrategier-och-profiler/
description: "Så styr prisprofilen timpris, påslag, spill, moms, ROT och vilket materialpris som används i rapporten."
category: "guide"
tags: ["prisprofil", "prisstrategi", "timpris", "påslag", "moms", "ROT", "listpris"]
audience: "user"
---

# Prisstrategier och profiler

En **prisprofil** samlar reglerna som styr hur Kalkyldata räknar fram kundpriset från kalkylens arbetstid och materialkostnader. Profilen kan styra bland annat timpris, påslag, moms, ROT och vilket materialpris som används i rapporten.

Du kan ha flera prisprofiler för olika kundtyper, avtal eller sätt att prissätta arbeten.

## Så väljer och redigerar du en prisprofil

1. Öppna rapporten.
2. Välj en **prisprofil** i listan i toolbaren.
3. Klicka på **Inställningar**.
4. Öppna fliken **Pris & ROT** för att se profilens regler.
5. Klicka på **Hantera profiler** för att öppna profilsidan.
6. Ändra profilens regler.
7. Spara profilen.
8. Gå tillbaka till rapporten.

Ändringar i en prisprofil påverkar nya rapporter som använder profilen. Redan sparade rapporter behåller sina priser.

## Prisregler i profilen

| Regel                        | Vad den gör                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| **Timpris**                  | Anger priset per arbetstimme.                                                                    |
| **Timpris per resurstyp**    | Anger ett eget timpris för en resurstyp, till exempel maskin.                                    |
| **Materialpåslag**           | Lägger till ett procentuellt påslag på materialpriset.                                           |
| **Påslag per resurstyp**     | Lägger till ett materialpåslag som bara gäller en viss resurstyp, till exempel underentreprenör. |
| **Spill**                    | Lägger till en procentuell mängd på materialet för spill, till exempel `3`–`10` %.               |
| **Förbrukningsmaterial**     | Lägger till en dold buffert på materialvärdet för till exempel skruv och tejp.                   |
| **Leverantörsrabatt**        | Ger rabatt på material från en viss grossist.                                                    |
| **Arbets-overhead**          | Lägger till ett påslag på arbetskostnaden.                                                       |
| **Arbetstidsjustering**      | Justerar antalet arbetstimmar upp eller ner.                                                     |
| **Påslag på slutsumman**     | Lägger till ett påslag för till exempel risk eller projektering före kundrabatten.               |
| **Kundrabatt**               | Ger rabatt på slutsumman.                                                                        |
| **Restid och milersättning** | Lägger till en separat rad för restid och körsträcka.                                            |

## Välj materialpris med en prisstrategi

Prisstrategin avgör vilket materialpris som används i rapporten.

| Strategi                      | Så väljs priset                                                           |
| ----------------------------- | ------------------------------------------------------------------------- |
| **Nettopris**                 | Använder priset från kalkylen, inklusive dina rabattbrev.                 |
| **Nettopris med prioordning** | Använder priset från den första grossisten i listan som har artikeln.     |
| **Högsta nettopris**          | Använder det högsta nettopriset bland de valda grossisterna.              |
| **Listpris med rabatt**       | Använder en vald grossists listpris minus den angivna rabatten.           |
| **Listpris med prioordning**  | Använder listpriset från den första grossisten i listan som har artikeln. |
| **Högsta listpris**           | Använder det högsta listpriset bland de valda grossisterna.               |
| **Lägsta listpris**           | Använder det lägsta listpriset bland de valda grossisterna.               |

Om en artikel saknar pris hos de valda grossisterna används kalkylpriset. Du får samtidigt en varning i valideringspanelen så att du kan kontrollera raden.

Rapporten blir alltså inte utan pris om en grossist saknar artikeln, men du bör kontrollera varningen innan du skickar offerten.

### Begränsningar för listprisstrategier

När en listprisstrategi är aktiv används inte **materialpåslag**, **förbrukningsmaterial** eller **leverantörsrabatt**.

Kalkyldata visar en varning om prisprofilen innehåller sådana regler.

## Moms och ROT

* **Moms** ställs in på prisprofilen med en momssats, normalt `25` %.
* **ROT** ställs in på prisprofilen och beräknas på arbetskostnaden inklusive moms.
* Kundens personnummer och fastighetsbeteckning fyller du i under **Pris & ROT** i rapportens inställningar.

Du kan till exempel ha en offertprofil utan moms och en fakturaprofil med moms. Då behöver du inte ändra dessa inställningar manuellt inför varje rapport.

## Bra att veta

* En notruta överst i rapporten visar vilken prisstrategi som används. Du kan stänga av den under **Visning**.
* Du kan sätta ett eget pris på en enskild rad utan att ändra prisprofilen.
* Vilka priser som finns i kalkylen från början beskrivs i [Så här sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).
