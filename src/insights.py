from collections import Counter
import pandas as pd


class InsightGenerator:

    def __init__(self, csv_path="outputs/results.csv"):
        self.df = pd.read_csv(csv_path)

    def percentage(self, count):
        return round((count / len(self.df)) * 100, 1)

    def auth_summary(self):
        counter = Counter()

        for value in self.df["auth_methods"]:
            methods = [m.strip() for m in str(value).split(",")]

            for method in methods:
                if method:
                    counter[method] += 1

        return counter

    def blocker_summary(self):
        return self.df["blocker"].value_counts()

    def category_summary(self):
        return self.df["category"].value_counts()

    def api_summary(self):
        return self.df["api_type"].value_counts()

    def toolkit_summary(self):
        return self.df["toolkit_priority"].value_counts()

    def difficulty_summary(self):
        return self.df["integration_difficulty"].value_counts()

    def self_serve_summary(self):
        return self.df["self_serve"].value_counts()

    def mcp_summary(self):
        return self.df["mcp_available"].value_counts()

    def buildable_summary(self):
        return self.df["buildable"].value_counts()

    def print_report(self):

        print("\n========== DATASET ==========")
        print(f"Apps Researched: {len(self.df)}")

        print("\n========== AUTH ==========")
        print(self.auth_summary())

        print("\n========== CATEGORY ==========")
        print(self.category_summary())

        print("\n========== API ==========")
        print(self.api_summary())

        print("\n========== BLOCKERS ==========")
        print(self.blocker_summary())

        print("\n========== SELF SERVE ==========")
        print(self.self_serve_summary())

        print("\n========== MCP ==========")
        print(self.mcp_summary())

        print("\n========== TOOLKIT PRIORITY ==========")
        print(self.toolkit_summary())

        print("\n========== DIFFICULTY ==========")
        print(self.difficulty_summary())

        print("\n========== BUILDABLE ==========")
        print(self.buildable_summary())
        