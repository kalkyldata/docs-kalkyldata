---
layout: default
title: Uppdateringar prislistor
nav_order: 4
---

# Uppdateringar prislistor
Här kan du följa hur vi löpande håller Kalkyldatas materialpriser uppdaterade. Vi loggar varje gång vi läser in nya prislistor från våra anslutna grossister och leverantörer.

---

{% assign changelog_array = site.data.pricelists | sort %}
{% assign current_year = "" %}

{% for entry in changelog_array reversed %}
  {% assign data = entry[1] %}
  {% assign entry_year = data.date | slice: 0, 4 %}

  {% if entry_year != current_year %}
    {% assign current_year = entry_year %}
## År {{ current_year }}
  {% endif %}

### {{ data.date }} – {{ data.title }}
{{ data.description }}

---
{% endfor %}
