---
layout: default
title: "Söksyntax"
parent: "Referens"
nav_order: 2
permalink: /referens/soksyntax/
description: "Syntax för snabbsök i chatten och sökfältet i kalkylen. Använd citattecken, minustecken och fältfilter för att styra sökningen."
category: "reference"
tags: ["snabbsök", "sök", "syntax", "filter", "kalkylartikel"]
audience: "user"
---

# Söksyntax

Snabbsök i chatten och sökfältet i kalkylen använder samma skrivsätt. Med citattecken, minustecken och fältfilter kan du snabbt begränsa sökningen och hitta rätt kalkylartikel eller rad.

## Grundregler för snabbsök

* Sökningen startar när du har skrivit **minst tre tecken**.
* Snabbsök söker i kalkylartikelns **namn**, **nyckelord**, **kategori** och **beskrivning**.
* Träffar i namnet rankas högst. Därefter kommer nyckelord, kategori och beskrivning.
* Sökningen tolererar mindre stavfel och liknande ord.
* Bara **publicerade** kalkylartiklar visas i snabbsök. Egna utkast hittar du under **Mina kalkylartiklar**.
* Snabbsök är inte tillgängligt för det allra första meddelandet i en ny chatt.

## Söksätt

| Skrivsätt      | Betyder                                    | Exempel                 |
| -------------- | ------------------------------------------ | ----------------------- |
| `ord ord`      | Alla ord måste finnas någonstans i träffen | `uttag infälld`         |
| `"exakt fras"` | Söker efter hela frasen i följd            | `"vägguttag infälld"`   |
| `-ord`         | Utesluter träffar som innehåller ordet     | `uttag -utanpåliggande` |
| `nr:`          | Söker på E-nummer                          | `nr:4100112`            |
| `kat:`         | Begränsar sökningen till en kategori       | `kat:belysning armatur` |

Du kan kombinera flera söksätt. Exempel:

```text
kat:belysning "downlight" -dimbar
```

Det söker efter kalkylartiklar i kategorin `belysning`, där frasen `"downlight"` finns, men utesluter träffar som innehåller `dimbar`.

## Stavfel och liknande ord

Snabbsök tolererar mindre stavfel och hittar även ord som liknar det du skriver. En exakt träff rankas högre än en träff som bygger på ett liknande ord.

Skriv därför hellre några få säkra sökord än en lång beskrivning.

Exempel:

```text
vägguttag infälld
```

är bättre än att skriva en hel mening om vad du vill hitta.

## Sökning i kalkylen

Sökfältet ovanför kalkyltabellen filtrerar de rader som redan finns i kalkylen. Sökningen omfattar:

* benämning
* E-nummer
* kommentarer

Du kan kombinera sökningen med kolumnfiltren för att begränsa resultatet ytterligare.

När en sökning är aktiv döljs de delar av kalkylen som inte innehåller någon träff.

**Snabbsök i chatten** används för att hitta kalkylartiklar som du vill lägga till i kalkylen. **Sökfältet i kalkylen** används för att hitta och filtrera sådant som redan finns i kalkylen.

## När sökningen inte ger någon träff

Prova följande:

1. Kontrollera att sökningen innehåller minst tre tecken.
2. Ta bort fältfilter som `nr:` eller `kat:` och sök bredare.
3. Kontrollera att kalkylartikeln är publicerad. Utkast visas inte i snabbsök.
4. Prova färre eller enklare sökord.
5. Beskriv i stället vad du vill göra i chatten och låt AI-agenten föreslå kalkylartiklar.

{: .note }

> Snabbsök hittar kalkylartiklar. Om du inte vet exakt vilken kalkylartikel du behöver kan du beskriva arbetet i chatten och låta AI-agenten föreslå ett upplägg.
