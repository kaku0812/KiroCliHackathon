KEYWORDS = [
    "rape", "sexual", "harassment", "molestation",
    "woman", "women", "girl", "assault", "stalking",
    "abuse", "violence", "attack", "molest"
]

# Dynamic location extraction - no hardcoded list
def classify(article):
    text = (article["title"] + article["summary"]).lower()
    return any(k in text for k in KEYWORDS)


def extract_location(article, user_location=None):
    """Extract location from article or use user-specified location"""
    text = (article["title"] + article["summary"]).lower()
    
    # If user specified a location, ONLY return if it matches
    if user_location:
        if user_location.lower() in text:
            article["location"] = user_location.title()
            return article
        else:
            return None  # Don't include articles that don't match user location
    
    # Auto-detect for all articles when no location specified
    cities = ["delhi", "mumbai", "bangalore", "chennai", "kolkata", 
              "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow",
              "south delhi", "north delhi", "dwarka", "rohini"]
    
    for city in cities:
        if city in text:
            article["location"] = city.title()
            return article
    
    article["location"] = "Unknown"
    return article
