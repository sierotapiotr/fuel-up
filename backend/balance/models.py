from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    balance = models.FloatField


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    average_cost = models.FloatField


class Ride(models.Model):
    date = models.DateField
    length = models.IntegerField
    car = models.ForeignKey(Car, related_name='rides')
    user = models.ForeignKey(User, related_name='rides')


class Refuel(models.Model):
    date = models.DateField
    price = models.IntegerField
    car = models.ForeignKey(Car, related_name='refuels')
    user = models.ForeignKey(User, related_name='refuels')


class Transaction(models.Model):
    amount = models.IntegerField
    payer = models.ForeignKey(User, related_name='outgoing_transactions')
    payee = models.ForeignKey(User, related_name='incoming_transactions')
