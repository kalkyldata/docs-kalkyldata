---
title: Vad är nytt?
layout: default
parent: Nyheter
nav_order: 1
permalink: /nyheter/vad-ar-nytt/
description: Senaste nyheterna och förbättringarna i Kalkyldata.
category: news
tags:
  - nyheter
  - uppdateringar
audience: user
---

# Vad är nytt?

Här hittar du de senaste nyheterna och förbättringarna i Kalkyldata.

---

{% assign news_array = site.data.news | sort %}
{% assign current_year = "" %}

{% for entry in news_array reversed %}
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
