---
layout: default
title: "Validera och felsök din JSON"
parent: "För avancerade användare"
nav_order: 6
permalink: /avancerat/validera-json/
description: "Checklista före publicering och felsökning när JSON, tidsuppslag eller prisuppslag inte ger det förväntade resultatet."
category: "reference"
tags: ["json", "validering", "felsökning", "kalkylartikel", "avancerat"]
audience: "advanced"
---

# Validera och felsök din JSON

Innan du importerar en kalkylartikel eller öppnar en pull request är det bra att gå igenom filen en gång till.

Problem med kalkylartiklar beror ofta på att en arbetskod eller ett artikelnummer inte ger någon träff i aktuella underlag. Det behöver inte innebära att JSON-filen är fel. Om du har angett reservvärden kan kalkylartikeln fortfarande innehålla användbar tid, benämning eller pris även när ett uppslag saknas.

## Checklista före publicering

Kontrollera följande innan du importerar eller publicerar en kalkylartikel:

- Filen innehåller giltig JSON och roten är ett objekt.
- `itm_name` finns och beskriver kalkylartikeln.
- `itm_tasks` innehåller de uppgifter som ska ingå i kalkylartikeln.
- Varje arbetsuppgift har rätt `tsk_work_type` och, när `SV-ATL` används, en arbetskod om det finns en kod att slå upp.
- Om en `SV-ATL`-kod saknas eller inte kan slås upp finns ett rimligt värde i `tsk_work_task_duration` om artikeln ska kunna användas även utan träff.
- Varje materialrad har rätt `tsk_material_type` och, när `SV-ENR` används, ett artikelnummer om det finns ett nummer att slå upp.
- Om ett `SV-ENR`-nummer saknas eller inte kan slås upp finns reservvärden för materialet om artikeln ska kunna användas även utan träff.
- Alla tal är skrivna som JSON-tal, med punkt som decimaltecken och utan citattecken.
- Inga `itm_id` eller `tsk_id` finns med.
- `tsk_construction_stage` och `tsk_resource_type` är ifyllda när uppgiften ska kunna grupperas korrekt i rapporter.
- `itm_comments` innehåller bara relevanta kommentarer och varje kommentar har fältet `text`.
- Sökorden i `itm_keywords` täcker de ord en användare faktiskt kan söka efter.

## Kontrollera att uppslagen träffade

Importera artikeln till en testkalkyl och kontrollera resultatet i kalkyltabellen.

| Vad du ser | Vad det kan betyda |
| --- | --- |
| Tid per enhet är ifylld och grå | Arbetsuppgiften har fått ett tidsuppslag och värdet kommer från underlaget. |
| Tid är `0,00` på en `SV-ATL`-rad | Arbetskoden saknas, ger ingen träff eller så saknas ett användbart reservvärde. |
| Tid visas trots att arbetskoden inte ger träff | Ett angivet reservvärde används. |
| Materialbenämning och leverantör är ifyllda | Artikelnumret har gett en träff i prisunderlaget. |
| Pris är `0,00` på en `SV-ENR`-rad | Artikelnumret ger ingen prisuppgift och inget användbart reservpris finns. |
| Pris och materialbenämning finns trots att artikelnumret inte ger träff | Angivna reservvärden används. |
| Priset känns högt | Kontrollera prisunderlag och rabattbrev för aktuell leverantör. |
| Ett streck visas i prisfältet | Inget pris kunde hämtas eller användas för raden. |

Läs mer om hur priserna sätts i [Materialpriser](/anvandarguide/kalkyl/materialpriser/).

## Vanliga symptom och orsaker

### Kalkylartikeln ger noll timmar

Kontrollera först `tsk_work_type`, `tsk_work_code` och `tsk_work_task_duration`.

Om `tsk_work_type` är `SV-ATL` försöker Kalkyldata slå upp arbetskoden i arbetstidslistan. Om koden inte ger någon träff kan ett angivet värde i `tsk_work_task_duration` användas som reserv.

Om `tsk_work_type` är `Övrig tid` används den tid som du själv har angett.

Kontrollera också att `tsk_total_quantity` är större än noll.

### Materialkostnaden blir orimligt hög

Kontrollera framför allt `tsk_material_amount`.

Materialmängden anges per utförd uppgift. Säljs exempelvis en artikel i ett hundrapack men du använder en styck ska mängden vara `0.01`.

Kontrollera även vilket pris som används efter prisuppslaget och att aktuella rabattbrev finns för de leverantörer som ska kunna ge nettopris.

### Materialbenämningen eller priset blir inte som förväntat

Kontrollera `tsk_material_type` och `tsk_material_number`.

Med `SV-ENR` försöker Kalkyldata slå upp materialet utifrån artikelnumret. Om uppslaget ger en träff används uppgifterna från prisunderlaget. Om det inte finns någon träff kan de värden som angetts i kalkylartikeln fungera som reserv.

Om du vill styra materialet helt manuellt använder du `Övrigt material`.

### Kommentarerna syns inte

Kommentarer i en kalkylartikel ska ligga i `itm_comments` på rotnivå.

Varje kommentar ska vara ett objekt som innehåller `text`.

```json
"itm_comments": [
  {
    "text": "Tiden bygger på summering av flera moment i arbetstidslistan."
  }
]
```

Kommentarer på uppgiftsnivå genom `tsk_comments` stöds inte.

### Importen avvisas

Kontrollera först att filen innehåller giltig JSON.

Vanliga orsaker är:

- filen är större än `1 MB`
- roten är en lista i stället för ett objekt
- ett kommatecken eller citattecken saknas
- ett tal har skrivits som text på ett sätt som inte är giltig JSON
- Markdown eller annan text har hamnat utanför själva JSON-objektet

Om du kopierar JSON från exempelvis en AI-modell, kontrollera att du kopierar själva JSON-innehållet och inte förklarande text runt omkring.

### Artikeln hittas inte i snabbsök

Kontrollera först att kalkylartikeln faktiskt har blivit importerad eller publicerad.

Snabbsök söker på bland annat benämning, sökord, kategori och beskrivning. Lägg till relevanta ord i `itm_keywords` om artikeln är svår att hitta.

Använd gärna de ord som en elektriker faktiskt skulle skriva när artikeln ska sökas fram. Ta med relevanta synonymer, förkortningar och vanliga branschbenämningar.

## Kontrollera JSON-strukturen

Om du misstänker att själva JSON-filen är problemet kan du börja med att kontrollera strukturen:

```json
{
  "itm_name": "Exempel på kalkylartikel",
  "itm_keywords": [
    "EXEMPEL",
    "KABEL",
    "INSTALLATION"
  ],
  "itm_tasks": [
    {
      "tsk_name": "Montering",
      "tsk_work_type": "SV-ATL",
      "tsk_work_code": "123456",
      "tsk_work_task_duration": 0.05,
      "tsk_total_quantity": 1,
      "tsk_quantity_unit": "st",
      "tsk_material_type": "SV-ENR",
      "tsk_material_number": "1234567",
      "tsk_material_name": "EXEMPELMATERIAL",
      "tsk_material_amount": 1,
      "tsk_material_user_price": 10.0
    }
  ]
}
```

Börja med den enklaste möjliga filen och lägg sedan till fler fält. Det gör det lättare att hitta vilket fält eller vilken uppgift som orsakar problemet.

## Om artikeln fungerar men ger fel resultat

Om JSON-filen går att importera men kalkylresultatet inte blir som förväntat är det oftast inte ett JSON-formatfel.

Kontrollera då i första hand:

1. arbetskod och arbetstyp
2. artikelnummer och materialtyp
3. reservvärden för tid och material
4. antal och materialmängder
5. resurstyp och moment
6. aktuella pris- och tidsunderlag

På så sätt kan du skilja mellan ett **JSON-fel** och ett **uppslags- eller kalkylfel**.
