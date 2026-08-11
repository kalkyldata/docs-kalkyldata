---

layout: default
title: "Beräkningsregler"
parent: "Referens"
nav_order: 4
permalink: /referens/berakningsregler/
description: "Så räknar Kalkyldata fram arbetstid, materialkostnad och summor i kalkylen."
category: "reference"
tags: ["beräkningsregler", "arbetstid", "materialkostnad", "summor", "påslag", "moms"]
audience: "user"
---

Här ser du hur Kalkyldata räknar fram arbetstid, materialkostnad och summor i kalkylen. Beräkningen börjar på uppgiftsnivå och summeras sedan till kalkylartiklar, delar och hela projektet.

## Uppgiftsnivå

För varje uppgift beräknas arbetstid och materialkostnad utifrån antal utföranden, tid per enhet, materialmängd och materialpris.

```text
Arbetstid = Tid per enhet × Antal utföranden
Materialkostnad = Materialmängd per utförande × Antal utföranden × Materialpris per enhet
```

### Materialpris per enhet

**Materialpris per enhet** är nettopriset för den pris-enhet som materialet säljs i. Enheten kan till exempel vara styck, meter eller förpackning.

Om materialet säljs i en förpackning om `50 st` och uppgiften använder `4 st`, räknas förbrukningen om till `4/50 = 0,08 förpackning`.

Om förpackningen kostar `100,00 kr` blir materialkostnaden:

```text
0,08 × 100,00 kr = 8,00 kr
```

Kalkylen belastas alltså med den del av förpackningen som används.

**Antal utföranden** anger hur många gånger uppgiften ska utföras. Om uppgiften använder fyra kabelklammer och utförs tre gånger blir den totala materialmängden `3 × 4 = 12 st`.

För en 50-pack motsvarar det:

```text
12/50 = 0,24 förpackning
```

### Kalkylartikelns antal

En kalkylartikel kan ha ett antal som multiplicerar alla uppgifter i kalkylartikeln.

Om en kalkylartikel har `itm_quantity = 3` räknas både arbetstid och materialkostnad för uppgifterna tre gånger.

```text
Kalkylartikelns arbetstid = summan av uppgifternas arbetstid × antal
Kalkylartikelns materialkostnad = summan av uppgifternas materialkostnad × antal
```

Det innebär att du kan använda en kalkylartikel som en återkommande enhet och ange hur många gånger den ska ingå i kalkylen.

## Materialpriser och arbetstid

Vissa värden fylls i automatiskt när Kalkyldata hittar en motsvarande post i sina register.

* **Materialpris** hämtas för material med ett E-nummer. För SV-ENR-material jämför Kalkyldata nettopriser från leverantörerna och väljer det lägsta priset.
* **Materialbenämning** och **leverantör** fylls i automatiskt när ett SV-ENR-material matchas mot prislistan.
* **Arbetstid** fylls i automatiskt för uppgifter med arbetstypen **SV-ATL** när en giltig arbetskod hittas.
* För **Övrig tid** fyller du i arbetsuppgifterna manuellt.
* För **Övrigt material** fyller du i materialuppgifterna manuellt.

### Rabatt och nettopris

För SV-ENR-material används leverantörernas listpriser tillsammans med dina rabattbrev.

Beräkningen sker i följande ordning:

```text
Nettopris = Listpris × (1 − rabatt / 100)
```

Kalkyldata jämför sedan nettopriset mellan leverantörerna och väljer det lägsta priset.

Om du saknar rabattbrev för en leverantör används leverantörens fulla listpris.

## Summering

Kalkyldata summerar uppgifterna i flera nivåer:

```text
Uppgift → Kalkylartikel → Del → Projekt
```

På varje nivå summeras arbetstid och materialkostnad från nivån under.

```text
Kalkylartikelns arbetstid
= SUM(uppgifternas arbetstid) × kalkylartikelns antal

Kalkylartikelns materialkostnad
= SUM(uppgifternas materialkostnad) × kalkylartikelns antal

Delens arbetstid
= SUM(kalkylartiklarnas arbetstid)

Delens materialkostnad
= SUM(kalkylartiklarnas materialkostnad)

Projektets arbetstid
= SUM(delarnas arbetstid)

Projektets materialkostnad
= SUM(delarnas materialkostnad)
```

Det innebär att en ändring av antal, arbetstid eller materialpris påverkar summorna på de överliggande nivåerna.

## Bra att veta

* `itm_quantity` är en multiplikator för hela kalkylartikeln. Ett antal på `3` tredubblar uppgifternas arbetstid och materialkostnad.
* Arbetstid anges i timmar per enhet.
* Materialkostnad beräknas utifrån faktisk materialmängd och materialets pris-enhet.
* Materialpriset för SV-ENR kan ändras om du laddar upp nya rabattbrev eller om masterpriserna ändras. Du kan då köra en prisuppdatering för kalkylen.
