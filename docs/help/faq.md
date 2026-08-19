---

layout: default
title: "Vanliga frågor"
parent: "Hjälp och felsökning"
nav_order: 1
permalink: /hjalp/vanliga-fragor/
description: "Korta svar på vanliga frågor om kalkyler, kalkylartiklar, materialpriser, rapporter och AI-agenten i Kalkyldata."
category: "help"
tags: ["vanliga frågor", "faq", "kalkyl", "priser", "rapport", "ai-agent"]
audience: "user"
---

# Vanliga frågor

Här hittar du korta svar på vanliga frågor om Kalkyldata. Varje svar ger dig det viktigaste direkt och länkar vidare när du behöver mer information.

## Kalkyl och delar

### Sparas min kalkyl automatiskt?

Ja. Kalkylen sparas löpande i din webbläsarsession och kopplas till chattråden. Du behöver inte klicka på någon spara-knapp.

### Vad är skillnaden mellan del, kalkylartikel och uppgift?

En **del** grupperar kalkylartiklar i kalkylen, till exempel ett våningsplan.

En **kalkylartikel** är en återanvändbar mall som innehåller en eller flera uppgifter.

En **uppgift** är det minsta arbetsmomentet i en kalkyl och kan innehålla arbetstid, material eller båda.

Se [Grundkoncept](/kom-igang/grundkoncept/).

### Ändrar jag originalet när jag ändrar en kalkylartikel i kalkylen?

Nej. När du lägger till en kalkylartikel i en kalkyl används en kopia av dess uppgifter. Ändringar du gör i kalkylen påverkar inte den ursprungliga kalkylartikeln.

### Varför syns inte alla kolumner?

Kalkyltabellen visar ett urval av kolumner som standard och anpassar sig efter skärmbredden. Du kan visa eller dölja kolumner i kolumnmenyn.

Se [Kolumnreferens](/referens/kolumner/).

## Materialpriser

### Varifrån kommer materialpriserna?

Materialpriser för artiklar med E-nummer hämtas från prislistor och justeras med de rabattbrev du har läst in. Om flera leverantörer har ett pris för artikeln jämför Kalkyldata nettopriserna och väljer det lägsta.

Se [Materialpriser](/anvandarguide/kalkyl/materialpriser/).

### Varför står det 0 kr på en materialrad?

Det kan bero på att raden saknar E-nummer eller att det saknas ett listpris för E-numret.

Fyll i E-numret och gör en prisuppdatering.

### Hur uppdaterar jag priserna i en gammal kalkyl?

Använd prisuppdateringen i kalkylmenyn. Den kör om prisuppslaget för materialrader med E-nummer.

Prisuppdateringen är särskilt användbar när du har läst in nya rabattbrev eller när priserna i prislistorna har ändrats.

## Kalkylartiklar

### Varför hittar snabbsök inte min kalkylartikel?

Snabbsök söker bland **publicerade** kalkylartiklar och kräver minst tre tecken.

Ett utkast visas inte i snabbsök. Egna utkast hittar du under **Mina kalkylartiklar**.

### Kan jag ändra en publik kalkylartikel?

Inte direkt. Du kan i stället **forka** kalkylartikeln. Då skapar du en egen kopia som du kan ändra utan att påverka originalet.

Se [Forka en kalkylartikel](/anvandarguide/kalkylartiklar/forka/).

### Vem ser mina kalkylartiklar?

En **privat** kalkylartikel kan bara du använda. En **publik** kalkylartikel kan andra användare hitta och använda.

Du väljer kalkylartikelns synlighet när du publicerar den.

## Rapporter

### Varför ändras inte rapporten när jag byter inställning?

Kontrollera vilken del av rapportinställningarna du ändrar:

* **Profil** styr priser.
* **Visning** styr vad som visas.
* **Villkor** styr texter.

Förhandsvisningen uppdateras direkt.

### Varför är en sparad rapport oförändrad när jag ändrar kalkylen?

En sparad rapport är en ögonblicksbild av kalkylen vid det tillfälle då rapporten skapades.

Skapa en ny rapport om du vill att de senaste ändringarna i kalkylen ska komma med.

### Hur får jag en PDF?

Öppna rapporten och skriv ut den. Välj sedan **Spara som PDF** i utskriftsdialogen.

Se [Utskrift och PDF](/anvandarguide/rapporter/utskrift/).

## Chatten och AI-agenten

### Vad är skillnaden mellan snabbsök och AI-agenten?

**Snabbsök** letar direkt efter befintliga kalkylartiklar utifrån bland annat namn och nyckelord.

**AI-agenten** tolkar det du beskriver, föreslår kalkylartiklar och kan hjälpa dig att styra gränssnittet.

Se [Snabbstart](/oversikt/snabbstart/).

### Varför blir det tyst efter att verktygen visats?

AI-agenten kan fortfarande arbeta med din fråga. Tänker-indikeringen ligger kvar tills svaret kommer.

Om det tar ovanligt lång tid kan du skicka frågan igen.

### Kan AI-agenten ändra min kalkyl?

AI-agenten kan föreslå innehåll och öppna rätt vy, men du bekräftar själv innan något läggs till i kalkylen.

Det innebär att du alltid kan granska förslaget innan kalkylen ändras.
