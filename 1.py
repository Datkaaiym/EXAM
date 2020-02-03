# Вам предоставляется файл air.txt, в котором записана новость с сайта 24.kg 
# о загрязнении воздуха в Бишкеке. 
# Вам необходимо прочесть этот файл и посчитать, 
# ___сколько раз повторяется___ тот или иной символ и ____записать все в отдельный словарь_____. 
# Учтите, что в файле есть символы, от которых необходимо _______избавиться: ‘\n’ 
# (символы переноса строки), ‘ ’ (пробелы), ‘.’ (точки) и ‘,’ (запятые)._________ 
# Определите ______самый повторяющийся________ символ в файле air.txt . 
# Поочередно выведите на экран ваш словарь и самый повторяющийся символ.

text = '''According to the data of the KyrgyzHydromet Pollution Observations Department, 
stationary posts have registered excess of the maximum permissible norms for nitrogen 
dioxide in 2.0 times, nitrogen oxide in 1.5 times, formaldehyde in 2.0 times.

The content of sulphur dioxide and ammonia did not exceed the maximum allowable 
norms for Nitrogen dioxide.

Automatic station recorded on Jan.22 the excess of average daily maximum 
permissible norms for carbon oxide in 9.5 times, for nitrogen oxide in 1.2 times, 
for nitrogen dioxide in 1.2 times, for sulfur dioxide in 1.0 times and for RM2.5 in 1.8 times. '''

text1 = ''.join([*filter(str.isalnum, text)])

dict_ = {}
for s in text1:
    if s not in dict_.keys():
        dict_[s] = 1
    else:
        dict_[s] += 1

print (dict_)   # выводится словарь, ключ - символ, значение - количество повторов

final_dict = dict([max(dict_.items(), key = lambda k_v: k_v[1])])
print(final_dict)  # выводится самый повторяемый символ

