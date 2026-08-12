# Kalkyldata – dokumentation

Det här repot innehåller dokumentationen för **Kalkyldata**, ett webbaserat kalkyl- och offertverktyg för elinstallationer.

Kalkyldata hjälper dig att bygga kalkyler genom att beskriva jobbet i en chatt. **AI-agenten** föreslår kalkylartiklar med uppgifter, material och arbetstid. Du kan sedan granska och justera kalkylen innan du skapar en offert, materiallista eller annan rapport.

## Dokumentationen

Den publicerade dokumentationen finns på:

**[kalkyldata.github.io/docs-kalkyldata/]([https://docs.kalkyldata.se/](https://kalkyldata.github.io/docs-kalkyldata/))**

Dokumentationen innehåller bland annat:

* guider för att komma igång och använda Kalkyldata
* information om kalkyler, delar, kalkylartiklar och uppgifter
* guider för materialpriser och rabattbrev
* sökning och filtrering
* offerter, rapporter och PDF
* import och export av kalkyldata
* prisstrategier och profiler
* frågor och svar
* nyheter och förändringar i tjänsten

Dokumentationen är skriven för användare av Kalkyldata och är utformad för att även kunna användas som kunskapsunderlag av AI-agenten.

## Om Kalkyldata

Kalkyldata är utvecklat för elbranschen och fokuserar på att göra kalkylering och offertarbete snabbare och enklare.

En kalkyl byggs upp i flera nivåer:

```text
Projekt
└── Del
    └── Kalkylartikel
        └── Uppgift
```

En **kalkylartikel** är en återanvändbar mall som innehåller en eller flera **uppgifter**. En uppgift beskriver ett arbetsmoment och kan innehålla material, arbetstid eller båda.

Materialpriser för standardartiklar hämtas från prisdata och kan jämföras mellan leverantörer utifrån användarens rabattbrev.

## Det här repot

Det här är **dokumentationsrepot för Kalkyldata**. Det innehåller inte själva Kalkyldata-applikationens källkod.

Dokumentationen är byggd med:

* [Jekyll](https://jekyllrb.com/)
* [Just the Docs](https://just-the-docs.github.io/just-the-docs/)
* GitHub Pages
* GitHub Actions

Markdown-filerna innehåller både själva dokumentationstexten och metadata som används för navigation, sökning och strukturering av innehållet.

## Struktur

Dokumentationen är organiserad efter vad användaren behöver göra och förstå.

Typiska delar är:

```text
Översikt
├── Vad är Kalkyldata?
└── ...

Guider
├── Kom igång
├── Kalkyl
├── Rapporter
└── ...

Referens
└── ...
```

Varje sida är en separat Markdown-fil med YAML-frontmatter som styr bland annat titel, navigation, URL, kategori och målgrupp.

## Utveckling och lokal förhandsvisning

Om du arbetar med dokumentationen lokalt behöver du ha Jekyll och Bundler installerat.

Installera projektets beroenden:

```bash
bundle install
```

Starta sedan en lokal utvecklingsserver:

```bash
bundle exec jekyll serve
```

Dokumentationen blir då tillgänglig lokalt på:

```text
http://localhost:4000
```

Den genererade webbplatsen hamnar i katalogen `_site`.

## Publicering

Dokumentationen publiceras automatiskt via **GitHub Actions** till GitHub Pages.

När ändringar pushas till den publicerade branchen byggs dokumentationen och den nya versionen publiceras automatiskt.

## Bidrag och ändringar

Bidrag till dokumentationen är välkomna. Du kan föreslå förbättringar, rätta fel, förtydliga instruktioner eller lägga till information som saknas.

### Så bidrar du

1. Skapa en fork av repot.
2. Gör dina ändringar i en separat branch.
3. Skicka en pull request med en kort beskrivning av vad du har ändrat och varför.

För mindre ändringar, som stavfel eller uppenbara rättelser, går det bra att skicka en pull request direkt utan att först öppna en issue.

Dokumentationen följer Kalkyldatas etablerade terminologi och skrivs med användaren i fokus. Vid större ändringar kan innehållet därför behöva justeras för att passa dokumentationens struktur och begrepp.


---

*Kalkyldata är ett kalkyl- och offertverktyg för elinstallationer.*
