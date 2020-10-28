from abc import ABC, abstractmethod
# импортировал абстрактные классы и методы


class Bird(ABC):
    # абстрактный класс 'Воробей'

    def __init__(self, IsFull):
        self.__IsFull = IsFull

    # приватный метод для хранения булевой переменной,
    # отвечающей за внутреннее состояние воробья

    def __SetNewDecision__(self, ExternalFactor):
        data = ExternalFactor.GetDicisionAction(self.__IsFull)
        self.__DicisionAction = data[0]
        self.__DicisionAction.Apply()
        if self.__IsFull != data[1]:
            print('воробей перешел в состояние Сытый') if data[1] else print('воробей перешел в состояние Голодный')
        self.__IsFull = data[1]
    # приватный метод для применения, изменения и вывода состояний воробья,
    # внешнего фактора. Ссылка data хранит в себе 2 обьекта:
    # абстрактный метод Apply() и булевую переменную IsFull


class DicisionAction(object):
    # класс для действий воробья
    @abstractmethod
    def Apply(self):
        pass
    # абстрактный метод Apply()


class Fly(DicisionAction):
    def Apply(self):
        print('улететь')
# калсс для отдельного состояния воробья


class Eat(DicisionAction):
    def Apply(self):
        print('съесть')
# калсс для отдельного состояния воробья


class Sit(DicisionAction):
    def Apply(self):
        print('сидеть')
# калсс для отдельного состояния воробья


class ExternalFactor(object):
    # класс для обработки входных факторов
    @abstractmethod
    def GetDicisionAction(self, IsFull):
        return DicisionAction, IsFull
    # абстрактный метод возвращающий класс действия воробья
    # и его внутреннее состояние


class Cat(ExternalFactor):
    # класс внешнего фактора 'Кошка'
    def GetDicisionAction(self, IsFull):
        if IsFull == 1:
            IsFull = False
            return Fly(), IsFull
        elif IsFull == 2:
            return Fly(), IsFull
    # метод для обработки внутреннего состояния воробья
    # и внешнего фактора 'Кошка', возвращающий действие воробья
    # и его измененное внутреннее состояние


class Seeds(ExternalFactor):
    # класс внешнего фактора 'Семечки'
    def GetDicisionAction(self, IsFull):
        if IsFull == 1:
            IsFull = False
            return Sit(), IsFull
        elif IsFull == 2:
            IsFull = True
            return Eat(), IsFull
    # метод для обработки внутреннего состояния воробья
    # и внешнего фактора 'Семечки', возвращающий действие воробья
    # и его измененное внутреннее состояние


class Program(object):
    # отдельный класс для основного метода программы
    def Main(self):

        print("Варианты статуса воробья:\n 1 - Сытый\n 2 - Голодный\n")
        status = input('Введите ваш выбор:\n')
        print('Варианты фактора воробья:\n 1 - Семечки\n 2 - Кошка\n')
        factor = input('Введите ваш выбор:\n')
        # выбор внутреннего состояния воробья
        # и внешнего фактора
        try:
            int(status)
            int(factor)
        except ValueError:
            print('выберите число!')
            return 'error'
        # обработчик ошибок выбора
        bird = Bird(int(status))
        if int(factor) == 1:
            print('Повдение воробья:\n')
            bird.__SetNewDecision__(Seeds())
        elif int(factor) == 2:
            print('Повдение воробья:\n')
            bird.__SetNewDecision__(Cat())
            # обработчик выбора пользователя

    if __name__ == '__main__':
        Main(self=True)
        # вызов функции Main()
