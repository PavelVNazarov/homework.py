# Домашнее задание
# Назаров ПВ
# module_14_1_old.py



from datetime import datetime

class SuperDate(datetime):
    # Словарь для определения сезонов
    seasons = {
        1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring',
        5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }
    
    # Словарь для определения времени суток
    times_of_day = {
        (0, 6): 'Night',
        (6, 12): 'Morning',
        (12, 18): 'Day',
        (18, 24): 'Evening'
    }

    def get_season(self):
        """Возвращает сезон года."""
        month = self.month
        return self.seasons.get(month, "Unknown season")

    def get_time_of_day(self):
        """Возвращает время суток."""
        hour = self.hour
        
        for time_range, time_of_day in self.times_of_day.items():
            if time_range[0] <= hour < time_range[1]:
                return time_of_day
        return "Unknown time"

# Пример работы класса
if __name__ == "__main__":
    a = SuperDate(2024, 2, 22, 12)

Для создания класса `SuperDate`, который наследуется от `datetime` и добавляет новые методы, можно использовать следующий подход. Мы создадим класс, который будет реализовывать методы `get_season` и `get_time_of_day`. Вот пример реализации:

```python
from datetime import datetime

class SuperDate(datetime):
    SEASONS = {
        (1, 2, 3): 'Winter',  # Декабрь, Январь, Февраль
        (3, 4, 5): 'Spring',  # Март, Апрель, Май
        (5, 6, 7): 'Summer',  # Июнь, Июль, Август
        (9, 10, 11): 'Autumn'  # Сентябрь, Октябрь, Ноябрь
    }

    def get_season(self):
        month = self.month
        for months, season in self.SEASONS.items():
            if month in months:
                return season
        return 'Unknown season'

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Day'
        elif 18 <= hour < 24:
            return 'Evening'
        else:
            return
