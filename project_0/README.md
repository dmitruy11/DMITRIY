### Оглавление
[1.Описание проекта]()

[2.Какой кейс решаем]()

[3.Краткая информация о данных]()

[4.Этапы работы над проектом]() 

[5. Результат]()

[6. Выводы]()

 ### Описание проекта
    Финальное задание к модулю PYTHON-8.
 Реализация проекта по созданию программы, которая угадывает загаданное компьютером число за минимальное количество попыток.

 ###  Какой кейс решаем?
    Нужно написать функцию, которая будет справляться с угадыванием меньше чем за 20 попыток.

 ###     Условия соревнования:

 Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под "угадать", подразумевается "написать программу, которая уадывает число".
 Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.


 
 ### Краткая информация о данных
 ### В алгоритме поиска:

 В качестве входного параметра используется целочисленная переменная number (искомое случайное число).
 Возвращается целочисленная переменная count (число попыток).
 ### В алгоритме проверки качества:

 В качестве входного параметра используется имя функции алгоритма поиска algoritm_name.
 В ходе выполнения алгоритма проверки качества формируется массив random_array из 1000 случайных целых чисел в интервале (1,100).
 Возвращается значение score (среднее значение количества попыток, затраченных алгоритмом поиска до нахождения случайного числа).
 Этапы работы над проектом
 В качестве алгоритма поиска выбран метод деления заданного интервала поиска пополам и отбрасывания части, не содержащей искомое число.
 Проведена проверка качества работы алгоритма на выборке из 1000 случайных чисел. Среднее количество попыток - 5.
 ## Результат
 По результатам проверки качества работы алгоритма среднее количество попыток - 5, что соответствует поставленной зада
