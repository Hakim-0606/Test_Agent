from datetime import datetime
from app.models import Task, TaskCreate, TaskUpdate


class InMemoryDB:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._counter: int = 0

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def create(self, payload: TaskCreate) -> Task:
        self._counter += 1
        task = Task(
            id=self._counter,
            title=payload.title,
            description=payload.description,
            done=payload.done,
            created_at=datetime.now()
        )
        self._tasks[self._counter] = task
        return task

    def update(self, task_id: int, payload: TaskUpdate) -> Task | None:
        task = self._tasks.get(task_id)
        if not task:
            return None
        updated = task.model_copy(update=payload.model_dump(exclude_none=True))
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True


db = InMemoryDB()
