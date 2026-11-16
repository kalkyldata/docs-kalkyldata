---
layout: default
title: "Partner och B2B"
nav_order: 10
permalink: /partner/
description: "Datatjänster, master grossistkatalog (Ahlsell, Rexel, Sonepar, Solar), produktbilds-CDN, ackordstidslistan (ATL), kalkylrecept och MCP-server för affärssystem och AI-agenter."
category: "partner"
tags: ["partner", "b2b", "api", "mcp", "grossistpriser", "grossistprisfil", "gnp", "ackordstidslista", "atl", "kdx", "e-nummer", "produktbilder", "gtin", "mpn", "ahlsell", "rexel", "sonepar", "solar"]
audience: "advanced"
has_children: true
---

# Partner och B2B: Datatjänster, API och MCP Server

Kalkyldatas kärna bygger på normaliserad, löpande uppdaterad grunddata för elinstallationsbranschen. För programvarubolag, affärssystem, e-handel, grossister och AI-utvecklare erbjuder vi indirekta tjänster, REST-API samt en officiell **MCP-server (Model Context Protocol)** för direktintegration med AI-assistenter.

Genom att använda Kalkyldata som datainfrastruktur slipper externa system bygga och underhålla egna register för grossistpriser - motsvarande grossistprisfil, E-nummer, GTIN, tillverkarnummer, produktbilder, rabattkoder, normtider och kalkylpaket.

## 1. Den sammanställda grossistprislistan

Vår masterprislista samlar och normaliserar materialdata från Sveriges fyra ledande elgrossister: **Ahlsell, Rexel, Sonepar och Solar**. Den är uppbyggd kring det sjusiffriga E-numret och tillverkarens identiteter, och innehåller betydligt mer matnyttig produkt- och marknadsdata än bara artikelnamn och listpris.

### Datainnehåll per artikel och grossist

| Fält / Information | Fältnamn (API/DB) | Beskrivning och användningsområde |
|---|---|---|
| **E-nummer** | `material_number` | Det sjusiffriga bransch-ID:t (SV-ENR) som entydigt binder ihop produkter mellan tillverkare och grossister. |
| **Grossistparallell** | `material_supplier` | Identifierar grossisten (`Ahlsell`, `Rexel`, `Sonepar` eller `Solar`). Möjliggör jämförelse av samtliga fyra grossisters villkor sida vid sida för samma artikel. |
| **Listpris / Bruttopris** | `material_list_price` | Aktuellt ordinarie listpris (GNP) per grossist, i SEK exkl. moms. |
| **Rabattkod / Rabattgrupp** | `material_discount_code` | Grossistens specifika rabattgruppskod (t.ex. `BCA`, `1817`). Nödvändig för att kunna beräkna kundspecifika nettopriser via rabattbrev. |
| **Artikelbenämning** | `material_name` | Grossistens standardiserade svenska produktbenämning enligt branschregistret. |
| **Tillverkarens artikelnamn** | `manufacturer_article_name` | Tillverkarens egna modell- eller produktbenämning för exakt korsreferens och specifikationskontroll. |
| **Fabrikat & Varumärke** | `manufacturer_brand` | Tillverkare eller varumärke (t.ex. Schneider Electric, ABB, Hager, Plejd, Wago, Nexans, NKT). |
| **Tillverkarens artikelnummer / MPN** | `manufacturer_part_number` | Tillverkarens eget artikelnummer, typkod eller katalognummer (t.ex. Schneider Exxact WDE002120 eller ABB E2704). Mycket efterfrågat då elektriker och föreskrivande konsulter ofta söker på tillverkarens beteckning. |
| **GTIN / EAN-streckkod** | `gtin` | Det 13-siffriga globala handelsartikelnumret (EAN/streckkod). Nödvändigt för e-handel, streckkodsscanning och koppling mot externa PIM-system. |
| **Mängdenhet** | `material_quantity_unit` | Försäljningsenhet (`st`, `m`, `frp`, `pkt`) så att mängdberäkningar och prissättning alltid sker i rätt skala. |
| **Förpackningsstorlek** | `package_quantity` | Grossistens minsta förpackningsstorlek och multipel (t.ex. 10 st/frp, 100 m/ring, 500 m/trumma), vilket förhindrar felbeställningar i inköpssystem. |
| **Aktiv / Utgående status** | `manufacturer_active` | Indikerar om produkten är aktiv i ordinarie sortiment (`AKTIV`), utgående (`UTGÅR`) eller har utgått (`UTGÅNGEN`). |
| **Ersatt av** | `manufacturer_replaced_by` | Hänvisning till ersättande E-nummer när en artikel utgått eller ersatts av en modernare variant. |
| **Revisionsdatum** | `date_created` / `updated_at` | Tidstämpel för senaste pris- och katalogrevidering, vilket ger full spårbarhet vid grossisternas återkommande prisjusteringar. |

### Vad grossist-API:et löser för externa system

- **Flergrossistjämförelse:** Ett anrop mot ett E-nummer eller MPN returnerar omedelbart pris, rabattgrupp och lagerstatusindikator hos samtliga fyra grossister samtidigt.
- **Automatisk nettoprissättning:** API:et kan applicera kundens egna rabattbrev mot grossisternas rabattkoder för att i realtid beräkna lägsta faktiska nettopris.
- **Katalogtvätt och validering:** Identifiera felaktiga eller utgångna E-nummer och få automatiska förslag på moderna ersättningsartiklar.
- **Streckkods- och tillverkaruppslag:** Hitta rätt E-nummer via GTIN eller tillverkarens modellnummer vid scanning på bygget eller från externa materialdatablad.

## 2. Produktbilder och Media-API (CDN)

En av branschens största utmaningar är att hålla uppdaterade, högupplösta produktbilder för elmateriel. De flesta affärs- och kalkylsystem visar enbart textrader eftersom bildhantering kräver kontinuerlig insamling, rensning och optimering.

Kalkyldata tillhandahåller ett **bild-API och globalt CDN** som mappar produktbilder direkt mot E-numret:

### Hur det fungerar

- **Prediktiv URL-struktur:** Bilder levereras via snabb CDN-infrastruktur strukturerat per materialtyp och E-nummer:  
  `https://img.kalkyldata.se/products/sv-enr-{artikelnummer}.webp`
- **Optimerade format:** Färdigskalade och komprimerade WebP/JPEG/PNG-bilder för webb, mobila appar och PDF-rapporter.
- **Galleri och miniatyrer:** Möjlighet att hämta primärbild samt relaterade detalj- och måttskisser per artikel.

### Användningsfall för bildtjänsten

- **Säljande offerter i affärssystem:** Bygglet, Next, Fortnox eller Visma kan enkelt berika sina materiallistor och offertbilagor med riktiga produktbilder utan att lagra bildfiler själva.
- **Inköps- och beställningsstöd:** Installatörer och montörer kan visuellt verifiera att rätt apparat, kåpa eller färg beställs.
- **E-handelsintegration:** Mindre grossister eller specialbutiker kan visa officiella produktbilder på tusentals E-nummer direkt.

## 3. Ackordstidslistan (ATL) som API

Kalkyldata tillhandahåller maskinläsbara uppslag mot **Elektrikernas ackordstidslista (2019)** — branschens etablerade normtidlista framtagen av installationsavtalets parter.

### Datainnehåll

- **Arbetskoder:** Officiella koder (t.ex. `207518106`) för enskilda arbetsmoment.
- **Normtid i timmar:** Ackordstiden per enhet (angiven i decimaltimmar).
- **Momentbeskrivning:** Standardiserad text som beskriver vad som ingår i momentet.
- **Byggskede & Resurstyp:** Kategorisering i moment (t.ex. Elkanalisation, Elinstallation, Elcentral) och yrkesroll.

Projektverktyg och tidsredovisningssystem kan låta sina användare söka fram officiella montagetider direkt i sina projektplaner och arbetsordrar.

## 4. Kalkylrecept och paketbibliotek (KDX/1)

Utöver enskilda material- och tidsrader tillhandahåller Kalkyldata ett omfattande bibliotek av **sammansatta kalkylartiklar (recept)**.

Ett recept kopplar ihop:
1. Nödvändigt installationsmaterial (specificerade E-nummer och mängder).
2. Tillhörande montagemoment (arbetskoder enligt ATL med tidsåtgång).
3. Hjälpmaterial och montagemetod.

Recepten levereras i det öppna och versionerade formatet **`kdx/1`** (se [Utbytesformatet kdx/1](/avancerat/kdx-format/)), vilket gör dem enkla att importera till andra system eller använda som grund för automatiska offertmallar.

## 5. Beräknings- och optimeringsmotor (Headless Engine)

För partners som vill erbjuda avancerad kalkylering utan att bygga beräkningslogik från grunden erbjuder vi beräkningstjänster via API:

- **Oberoende korsreferenser & Ersättningsregler:** Till skillnad från grossisternas egna system erbjuder Kalkyldata oberoende förslag på likvärdigt material (t.ex. byta mellan Schneider, ABB och Hager) för att optimera täckningsbidrag eller lösa tillgänglighetsproblem.
- **Nettokalkylator för rabattbrev:** Skicka in kundens rabattfil och en materialförteckning – motorn räknar ut optimal grossistfördelning och total nettokostnad.
- **Headless Kalkylmotor:** Skicka in en mängdförteckning och erhåll en komplett kalkylstruktur med summerade timmar, materialkostnader, rekommenderat á-pris och påslagsberäkning.

## 6. Kalkyldata MCP Server (Model Context Protocol)

För partners och contech-bolag som bygger **AI-assistenter, offertrobotar och automatiserade anbudsanalyser** tillhandahåller Kalkyldata en officiell **MCP-server**.

Model Context Protocol (MCP) är den öppna standarden som låter stora språkmodeller (LLM:er som Claude, GPT-4o, Cursor och interna enterprise-agenter) anropa externa verktyg och datakällor säkert och dynamiskt utan skräddarsydd integrationskod.

### Varför MCP för installationsdata?

- **Inga API-wrappers:** Utvecklare som bygger AI-agenter slipper skriva prompt-adaptrar, REST-anrop och felhantering. Modellerna känner själva till verktygens syfte och parametrar.
- **Realtidskontext i chatten:** En projektledare eller kalkylator kan i Claude Desktop, Cursor eller en intern företagschatt fråga: *"Vad är billigast hos Solar kontra Ahlsell för 20 st Schneider Exxact 2-vägsuttag, och hur lång montagetid krävs enligt ATL?"* — och agenten slår upp svaret direkt i Kalkyldatas databas.
- **Offert- och anbudsagenter:** Autonoma agenter kan analysera rumsbeskrivningar i PDF-anbudshandlingar, bryta ned dem till kalkylrecept via Kalkyldata MCP och returnera en komplett prissatt kalkyl.

### Exponerade MCP-verktyg

| MCP Tool | Parametrar | Svar & Funktion |
|---|---|---|
| `search_articles` | `query`, `supplier?`, `limit?` | Söker på E-nummer, benämning, fabrikat eller tillverkarkod och returnerar matchande artiklar med grossistpriser. |
| `get_article_details` | `material_number`, `type?` | Returnerar komplett masterkort: alla fyra grossisters listpriser, rabattkoder, fabrikat, MPN, GTIN, enhet, status och bild-URL. |
| `compare_wholesale_prices` | `materials[]`, `user_id?` | Jämför priser mellan Ahlsell, Rexel, Sonepar och Solar. Om rabattbrev är kopplade returneras faktiska nettopriser och billigaste grossist. |
| `get_labor_time` | `work_code` eller `description` | Slår upp Elektrikernas ackordstidslista (ATL) och returnerar normtid i timmar, momentbeskrivning och byggskede. |
| `get_replacement_article` | `material_number` | Returnerar förslag på likvärdiga ersättningsartiklar och korsreferenser mellan fabrikat om en artikel utgått eller saknas. |
| `calculate_recipe` | `recipe_id` eller `recipe_slug`, `quantity`, `supplier?` | Kör ett komplett kalkylrecept och returnerar summerad materialkostnad, arbetstid i timmar och ingående komponenter. |
| `get_product_media` | `material_number` | Returnerar högupplösta CDN-bildlänkar (WebP/JPEG) och eventuella måttskisser för specificerat E-nummer. |

### Anslutning och arkitektur

MCP-servern levereras som en molnhostad tjänst med stöd för **HTTP Streamable / Server-Sent Events (SSE)**. Partnern anger endast MCP-serverns URL och sin partner-API-nyckel i sin agentkonfiguration (`claude_desktop_config.json`, n8n AI Agent, LangChain eller Cursor).

## 7. Målgrupper och typiska användningsfall

| Partnertyp | Användningsområde | Värde |
|---|---|---|
| **Affärs- & projektverktyg** (verksamhetssystem) | Bädda in el-kalkylering, normtider och bildberikade offertbilagor via REST-API. | Får en komplett elmodul utan att underhålla prisdatabaser, tidlistor eller bildbanker. |
| **Contech- & AI-startups** (Offertagenter, anbudsgranskare) | Koppla upp Kalkyldata MCP Server till sina AI-modeller. | Ger agenterna omedelbar domänkunskap om svenska grossistpriser, E-nummer och ATL-tider. |
| **Stora installationsföretag** | Interna AI-assistenter i Teams eller mobilen för projektledare och ledande montörer. | Snabb koll på priser, ersättningsartiklar och ackordstider direkt i fält. |
| **Grossister & E-handel** | Visa beräknad montagetid (ATL) direkt på produktsidan för inloggade installatörer. | Hjälper installatören att kalkylera direkt vid beställning och driver lojalitet. |
| **Tillverkare av installationsmateriel** | Se till att produkter har rätt ATL-koppling, MPN/GTIN och officiella produktbilder i kalkylskedet. | Säkerställer att produkternas montagefördelar syns tidigt i kalkylprocessen. |
| **Inköpsportaler & Konsulter** | Flergrossistjämförelser, oberoende korsreferenser och automatiserade kalkylunderlag. | Neutral jämförelse av nettokostnader och snabbare förfrågningsunderlag. |

## 8. Tekniskt gränssnitt och format

- **REST API:** HTTPS med JSON-nyttolaster för traditionella systemintegrationer.
- **MCP Server:** SSE (Server-Sent Events) och HTTP Streamable Transport enligt officiella Model Context Protocol-specifikationen.
- **Bildleverans:** Globalt CDN över HTTPS med fasta URL-mönster per E-nummer (`img.kalkyldata.se`).
- **Datamodeller:** Återanvänder Kalkyldatas etablerade scheman (`itm_*`, `tsk_*`, `kdx/1`).
- **Autentisering:** Organisationstilldelade API-nycklar via HTTP Header (`Authorization: Bearer <token>`).
- **Prestanda & SLA:** Hög tillgänglighet med sub-100ms svarstider för enstaka uppslag samt stöd för batch-anrop.

## 9. Affärsmodell och licensiering

Eftersom datatjänsterna är ett fokuserat B2B-erbjudande tillämpar vi en renodlad partnermodell:

1. **Modulbaserad årslicens:** Fasta B2B-avtal baserade på vilka datamoduler som ingår (Grossistlista, Bild-CDN, ATL, Kalkylrecept, Beräkningsmotor, MCP Server) samt anropsvolym.
2. **Standardiserad leverans (Strict As-is):** Tjänsterna levereras mot vår fullständiga API- och verktygsdokumentation. Partnern ansvarar för integrationen i sitt eget system eller agent.
3. **Upphovsrätt och branschavtal:** Kalkyldata tillhandahåller teknisk infrastruktur, bildoptimering, normalisering och sökindex. Användande part ansvarar för att eventuella branschspecifika avtal efterlevs i den egna verksamheten.

## 10. Begär partneråtkomst

API-nycklar, MCP-slutpunkter och partneravtal sätts upp manuellt efter genomgång av era tekniska behov. 

Kontakta oss via [Kontakta support](/hjalp/kontakt/) med följande information:

1. **Företagsnamn och verksamhetstyp** (affärssystem, AI/contech-bolag, grossist, e-handel, installationsföretag).
2. **Vilka moduler och gränssnitt ni är intresserade av** (REST API, MCP Server, grossistkatalog, bild-CDN, ATL, kalkylrecept).
3. **Förväntad anropsvolym** (agentuppslag, bildvisningar, nattliga batch-synkningar).
4. **Teknisk kontaktperson**.

Vi återkommer med tekniska specifikationer, provnyckel för sandboxmiljö och avtalsförslag.
