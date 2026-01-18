from collections import defaultdict

# Category keywords for intelligent classification
CATEGORY_KEYWORDS = {
    "sexual_harassment": ["harassment", "molest", "grope", "inappropriate"],
    "rape": ["rape", "sexual assault", "gang rape"],
    "stalking": ["stalk", "follow", "chase"],
    "domestic_violence": ["domestic", "husband", "family", "home"],
    "assault": ["assault", "attack", "beat", "violence"],
    "abuse": ["abuse", "torture", "cruelty"]
}

def determine_category(article):
    """Intelligently determine category based on article content"""
    text = (article["title"] + article["summary"]).lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    
    return "women_safety_incident"


def cluster_articles(articles):
    clusters = defaultdict(list)

    for a in articles:
        category = determine_category(a)
        key = (a.get("location", "Unknown"), category)
        clusters[key].append(a)

    results = []
    for (location, category), items in clusters.items():
        results.append({
            "cluster_title": f"{category.replace('_',' ').title()} in {location}",
            "location": location,
            "category": category,
            "incident_count": len(items),
            "articles": items
        })

    return results
