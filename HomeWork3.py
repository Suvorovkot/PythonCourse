from random import uniform


# Первое задание - температуры

def task1():
    temperatures = list()
    for i in range(10):
        temperatures.append(uniform(10, 25))
    print("Celsius start values:", temperatures)
    ftemperatures = list(map(lambda x: 9 / 5 * x + 32, temperatures))
    print("Fahrenheit:", ftemperatures)
    ctemperatures = list(map(lambda x: 5 / 9 * (x - 32) + 273.15, ftemperatures))
    print("Calvin:", ctemperatures)
    temperatures1 = list(map(lambda x: x - 273.15, ctemperatures))
    print("Celsius finish values:", temperatures1)
    print("Differeces:", list(map(lambda x, y: abs(x - y), temperatures1, temperatures)))

# Второе задание - новый словарь с элементами исходного

def dict_filter(d):
    return dict(filter(lambda x: type(x[0]) == type(""), d.items()))
def task2():
    d = {'x':2, 4:'y', 4.0:'12', '3':'fdfs', 'a':9., b'pp':52}
    print(dict_filter(d))
