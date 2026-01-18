from mcp.server.fastmcp import FastMCP

from rss_sources import RSS_SOURCES
from fetcher import fetch_all
from processor import classify, extract_location
from clustering import cluster_articles
from geocode import geocode
from html_generator import generate_html

mcp = FastMCP("women-safety-news")

@mcp.tool()
def women_safety_news_dashboard(location: str = None):
    """
    Generate a clustered women safety news dashboard with map and links.
    Fetches RSS feeds, filters women safety incidents, clusters by location
    
    Args:
        location: Optional location to filter articles (e.g., "delhi", "mumbai", "bangalore")
    """
    try:
        # Fetch articles
        raw = fetch_all(RSS_SOURCES)
        
        # Filter and process
        processed = []
        for a in raw:
            if classify(a):
                article = extract_location(a, location)
                if article:  # Only add if not None
                    processed.append(article)
        
        if not processed:
            return {
                "message": "No relevant articles found",
                "file": None,
                "clusters": []
            }
        
        # Cluster by location
        clusters = cluster_articles(processed)
        
        return {
            "message": f"Found {len(processed)} articles in {len(clusters)} clusters",
            "clusters": clusters
        }
        
    except Exception as e:
        return {
            "message": f"Error generating summary of news articles: {str(e)}",
            "error": str(e)
        }

if __name__ == "__main__":
    mcp.run(transport="stdio")
