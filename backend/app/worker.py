import sys
sys.path.append('/app')
from app import create_app, db
import json
from app.models.product import Product


app = create_app()
redis_client = app.redis


def process_message(message):
    msg = json.loads(message)
    op = msg["operation"]
    data = msg["data"]

    print(f"[WORKER] Recebida operação: {op} | Dados: {data}")

    if op == "create":
        p = Product(**data)
        db.session.add(p)
        print(f"[WORKER] Produto criado: {p}")

    elif op == "update":
        p = Product.query.get(data["id"])
        if p:
            p.name = data.get("name", p.name)
            p.price = data.get("price", p.price)
            print(f"[WORKER] Produto atualizado: {p}")
        else:
            print(f"[WORKER] Produto id={data['id']} não encontrado para atualização.")

    elif op == "delete":
        p = Product.query.get(data["id"])
        if p:
            db.session.delete(p)
            print(f"[WORKER] Produto deletado: id={data['id']}")
        else:
            print(f"[WORKER] Produto id={data['id']} não encontrado para deleção.")

    db.session.commit()
    print(f"[WORKER] Operação '{op}' processada.")


def run_worker():
    print("[WORKER] Iniciando...")
    with app.app_context():
        queue_name = app.config.get("REDIS_QUEUE_NAME", "products_queue")
        while True:
            message = redis_client.brpop(queue_name)
            process_message(message[1])


if __name__ == "__main__":
    run_worker()
