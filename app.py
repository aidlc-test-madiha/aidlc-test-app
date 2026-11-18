tasks = []


def add_task(title):
    tasks.append({"title": title, "done": False})
    return tasks[-1]


def complete_task(index):
    tasks[index]["done"] = True
    return tasks[index]


def list_tasks():
    return tasks
