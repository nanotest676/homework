class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                training_type: float,
                duration: float,
                distance: float,
                speed: float,
                calories: float
                ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        
    
    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type:.3f}; '
                f'Длительность: {self.duration:.3f} ч.; Дистанция: {self.distance:.3f} км;' 
                f'Ср. скорость: {self.speed:.3f} км/ч; Потрачено ккал: {self.calories:.3f}.')
    


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float
               # M_IN_KM: 
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = LEN_STEP
        self.M_IN_KM = 1000
        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return super().get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage() 


class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                action: int,
                duration: float,
                weight: float
                ):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000
        
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    
    def get_spent_calories(self) -> float:
        Duration_in_min = (self.duration * 60)
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * super().get_mean_speed()
                 + self.CALORIES_MEAN_SPEED_SHIFT)
                 * self.weight / self.M_IN_KM * self.Duration_in_min)
 


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
            action: int,
            duration: float,
            weight: float,
            height: float,
            speed: float
            ):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.height = height
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000
        self.speed = speed
        Speed_in_second = self.speed * 1000 / 3600
        Duration_in_min = self.duration * 60
    def get_spent_calories(self) -> float:
        return (0.035 * self.weight + (self.Speed_in_second **2 / self.height)
           * 0.029 * self.weight) * self.Duration_in_min


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,
            count_pool: int
            ):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38
        self.M_IN_KM = 1000

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight * self.duration
    #Формула для расчёта израсходованных калорий:
    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration 
    #Формула расчёта средней скорости при плавании:
    
    #LEN_STEP
    
    #Есть и ещё один параметр, который надо переопределить, 
    # ведь расстояние, преодолеваемое за один гребок, отличается от 
    # длины шага. Значит, необходимо переопределить 
    # атрибут LEN_STEP базового класса.
    


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    Sport = {'RUN': Running,
             'WLK': SportsWalking,
             'SWM': Swimming}
    training = Sport[workout_type](*data)
    return training

def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)



