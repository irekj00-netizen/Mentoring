#2
class Counter:
  def __init__(self, stan):
    self.stan = stan
  def increment(self, stan):
    self.stan += 1
  def show(self):
    print(self.stan)
  def reset(self):
    self.stan = 0

#6
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  def __len__(self):
    return self.pages

#8
class Animal:
  def __init__(self, name, number_of_legs, breed, age):
    self.name = name
    self.number_of_legs = number_of_legs
    self.breed = breed
    self.age = age
class Dog(Animal):
  def make_sound(self):
    return "Hau, hau!"
class Cat(Animal):
  def make_sound(self):
    return "Miau, miau!"

#13
class BankAccount:
  def __init__(self, balance):
    self.__balance = balance
  def get_balance(self):
    if self.__balance < 0:
      print("Uwaga! Ujemny stan konta: ",self.__balance)
    return self.__balance
  def set_balance(self, amount):
    self.__balance = amount

#15
class RivalBankAccount:
  def __init__(self, balance):
    self.__balance = balance
  @property
  def balance(self):
    if self.__balance < 0:
      print("Uwaga! Ujemny stan konta: ",self.__balance)
    return self.__balance
  @balance.setter
  def balance(self, amount):
    self.__balance = amount

#16
class Temperature:
  def __init__(self, temp):
    self.__temp = temp
  @property
  def celsius(self):
    return (self.__temp - 32) * 5/9
  @property
  def fahrenheit(self):
    return (self.__temp * 9/5) + 32