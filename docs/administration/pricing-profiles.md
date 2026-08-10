---
layout: default
title: "Hantera prisprofiler"
parent: "Administration"
nav_order: 2
permalink: /administration/prisprofiler/
description: "Skapa, kopiera, redigera och ta bort prisprofiler som styr priserna i rapporter."
category: "guide"
tags: ["prisprofil", "prisprofiler", "rapport", "timpris", "materialpåslag", "ROT"]
audience: "user"
---

En **prisprofil** samlar de prisregler du vill använda när du skapar en rapport. Profilen kan innehålla timpriser, materialpåslag, moms, ROT-avdrag och vilken priskälla som ska användas.

När du skapar en rapport väljer du en prisprofil. Kalkyldata använder då profilens inställningar när priserna beräknas.

Vill du förstå hur de olika prisreglerna påverkar priset, läs [Prisstrategier och profiler](/anvandarguide/rapporter/prisstrategier-och-profiler/).

## Så öppnar du prisprofilerna

1. Öppna en rapport eller klicka **Skapa rapport…** i kalkylens meny.
2. Klicka **Inställningar**.
3. Välj fliken för profil.
4. Klicka på länken för att hantera alla profiler.

Du kan även öppna sidan **Prisprofiler** direkt.

## Så skapar du en profil

1. Klicka **Ny profil**.
2. Skriv ett tydligt namn, till exempel `Serviceuppdrag privatkund` eller `Entreprenad utan ROT`.
3. Ange timpris för de arbetstyper du använder.
4. Ange påslag på material.
5. Välj momssats och om ROT ska tillämpas.
6. Välj priskälla, till exempel nettopris via rabattbrev eller listpris.
7. Klicka **Spara**.

Namnge profilerna efter kundtyp eller uppdragstyp. Då blir det enklare att välja rätt profil när du skapar en rapport.

## Så kopierar du en profil

1. Hitta profilen i listan.
2. Klicka på kopieringsikonen.
3. Ändra namnet på kopian.
4. Justera de värden som skiljer sig.
5. Klicka **Spara**.

Att kopiera en profil är praktiskt när du vill skapa en variant av en befintlig profil, till exempel en profil med ROT och en utan ROT.

## Så redigerar du en profil

1. Klicka på pennikonen vid profilen.
2. Justera värdena.
3. Klicka **Spara**.

Ändringar i en prisprofil påverkar inte redan sparade rapporter. En sparad rapport behåller de priser som gällde när rapporten sparades.

## Så tar du bort en profil

1. Klicka på papperskorgsikonen vid profilen.
2. Bekräfta i dialogen.

En borttagen profil kan inte längre väljas när du skapar nya rapporter. Redan sparade rapporter påverkas inte.

## Rapportinställningar i profilen

En prisprofil kan även innehålla inställningar för hur rapporten ska visas, till exempel gruppering och vilka kolumner som ska visas.

## Materialpris saknas

Om ett materialpris saknas för den valda priskällan använder Kalkyldata kalkylpriset och visar en varning i valideringspanelen.

Läs mer i [Validering och felsökning av rapporter](/anvandarguide/rapporter/validering/).
