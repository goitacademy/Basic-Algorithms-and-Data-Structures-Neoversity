import heapq


class Task:
    def __init__(self, description, story_points, priority_level):
        self.description = description
        self.story_points = story_points
        self.priority_level = priority_level

    def __lt__(self, other):
        # Порівнюємо спочатку за рівнем пріоритету, потім за кількістю story points
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        if priority_order[self.priority_level] == priority_order[other.priority_level]:
            return self.story_points < other.story_points
        return priority_order[self.priority_level] < priority_order[other.priority_level]

    def __repr__(self):
        return f"Task(description={self.description}, story_points={self.story_points}, priority_level={self.priority_level})"


class TaskBoard:
    def __init__(self):
        self.task_heap = []

    def add_task(self, description, story_points, priority_level):
        task = Task(description, story_points, priority_level)
        heapq.heappush(self.task_heap, task)

    def get_next_task(self):
        return heapq.heappop(self.task_heap) if self.task_heap else None

    def peek_next_task(self):
        return self.task_heap[0] if self.task_heap else None

    def is_empty(self):
        return len(self.task_heap) == 0


# Приклад використання
def example_usage():
    task_board = TaskBoard()
    task_board.add_task("Implement login feature", 5, "high")
    task_board.add_task("Fix bug in user profile", 2, "medium")
    task_board.add_task("Update documentation", 1, "low")
    task_board.add_task("Refactor codebase", 8, "medium")
    task_board.add_task("Write unit tests", 3, "high")

    # Перегляд завдань
    print("All tasks on the board:")
    for task in task_board.task_heap:
        print(task)

    # Отримання наступного завдання
    print("\nNext task to work on:")
    print(task_board.get_next_task())  # Очікуємо завдання з пріоритетом "high" і найменшою кількістю story points

    # Перегляд наступного завдання без його видалення
    print("\nPeek next task without removing:")
    print(task_board.peek_next_task())  # Очікуємо завдання з пріоритетом "high" (наступне за важливістю)

    # Видалення і отримання всіх завдань у порядку пріоритету
    print("\nRemoving tasks in order of priority:")
    while not task_board.is_empty():
        print(task_board.get_next_task())


# Виконання прикладу
example_usage()
