from abc import ABC, abstractmethod


class Resurse():
    def __init__(self, resurse_name: str, num_per_minute: float = 0):
        self.resurse_name = resurse_name
        self.num_per_minute = num_per_minute

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.resurse_name == other.resurse_name

    def __add__(self, other):
        if self == other:
            self.num_per_minute += other.num_per_minute
            return self
        elif isinstance(other, (int, float)):
            self.num_per_minute += other
            return self

    def __sub__(self, other):
        if self == other:
            self.num_per_minute -= other.num_per_minute
            return self
        elif isinstance(other, (int, float)):
            self.num_per_minute -= other
            return self

    def __hash__(self):
        return hash(self.resurse_name)

    def __str__(self):
        return f'{self.resurse_name}({self.num_per_minute})'


class Factory():

    def __init__(self, recept_name:str, count:int = 1, power:float = 100):
        self.recept = self.recept_list[recept_name]
        self.count = count
        self.power = power

class Costruct(Factory):
    recept_list = {'Железная пластина': ((Resurse('Железный слиток', 30),), (Resurse('Железная пластина', 20),)),
                   'Железный прут': ((Resurse('Железный слиток', 15),), (Resurse('Железный прут', 15),)),
                   'Стальная балка': ((Resurse('Стальной слиток', 60),), (Resurse('Стальная балка', 15),)),
                   'Стальная труба': ((Resurse('Стальной слиток', 30),), (Resurse('Стальная труба', 20),)),
                   'Пустая канистра': ((Resurse('Пластик', 30),), (Resurse('Пустая канистра', 60),)),
                   'Кварцевый кристалл': ((Resurse('Неогранённый кварц', 37.5),), (Resurse('Кварцевый кристалл', 22.5),)),
                   'Алюминиевый корпус': ((Resurse('Алюминиевый слиток', 90),), (Resurse('Алюминиевый корпус', 60),)),
                   'Кремнезём': ((Resurse('Неогранённый кварц', 22.5),), (Resurse('Кремнезём', 37.5),)),
                   'Медный лист': ((Resurse('Медный слиток', 20),), (Resurse('Медный лист', 10),)),
                   'Медный порошок': ((Resurse('Медный слиток', 300),), (Resurse('Медный порошок', 50),)),
                   'Пустой баллон': ((Resurse('Алюминиевый слиток', 60),), (Resurse('Пустой баллон', 60),)),
                   'Сверхпроволока': ((Resurse('Катерийный слиток', 12),), (Resurse('Сверхпроволока', 60),)),
                   'Бетон': ((Resurse('Известняк', 45),), (Resurse('Бетон', 15),)),
                   'Винты': ((Resurse('Железный прут', 10),), (Resurse('Винты', 40),)),
                   'Кабель': ((Resurse('Проволока', 60),), (Resurse('Кабель', 30),)),
                   'Проволока': ((Resurse('Медный слиток', 15),), (Resurse('Проволока', 30),)),
                   'Альт.: Стальной прут': ((Resurse('Стальной слиток', 12),), (Resurse('Железный прут', 48),)),
                   'Альт.: Стальная канистра': ((Resurse('Стальной слиток', 60),), (Resurse('Пустая канистра', 40),)),
                   'Альт.: Катерийная проволока': ((Resurse('Катерийный слиток', 15),), (Resurse('Проволока', 120),)),
                   'Альт.: Железная проволока': ((Resurse('Железный слиток', 12.5),), (Resurse('Проволока', 22.5),)),
                   'Альт.: Cтальные винты': ((Resurse('Стальная балка', 5),), (Resurse('Винты', 260),)),
                   'Альт.: Литые винты': ((Resurse('Железный слиток', 12.5),), (Resurse('Винты', 50),))

                   }


class Drilling(Factory):
    '''
    класс буровая
    '''
    def __init__(self, recept_name:str, production:float, count:int = 1, power:float = 100):
        self.recept = ((), (Resurse(recept_name, production),))
        self.count = count
        self.power = power

class Resurse_List():
    def __init__(self):
        self.resurse_list = [Resurse('Известняк'),  #  Руды
                             Resurse('Железная руда'),
                             Resurse('Медная руда'),
                             Resurse('Катерийная руда'),
                             Resurse('Уголь'),
                             Resurse('Неограненный кварц'),
                             Resurse('Сера'),
                             Resurse('Боксит'),
                             Resurse('Руда СИМ'),
                             Resurse('Уран'),

                             Resurse('Железный слиток'),  #  Слитки
                             Resurse('Медный слиток'),
                             Resurse('Катерийный слиток'),
                             Resurse('Стальной слиток'),
                             Resurse('Алюминиевый слиток'),

                             Resurse('Бетон'),  #  Минералы
                             Resurse('Кварцевые кристалы'),
                             Resurse('Кремнезем'),
                             Resurse('Медный порошок'),
                             Resurse('Полимерная смола'),
                             Resurse('Нефтяной кокс'),
                             Resurse('Алюминиевый лом'),

                             Resurse('Вода'),  #  Жидкости, газы
                             Resurse('Сырая нефть'),
                             Resurse('Мазут'),
                             Resurse('Топливо'),
                             Resurse('Турботопливо'),
                             Resurse('Раствор глинозема'),
                             Resurse('Серная кислота'),
                             Resurse('Азотная кислота'),
                             Resurse('Азот'),


                             Resurse('Железный прут'), #  Стандартные детали
                             Resurse('Винты'),
                             Resurse('Железная пластина'),
                             Resurse('Усиленная железная пластина'),
                             Resurse('Медный лист'),
                             Resurse('Дюраалюминиевый лист'),
                             Resurse('Алюминиевый корпус'),
                             Resurse('Стальная труба'),
                             Resurse('Стальная балка'),
                             Resurse('Железобетонная балка'),
                             Resurse('Модульный каркас'),
                             Resurse('Тяжелый модульный каркас'),
                             Resurse('Сплавленный модульный каркас'),
                             Resurse('Ткань'),
                             Resurse('Пластик'),
                             Resurse('Резина'),

                             Resurse('Ротор'),  #  Промышленные детали
                             Resurse('Статор'),
                             Resurse('Аккумулятор'),
                             Resurse('Мотор'),
                             Resurse('Радиатор'),
                             Resurse('Система охлаждения'),
                             Resurse('Турбомотор'),

                             Resurse('Проволока'),  #  Электроника
                             Resurse('Кабель'),
                             Resurse('Сверхпроволока'),
                             Resurse('Печатная плата'),
                             Resurse('Ограничитель ИИ'),
                             Resurse('Скоростной разъем'),

                             Resurse('Компьютер'),  #  Коммуникации
                             Resurse('Суперкомпьютер'),
                             Resurse('Квантовый компьютер'),
                             Resurse('Блок управления'),
                             Resurse('Кварцевый резонатор'),
                             Resurse('Суперпозиционный резонатор'),

                             Resurse('Пустая канистра'),  #  Емкости
                             Resurse('Пустой баллон'),
                             Resurse('Куб преобразования давления'),
                             Resurse('Бутыль воды'),
                             Resurse('Бутыль раствора глинозема'),
                             Resurse('Канистра серной кислоты'),
                             Resurse('Канистра азотной кислоты'),
                             Resurse('Баллон Азота'),


                             Resurse('Угольный брикет'),#  Топливо
                             Resurse('Канистра топлива'),
                             Resurse('Канистра турботоплива'),
                             Resurse('Урановый стержень'),
                             Resurse('Плутониевый стержень'),

                             Resurse('Электромагнитный регулирующий стержень'),
                             Resurse('Обетонированная урановая ячейка'),
                             Resurse('Нерасщепляемый уран'),
                             Resurse('Плутониевая таблетка'),
                             Resurse('Обетонированная плутониевая ячейка'),
                             ]
        self.maxlenght = len(max(self.resurse_list, key = lambda x: len(x.resurse_name)).resurse_name)+5


    def __str__(self):
        rezult = 'Запас ресурсов'.ljust(self.maxlenght) + '|  Недостаток ресурсов\n'
        for resurse in self.resurse_list:
            if resurse.num_per_minute !=0:
                rezult += f'{resurse.resurse_name}({resurse.num_per_minute})'.ljust(self.maxlenght) + "|"+ "\n" if resurse.num_per_minute>= 0 else ' '.ljust(self.maxlenght) + f'|   {resurse.resurse_name}({resurse.num_per_minute})\n'
        return rezult

    def add_resurse(self, other, count =1, power =100):

        if other.__class__.__name__ == 'Resurse':
            if other in self.resurse_list:
                index =  self.resurse_list.index(other)
                self.resurse_list[index] =  self.resurse_list[index] + other.num_per_minute * count * power / 100
            else:
                raise IndexError('Такого ресурса нет в списке')


    def sub_resurse(self, other, count =1, power =100):

        if other.__class__.__name__ == 'Resurse':
            if other in self.resurse_list:
                index =  self.resurse_list.index(other)
                self.resurse_list[index] =  self.resurse_list[index] - other.num_per_minute * count * power / 100
            else:
                raise IndexError('Такого ресурса нет в списке')


    def __add__(self, other: (Resurse,Factory)):
            if other.__class__.__name__ == 'Resurse':
                self.add_resurse(other)
            elif other.__class__.__base__.__name__ == 'Factory':
                for resurse in other.recept[0]:
                    self.sub_resurse(resurse, other.count, other.power)

                for resurse in other.recept[1]:
                    self.add_resurse(resurse, other.count, other.power)
            return self


    def __sub__(self, other: (Resurse, Factory)):
            if other.__class__.__name__ == 'Resurse':
                self.sub_resurse(other)
            return self




rr= Resurse('Известняк', 1000)
# #
# bb= Resurse('Sand', 300)
# #
# dd= Resurse('Water', 500)
# #
# cc= Resurse('ferum', 200)

factory = Costruct("Железная пластина",16)

drill60 = Drilling('Железная руда', 180)
# print(super(factory))



resurse_list = Resurse_List()
resurse_list -= rr
resurse_list += factory
resurse_list += drill60

# resurse_list += bb
# resurse_list += bb
# resurse_list += dd
# resurse_list += cc
# resurse_list += factory
print(resurse_list)







