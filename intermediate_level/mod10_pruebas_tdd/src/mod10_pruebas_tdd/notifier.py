def send_notification(message: str) -> bool:  # send_notification mock dependency
    return True


def notify_user(message: str) -> bool:
    return send_notification(message)
