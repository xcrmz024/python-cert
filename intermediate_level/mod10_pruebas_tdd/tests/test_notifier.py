from unittest.mock import patch

from mod10_pruebas_tdd.notifier import notify_user


@patch("mod10_pruebas_tdd.notifier.send_notification")
def test_notify_user(mock_send_notification):
    mock_send_notification.return_value = True

    result = notify_user("Test message")

    assert result is True
    mock_send_notification.assert_called_once_with("Test message")
