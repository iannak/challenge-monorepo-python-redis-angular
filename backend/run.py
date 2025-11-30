from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    import subprocess
    print("[INIT] Executando flask db upgrade...")
    subprocess.run(["flask", "db", "upgrade"])
    app.run(host="0.0.0.0", port=5000, debug=True)
