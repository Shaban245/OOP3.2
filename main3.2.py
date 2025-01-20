class Patient:
    def __init__(self, first_name: str, second_name: str, age: int, day: int, month: str, time: str, virus: str):
        """
        :param first_name: имя
        :param second_name: фамилия
        :param age: возраст
        :param day: день
        :param month: месяц
        :param time: время типа 00:00
        :param virus: болезнь
        """
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.day = day
        self.month = month
        self.time = time
        self.virus =virus

    def reception(self):
        return f"{self.first_name, self.second_name },  вы были записаны {self.day , self.month} в {self.time}"

    def status_patient(self):
        return f"Статус пациента \nИмя: {self.first_name} \nФамилия: {self.second_name} \nБолезнь: {self.virus}"


class TouristSpot:
    def __init__(self, name: str, country: str, type: str, data: str ):
        """

        :param name: название достопримечательности
        :param country: страна в которой находиится достопримечательность
        :param type: тип: историческая религиозная и тп
        :param data: год основания
        """
        self.name = name
        self.country = country
        self.type = type
        self.data = data


