# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('C:\\Users\\user\\Desktop\\Python Homework\\Homework_8\\app\\log.txt', 'a+') as file:
        file.write(f"Задача: {expr}, Ответ: {result}\n")



def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('C:\\Users\\user\\Desktop\\Python Homework\\Homework_8\\app\\log.txt', 'r') as file:
        data = file.read()
        print(f"{data}")