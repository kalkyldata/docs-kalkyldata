---

layout: default
title: "Terminologi"
parent: "Översikt"
nav_order: 2
permalink: /oversikt/terminologi/
description: "Ordlista över de begrepp som används i Kalkyldatas gränssnitt och dokumentation."
category: "reference"
tags: ["terminologi", "kalkyl", "kalkylartikel", "uppgift", "rapport", "ai-agenten"]
audience: "user"
----------------

## Om terminologin

Den här ordlistan förklarar de viktigaste begreppen i Kalkyldata. Samma begrepp används i gränssnittet, användarguiderna och AI-agentens svar.

## Kalkylens nivåer

| Begrepp           | Betyder                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Kalkyl**        | Hela kalkylen för ett arbete. Innehåller delar, kalkylartiklar och uppgifter samt projektinformation som kund, ort och projekttyp.    |
| **Del**           | En grupp i kalkylen som ger struktur åt arbetet, till exempel **Belysning källare** eller **Plan 2**. Varje del har egna summeringar. |
| **Kalkylartikel** | En återanvändbar mall som innehåller en eller flera uppgifter, till exempel **Montage vägguttag infälld**.                            |
| **Uppgift**       | Ett enskilt arbetsmoment med arbetstid och eventuellt material. Uppgiften är den minsta enheten i kalkylen.                           |

En **kalkylartikel** fungerar som en mall. När du lägger till en kalkylartikel i en kalkyl skapas kopior av dess uppgifter i kalkylen. Ändringar i kalkylen påverkar inte den ursprungliga kalkylartikeln.

## Kalkylartiklar och katalogen

| Begrepp             | Betyder                                                                                                                                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Katalog**         | Den gemensamma samlingen av publicerade kalkylartiklar som användare kan söka i.                                                                |
| **Standardartikel** | En kalkylartikel som följer med Kalkyldata. Den kan inte ändras direkt, men du kan skapa en egen kopia genom att forka den.                     |
| **Forka**           | Skapa en egen kopia av en kalkylartikel. Kopian blir fristående från originalet och kan ändras fritt.                                           |
| **Utkast**          | En kalkylartikel som inte är publicerad. Bara du kan se den under **Mina kalkylartiklar**.                                                      |
| **Publicerad**      | En kalkylartikel som är genomgången av AI och sökbar i katalogen.                                                                               |
| **Synlighet**       | Anger vem som kan använda kalkylartikeln. **Privat** betyder att bara du ser den. **Publik** betyder att alla användare kan se och använda den. |
| **Favorit**         | En kalkylartikel som du har markerat med en stjärna. Favoriter används också av AI-agenten när den föreslår kalkylartiklar.                     |

## Material och priser

| Begrepp             | Betyder                                                                                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **E-nummer**        | Artikelnumret som används för att hitta materialet i prislistorna. Ett material utan E-nummer kan inte prisuppdateras genom prislistan. |
| **Listpris**        | Leverantörens ordinarie pris före rabatt.                                                                                               |
| **Nettopris**       | Priset efter den rabatt som gäller enligt dina inlästa rabattbrev.                                                                      |
| **Rabattbrev**      | En leverantörs rabattfil som du läser in för att få fram dina nettopriser.                                                              |
| **Prisuppdatering** | Funktionen som hämtar aktuella priser för materialrader med E-nummer och räknar om priset utifrån dina rabattbrev.                      |

För material med E-nummer jämför Kalkyldata priser från tillgängliga leverantörer och väljer det lägsta nettopriset när priset uppdateras.

## Rapporter och priser

| Begrepp            | Betyder                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Rapport**        | En färdig presentation av kalkylen, till exempel en offert eller materiallista.                                              |
| **Prisprofil**     | Sparade inställningar för bland annat timpris, påslag, moms och ROT.                                                         |
| **Prisstrategi**   | Anger om rapporten ska beräknas med nettopris eller listpris.                                                                |
| **Visning**        | Inställningar som styr vad som visas i rapporten, till exempel gruppering, kolumner, uppgifter, nollrader och sidbrytningar. |
| **Villkor**        | Kunduppgifter, standardavtal, reservationer och egna texter som kan visas i rapportens sidhuvud och sidfot.                  |
| **Sparad rapport** | En sparad ögonblicksbild av kalkylen vid ett visst tillfälle. Den påverkas inte när du senare ändrar kalkylen.               |

## Chat och AI

| Begrepp                | Betyder                                                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Snabbsök**           | Sökfunktionen i chatten som letar direkt bland publicerade kalkylartiklar. Sökningen kräver minst tre tecken.                       |
| **AI-agenten**         | Assistenten i chatten som tolkar det du beskriver, föreslår kalkylartiklar och kan öppna rätt vy.                                   |
| **Verktygsindikering** | Texten som visar vilket steg AI-agenten arbetar med just nu.                                                                        |
| **Inline-knapp**       | En knapp i ett chattsvar som tar dig direkt till en relevant vy, till exempel **Visa kalkyl**.                                      |
| **Projektinfo**        | Informationen om projektet som hjälper AI-agenten att ge mer träffsäkra förslag, till exempel projekttyp, kund, ort och omfattning. |

## Ord som inte används

Använd Kalkyldatas etablerade begrepp konsekvent:

| Undvik             | Använd                              |
| ------------------ | ----------------------------------- |
| artikel            | **kalkylartikel**                   |
| item               | **kalkylartikel**                   |
| task               | **uppgift**                         |
| part               | **del**                             |
| berika / berikning | **AI går igenom** / **AI fyller i** |
| enrichment         | **AI går igenom** / **AI fyller i** |

Tekniska namn som `item`, `task` och `part` kan förekomma i teknisk dokumentation och kod, men ska inte användas som användarbegrepp i gränssnittet eller användarguiderna.
