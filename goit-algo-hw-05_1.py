def caching_fibonacci():        # Функція для створення та повернення внутрішньої функції fibonacci(n)
    cache = {}                  # Пустий словник для кешу

    def fibonacci(n):           # Функція для обчислення n-го числа Фібоначчі
        if n is cache:          # Перевірка чи є число у кеші
            return cache[n]     # Повернення якщо є
        
        if n <= 1:              # Перевірка на нуль та один
            return n

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Обчислення 
        return cache[n]

    return fibonacci


fib = caching_fibonacci() # Виклик функції
print(fib(10)) # Прінтуємо 
print(fib(15))
