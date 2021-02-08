class Money:

    def __init__(self):
        self.__saved_money = 1000

    def send_money(self, salay: int = 0):
        self.__saved_money += salay

    def select_money(self, name):
        return self.__saved_money

    def __select_money1(self):
        return self.__saved_money


if __name__ == '__main__':
    a = Money
    print(a.__dict__.keys())
