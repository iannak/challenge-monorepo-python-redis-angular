import json
from app import redis_client


def enqueue_operation(operation, data):
    from app import redis_client
    from flask import current_app
    message = json.dumps({
        "operation": operation,
        "data": data
    })
    queue_name = current_app.config.get("REDIS_QUEUE_NAME", "products_queue")
    redis_client.lpush(queue_name, message)
