from tasks import power_up

if __name__ == "__main__":
    result = power_up.delay("Goku")
    print("Task sent to Celery worker. Waiting for result...")
    print(result.get(timeout=20))
