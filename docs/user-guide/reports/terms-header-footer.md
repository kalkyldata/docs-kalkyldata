---

layout: default
title: "Validering och felsökning av rapporter"
parent: "Rapporter"
grand_parent: "Användarguide"
nav_order: 5
permalink: /anvandarguide/rapporter/validering/
description: "Förstå varningar och fel i rapportens valideringspanel och kontrollera rapporten innan du skickar offerten."
category: "guide"
tags: ["validering", "varning", "fel", "rapport", "offert", "felsökning"]
audience: "user"
---

# Validering och felsökning av rapporter

Valideringspanelen visar anmärkningar som Kalkyldata hittar i rapportens inställningar och prisberäkning. **Fel** visar sådant som behöver kontrolleras eller rättas. **Varningar** uppmärksammar sådant som kan påverka resultatet och bör kontrolleras innan du skickar rapporten.

## Så hanterar du en anmärkning

1. Öppna rapporten och läs anmärkningarna i valideringspanelen.
2. Identifiera vilken inställning eller rad som anmärkningen gäller.
3. Öppna **Inställningar** om anmärkningen gäller rapportens inställningar.
4. Rätta värdet eller kontrollera den berörda raden.
5. Kontrollera att anmärkningen försvinner.
6. Spara rapporten när du har kontrollerat resultatet.

## Fel

Fel betyder att något i rapportens inställningar eller beräkning behöver rättas. Kontrollera värdet som anges i anmärkningen och ändra det innan du använder rapporten.

Exempel på fel kan vara:

* Ett ogiltigt timpris.
* Ett materialpåslag som ger ett ogiltigt resultat.
* En felaktig rabattsats.
* En arbetstidsjustering som ger ett ogiltigt resultat.
* En prisstrategi som saknar en inställning som krävs för att kunna beräkna priset.
* En restidsregel med ogiltiga värden.

## Varningar

Varningar betyder att Kalkyldata har hittat något som du bör kontrollera. En varning behöver inte betyda att rapporten är fel, men den kan påverka hur priserna beräknas eller vad som visas i rapporten.

Exempel på varningar kan vara:

* Profilen saknar timpris.
* Kalkylen innehåller inga rader som kan prissättas.
* En leverantörsrabatt används inte av någon rad i kalkylen.
* En inställning i prisstrategin påverkar vilka prisregler som används.
* En leverantör eller regel förekommer flera gånger i en prisstrategi.
* En radjustering hänvisar till en rad som inte längre finns.

Kontrollera alltid varningen mot rapportens innehåll innan du skickar offerten.

## Pris saknas för en kalkylartikel

Om Kalkyldata inte hittar ett pris för en kalkylartikel hos de valda leverantörerna får du en varning. Kontrollera då raden och priset innan du skickar rapporten.

Om du behöver använda ett annat pris kan du ange det med en radjustering i rapporten.

## Bra att veta

* Valideringsanmärkningar blockerar inte utskrift eller sparande av rapporten.
* **Radjusteringar** gäller bara rapporten och ändrar inte kalkylen.
* Kontrollera alltid varningar som kan påverka priset innan du skickar en offert.
* Läs mer om hur priserna beräknas i [Prisstrategier och profiler](/anvandarguide/rapporter/prisstrategier-och-profiler/).
