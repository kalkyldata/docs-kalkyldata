---
layout: default
title: "Prisoptimering"
parent: "Kalkyl"
grand_parent: "Användarguide"
nav_order: 7
permalink: /anvandarguide/kalkyl/prisoptimering/
description: "Byt ut material mot billigare tillåtna alternativ med ersättningsregler och godkänn förslagen innan något ändras."
category: "guide"
tags: ["prisoptimering", "ersättningsregler", "materialpriser", "kalkyl"]
audience: "user"
---
# Prisoptimering
Prisoptimering jämför material i din kalkyl med de alternativ som är tillåtna enligt dina ersättningsregler. Du får förslag på byten och väljer själv vilka som ska genomföras.

Inget material ändras automatiskt.

## Så använder du prisoptimering

1. Öppna kalkylens meny **⋯** uppe till höger i kalkyltabellen.
2. Klicka **Optimera priser med regler…**.
3. Vänta medan Kalkyldata hämtar regler och kontrollerar priser på tillåtna ersättare.
4. Granska de föreslagna bytena i diffen.
5. Avmarkera de byten du inte vill genomföra.
6. Klicka **Byt rader** för att genomföra de markerade bytena.

Längst ned i diffen ser du den sammanlagda kostnadsförändringen för de rader du har markerat.

## Så läser du förslagen

Varje rad i diffen visar ett föreslaget materialbyte.

| Kolumn        | Vad den visar                                                      |
| ------------- | ------------------------------------------------------------------ |
| **Placering** | Var uppgiften finns i kalkylen och vilken regel som föreslår bytet |
| **Byte**      | Artikelnummer före och efter bytet                                 |
| **Mängd**     | Mängd före och efter bytet                                         |
| **Pris**      | Nettopris före och efter bytet                                     |
| **Differens** | Kostnadsförändringen för raden                                     |

Gröna värden visar att bytet minskar materialkostnaden.

### När mängden ändras

En ersättare kan ha en annan förpackningsstorlek eller säljas i en annan enhet.

Då kan ersättningsregeln använda en mängdfaktor som räknar om mängden.

Exempel:

* En kalkylrad innehåller `3` lösa artiklar.
* Ersättaren säljs i en förpackning där en förpackning motsvarar tre artiklar.
* Regeln använder en mängdfaktor som räknar om mängden till rätt antal förpackningar.

Mängdfaktorn påverkar både prisjämförelsen och den nya mängden när du genomför bytet.

## Rader som inte kan optimeras

Ibland hittar prisoptimeringen en ersättningsregel men kan inte föreslå något byte.

Det kan till exempel bero på att ingen tillåten ersättare har ett tillgängligt pris.

Dessa rader visas i varningslistan högst upp i diffen och ändras inte.

## Efter att du har genomfört byten

När du genomför ett byte uppdateras materialinformationen för den nya artikeln.

Kalkyldata:

* hämtar nytt materialnamn
* uppdaterar priset
* uppdaterar leverantören
* tar bort den tidigare produktlänken
* lägger till en systemkommentar med regelns namn och tidigare artikelnummer

Arbetstid påverkas inte av prisoptimeringen.

## Skapa egna ersättningsregler

Du kan skapa egna regler som bestämmer vilka material som får bytas och vilka ersättare som är tillåtna.

1. Öppna kalkylens meny **⋯**.
2. Klicka **Hantera ersättningsregler…**.
3. Klicka **Ny regel**.
4. Välj vilka artiklar regeln ska leta efter.
5. Välj vilka artiklar som får användas som ersättare.
6. Kontrollera att regeln fungerar och spara den.

Du kan skapa regler visuellt i **Byggare** eller använda fliken **JSON** för att klistra in eller redigera en regeluppsättning.

För en fullständig guide till hur ersättningsregler fungerar, se [Ersättningsregler](/avancerat/ersattningsregler/).

## System- och publika regler

Du kan även använda regler som delas av andra.

### Systemregler

Regler märkta **Systemregel** underhålls centralt och är tillgängliga för alla användare.

Du kan:

* visa hur regeln är byggd
* använda regeln i prisoptimeringen
* kopiera regeln till en egen regel

Du kan inte redigera själva systemregeln i Kalkyldata.

Vill du bidra med en ny systemregel eller föreslå en ändring kan du läsa [Bidra med ersättningsregler via GitHub](/avancerat/github-bidrag-ersattningsregler/).

### Publika regler

Publika regler är regler som andra användare har valt att dela.

Du kan visa dem och använda dem som utgångspunkt för dina egna regler.

## Bra att veta

* **Du godkänner alltid själv.** Prisoptimeringen ändrar inget förrän du klickar **Byt rader**.
* **Alla regler körs inte på alla rader.** En regel måste matcha materialet i uppgiften.
* **Ersättare utan pris används inte.** Om ingen tillåten ersättare har ett pris lämnas raden oförändrad.
* **En uppgift kan bara bytas en gång per körning.** Om flera regler matchar används den regel som har högst prioritet.
* **Arbetstid påverkas inte.** Prisoptimeringen ändrar bara material.
* **Du kan köra prisoptimeringen igen.** Nya regler eller ändrade priser kan ge nya förslag.

## Relaterade guider

* [Ersättningsregler](/avancerat/ersattningsregler/)
* [Bidra med ersättningsregler via GitHub](/avancerat/github-bidrag-ersattningsregler/)
