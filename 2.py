# 2)Создайте класс CoffeeMachine,
#  конструктор которого имеет параметры milk (молоко), coffee (кофе), sugar (сахар). 
#  По умолчанию значения количества молока, кофе и сахара в кофейном аппарате будут 
#  равны: milk = 1000 (мл), coffee= 1000 (гр), sugar = 1000 (гр). Добавьте метод make_coffee,
#   который будет принимать параметры milk, coffee, sugar. Пусть эти данные вводит пользователь.
# В самом начале проверьте, хватит ли вам ингредиентов. Если его хватит для приготовления кофе,
# то вычтите использованное количество ингредиентов, но не напрямую,
# а с помощью приватных методов __subtract_ milk, __subtract_coffee, __subtract_sugar.
# Помимо этого пусть метод make_coffee распечатает на экран “Процесс приготовления
# кофезавершен!”. 
# 
# Если же ингредиентов не хватит, то распечатайте, какого именно
# ингредиента (ингредиентов) не хватает и сколько нужно пополнить запасов. 
# 
# То есть,
# должны вывести сообщение, например: “Пополните запасы молока на 500 мл!
# Пополните запасы кофе на 100 гр! Пополните запасы сахара на 100 гр.”. 
# Не забудьте использовать конструкцию if __name__ == ‘__main__’.


class CoffeeMachine:
    def __init__(self, milk,coffee,sugar):
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar
    def make_coffee(self,milk,coffee,sugar):
        if milk > self.milk and coffee > self.coffee and sugar > self.sugar:
            resultat = milk - self.milk
            resultat2 = coffee - self.coffee
            resultat3 = sugar - self.sugar
            print(f"Не хватает: \nмолоко-{resultat} мл\nкофе-{resultat2} гр\nсахар-{resultat3} гр")
        elif milk > self.milk and coffee > self.coffee and sugar < self.sugar:
            resultat = milk - self.milk
            resultat2 = coffee - self.coffee
            print(f"Пополните запасы молока на-{resultat} мл и кофе-{resultat2} гр")
        elif milk > self.milk and coffee < self.coffee and sugar > self.sugar:
            resultat = milk - self.milk
            resultat2 = coffee - self.coffee
            print(f"Пополните запасы молока на-{resultat} мл и сахара-{resultat2} гр")
        elif milk < self.milk and coffee > self.coffee and sugar > self.sugar:
            resultat = sugar - self.sugar
            resultat2 = coffee - self.coffee
            print(f"Пополните запасы кофе на-{coffee} гр и сахара-{sugar} гр")
        elif milk > self.milk and coffee < self.coffee and sugar < self.sugar:
            resultat = milk - self.milk
            print(f"Пополните запасы молока на-{resultat} мл")
        elif milk < self.milk and coffee > self.coffee and sugar < self.sugar:
            resultat = coffee - self.coffee
            print(f"Пополните запасы кофе на-{resultat} гр")
        elif milk < self.milk and coffee < self.coffee and sugar > self.sugar:
            resultat = sugar - self.sugar  
            print(f"Пополните запасы сахара на-{resultat} гр")
        elif milk < self.milk and coffee < self.coffee and sugar < self.sugar:
            self.__substract_milk(milk)
            self.__substract_coffee(coffee)
            self.__subtsract_sugar(sugar)
            print(f"\n\nПроцесс приготовления кофе завершен!\nУ Вас осталось: \nмолоко-{self.milk} мл\nкофе-{self.coffee} гр\nсахар-{self.sugar} гр")
    def __substract_milk(self,milk):
        self.milk -= milk  
    def __substract_coffee(self,coffee):
        self.coffee -= coffee
    def __subtsract_sugar(self,sugar):
        self.sugar -= sugar
def main():
    my_coffee = CoffeeMachine(1000,1000,1000)
    my_coffee.make_coffee(int(input("молоко: ")),int(input("кофе: ")),int(input("сахар: ")))
if __name__ == "__main__":
    main()