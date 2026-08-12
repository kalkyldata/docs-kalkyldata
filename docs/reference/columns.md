---

layout: default
title: "Kolumnreferens"
parent: "Kalkyl"
nav_order: 8
permalink: /anvandarguide/kalkyl/kolumnreferens/
description: "Förklaring av alla kolumner i kalkyltabellen och kalkylartikelkorten, inklusive innehåll, redigerbarhet och standardvisning."
category: "guide"
tags: ["kolumner", "kalkyl", "kalkylartikel", "uppgift", "tabell"]
audience: "user"
----------------

# Kolumnreferens

Kalkyltabellen visar kalkylen i tre nivåer: **delar**, **kalkylartiklar** och **uppgifter**. Samma kolumner används för kalkylartiklar i kalkyltabellen och i kalkylartikelkorten i chatten. På mobil anpassas visningen och alla kolumner visas därför inte samtidigt.

Varje nivå har sin egen uppsättning kolumner och en egen flik i kolumnmenyn. Här ser du vad varje kolumn innehåller, om du kan redigera den och om den visas från början.

## Tänd och släck kolumner

1. Öppna kalkylpanelen.
2. Klicka **Kolumner** i verktygsraden. Knappen visar hur många kolumner som är aktiva, till exempel `18/24`.
3. Välj fliken **Delar**, **Artiklar** eller **Uppgifter**.
4. Klicka på en kolumn i listan för att tända eller släcka den. En bock betyder att kolumnen visas.
5. Klicka utanför menyn för att stänga den.

Kolumnvalet är en visningsinställning. Det raderar ingen information, ändrar inga värden och påverkar inte kalkylens beräkningar.

Vissa kolumner är alltid synliga och kan därför inte släckas. De behövs för att kunna arbeta med kalkylen, till exempel för att visa namn eller hantera raden.

En pilsymbol bredvid ett kolumnnamn i kolumnmenyn betyder att kolumnen går att sortera på. Klicka på kolumnrubriken i tabellen för att sortera. Klicka igen för att växla mellan stigande och fallande ordning.

## Standardvisning på mobil och dator

På en bred skärm visas de flesta kolumner från början. På en smal mobilskärm visas bara de viktigaste kolumnerna så att innehållet blir lättare att läsa. Du kan tända fler kolumner manuellt via kolumnmenyn.

Kalkylartikelkorten i chatten använder samma kolumner som kalkyltabellen. På mobil anpassas korten och alla kolumner visas därför inte samtidigt.

Kolumnen **Export** är släckt från början på alla nivåer. Den används när du vill exportera data som JSON.

## Kalkylnivån

Kalkylen som helhet har inga egna tabellkolumner. Den visas i stället som en summeringsrad högst upp i kalkylpanelen.

| Fält          | Innehåll                                          |
| ------------- | ------------------------------------------------- |
| **Arbetstid** | Total arbetstid i timmar för hela kalkylen.       |
| **Material**  | Total materialkostnad i kronor för hela kalkylen. |
| **Delar**     | Antal delar i kalkylen.                           |
| **Artiklar**  | Antal kalkylartiklar i kalkylen.                  |
| **Uppgifter** | Antal uppgifter i kalkylen.                       |

Summeringsraden räknas om när du ändrar antal, arbetstid eller materialpris i kalkylen.

## Delnivån

En **del** grupperar kalkylartiklar i kalkylen, till exempel `Plan 1`, `Kök` eller `Belysning`.

| Kolumn       | Innehåll                                                      | Redigerbar | Visas som standard |
| ------------ | ------------------------------------------------------------- | ---------- | ------------------ |
| **Del**      | Delens namn, till exempel Plan 1 eller Kök.                   | Ja         | Ja (låst)          |
| **Innehåll** | Sammanfattning av antal kalkylartiklar och uppgifter i delen. | Nej        | Ja på dator        |
| **Tid (h)**  | Summerad arbetstid för delen.                                 | Nej        | Ja                 |
| **Andel**    | Visar delens andel av kalkylens totala arbetstid.             | Nej        | Ja på dator        |
| **Material** | Summerad materialkostnad för delen.                           | Nej        | Ja                 |
| **Komm.**    | Kommentarer på delen.                                         | Ja         | Ja på dator        |
| **Export**   | Exporterar delen som JSON.                                    | Nej        | Nej                |

## Kalkylartikelnivån

En **kalkylartikel** är en återanvändbar mall som innehåller en eller flera uppgifter. Samma kolumner används för kalkylartiklar i kalkyltabellen och i kalkylartikelkorten i chatten.

| Kolumn           | Innehåll                                                                                                                | Redigerbar | Visas som standard |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------ |
| **Benämning**    | Kalkylartikelns namn.                                                                                                   | Ja         | Ja (låst)          |
| **★**            | Markerar kalkylartikeln som favorit. Favoriter används av AI-agenten för att prioritera dina vanligaste kalkylartiklar. | Ja         | Ja på dator        |
| **Ägare**        | Visar om kalkylartikeln är en systemartikel eller skapad av dig.                                                        | Nej        | Ja på dator        |
| **Källa**        | Länk till kalkylartikelns ursprung för systemartiklar.                                                                  | Nej        | Ja på dator        |
| **Forka**        | Skapar en egen kopia av kalkylartikeln som du kan ändra.                                                                | Nej        | Ja på dator        |
| **Rapport**      | Används för att rapportera fel eller förbättringsförslag på kalkylartikeln.                                             | Nej        | Ja på dator        |
| **Bild**         | Visar en miniatyrbild när kalkylartikeln har en bild.                                                                   | Nej        | Ja på dator        |
| **Kategori**     | Kalkylartikelns kategori.                                                                                               | Ja         | Ja på dator        |
| **Antal**        | Hur många gånger kalkylartikeln ingår i kalkylen. Antalet multiplicerar kalkylartikelns arbetstid och materialkostnad.  | Ja         | Ja                 |
| **Tot tid (h)**  | Kalkylartikelns sammanlagda arbetstid efter att antal har räknats med.                                                  | Nej        | Ja                 |
| **Tot material** | Kalkylartikelns sammanlagda materialkostnad efter att antal har räknats med.                                            | Nej        | Ja                 |
| **Andel**        | Visar kalkylartikelns andel av delens arbetstid.                                                                        | Nej        | Ja på dator        |
| **Beskrivning**  | Fritext som beskriver vad kalkylartikeln omfattar.                                                                      | Ja         | Ja på dator        |
| **Nyckelord**    | Söktermer som gör kalkylartikeln lättare att hitta.                                                                     | Ja         | Ja på dator        |
| **Kommentarer**  | Kommentarer på kalkylartikeln.                                                                                          | Ja         | Ja på dator        |
| **Export**       | Exporterar kalkylartikeln som JSON.                                                                                     | Nej        | Nej                |

## Uppgiftsnivån

En **uppgift** beskriver ett arbetsmoment och kan innehålla arbetstid, material eller både och. Det är på uppgiftsnivån som arbetstid och material anges.

### Arbete

| Kolumn                | Innehåll                                                                         | Redigerbar | Visas som standard |
| --------------------- | -------------------------------------------------------------------------------- | ---------- | ------------------ |
| **Uppgift**           | Uppgiftens namn.                                                                 | Ja         | Ja (låst)          |
| **Moment**            | Byggmoment eller etapp som uppgiften tillhör, till exempel Rör eller Inkoppling. | Ja         | Ja                 |
| **Enhet**             | Enhet för uppgiftens antal, till exempel `st` eller `m`.                         | Ja         | Ja på dator        |
| **Antal**             | Hur många gånger uppgiften utförs.                                               | Ja         | Ja på dator        |
| **Tid/st**            | Arbetstid per enhet i timmar.                                                    | Ja         | Ja på dator        |
| **Tot tid**           | Total arbetstid baserat på tid per enhet och antal.                              | Nej        | Ja                 |
| **Yrkesroll**         | Vilken resurstyp som utför arbetet, till exempel montör.                         | Ja         | Ja på dator        |
| **Arbetstyp**         | Anger vilken typ av arbete uppgiften använder.                                   | Ja         | Ja på dator        |
| **Arbetskod**         | Kod som identifierar arbetsmomentet vid automatiskt tidsuppslag.                 | Ja*        | Ja på dator        |
| **Arbetsbeskrivning** | Beskrivning av arbetsmomentet.                                                   | Ja*        | Ja på dator        |

* För **SV-ATL** fylls arbetskod, arbetstid, yrkesroll och arbetsbeskrivning automatiskt från arbetsregistret. Dessa värden kan inte ändras manuellt. För **Övrig tid** anges arbetsuppgifterna manuellt.

### Material

| Kolumn           | Innehåll                                                                                                                                      | Redigerbar | Visas som standard |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------ |
| **Material**     | Materialets benämning. För **SV-ENR** hämtas benämningen från vald grossist.                                                                  | Ja*        | Ja på dator        |
| **Mat.mängd**    | Materialåtgång per utförande av uppgiften.                                                                                                    | Ja         | Ja på dator        |
| **Pris/st**      | Pris per materialenhet. För **SV-ENR** hämtas priset utifrån vald grossist och aktuella prisuppgifter.                                        | Ja*        | Ja på dator        |
| **Tot material** | Total materialkostnad baserat på materialmängd, pris och antal.                                                                               | Nej        | Ja                 |
| **Grossist**     | Vald grossist för materialet. För **SV-ENR** kan du byta grossist. När du väljer en annan grossist hämtas den grossistens pris och benämning. | Ja         | Ja på dator        |
| **Mat.nummer**   | Materialets artikelnummer, till exempel E-nummer.                                                                                             | Ja*        | Ja på dator        |
| **Mat.typ**      | Anger materialets typ, till exempel standardmaterial eller **Övrigt material**.                                                               | Ja         | Ja på dator        |
| **Länkar**       | Uppslagslänkar till materialet och leverantörernas sortiment när sådana finns.                                                                | Nej        | Ja på dator        |
| **Export**       | Exporterar uppgiften som JSON.                                                                                                                | Nej        | Nej                |

* För **SV-ENR** hämtas vissa materialuppgifter automatiskt från prisinformationen. För **Övrigt material** anges materialuppgifterna manuellt.

När du ändrar **Grossist** för ett **SV-ENR**-material hämtas pris och benämning från den valda grossisten. Du kan göra ändringen direkt i kalkyltabellen eller i kalkylartikelkortet i chatten.

Läs mer om hur priset i **Pris/st** sätts på [Så här sätts materialpriserna](/anvandarguide/kalkyl/materialpriser/).

## Bra att veta

* Beräknade kolumner, till exempel **Tot tid** och **Tot material**, kan inte redigeras. Ändra i stället de värden som ligger till grund för beräkningen.
* Att släcka en kolumn påverkar bara visningen. Informationen finns kvar i kalkylen.
* Kolumnerna för kalkylartiklar används både i kalkyltabellen och i kalkylartikelkorten i chatten.
* På mobil visas ett begränsat antal kolumner för att göra innehållet lättare att läsa.
* Kolumnvalet påverkar kalkyltabellen men styr inte vilka kolumner som visas i en rapport.
* Använd [Sök och filtrera i kalkylen](/anvandarguide/kalkyl/sok-och-filtrera/) när du vill hitta en viss rad eller filtrera kalkylens innehåll.
