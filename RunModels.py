from Account import Account
from Person import Person
from Dog import Dog
from Dog import Bulldog
from Shape import square
from Shape import circle


some_account = Account(100)
some_account.deposit(500)
some_account.deposit(100)
some_account.withdraw(200)
print(some_account.getbalance())

jay = Person("jay", 20)
jay.GetInformation()

maindog = Dog("justin", "breed")
maindog.bark()

bdog = Bulldog("justin", "bulldog")
bdog.run()


square_area = square("name ", 5, 5)
print(square_area.area())

circle = circle("name ", 10, 3.14)
print(circle.circumference())
