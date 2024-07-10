print("Stack")
# class Stack:
#   def __init__(self):
#     self.stack = []
#
#   # Додавання елемента до стеку
#   def push(self, item):
#     self.stack.append(item)
#
#   # Видалення елемента зі стеку
#   def pop(self):
#     if len(self.stack) < 1:
#       return None
#     return self.stack.pop()
#
#   # Перевірка, чи стек порожній
#   def is_empty(self):
#     return len(self.stack) == 0
#
#   # Перегляд верхнього елемента стеку без його видалення
#   def peek(self):
#     if not self.is_empty():
#       return self.stack[-1]
#
#   def __str__(self):
#     if not self.is_empty():
#       return str(self.stack)
#     else:
#       return None
#
#
# if __name__ == '__main__':
#     stack = Stack()
#
#     for i in range(5):
#         stack.push(i)
#
#     print(stack)
#     print(stack.peek())
#     print("Pop", stack.pop())
#     print(stack)
#     print(stack.peek())

print("Inf Post")
def infix_to_postfix(exp: str) -> str:
    priority = {'+': 1, "-": 1, "*": 2, "/": 2}  # Оператори та їх пріоритети
    output = []  # Список для зберігання постфіксного виразу
    stack = []   # Стек для тимчасового зберігання операторів
    # Розділяємо вхідний інфіксний вираз на токени (операнди та оператори)
    for token in exp.split():
        if token.isdigit():
            output.append(token)  # Якщо токен є операндом (число), додаємо його до виходу
        elif token in priority:
            # Якщо токен є оператором, обробляємо пріоритет операторів за допомогою стеку
            while stack and priority[stack[-1]] >= priority[token]:
                output.append(stack.pop())  # Видаляємо оператори з вищим або рівним пріоритетом
            stack.append(token)  # Додаємо поточний оператор до стеку
    # Видаляємо всі залишкові оператори зі стеку до виходу
    while stack:
        output.append(stack.pop())
    # Повертаємо постфіксний вираз у вигляді рядка
    return ' '.join(output)
#
# # Вхідний інфіксний вираз
# expression = "3 + 4 * 2 + 1 - 3 * 2"
# # Перетворюємо інфіксний вираз в постфіксний
# postfix_expr = infix_to_postfix(expression)
# # Виводимо результат
# print(postfix_expr)  # Виведе "3 4 2 * + 1 + 3 2 * -"
# print(eval(expression))
