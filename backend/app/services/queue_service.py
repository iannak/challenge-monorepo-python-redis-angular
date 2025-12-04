import json
from flask import current_app


def enqueue_operation(operation, data):
    message = json.dumps({
        "operation": operation,
        "data": data
    })
    queue_name = current_app.config.get("REDIS_QUEUE_NAME", "products_queue")
    redis_client = current_app.redis
    redis_client.lpush(queue_name, message)
