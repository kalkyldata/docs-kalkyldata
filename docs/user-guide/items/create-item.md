---

layout: default
title: "Skapa egna kalkylartiklar"
parent: "Kalkylartiklar"
grand_parent: "Användarguide"
nav_order: 1
permalink: /anvandarguide/kalkylartiklar/skapa/
description: "Så skapar du en egen kalkylartikel i Kalkyldata, lägger till uppgifter, sparar ett utkast och publicerar artikeln."
category: "guide"
tags: ["kalkylartikel", "skapa", "utkast", "publicera", "uppgifter"]
audience: "user"
---

Skapa en egen **kalkylartikel** när du vill återanvända samma kombination av arbetsmoment och material. Du kan bygga artikeln från grunden, hämta uppgifter från en befintlig kalkylartikel eller importera kalkyldata från en JSON-fil.

## Så skapar du en kalkylartikel

1. Öppna **Mina kalkylartiklar** i profilmenyn längst ned i sidopanelen.
2. Klicka på **Ny kalkylartikel**.
3. Fyll i **Benämning**. Använd ett namn som gör artikeln lätt att hitta, till exempel `Vägguttag 1-fas infälld`.
4. Lägg till **uppgifter** på ett av tre sätt:

   * **Manuellt** — lägg till arbetsmoment med arbetstid och material.
   * **Kopiera från befintlig artikel** — sök fram en kalkylartikel och hämta hela eller delar av dess uppgiftslista.
   * **Importera JSON** — importera kalkyldata som du har exporterat tidigare.
5. Fyll i **Beskrivning** och **Antal** om artikeln normalt används med ett visst antal.
6. Välj **Synlighet**: `Privat` om bara du ska kunna använda artikeln eller `Publik` om andra inloggade användare ska kunna hitta och använda den.
7. Klicka på **Publicera** när artikeln är klar.

Utkastet sparas medan du arbetar. Du kan lämna sidan och fortsätta senare. Artikeln ligger kvar med status **Utkast** tills du publicerar den.

## Vad händer när du publicerar?

När du publicerar en kalkylartikel går den igenom följande statusar:

| Status            | Vad det betyder                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| **Utkast**        | Kalkylartikeln är inte publicerad och är bara tillgänglig för dig.                                  |
| **AI går igenom** | AI-agenten går igenom kalkylartikeln och fyller i information som behövs för sökning och katalogen. |
| **Publicerad**    | Kalkylartikeln är klar och kan sökas fram enligt den valda synligheten.                             |

När AI-agenten är klar fylls bland annat **Kategori** och **Nyckelord** i. Dessa används för att göra kalkylartikeln lättare att hitta.

## Fält i kalkylartikeln

| Fält            | Används till                                                                         |
| --------------- | ------------------------------------------------------------------------------------ |
| **Benämning**   | Namnet på kalkylartikeln och det viktigaste fältet för att identifiera den.          |
| **Beskrivning** | Förklarar vad kalkylartikeln innehåller och när den ska användas.                    |
| **Kategori**    | Kategoriserar kalkylartikeln och används bland annat vid sökning.                    |
| **Nyckelord**   | Alternativa ord och uttryck som hjälper dig och AI-agenten att hitta kalkylartikeln. |
| **Antal**       | Förvalt antal när kalkylartikeln läggs in i en kalkyl.                               |
| **Bild**        | Bild som hjälper till att identifiera kalkylartikeln.                                |
| **Synlighet**   | Anger om kalkylartikeln är `Privat` eller `Publik`.                                  |
| **Uppgifter**   | Kalkylartikelns arbetsmoment med arbetstid och material.                             |

## Bra att veta

* En kalkylartikel utan uppgifter kan sparas som utkast, men innehåller inget som kan användas i en kalkyl. Lägg till minst en uppgift innan du publicerar artikeln.
* AI-agenten går igenom kalkylartikeln när du publicerar den och fyller i information som behövs för sökning.
* Standardartiklar från Kalkyldata går inte att redigera. Använd [Forka och anpassa](/anvandarguide/kalkylartiklar/forka/) om du vill skapa en egen version.
* När du använder en kalkylartikel i en kalkyl får kalkylen en egen kopia av artikelns uppgifter. Senare ändringar i kalkylartikeln påverkar därför inte kalkyler som redan använder den.
