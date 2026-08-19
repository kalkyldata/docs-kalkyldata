---
layout: default
title: "Felmeddelanden och åtgärder"
parent: "Hjälp och felsökning"
nav_order: 2
permalink: /hjalp/felmeddelanden/
description: "Vad varningar och felmeddelanden i kalkylen, rapportvalideringen, importen och kalkylartiklarna betyder och hur du åtgärdar dem."
category: "help"
tags: ["felmeddelande", "varning", "validering", "import", "felsökning"]
audience: "user"
---

# Felmeddelanden och åtgärder

Kalkyldata skiljer på **fel** som stoppar dig och **varningar** som uppmärksammar dig på något som kan behöva åtgärdas. En varning hindrar inte att du sparar eller skriver ut en rapport.

## Fel i rapportvalideringen

Valideringspanelen visas bredvid rapportens förhandsvisning. Där ser du om rapporten innehåller något som behöver åtgärdas innan du använder den.

| Meddelande              | Betyder                                                      | Åtgärd                                                                                     |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Rapporten saknar rader  | Kalkylen är tom eller alla rader är bortfiltrerade           | Kontrollera att kalkylen har innehåll och stäng av **Dölj nollrader**                      |
| Timpris saknas          | Vald prisprofil har inget timpris                            | Öppna fliken **Profil** och fyll i timpriset                                               |
| Kunduppgifter saknas    | Obligatoriska kundfält är tomma                              | Fyll i kundnamn under fliken **Villkor**                                                   |
| Listpris saknas för rad | Prisstrategin är listpris men raden saknar aktuellt listpris | Kalkylartikelns sparade pris används i stället, eller fyll i E-nummer och uppdatera priser |
| Negativt påslag         | Ett påslag är angivet som negativt tal                       | Kontrollera påslagen i prisprofilen                                                        |

## Varningar i kalkylen

Varningar uppmärksammar dig på uppgifter som kan påverka kalkylen.

* **Pris saknas för E-nummer** — E-numret finns inte i prislistan. Kontrollera att E-numret är rätt skrivet, utan mellanslag.
* **Ingen leverantör matchar** — du har inget rabattbrev för leverantören. Läs in rabattbrevet eller använd listpris.
* **Arbetstid saknas** — uppgiftstypen har ingen tid i tidsdatabasen. Fyll i tiden manuellt på raden.

## Fel vid import av kalkyldata

Importen kontrollerar filens format och innehåll innan kalkyldata läggs till.

* **Filformatet känns inte igen** — filen har inte ett format som Kalkyldata kan importera. Använd en JSON-fil i ett format som Kalkyldata stöder.
* **Filen är för stor** — dela upp innehållet i flera filer och importera dem separat.
* **Misstänkt innehåll i texten** — importen innehåller tecken eller innehåll som kan tolkas som kod. Ta bort HTML och skripttaggar ur texten och försök igen.
* **Inget importerades** — kontrollera att filen innehåller uppgifter och att JSON-strukturen är komplett.

## Fel med kalkylartiklar

* **AI-granskningen tog för lång tid** — AI går igenom kalkylartikeln i bakgrunden. Ladda om sidan efter en stund och kontrollera statusen under **Mina kalkylartiklar**.
* **Artikeln har ändrats av någon annan** — du hade en äldre version öppen. Ladda om sidan och gör om ändringen.
* **Utkastet är för stort** — kalkylartikeln innehåller mer innehåll än vad som kan hanteras i ett utkast. Ta bort uppgifter eller dela upp innehållet i flera kalkylartiklar.

## Inloggning och behörighet

* **Du måste vara inloggad** — vissa funktioner kräver konto, till exempel favoriter, egna kalkylartiklar, rabattbrev och sparade rapporter.
* **Sessionen har gått ut** — logga in igen. Kalkylen i den aktuella tråden ligger kvar.
* **Åtkomst nekad** — du försöker öppna något som tillhör ett annat konto.

## Om felet inte försvinner

Ladda om sidan och försök igen. Om problemet kvarstår kan du prova i ett nytt webbläsarfönster.

Om felet fortfarande finns kvar, skicka en felrapport enligt [Kontakta support](/hjalp/kontakt/). Ta gärna med felmeddelandet och vad du gjorde när felet uppstod.
