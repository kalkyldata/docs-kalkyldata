---

layout: default
title: "Prisoptimering"
parent: "Kalkyl"
grand_parent: "Användarguide"
nav_order: 7
permalink: /anvandarguide/kalkyl/prisoptimering/
description: "Sök efter billigare tillåtna ersättningsartiklar i kalkylen och välj själv vilka artikelbyten du vill genomföra."
category: "guide"
tags: ["prisoptimering", "ersättningsregler", "materialpriser", "kalkyl"]
audience: "user"
---

# Prisoptimering

Prisoptimering hjälper dig att hitta billigare tillåtna ersättningsartiklar i kalkylen. Funktionen använder dina ersättningsregler och jämför priser på de artiklar som får ersätta varandra.

Inget ändras automatiskt. Du granskar varje föreslaget byte och väljer själv vilka rader du vill ändra.

## Så använder du prisoptimering

1. Klicka på kalkylens meny **⋯** uppe till höger i kalkyltabellen.
2. Välj **Optimera priser med regler…**.
3. Vänta medan Kalkyldata hämtar ersättningsregler och jämför priser på tillåtna ersättningsartiklar.
4. Granska de föreslagna bytena.
5. Avmarkera de byten du inte vill genomföra.
6. Klicka på **Byt rader** för att genomföra de markerade bytena.

## Granska föreslagna byten

Prisoptimeringen visar en jämförelse för varje rad där ett tillåtet och prissatt alternativ har hittats.

| Kolumn        | Betydelse                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| **Placering** | Visar var uppgiften finns i kalkylen och vilken ersättningsregel som föreslår bytet.                         |
| **Byte**      | Visar vilket artikelnummer som byts ut och vilket artikelnummer som föreslås som ersättare.                  |
| **Mängd**     | Visar mängden före och efter bytet. En ersättningsregel kan ange att mängden ska justeras när artikeln byts. |
| **Pris**      | Visar nettopriset före och efter bytet.                                                                      |
| **Differens** | Visar hur mycket materialkostnaden förändras för raden.                                                      |

Längst ned visas den sammanlagda kostnadsförändringen för de rader du har markerat.

{: .note }

> Grönt visar att bytet sänker kostnaden.

## När inget alternativ kan prissättas

En ersättningsregel kan innehålla flera tillåtna ersättningsartiklar. Om Kalkyldata inte hittar ett pris för någon av dem visas raden i varningslistan.

Raden ändras inte och du behöver inte göra något för att behålla den ursprungliga artikeln.

## Efter ett artikelbyte

När du genomför ett byte uppdateras artikelnumret på den berörda uppgiften.

Kalkyldata sparar också en systemkommentar med:

* vilken ersättningsregel som användes
* tidigare artikelnummer
* datum för bytet

En eventuell produktlänk tas bort eftersom den hörde till den tidigare artikeln.

Arbetstid påverkas inte av prisoptimeringen. Antal och mängd ändras bara om ersättningsregeln uttryckligen anger att mängden ska justeras.

## Skapa egna ersättningsregler

Du kan skapa och hantera egna ersättningsregler från kalkylens meny.

1. Klicka på **⋯** uppe till höger i kalkyltabellen.
2. Välj **Hantera ersättningsregler…**.
3. Skapa eller ändra de regler som ska användas vid prisoptimering.

Läs mer om hur ersättningsregler är uppbyggda i [Ersättningsregler](/advanced/replacement-rules/).

## Bra att veta

* Prisoptimering byter aldrig artiklar automatiskt.
* Du väljer själv vilka föreslagna byten som ska genomföras.
* Endast artiklar som omfattas av en ersättningsregel kan bytas.
* Ett alternativ måste kunna prissättas för att kunna föreslås som ersättare.
* Prisoptimering påverkar inte arbetstid.
* Originalartikeln behålls om du avmarkerar eller avstår från ett föreslaget byte.
