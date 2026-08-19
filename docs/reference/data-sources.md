---
layout: default
title: "Prislistor och tidlistor"
parent: "Referens"
nav_order: 6
permalink: /referens/prislistor-och-tidlistor/
description: "Vilka pris- och tidsunderlag Kalkyldata använder för materialpriser och arbetstider, och hur uppgifterna används i kalkylen."
category: "reference"
tags: ["gnp", "prislista", "e-nummer", "ackordstidslista", "atl", "sv-enr", "sv-atl"]
audience: "user"
---

# Prislistor och tidlistor

Kalkyldata använder två typer av grunddata när kalkylen räknas fram:

- **Prisunderlag** för material och grossistpriser.
- **Arbetstidsunderlag** för arbetstid och arbetsmoment.

Den här sidan förklarar vilka underlag som används och hur de kopplas till kalkylen.

## Materialpriser

Kalkyldata använder prislistor från elgrossister som underlag för materialpriser.

Varje materialartikel identifieras med sitt **E-nummer**. När en uppgift använder materialtypen **SV-ENR** används artikelnumret för att hitta motsvarande artikel i prisunderlaget.

### Begrepp

| Begrepp | Betyder |
| --- | --- |
| **E-nummer** | Det artikelnummer som används för att identifiera elmaterial i prisunderlaget. |
| **Listpris** | Grossistens pris före din avtalsrabatt. |
| **Nettopris** | Priset efter den rabatt som gäller enligt ditt rabattbrev. |
| **Rabattbrev** | Underlag med dina avtalade rabatter hos en grossist. |

När Kalkyldata hittar samma artikel hos flera grossister beräknas nettopriset utifrån dina rabattbrev och de tillgängliga prisuppgifterna. Kalkyldata kan därefter välja den grossist som ger det lägsta nettopriset.

Läs mer om [hur materialpriserna sätts](/anvandarguide/kalkyl/materialpriser/) och [hur du hanterar rabattbrev](/administration/rabattbrev/).

### Om ett pris saknas

Om ett artikelnummer inte kan hittas i prisunderlaget kan Kalkyldata inte göra ett normalt `SV-ENR`-uppslag för artikeln.  Prisuppslaget faller tillbaka till det uppskattade pris som är angivet i uppgiften.

Du kan använda **Övrigt material** om materialet ska anges manuellt.

## Arbetstider

Kalkyldata använder **Elektrikernas ackordstidslista 2019** som underlag för arbetstider.
Ackortstidslistan går, i sin helhet, att ladda ner på Elektrikernas hemsida:
https://www.sef.se/stod-pa-jobbet/jobba-pa-ackord/ackordstidlistan/

Tidlistan innehåller arbetsmoment med tillhörande arbetskoder och tider. När en uppgift använder arbetstypen **SV-ATL** kan Kalkyldata slå upp uppgifterna utifrån arbetskoden.

### Begrepp

| Begrepp | Betyder |
| --- | --- |
| **Arbetskod** | Koden som identifierar ett arbetsmoment i arbetstidslistan. |
| **Ackordstid** | Den tid som anges för arbetsmomentet i tidlistan. |
| **SV-ATL** | Arbetstypen i Kalkyldata som använder arbetskoden för tidsuppslag. |
| **Övrig tid** | Arbetstypen som används när du själv vill ange arbetstiden. |

När en `SV-ATL`-kod ger träff fyller Kalkyldata i arbetsbeskrivning, tid per enhet och resurstyp från underlaget. Dessa värden kan då inte redigeras direkt på raden.

Om arbetskoden inte ger någon träff kan ett värde som redan finns angivet i kalkylartikeln användas som reserv. Det gör att en kalkylartikel kan innehålla en användbar tid även om ett aktuellt tidsuppslag saknas.

Vill du ange arbetstiden helt själv använder du **Övrig tid**.

### Arbetskod

En arbetskod för SV-ATL i Kalkyldata består av fem delar som anger var arbetsmomentet finns i ackordstidslistans struktur.

Exempel för arbetstyp **SV-ATL** och arbetskod **`208502101`**

* `20` – **Lista**
* `8` – **Del**
* `502` – **Grupp**
* `10` – **Rad**
* `1` – **Tillägg**

Arbetskoden `208502101` i kombination med arbetstyp SV-ATL betyder alltså **Lista 20, Del 8, Grupp 502, Rad 10, Tillägg 1**.
Arbetskoden `208502101` avser montage av  **Utvändig apparat med 1 kabel och 3 inkopplingar av ledare**. Ackordstiden är 0,18 tim för momentet.

## Uppslag och manuella värden

`SV-ATL` och `SV-ENR` är till för uppslag mot Kalkyldatas underlag. Det är därför normalt bäst att ange arbetskod respektive artikelnummer när motsvarande underlag finns.

Samtidigt kan en kalkylartikel innehålla värden som fungerar som reserv om ett uppslag inte ger någon träff.

Det innebär att du kan bygga kalkylartiklar som både använder aktuella uppgifter när de finns och fortfarande har ett användbart grundvärde om ett uppslag saknas.

## Bra att veta

- Prisunderlag och rabattbrev påverkar materialpriset, men inte den materialmängd du har angett.
- Arbetstidsunderlaget påverkar uppgiftens tid när `SV-ATL` används.
- Pris- och tidsuppslag kan ändras när underliggande data uppdateras.
- Befintliga kalkyler räknas inte automatiskt om bara för att prisunderlaget eller ett rabattbrev ändras. Använd **Prisuppdatering** när du vill uppdatera priser i en befintlig kalkyl.
- Behöver du ange en egen arbetstid använder du **Övrig tid**.
- Behöver du ange ett material utan prisuppslag använder du **Övrigt material**.

Läs mer om hur värdena används i kalkylen i [Beräkningsregler](/referens/berakningsregler/).
