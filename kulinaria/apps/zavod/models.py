from django.db import models

class Suplier(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Поставщик", unique=True)

    def __str__(self):
        return self.company_name


class Ingredients(models.Model):
    name = models.CharField(max_length=255, unique=True)
    count = models.IntegerField()
    delivery = models.ForeignKey(Suplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Store(models.Model):
    store_name = models.CharField(max_length=255, verbose_name="Название магазина")
    address = models.CharField(max_length=255, verbose_name="Адрес магазина")

    def __str__(self):
        return self.store_name


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.ManyToManyField(Ingredients, verbose_name="Необходимые ингредиенты для выпечки")
    transfer_to = models.ManyToManyField(Store)
    cost = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.name


class Produced(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество")
    date = models.DateField(verbose_name="Дата выпечки")

    def __str__(self):
        return self.menu.name


class Purchase(models.Model):
    Sell = models.ForeignKey(Menu, to_field="name", verbose_name="Prodano", on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.Sell} {self.count} {self.date}"


