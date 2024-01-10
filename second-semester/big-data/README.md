# BigData
<details>
  <summary><b>1. Многопоточность и memory-mapped file (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/01.%20memory_mapped_files/01.%20memory_mapped_files.ipynb">01. memory_mapped_file.ipynb</a>)</b></summary>

Написать две программы:

- Первая создает бинарный файл (min 2Гб), состоящий из случайных 32-разрядных беззнаковых целых чисел (big endian).
- Вторая считает сумму этих чисел (с применением длинной арифметики), находит минимальное и максимальное число.

Реализуйте две версии:

1. Простое последовательное чтение 
2. Многопоточная + memory-mapped files. Сравните время работы.
</details>


<details>
  <summary><b>2. Multiprocessing, Ray, Dask, PySpark (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/02.%20multiprocessing">02. multiprocessing</a>)</b></summary>

1. Нужно сгенерировать файл, содержащий 5000 32-битных случайных целых чисел, каждое число на отдельной строке. 

2. Посчитать, какое суммарное количество простых множителей присутствует при факторизации всех чисел.  Например, пусть всего два числа: 6 и 8. 
6 = 2 * 3, 8 = 2 * 2 * 2. Ответ 5.  

3. Реализовать подсчет 
    - простым последовательным алгоритмом
    - многопоточно (на CPython - multiprocessing), с использованием примитивов синхронизации 
    - с помощью Ray/Dask/PySpark
    - (*) с использованием Go (go-рутин) (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/02.%20multiprocessing.ipynb/gorutine.go">gorutine.go</a>)

4. Измерить время выполнения для каждого случая.
</details>
  
<details>
  <summary><b>3. Hadoop, mrjob (<a href="https://github.com/DmitryMogilnikov/BigData/tree/main/notebooks/03.%20mrjob">03. mrjob</a>)</b></summary>

Результаты измерений с выводами (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/03.%20mrjob/time_results.txt">time_results.txt</a>)
</details>
  
<details>
  <summary><b>4. PySpark_wiki (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/04.pyspark_wiki/04.%20pyspark_wiki.ipynb">04. pyspark_wiki.ipynb</a>)</b></summary>
  
1. Напишите программу, которая находит самое длинное слово.
2. Напишите программу, которая находит среднюю длину слов. 
3. Напишите программу, которая находит самое частоупотребляемое слово, состоящее из латинских букв.
4. Все слова, которые более чем в половине случаев начинаются с большой буквы и встречаются больше 10 раз.
5. Напишите программу, которая с помощью статистики определяет устойчивые сокращения вида `пр.`, `др.`, ...
6. Напишите программу, которая с помощью статистики определяет устойчивые сокращения вида  `т.п.`, `н.э.`, ...
7. Напишите программу, которая с помощью статистики находит имена, употребляющиеся в статьях. 
</details>



<details>
  <summary><b>5. PySpark temperature (<a href="https://github.com/DmitryMogilnikov/BigData/blob/main/notebooks/05.%20pyspark_temperature/05.%20pyspark_temperature.ipynb">05. pyspark_temperature.ipynb</a>)</b></summary>
  
1. Напишите программу, которая находит самое длинное слово.
2. Напишите программу, которая находит среднюю длину слов. 
3. Напишите программу, которая находит самое частоупотребляемое слово, состоящее из латинских букв.
4. Все слова, которые более чем в половине случаев начинаются с большой буквы и встречаются больше 10 раз.
5. Напишите программу, которая с помощью статистики определяет устойчивые сокращения вида `пр.`, `др.`, ...
6. Напишите программу, которая с помощью статистики определяет устойчивые сокращения вида  `т.п.`, `н.э.`, ...
7. Напишите программу, которая с помощью статистики находит имена, употребляющиеся в статьях. 
</details>
