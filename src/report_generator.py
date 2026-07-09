import pandas as pd
from pathlib import Path

OUTPUT = Path("outputs/results.csv")
REPORT = Path("outputs/report.html")


def generate_report():

    df = pd.read_csv(OUTPUT)

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>AI Product Ops Assignment</title>

<style>

body {{
    font-family: Arial;
    max-width: 1200px;
    margin:auto;
    padding:40px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th,td {{
    border:1px solid #ddd;
    padding:8px;
}}

th {{
    background:#111;
    color:white;
}}

h1,h2 {{
    margin-top:40px;
}}

.card {{
    background:#f6f6f6;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
}}

</style>

</head>

<body>

<h1>AI Product Ops Research Report</h1>

<div class="card">

<h2>Overview</h2>

<p>Total Apps: {len(df)}</p>

<p>Buildable:
{df["buildable"].sum()}</p>

<p>MCP Available:
{df["mcp_available"].sum()}</p>

<p>Self Serve:
{(df["self_serve"]=="Yes").sum()}</p>

</div>

<h2>Research Results</h2>

{df.to_html(index=False)}

</body>

</html>
"""

    REPORT.write_text(
        html,
        encoding="utf-8"
    )

    print("Report Generated!")