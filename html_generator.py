def generate_html(clusters):
    markers = ""
    cards = ""

    for c in clusters:
        lat, lng = c["lat"], c["lng"]

        markers += f"""
        L.marker([{lat}, {lng}]).addTo(map)
          .bindPopup("<b>{c['cluster_title']}</b><br>{c['incident_count']} reports");
        """

        article_links = "".join(
            f"<li><a href='{a['url']}' target='_blank'>{a['title']}</a></li>"
            for a in c["articles"]
        )

        cards += f"""
        <div class="card">
          <h3>{c['cluster_title']}</h3>
          <p>{c['incident_count']} related reports</p>
          <ul>{article_links}</ul>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
  <title>Women Safety News</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="static/styles.css">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
</head>
<body>

<h1>Women Safety Incidents – Delhi</h1>

<div id="map"></div>

<div class="grid">{cards}</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  const map = L.map('map').setView([28.6139, 77.2090], 11);
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    attribution: '© OpenStreetMap contributors'
  }}).addTo(map);
  {markers}
</script>

</body>
</html>
"""
