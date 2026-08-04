# Så här sätts materialpriserna

Materialpriserna i Kalkyldata kommer från en kombination av branschprislistor och dina egna rabattbrev. Systemet gör jämförelsen åt dig och väljer det billigaste priset automatiskt.

## När hämtas priser?

Priser hämtas för material i uppgifter som är märkta som **SV-ENR**. Det är standardartiklar med ett E-nummer, till exempel `2203006` för ett vägguttag.

För material som är märkta som **Övrigt material** anger du priset själv.

## Så går prisberäkningen till

1. **Systemet slår upp artikeln i prislistan.**  
   Varje leverantör har ett listpris för artikeln.

2. **Dina rabattbrev appliceras.**  
   Om du har laddat upp ett rabattbrev för en leverantör räknas rabatten av från listpriset.

3. **Nettopriset jämförs mellan leverantörerna.**  
   Systemet väljer det lägsta nettopriset och visar vilken leverantör priset kommer ifrån.

### Formeln

```text
nettopris = listpris × (1 − rabattprocent / 100)
```

Om du till exempel har `20 %` rabatt på en artikel med listpriset `100 kr` blir nettopriset `80 kr`.

## Vad händer om en leverantör saknar rabattbrev?

Då används leverantörens listpris i jämförelsen.

Det betyder att en leverantör utan rabattbrev fortfarande kan vara billigast om listpriset är tillräckligt lågt.

## Vilka leverantörer jämförs?

Kalkyldata jämför priser från:

- Ahlsell
- Solar
- Rexel
- Sonepar

## Vad händer om inget pris hittas?

Om artikeln inte finns i prislistorna, eller om ingen leverantör har ett giltigt pris, behålls det pris som redan finns angivet på kalkylartikeln.

Det är oftast ett standardpris eller ett uppskattat inköpspris. Rapporten visar då en varning så att du vet att priset behöver kontrolleras.

## Uppdatera priser i efterhand

När du har laddat upp nya rabattbrev eller när prislistorna har uppdaterats kan du köra en **prisuppdatering**.

Då går systemet igenom alla SV-ENR-material i kalkylen på nytt och väljer det billigaste priset enligt aktuella uppgifter.

Knappen för **prisuppdatering** hittar du i sidopanelen för kalkyltabellen.

## Så här får du rätt pris i två steg

1. Kontrollera att dina rabattbrev är uppladdade och uppdaterade under **Profil → Rabattbrev**.
2. Kör en **prisuppdatering** efter att du har laddat upp nya rabattbrev eller när prislistorna har ändrats.

## Vanliga frågor

### Varför ändras leverantören när jag uppdaterar priser?

Det betyder att en annan leverantör nu har det lägsta nettopriset.

Det kan bero på att:

- rabattsatsen har ändrats,
- listpriserna har uppdaterats,
- en annan leverantör har fått ett bättre nettopris.

### Kan jag välja en specifik grossist?

Nej. Kalkylen väljer alltid det lägsta nettopriset automatiskt för att ge lägsta möjliga materialkostnad.

Om du vill använda ett annat materialpris för en enskild uppgift kan du istället:

- välja en specifik grossist för materialet i uppgiften genom att redigera kalkylartikeln, antingen när du lägger till den eller senare direkt i kalkyltabellen,
- eller välja **Övrigt material** och ange priset manuellt.

Om du vill påverka hur priser väljs för hela kalkylen är det normalt bättre att välja en lämplig **prisstrategi** när du skapar rapporten.

Där kan du bland annat:

- prioritera grossister i valfri ordning,
- välja högsta eller lägsta pris,
- ange påslag eller rabatt,
- justera priser individuellt per uppgift.

### Påverkar prisvalet rapporten?

Ja. När du skapar en rapport kan du välja om prisstrategin ska baseras på **nettopris** (det pris rabattbreven ger) eller **listpris**. Nettopris är standardvalet och ger den mest aktuella kostnaden.
