---
layout: default
title: Changelog
nav_order: 6
---

# Uppdateringar och Changelog
Här kan du se allt nytt som händer i systemet, från stort till smått.

---

{% assign changelog_array = site.data.changelog | sort %}
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
