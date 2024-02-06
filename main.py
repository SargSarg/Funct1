# объявили функцию для подсчета количества символов в тексте
def char_frequency(): #в эти скобки можно сунуть переменную text и тогда можно не менять текст в самой функции
   text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   """

   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчета символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")

...

# вызвали функцию в любом месте программы
char_frequency()

#2функция
def print_2_add_2(): #обязательно придумываем название функции
   result = 2 + 2  #тело функции
   print(result)

print_2_add_2()#вызываем именно функцию а не переменные внутри неё. Тут переменная не работает за пределами функции

#3 функция
def hello_world():
   print("Hello World")

hello_world()

#4функция
# функция, которая возводит любое число в степень n
def pow_func(base, n=2): #здесь указана степень по умолчанию и кст названия base и n мы сами придумали
   print(base ** n)

pow_func(3)  # 9 так как здесь выпала степень по умолчанию
pow_func(5, 3)  # 125 тк мы сами выбрали степень

#5функция является ли чисто n делителем числа a
def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5

#6функция
def reverse_stair(c): #нужно получисть звезды в строку по убыванию
   for i in range(c, 0, -1):
       print("*" * i)

reverse_stair(5)

#7функция тут функция выдаст ответы 9 и none
def pow_func(base, n=2):
   print(base ** n)

print(pow_func(3))

#но спомощью return можно убрать этот нон сделав так чтоб оставался только один ответ
def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result

print(pow_func(3))

#а теперь присвоим результат этой функции какой-нибудь переменной
outside_result = pow_func(3)
print(outside_result)

#8функция найти кол-во делителей у числа
def get_multipliers(b):
   count = 0
   for n in range(1, b + 1):
       if b % n == 0:
           count += 1

   return count

l = get_multipliers(5)  # 2 #если в этом случае не ввести новые переменные то ответ не выдаст
k = get_multipliers(4)  # 3
print(l)
print(k)

def check_palindrome(str_): #является ли текст зеркальным
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

v = check_palindrome("test")  # False   тут тоже пришлось ввести переменные
m = check_palindrome("Кит на море не романтик")  # True

print(v)
print(m)