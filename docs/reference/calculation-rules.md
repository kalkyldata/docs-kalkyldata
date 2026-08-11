---

layout: default
title: "Beräkningsregler"
parent: "Referens"
nav_order: 4
permalink: /referens/berakningsregler/
description: "Så räknar Kalkyldata fram tid, material och summor från uppgifter till kalkylartiklar, delar och hela kalkylen."
category: "reference"
tags: ["beräkningsregler", "Tid/st", "Tot tid", "Mat.mängd", "Pris/st", "Tot material", "Antal"]
audience: "user"
---

Kalkyldata räknar fram tid och material på **uppgiftsnivå**. Värdena summeras sedan upp till **kalkylartikeln**, **delen** och slutligen hela **kalkylen**.

Det viktigaste att känna till är att **Antal** och **Mat.mängd** har olika betydelser. **Antal** anger hur många gånger uppgiften utförs, medan **Mat.mängd** anger hur mycket material som går åt varje gång.

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

**Enhet** anger vad `Antal` avser, till exempel `st` eller `m`.

**Tid/st** är arbetstiden för en enhet. **Tot tid** är den sammanlagda arbetstiden för uppgiften och räknas fram automatiskt.

### Material

Materialberäkningen använder fyra värden:

* **Antal** — hur många gånger uppgiften utförs
* **Mat.mängd** — hur mycket material som används per utförande
* **Pris/st** — priset för en materialenhet
* **Tot material** — den beräknade materialkostnaden

Beräkningen är:

```text
Tot material = Antal × Mat.mängd × Pris/st
```

Exempel:

```text
Antal:      12 st
Mat.mängd:   1 st
Pris/st:    42,50 kr

Tot material = 12 × 1 × 42,50
             = 510,00 kr
```

### Mat.mängd och materialets pris-enhet

**Mat.mängd** anger materialåtgången per utförande. **Pris/st** anger priset för den materialenhet som används i beräkningen.

Om ett material säljs i en förpackning om `50 st` och en uppgift använder `4 st`, räknas materialåtgången om till den pris-enhet som **Pris/st** avser.

Om en förpackning kostar `100,00 kr` blir beräkningen:

```text
Mat.mängd: 4 st
Pris/st:   100,00 kr per 50 st

4 / 50 = 0,08
0,08 × 100,00 kr = 8,00 kr
```

Materialkostnaden för ett utförande blir alltså `8,00 kr`.

Om uppgiften utförs tre gånger:

```text
Antal: 3
Mat.mängd: 4 st

3 × 4 = 12 st
12 / 50 = 0,24 förpackning

0,24 × 100,00 kr = 24,00 kr
```

Det är därför viktigt att skilja på **Antal** och **Mat.mängd**:

| Kolumn           | Betyder                                     |
| ---------------- | ------------------------------------------- |
| **Antal**        | Hur många gånger uppgiften utförs           |
| **Mat.mängd**    | Hur mycket material som används varje gång  |
| **Pris/st**      | Pris för den materialenhet som priset avser |
| **Tot material** | Materialkostnaden för hela uppgiften        |

Kolumnreferensen beskriver **Mat.mängd** som materialåtgång per uppgift och **Tot material** som materialmängd × pris per styck × antal.

## Kalkylartikeln

En kalkylartikel består av en eller flera uppgifter.

**Antal** på kalkylartikeln anger hur många gånger hela kalkylartikeln ingår i kalkylen. Det multiplicerar både **Tot tid** och **Tot material** för kalkylartikelns uppgifter.

Exempel:

En kalkylartikel innehåller en uppgift med:

```text
Tot tid:      0,50 h
Tot material: 100,00 kr
```

Om kalkylartikelns **Antal** är `4` blir:

```text
Tot tid:      0,50 × 4 = 2,00 h
Tot material: 100 × 4   = 400,00 kr
```

På kalkylartikeln visas resultatet som **Tot tid (h)** och **Tot material**.

Det innebär att det finns två olika **Antal** i kalkylen:

* **Antal på uppgiften** multiplicerar just den uppgiftens tid och material.
* **Antal på kalkylartikeln** multiplicerar hela kalkylartikelns resultat.

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

För material med E-nummer kan **Pris/st** fyllas i automatiskt. Kalkyldata använder leverantörernas prislistor och dina rabattbrev för att räkna fram nettopriset och väljer det lägsta tillgängliga nettopriset.

Du kan läsa mer om hur **Pris/st** sätts i [Så här sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).

## Hela beräkningsflödet

Ett materialvärde går genom kalkylen i följande ordning:

```text
Antal
  ×
Mat.mängd
  ×
Pris/st
  ↓
Tot material
  ↓
Kalkylartikelns Tot material
  ↓
Delens Material
  ↓
Kalkylens Material
```

Arbetstiden följer motsvarande flöde:

```text
Antal
  ×
Tid/st
  ↓
Tot tid
  ↓
Kalkylartikelns Tot tid (h)
  ↓
Delens Tid (h)
  ↓
Kalkylens Arbetstid
```

Det gör att du kan följa varje materialsumma och varje tidsumma från den enskilda uppgiften hela vägen till kalkylens totalsumma.

## Bra att veta

* **Tot tid** och **Tot material** är beräknade värden. Du ändrar i stället de värden som ligger till grund för beräkningen.
* **Antal** på en uppgift och **Antal** på en kalkylartikel har olika funktioner. Uppgiftens **Antal** påverkar uppgiften; kalkylartikelns **Antal** multiplicerar hela kalkylartikeln.
* **Mat.mängd** avser materialåtgång per utförande. **Antal** anger hur många utföranden som ska räknas.
* **Pris/st** ska läsas tillsammans med den materialenhet som priset avser. Ett förpackningspris kan därför behöva räknas om när bara en del av förpackningen används.
* Ändringar av **Antal**, **Tid/st**, **Mat.mängd** eller **Pris/st** påverkar summeringarna på högre nivåer.
