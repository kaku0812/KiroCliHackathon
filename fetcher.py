import feedparser

def fetch_rss(url):
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "summary": entry.get("summary", ""),
            "published": entry.get("published", ""),
            "url": entry.link,
            "source": feed.feed.get("title", "Unknown")
        })

    return articles


def fetch_all(sources):
    all_articles = []
    for urls in sources.values():
        for url in urls:
            all_articles.extend(fetch_rss(url))
    return all_articles
