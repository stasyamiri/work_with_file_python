file_1 = open('/Users/Анастасия/.PyCharmCE2019.3/Hillel/data.txt', 'r')
for line in file_1:
    print(line)



file_1.seek(0)                                                                 # курсор на начало файла


file_2 = open('/Users/Анастасия/.PyCharmCE2019.3/Hillel/data_2.txt', 'w')
file_2.write(file_1.read())                                                    # сразу записываем во второй файл то, что читаем с первого
# file_1.close()
# file_2.close()


file_2 = open('/Users/Анастасия/.PyCharmCE2019.3/Hillel/data_2.txt', 'w')
file_2.writelines("I love Data Science!!!!!!\n")
file_2.close()
