from pathlib import Path

import pandas as pd

OUTPUT = Path("outputs/results.csv")


def save(app):

    row = {
        "name": app.name,
        "category": app.category,
        "description": app.description,
        "auth_methods": ", ".join(app.auth_methods),
        "self_serve": app.self_serve,
        "api_type": app.api_type,
        "api_scope": app.api_scope,
        "mcp_available": app.mcp_available,
        "buildable": app.buildable,
        "blocker": app.blocker,
        "evidence": ", ".join(app.evidence),
        "toolkit_priority": app.toolkit_priority,
        "integration_difficulty": app.integration_difficulty,
    }

    if OUTPUT.exists():
        df = pd.read_csv(OUTPUT)

        # Update existing row if app already exists
        df = df[df["name"] != app.name]

        df = pd.concat(
            [df, pd.DataFrame([row])],
            ignore_index=True,
        )

    else:
        df = pd.DataFrame([row])

    df.to_csv(
        OUTPUT,
        index=False,
    )