from profpy.web import SecureFlaskApp
from profpy.db import get_sql_alchemy_oracle_engine
from flask import render_template
{asset_import}

engine = get_sql_alchemy_oracle_engine()
tables = {tables}

app = SecureFlaskApp(
    __name__, "{app_name}", engine, tables
)

{asset_config}

@app.route("/index")
@app.secured()
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)