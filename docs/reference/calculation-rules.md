---
layout: default
title: "Beräkningsregler"
parent: "Referens"
nav_order: 3
permalink: /referens/berakningsregler/
description: "Så räknar Kalkyldata fram tid, material och summor från uppgifter till kalkylartiklar, delar och hela kalkylen."
category: "reference"
tags: ["beräkningsregler", "Tid/st", "Tot tid", "Mat.mängd", "Pris/st", "Tot material", "Antal"]
audience: "user"
---

# Beräkningsregler

Kalkyldata räknar fram tid och material på **uppgiftsnivå**. Värdena summeras sedan upp till **kalkylartikeln**, **delen** och slutligen hela **kalkylen**.

Det viktigaste att känna till är att **Antal** och **Mat.mängd** har olika betydelser. **Antal** anger hur många gånger uppgiften utförs, medan **Mat.mängd** anger hur mycket material som används per utförande.

## Så hänger beräkningen ihop

En kalkyl är uppbyggd i fyra nivåer:

```text
Kalkyl
  └── Del
       └── Kalkylartikel
            └── Uppgift
```

**Uppgiften** är den nivå där du anger arbetstid och material. Kalkylartikeln samlar sina uppgifter, delen samlar sina kalkylartiklar och kalkylen samlar sina delar.

Det betyder att en ändring längst ned i strukturen kan påverka flera summeringar högre upp.

## Uppgiften

På uppgiftsnivån finns både arbets- och materialuppgifter.

### Arbete

Arbetstiden utgår från **Antal** och **Tid/st**.

```text
Tot tid = Antal × Tid/st
```

Exempel:

```text
Antal:  12 st
Tid/st: 0,15 h

Tot tid = 12 × 0,15
        = 1,80 h
```

**Enhet** anger vad **Antal** avser, till exempel `st` eller `m`.

**Tid/st** är arbetstiden för en enhet. **Tot tid** är den sammanlagda arbetstiden för uppgiften och räknas fram automatiskt.

För arbetstypen **SV-ATL** hämtas **Tid/st** normalt från tidsdatabasen när en arbetskod finns. För **Övrig tid** fyller du själv i **Tid/st**.

### Material

Materialberäkningen använder tre värden:

* **Antal** — hur många gånger uppgiften utförs
* **Mat.mängd** — hur mycket material som används per utförande
* **Pris/st** — priset för den materialenhet som priset avser

Resultatet visas i **Tot material**.

```text
Tot material = Antal × Mat.mängd × Pris/st
```

Exempel:

```text
Antal:      12 st
Mat.mängd:   1
Pris/st:    42,50 kr

Tot material = 12 × 1 × 42,50
             = 510,00 kr
```

### Mat.mängd och Pris/st

Kolumnen **Pris/st** heter så i kalkyltabellen, men betyder i praktiken pris per materialenhet i prislistan. Materialienheten kan till exempel vara en styck, meter eller förpackning.

**Mat.mängd** ska anges i samma materialenhet som **Pris/st** avser.

Om priset avser en hel förpackning med `50 st` och du använder fyra kabelklammer anger du därför:

```text
Mat.mängd: 4 / 50 = 0,08
Pris/st:   100,00 kr per förpackning
```

Om uppgiften utförs en gång blir materialkostnaden:

```text
1 × 0,08 × 100,00 = 8,00 kr
```

Om uppgiften utförs tre gånger:

```text
3 × 0,08 × 100,00 = 24,00 kr
```

Kalkyldata räknar alltså inte själv om `4 st` till `0,08 förpackning`. **Mat.mängd** ska redan vara angiven i den materialenhet som **Pris/st** använder.

Det är viktigt att skilja på **Antal** och **Mat.mängd**:

| Kolumn           | Betyder                                     |
| ---------------- | ------------------------------------------- |
| **Antal**        | Hur många gånger uppgiften utförs           |
| **Mat.mängd**    | Hur mycket material som används varje gång  |
| **Pris/st**      | Pris för den materialenhet som priset avser |
| **Tot material** | Materialkostnaden för hela uppgiften        |

## Kalkylartikeln

En kalkylartikel består av en eller flera uppgifter.

**Antal** på kalkylartikeln anger hur många gånger hela kalkylartikeln ingår i kalkylen. Det multiplicerar både **Tot tid** och **Tot material** för kalkylartikelns uppgifter.

Exempel:

En kalkylartikel innehåller en uppgift med:

```text
Tot tid:      0,50 h
Tot material: 100,00 kr
```

Om kalkylartikelns **Antal** är `4` blir resultatet:

```text
Tot tid:      0,50 × 4 = 2,00 h
Tot material: 100 × 4   = 400,00 kr
```

På kalkylartikeln visas resultatet som **Tot tid (h)** och **Tot material**.

Det finns alltså två olika **Antal** i kalkylen:

* **Antal** på uppgiften multiplicerar den enskilda uppgiftens tid och material.
* **Antal** på kalkylartikeln multiplicerar hela kalkylartikelns resultat.

## Delen

En **del** samlar kalkylartiklar, till exempel `Kök` eller `Plan 1`.

Delens **Tid (h)** och **Material** är summan av kalkylartiklarna som ingår i delen.

```text
Delens Tid (h)
= summan av kalkylartiklarnas Tot tid

Delens Material
= summan av kalkylartiklarnas Tot material
```

Du ändrar alltså inte delens tid eller material direkt. Ändra i stället uppgifterna eller kalkylartiklarnas **Antal**.

## Kalkylen

Kalkylen som helhet summerar alla delar.

I kalkylens summeringsrad visas:

* **Arbetstid** — total arbetstid
* **Material** — total materialkostnad
* **Delar** — antal delar
* **Artiklar** — antal kalkylartiklar
* **Uppgifter** — antal uppgifter

När du ändrar **Antal**, **Tid/st**, **Mat.mängd** eller **Pris/st** uppdateras beräkningarna och summeringarna högre upp i kalkylen.

## Materialpris

För material av typen **SV-ENR** med E-nummer kan **Pris/st** fyllas i automatiskt. Kalkyldata jämför tillgängliga nettopriser och väljer normalt det lägsta.

Du kan därefter välja en annan **Grossist** för den enskilda uppgiften.

För **Övrigt material** anger du själv materialets benämning och pris.

Läs mer om hur **Pris/st** sätts på [Så här sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).

## Hela beräkningsflödet

Materialet följer detta flöde genom kalkylen:

```text
Antal på uppgiften
  ×
Mat.mängd
  ×
Pris/st
  ↓
Uppgiftens Tot material
  ×
Antal på kalkylartikeln
  ↓
Kalkylartikelns Tot material
  ↓
Delens Material
  ↓
Kalkylens Material
```

Arbetstiden följer motsvarande flöde:

```text
Antal på uppgiften
  ×
Tid/st
  ↓
Uppgiftens Tot tid
  ×
Antal på kalkylartikeln
  ↓
Kalkylartikelns Tot tid (h)
  ↓
Delens Tid (h)
  ↓
Kalkylens Arbetstid
```

Du kan alltså följa varje materialkostnad och arbetstid från den enskilda uppgiften hela vägen till kalkylens totalsumma.

## Bra att veta

* **Tot tid** och **Tot material** är beräknade värden. Ändra i stället de värden som ligger till grund för beräkningen.
* **Antal** på en uppgift och **Antal** på en kalkylartikel har olika funktioner. Uppgiftens **Antal** påverkar uppgiften; kalkylartikelns **Antal** multiplicerar hela kalkylartikeln.
* **Mat.mängd** avser materialåtgång per utförande och ska anges i samma materialenhet som **Pris/st** avser.
* **Pris/st** ska läsas tillsammans med den materialenhet som priset avser. Om priset gäller en förpackning behöver **Mat.mängd** anges som en andel av förpackningen.
* Ändringar av **Antal**, **Tid/st**, **Mat.mängd** eller **Pris/st** påverkar summeringarna på högre nivåer.
