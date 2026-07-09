from scraper import scrape
from llm_service import analyze


class ResearchAgent:

    def research(
        self,
        app_name: str,
        docs_url: str,
    ):

        print(f"Scraping {docs_url}")

        documentation = scrape(docs_url)

        print(f"Collected {len(documentation)} characters")

        result = analyze(
            app_name,
            documentation,
            docs_url,
        )

        return result