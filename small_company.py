class User:
    """Класс для представления обычного пользователя."""

    def __init__(self, user_id, name):
        self.__user_id = user_id  # Уникальный идентификатор пользователя
        self.__name = name  # Имя пользователя
        self.__access_level = 'user'  # Уровень доступа по умолчанию

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):
    """Класс для представления администратора, наследуется от User."""

    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Инициализация родительского класса
        self.__access_level = 'admin'  # Уровень доступа для администратора

    # Метод для добавления пользователя в систему
    def add_user(self, user_list, user):
        """Добавляет пользователя в список пользователей."""
        user_list.append(user)  # Добавляем пользователя в список

    # Метод для удаления пользователя из системы
    def remove_user(self, user_list, user):
        """Удаляет пользователя из списка пользователей."""
        if user in user_list:
            user_list.remove(user)  # Удаляем пользователя из списка
        else:
            print("Пользователь не найден в списке.")  # Сообщение, если пользователь не найден
