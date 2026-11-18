import app


def test_add_task():
    app.tasks.clear()
    task = app.add_task("Buy milk")
    assert task["title"] == "Buy milk"
    assert task["done"] is False


def test_complete_task():
    app.tasks.clear()
    app.add_task("Read book")
    assert app.complete_task(0)["done"] is True
