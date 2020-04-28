from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return "{name} {surname}".format(name=self.name, surname=self.surname)


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)
    average_cost = models.FloatField(default=0)

    def __str__(self):
        return "{make} {model}".format(make=self.make, model=self.model)


class Ride(models.Model):
    entry_date = models.DateField(null=True)
    date = models.DateField(null=True)
    distance = models.IntegerField(default=0)
    car = models.ForeignKey(Car, related_name='rides', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return "{distance} km at {entry_date}".format(distance=self.distance, entry_date=self.entry_date)


class Refuel(models.Model):
    date = models.DateField(null=True)
    price = models.IntegerField(default=0)
    car = models.ForeignKey(Car, related_name='refuels', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='refuels', on_delete=models.CASCADE)

    def __str__(self):
        return "{car} at {date} for {price} PLN".format(car=str(self.car), date=self.date, price=self.price)


class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    payer = models.ForeignKey(User, related_name='outgoing_transactions', on_delete=models.CASCADE)
    payee = models.ForeignKey(User, related_name='incoming_transactions', on_delete=models.CASCADE)

    def __str__(self):
        return "{amount} PLN from {payer} to {payee}".format(amount=self.amount, payer=self.payer, payee=self.payee)
