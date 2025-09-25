from helper import User

def main():
    user = User(name="Павел", age=22)

    print(f"Имя: {user.name}, возраст: {user.age}")
    if user.is_adult():
        print("Совершеннолетний, доступ разрешён.")
    else:
        print("Несовершеннолетний, доступ ограничен.")


if __name__ == "__main__":
    main()