---
layout: default
title: "Hantera rabattbrev"
parent: "Administration"
nav_order: 3
permalink: /administration/rabattbrev/
description: "Se vilka rabattbrev som är inlästa, ersätt ett rabattbrev när avtalet ändras och uppdatera priser i befintliga kalkyler."
category: "guide"
tags: ["rabattbrev", "leverantör", "nettopris", "prisuppdatering", "administration"]
audience: "user"
---

# Hantera rabattbrev

Ett **rabattbrev** innehåller dina avtalade rabatter hos en grossist. Kalkyldata använder rabattbreven tillsammans med grossisternas listpriser för att räkna fram nettopriser.

Här ser du hur du hanterar rabattbrev när avtal ändras eller när du lägger till en ny leverantör.

Laddar du upp rabattbrev för första gången, se [Ladda upp rabattbrev](/kom-igang/rabattbrev/).

## Så ser du vilka rabattbrev du har

1. Öppna profilmenyn längst ned i sidopanelen till vänster.
2. Klicka på **Rabattbrev**.
3. Kontrollera statusen för respektive leverantör.

Statusen visar vilka leverantörer som har ett inläst rabattbrev och vilka som saknar rabattunderlag.

Om en leverantör saknar rabattbrev kan Kalkyldata fortfarande hitta ett pris, men då används leverantörens listpris utan din avtalsrabatt.

## Så ersätter du ett rabattbrev

När du får ett nytt rabattbrev för ett befintligt avtal behöver du inte ta bort det gamla först.

1. Öppna panelen **Rabattbrev**.
2. Välj leverantören.
3. Ladda upp det nya rabattbrevet.
4. Vänta tills statusen visar att filen är inläst.

Det nya rabattbrevet ersätter det tidigare rabattbrevet för samma leverantör.

Det påverkar framtida prisuppslag. **Priser i befintliga kalkyler ändras inte automatiskt.**

## Så uppdaterar du priser i en befintlig kalkyl

Om du har laddat upp ett nytt rabattbrev och vill använda de nya priserna i en kalkyl behöver du köra en prisuppdatering.

1. Öppna kalkylen.
2. Klicka på **Kalkyl-åtgärder** med tre punkter.
3. Välj **Prisuppdatering**.
4. Granska vilka rader som får nya priser.
5. Bekräfta uppdateringen.

Prisuppdateringen använder de aktuella pris- och rabattuppgifterna och räknar om priserna på de berörda raderna.

Det gör att du själv bestämmer när en pågående kalkyl ska börja använda de nya avtalspriserna.

## När du bör uppdatera

| Situation | Åtgärd |
| --- | --- |
| Du får ett nytt avtal med en grossist | Ladda upp det nya rabattbrevet för leverantören. |
| Du lägger till en ny grossist | Ladda upp rabattbrevet för leverantören så att Kalkyldata kan använda dina avtalspriser. |
| Rabattnivåerna ändras | Ersätt det befintliga rabattbrevet med det nya. |
| En pågående kalkyl fortfarande använder gamla priser | Kör **Prisuppdatering** i kalkylens meny. |
| Du vill använda en annan grossist på en enskild rad | Byt leverantör manuellt på raden eller i kalkylartikelns kort. |

## Så väljs priset

När Kalkyldata gör ett prisuppslag jämförs tillgängliga nettopriser från dina grossister.

Listpriset kombineras med rabattuppgifterna i dina rabattbrev och Kalkyldata kan därefter välja den leverantör som ger det bästa nettopriset.

Du kan fortfarande välja en annan leverantör manuellt på en enskild rad när du vill styra var materialet ska köpas.

Läs mer om hur priset väljs i [Så sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).

## Bra att veta

- Rabattbreven gäller bara ditt konto och delas inte med andra användare.
- Ett nytt rabattbrev ändrar inte automatiskt priser som redan finns i dina kalkyler.
- Använd **Prisuppdatering** när du vill att en befintlig kalkyl ska använda de nya priserna.
- Du kan byta leverantör manuellt på en enskild kalkylrad eller i kalkylartikelns kort.
- Om en leverantör saknar rabattbrev kan listpris användas för den leverantören.
