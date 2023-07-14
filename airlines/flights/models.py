from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} - {self.code}"


class Flight(models.Model):
    """Аргумент CASCADE - Каскадное поведение обычно используется при настройке отношений между моделями.
     Когда объект, на который имеется ссылка, удаляется, все объекты, ссылающиеся на этот объект, также будут удалены."""
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,
                               related_name='departures')  # Связываем две таблицы on_delete - нужен если мы удаляем из одной таблицы, то мы удаляем и из другой с помощбю models.CASCADE
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE,
                                    related_name='arrivals')  # related_name - используется для досьупа в обратном порядке hrl.arrivals.all() в консоле для просмотра данных
    duration = models.IntegerField()

    def __str__(self):
        return f"from {self.origin} to {self.destination} for {self.duration}"

    """Создай таблицы, а потом зарегай их в admin.py 
    admin.site.register(Airport)
    admin.site.register(Flight) - это важно, но сначала миграции"""


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passenger')

    def __str__(self):
        return f"{self.first} {self.last}: {self.flights}"

