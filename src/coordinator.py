import time
from pathlib import Path

import pandas as pd

from research_agent import ResearchAgent
from storage import save

RESULTS = Path("outputs/results.csv")

completed = set()

if RESULTS.exists():
    completed = set(pd.read_csv(RESULTS)["name"].tolist())


class Coordinator:

    def __init__(self):
        self.agent = ResearchAgent()

    def run(self):

        apps = pd.read_csv("data/apps.csv")

        total = len(apps)

        for index, row in apps.iterrows():

            app_name = row["name"]
            docs_url = row["docs_url"]

            # 👇 PASTE IT HERE
            if app_name in completed:
                print(f"⏭️ Skipping {app_name} (already processed)")
                continue

            print(f"\n{'='*60}")
            print(f"[{index+1}/{total}] {app_name}")
            print(f"{'='*60}")

            try:

                result = self.agent.research(
                    app_name,
                    docs_url,
                )

                save(result)

                print(f"✅ Saved {app_name}")

                time.sleep(2)

            except Exception as e:

                print(f"❌ Failed: {app_name}")
                print(e)