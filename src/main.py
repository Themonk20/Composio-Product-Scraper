from coordinator import Coordinator
from insights import InsightGenerator

from report_generator import generate_report


Coordinator().run()

print("\nResearch Complete!")

insights = InsightGenerator()

insights.print_report()


generate_report()