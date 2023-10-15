from manager import exit_command


# Чистые функции
def test_exit_command():
    assert exit_command() is True
