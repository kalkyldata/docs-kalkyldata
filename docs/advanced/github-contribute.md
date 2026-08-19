---
layout: default
title: "Bidra till artikelbiblioteket via GitHub"
parent: "För avancerade användare"
nav_order: 5
permalink: /avancerat/github-bidrag/
description: "Lägg till eller ändra kalkylartiklar i Kalkyldatas gemensamma bibliotek via GitHub."
category: "reference"
tags: ["github", "bidrag", "kalkylartikel", "bibliotek", "publicering"]
audience: "advanced"
---

# Bidra till artikelbiblioteket via GitHub

Kalkyldatas gemensamma artikelbibliotek består av JSON-filer i ett GitHub-repo. Varje fil beskriver en **kalkylartikel** med en eller flera **uppgifter**.
Du hittar arkivet här: https://github.com/kalkyldata/items 

När en fil läggs till eller ändras kan det automatiska flödet läsa in ändringen, låta AI gå igenom kalkylartikeln och publicera den i katalogen. När kalkylartikeln är publicerad kan användare hitta den i snabbsök och AI-agenten kan föreslå den.

Vill du bara använda en kalkylartikel själv behöver du inte GitHub. Skapa eller importera den under **Mina kalkylartiklar** istället.

## Mappstruktur och filnamn

Mapparna används för att organisera kalkylartiklarna. Filnamnet är en slug av kalkylartikelns benämning.

```text
ELINSTALLATION/
└── KABEL/
    └── INSTALLATIONSKABEL/
        └── eqlq-3g1-5-i-kanal.json
DATA/
└── PATCHPANEL/
    └── patchpanel-kat6a-utp-24-portar.json
```

Följ dessa regler för filnamn:

* Använd små bokstäver.
* Använd bindestreck mellan orden.
* Skriv `å` som `a`, `ä` som `a` och `ö` som `o`.
* Använd inga mellanslag eller specialtecken.
* Använd en JSON-fil per kalkylartikel.

Placera filen i den mapp som bäst beskriver **arbetet**, inte det enskilda materialet. En kalkylartikel för montering av en patchpanel hör exempelvis hemma under data och patchpanel, inte under kabel.

## Så går ett bidrag till

1. Skapa en egen gren eller en fork av repot.
2. Lägg till eller ändra JSON-filen enligt [JSON-formatet för en kalkylartikel](/avancerat/json-format/).
3. Kontrollera JSON-filen enligt [Validera och felsök din JSON](/avancerat/validera-json/).
4. Öppna en pull request och beskriv kort vad kalkylartikeln avser och vilket underlag som används för arbetstiderna.
5. Efter granskning och merge läser det automatiska flödet in ändringen.
6. Kalkylartikeln går igenom den automatiska behandlingen och publiceras i katalogen.
7. När publiceringen är klar kan användare hitta kalkylartikeln i snabbsök och AI-agenten kan föreslå den.

Om en fil tas bort avpubliceras motsvarande kalkylartikel.

## Källa till kalkylartikeln

Kalkylartiklar som kommer från artikelbiblioteket har en **Källa**-ikon i kolumnen med samma namn. Länken går till JSON-filen på GitHub.

Där kan du se vilket underlag som ligger bakom kalkylartikeln, inklusive uppgifter, arbetskoder och materialnummer.

Egna kalkylartiklar som du har skapat i **Mina kalkylartiklar** har ingen sådan GitHub-länk.

## Vad fylls i automatiskt?

Det automatiska flödet kan komplettera kalkylartikeln med bland annat:

* sökord
* kategori
* beskrivning

Materialuppgifter och arbetstidsuppgifter hanteras däremot utifrån de data som finns i kalkylartikelns uppgifter och Kalkyldatas uppslagsdata.

För material med typen `SV-ENR` används E-numret för prisuppslag. Kalkyldata kan då hämta aktuell materialbenämning, pris och leverantör utifrån användarens prisunderlag.

För arbetsuppgifter med typen `SV-ATL` används arbetskoden för att slå upp arbetsbeskrivning, arbetstid och resurstyp.

Du kan därför fokusera JSON-filen på själva kalkylartikeln och dess uppgifter. Lägg gärna till egna sökord när du känner till branschuttryck som användarna kan tänkas söka på.

## Vad gör en bra kalkylartikel?

En bra kalkylartikel beskriver ett tydligt och återanvändbart arbetsmoment. Den bör innehålla tillräckligt med information för att en annan kalkylator ska förstå vad som ingår utan att behöva läsa källfilen.

Tänk särskilt på:

* en tydlig och beskrivande benämning
* relevanta uppgifter
* korrekta arbetskoder när `SV-ATL` används
* korrekta E-nummer när `SV-ENR` används
* rimliga mängder och enheter
* relevanta egna sökord
* tydliga kommentarer när något behöver förklaras

## Innan du öppnar en pull request

Kontrollera JSON-filen med [Validera och felsök din JSON](/avancerat/validera-json/).

Kontrollera särskilt att:

* JSON-syntaxen är korrekt
* kalkylartikelns benämning är tydlig
* alla uppgifter har rätt struktur
* arbetskoder och E-nummer är korrekta
* mängder och enheter stämmer
* befintliga sökord och annan information inte tas bort av misstag
