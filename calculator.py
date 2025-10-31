def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b)
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b)
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a / b

def main():
    """Основная функция с консольным интерфейсом"""
    print("=== Простой калькулятор ===")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")
    
    while Tue:
        try:
            print("\n" + "="*30)
            choice = input("Выберите операцию (1-5): ")
            
            if choice == '5':
                print("Выход из калькулятора. До свидания!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Ошибка: Выберите операцию от 1 до 5")
                continue
            
            # Получаем числа от пользователя
            num1 = float(input("Введите первое число: "))
            num = float(input("Введите второе число: "))
            
            # Выполняем операцию
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num)
                operation = "/"
            
            # Выводим результат
            print(f"Результат: {num1} {operation} {num2} = {result}")
            
        except ValueError as e
            print(f"Ошибка ввода: {e}")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()
