---
layout: default
title: "JSON-formatet för en kalkylartikel"
parent: "För avancerade användare"
nav_order: 2
permalink: /avancerat/json-format/
description: "Fältreferens för en kalkylartikel i JSON: itm-fält på rotnivå, tsk-fält per uppgift, tidsuppslag med SV-ATL och prisuppslag med SV-ENR."
category: "reference"
tags: ["json", "itm", "tsk", "sv-atl", "sv-enr", "kalkylartikel", "fältreferens"]
audience: "advanced"
---

# JSON-formatet för en kalkylartikel

En kalkylartikel skrivs som ett JSON-objekt med fält som börjar på `itm_` och en lista `itm_tasks` där varje uppgift har fält som börjar på `tsk_`. Fältnamnen är på engelska, värdena på svenska. Den här sidan går igenom varje fält, vad som händer om du utelämnar det och hur uppslagen mot arbetstidslistan och prislistan fungerar.

## Minsta möjliga fil

```json
{
  "itm_name": "RJ45 modularjack kat6A UTP",
  "itm_tasks": [
    {
      "tsk_name": "Ijackning och kontaktering",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "2020759-UTP",
      "tsk_total_quantity": 1,
      "tsk_quantity_unit": "st",
      "tsk_material_type": "SV-ENR",
      "tsk_material_number": "2203006",
      "tsk_material_amount": 1
    }
  ]
}
```

Bara `itm_name` är obligatoriskt. Allt annat har standardvärden, men en kalkylartikel utan uppgifter ger varken tid eller kostnad.

## Fält på rotnivå

| Fält | Typ | Standard | Beskrivning |
| --- | --- | --- | --- |
| `itm_name` | text | — | Benämning. Obligatorisk. Visas i tabellen och i snabbsök. |
| `itm_description` | text | `""` | Kort beskrivning. Används i sökning. |
| `itm_category` | text | `""` | Kategori, till exempel `Kabel` eller `Data`. Används i sökning och filter. |
| `itm_keywords` | lista med text | `[]` | Sökord. Träffas av snabbsök, så lägg in synonymer och vanliga stavningar. |
| `itm_quantity` | tal | `1` | Multiplikator för hela kalkylartikeln. Antal `3` tredubblar tid och materialkostnad. |
| `itm_image` | text | `""` | Bildadress. |
| `itm_comments` | lista med objekt | `[]` | Noteringar. Se [Kommentarer och noteringar i JSON](/avancerat/json-kommentarer/). |
| `itm_tasks` | lista med objekt | `[]` | Uppgifterna som utgör arbetet. |

Skriv inte `itm_id`. Kalkyldata genererar ett nytt id vid import.

## Fält per uppgift

### Arbete

| Fält | Typ | Standard | Beskrivning |
| --- | --- | --- | --- |
| `tsk_name` | text | `""` | Uppgiftens namn, till exempel `Ijackning och kontaktering`. |
| `tsk_work_type` | text | `SV-ATL` | `SV-ATL` ger tidsuppslag via arbetskod. `Övrig tid` betyder att du sätter tiden själv. |
| `tsk_work_code` | text | `""` | Arbetskod som slås upp i arbetstidslistan när typen är `SV-ATL`. |
| `tsk_work_description` | text | `""` | Fylls i automatiskt vid `SV-ATL`. Skriv själv vid `Övrig tid`. |
| `tsk_work_task_duration` | tal | `0` | Timmar per enhet. Fylls i automatiskt vid `SV-ATL`. |
| `tsk_resource_type` | text | `""` | Resurstyp, till exempel `Elektriker`. Styr gruppering i rapporter. |
| `tsk_construction_stage` | text | `""` | Etapp, till exempel `Elkanalisation` eller `Elinstallation`. Styr gruppering och diagram. |
| `tsk_total_quantity` | tal | `1` | Hur många gånger uppgiften utförs. |
| `tsk_quantity_unit` | text | `"st"` | Enhet, till exempel `st`, `m` eller `tim`. |

### Material

| Fält | Typ | Standard | Beskrivning |
| --- | --- | --- | --- |
| `tsk_material_type` | text | `SV-ENR` | `SV-ENR` ger prisuppslag via artikelnummer. `Övrigt material` betyder att du sätter pris själv. |
| `tsk_material_number` | text | `""` | Artikelnummer eller E-nummer. Utlöser prisuppslaget. |
| `tsk_material_name` | text | `""` | Fylls i automatiskt vid `SV-ENR`. |
| `tsk_material_amount` | tal | `0` | Materialmängd per utförd uppgift. Kan vara ett decimaltal. |
| `tsk_material_user_price` | tal | `0` | Nettopris per enhet. Fylls i automatiskt vid `SV-ENR`. |
| `tsk_material_supplier` | text | `""` | Leverantör. Väljs automatiskt vid `SV-ENR` utifrån bästa nettopris. |
| `tsk_material_url` | text | `""` | Länk till produktblad. Visas i kolumnen **Länkar** och går inte att redigera i appen. |

Skriv inte `tsk_id`. Det genereras vid import.

## Fält i JSON mot kolumner i appen

Tabellen nedan visar vilket JSON-fält som motsvarar vilken kolumnrubrik i kalkyltabellen. Använd den när du vill gå mellan filen och tabellvyn. Kolumner som saknar JSON-fält är beräknade och finns aldrig i filen. En fullständig beskrivning av varje kolumn finns i [Kolumnreferensen](/referens/kolumner/).

### Kalkylartikel

| JSON-fält | Kolumn i appen |
| --- | --- |
| `itm_name` | Benämning |
| `itm_description` | Beskrivning |
| `itm_category` | Kategori |
| `itm_keywords` | Nyckelord |
| `itm_quantity` | Antal |
| `itm_image` | Bild |
| `itm_comments` | Kommentarer |
| — | Tot tid (h), beräknad |
| — | Tot material, beräknad |
| — | Andel, beräknad |
| — | Ägare, Källa, ★, Forka, Rapport — systemfält |

### Uppgift, arbete

| JSON-fält | Kolumn i appen |
| --- | --- |
| `tsk_name` | Uppgift |
| `tsk_construction_stage` | Moment |
| `tsk_quantity_unit` | Enhet |
| `tsk_total_quantity` | Antal |
| `tsk_work_task_duration` | Tid/st |
| `tsk_resource_type` | Yrkesroll |
| `tsk_work_type` | Arbetstyp |
| `tsk_work_code` | Arbetskod |
| `tsk_work_description` | Arbetsbeskrivning |
| — | Tot tid, beräknad |

### Uppgift, material

| JSON-fält | Kolumn i appen |
| --- | --- |
| `tsk_material_name` | Material |
| `tsk_material_amount` | Mat.mängd |
| `tsk_material_user_price` | Pris/st |
| `tsk_material_supplier` | Grossist |
| `tsk_material_number` | Mat.nummer |
| `tsk_material_type` | Mat.typ |
| `tsk_material_url` | Produktlänk, visas även i Länkar |
| — | Kommentarer hanteras på kalkylartikelnivå via `itm_comments` |
| — | Tot material, beräknad |

Observera att kolumnen **Mat.typ** motsvarar `tsk_material_type`, alltså valet mellan `SV-ENR` och `Övrigt material` — inte en produktgrupp du hittar på själv. Samma sak gäller **Arbetstyp** och `tsk_work_type`.

## Så fungerar tidsuppslaget

När `tsk_work_type` är `SV-ATL` läses `tsk_work_code` mot arbetstidslistan. Träffar koden fylls beskrivning, tid per enhet och resurstyp i automatiskt och kan inte redigeras i tabellen. Träffar koden inte blir tiden `0` och fältet står tomt — det är den vanligaste orsaken till att en kalkylartikel ger noll timmar.

Koden slås upp exakt som den står. Du kan inte räkna om en listad tid med uttryck i kodfältet, till exempel dela med tio. Anger listan tid per tio meter men du kalkylerar per meter, får du i stället använda en kod som gäller per meter, eller sätta `tsk_work_type` till `Övrig tid` och skriva den omräknade tiden i `tsk_work_task_duration`.

Ska raden inte ha någon tid alls, sätt `tsk_work_task_duration` till `0` och lämna `tsk_work_code` tomt.

## Så fungerar prisuppslaget

När `tsk_material_type` är `SV-ENR` slås `tsk_material_number` upp i prislistan. Systemet hämtar listpriset hos varje leverantör, drar av rabatten från dina uppladdade rabattbrev och väljer det lägsta nettopriset. Benämning, pris och leverantör fylls i automatiskt.

`tsk_material_amount` är mängden per utförd uppgift och behöver inte vara ett heltal. Säljs artikeln i förpackningar om 100 men du använder en styck, skriv `0.01`. Använd punkt som decimaltecken och skriv talet utan citattecken.

Har raden inget artikelnummer, sätt `tsk_material_type` till `Övrigt material` och ange `tsk_material_name` och `tsk_material_user_price` själv.

## Så räknas summorna

```text
uppgiftens tid       = tsk_work_task_duration × tsk_total_quantity
uppgiftens material  = tsk_total_quantity × tsk_material_amount × tsk_material_user_price

kalkylartikelns tid       = summa av uppgifternas tid × itm_quantity
kalkylartikelns material  = summa av uppgifternas material × itm_quantity
```

Summorna finns aldrig i filen. De räknas fram varje gång kalkylen visas.

## Fullständigt exempel

Exemplet nedan är en riktig kalkylartikel: en meter EXQ 3G1,5 förlagd i VP-rör på plattbärlag, med rör, kabel, skarvmuff och buntband som separata uppgifter.

```json
{
  "itm_name": "EXQ 3G1,5 I RÖR PÅ PLATTBÄRLAG",
  "itm_description": "EXQ 3G1,5 I RÖR PÅ PLATTBÄRLAG, FILIGRANBJÄLKLAG ELLER PLANBJÄLKLAG INKLUSIVE VP-RÖR OCH BUNTBAND.",
  "itm_image": "images/images_articles/EXQ.jpg",
  "itm_keywords": [
    "KABEL",
    "CPR",
    "KOPPARKABEL",
    "KOPPAR",
    "EKK",
    "VIT",
    "HALOGENFRI",
    "S05XZ1-U",
    "I VALV",
    "PÅ VALV"
  ],
  "itm_quantity": 1,
  "itm_comments": [],
  "itm_tasks": [
    {
      "tsk_name": "BUNTBAND 200 mm",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "",
      "tsk_work_description": "",
      "tsk_construction_stage": "Kanalisation i platta/mark",
      "tsk_quantity_unit": "st",
      "tsk_total_quantity": 3.0,
      "tsk_work_task_duration": 0.0,
      "tsk_material_number": "1516068",
      "tsk_material_name": "BUNTBAND T30L SVA 100 ST",
      "tsk_material_type": "SV-ENR",
      "tsk_material_amount": 0.01,
      "tsk_material_user_price": 142.0,
      "tsk_resource_type": "Elektriker"
    },
    {
      "tsk_name": "SKARVMUFF 20",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "",
      "tsk_work_description": "",
      "tsk_construction_stage": "Kanalisation i platta/mark",
      "tsk_quantity_unit": "st",
      "tsk_total_quantity": 1.0,
      "tsk_work_task_duration": 0.0,
      "tsk_material_number": "1400653",
      "tsk_material_name": "SKARVMUFF 20MM LSZH",
      "tsk_material_type": "SV-ENR",
      "tsk_material_amount": 0.3,
      "tsk_material_user_price": 2.0,
      "tsk_resource_type": "Elektriker"
    },
    {
      "tsk_name": "VP-RÖR 20 HALOGENFRITT PÅ PLATTBÄRLAG",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "206501112",
      "tsk_work_description": "Montage VP-RÖR",
      "tsk_construction_stage": "Kanalisation i platta/mark",
      "tsk_quantity_unit": "m",
      "tsk_total_quantity": 1.0,
      "tsk_work_task_duration": 0.06,
      "tsk_material_number": "1416753",
      "tsk_material_name": "VP-RÖR 20MM 750N HF, 3M",
      "tsk_material_type": "SV-ENR",
      "tsk_material_amount": 1.0,
      "tsk_material_user_price": 55.0,
      "tsk_resource_type": "Elektriker"
    },
    {
      "tsk_name": "EXQ 3G1,5 I RÖR PÅ PLATTBÄRLAG",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "207510103",
      "tsk_work_description": "INST KABLAR RÖR T O M 2,5KVMM",
      "tsk_construction_stage": "Infälld kabelförläggning",
      "tsk_quantity_unit": "m",
      "tsk_total_quantity": 1.0,
      "tsk_work_task_duration": 0.03,
      "tsk_material_number": "0445602",
      "tsk_material_name": "EXQ-PURE 3G1,5 R100",
      "tsk_material_type": "SV-ENR",
      "tsk_material_amount": 1.0,
      "tsk_material_user_price": 20.0,
      "tsk_resource_type": "Elektriker"
    }
  ]
}
```

Notera att rena materialrader — buntband och skarvmuff — saknar arbetskod och har `tsk_work_task_duration` satt till `0`. De bidrar med materialkostnad men ingen tid. Priserna i filen skrivs över av prisuppslaget när artikelnumret träffar.

## Vanliga fel

| Fel | Följd | Åtgärd |
| --- | --- | --- |
| `SV-ATL` utan `tsk_work_code` | Tiden blir `0` | Ange kod eller byt till `Övrig tid` |
| `SV-ENR` utan `tsk_material_number` | Priset blir `0` och benämningen tom | Ange artikelnummer eller byt till `Övrigt material` |
| Decimal som text, `"0,11"` | Värdet tolkas inte som tal | Skriv `0.11` utan citattecken |
| Komma som decimaltecken i JSON | Filen går inte att läsa | Använd punkt |
| `itm_id` eller `tsk_id` medskickade | Ignoreras | Utelämna dem |
| Egna priser på `SV-ENR`-rader | Skrivs över av uppslaget | Låt fälten vara tomma |
| Listan `itm_tasks` saknas | Kalkylartikeln ger varken tid eller kostnad | Lägg till minst en uppgift |
