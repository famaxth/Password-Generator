# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @por0vos1k


from etc.functions import create_password

print(""" 

                     +syyyys+
                  +hhs+////+shho
                 hh//yhyyyyhy//yh
                ds/od+      +do/sd
               +N//N          N//mo                 ╔================================╗
               om/+N          mo/ds                 ║                                ║
               om/+N          mo/ds                 ║                                ║
             hhhhhhdyyyyyyyyyyhhhhhhh               ║       PASSWORD GENERATOR       ║
            yh                      hy              ║                                ║
            yh                      hy              ║   https://github.com/famaxth   ║
            yh        mo//oN        hy              ║                                ║
            yh        +M++N+        hy              ║                                ║
            yh        oNooNo        hy              ╚================================╝
            yh        +oooo+        hy
            yh                      hy                            v1.0
            +dyssssssssssssssssssssyd+


""")

data = []

language = int(input("Choose the language.\n\n1 - English\n2 - Russian\n\nEnter the number...\n\n\n"))


if language == 1:

    print("The language has changed successfully!")

    length_eng = int(input("""Enter the password length:\n\n\n"""))

    if length_eng >= 1 and length_eng <= 100:

        special_symbol_eng = str(input("""Do you want to use special characters?\n\nExample: %, *, ),?, @, #, $, ~\n\n\n"""))

        big_symbol_eng = str(input("Do you want to use large letters A-Z?\n\n\n"))

        numbers_eng = str(input("Do we use numbers 0-9?\n\n\n"))

        small_symbol_eng = str(input("Do you want to use lowercase letters a-z?\n\n\n"))

        try:
            text = create_password(length_eng, special_symbol_eng, big_symbol_eng, numbers_eng, small_symbol_eng)
            print("Your new password: {}\n\n\n".format(text))
        except:
            print("Your new password: \n\n\n")

    else:
        print("Error! Valid numbers from 1 to 100\n\n\n")


elif language == 2:

    print("Язык успешно изменен!")

    length_ru = int(input("""Введите длину пароля:\n\n\n"""))

    if length_ru >= 1 and length_ru <= 100:

        special_symbol_ru = str(input("""Хотите использовать спец. символы?\n\nПример: %, *, ),?, @, #, $, ~\n\n\n"""))

        big_symbol_ru = str(input("Вы хотите использовать заглавные буквы A-Z?\n\n\n"))

        numbers_ru = str(input("Будем использовать цифры 0-9?\n\n\n"))

        small_symbol_ru = str(input("Вы хотите использовать строчные буквы a-z?\n\n\n"))

        try:
            text = create_password(length_ru, special_symbol_ru, big_symbol_ru, numbers_ru, small_symbol_ru)
            print("Ваш новый пароль: {}\n\n\n".format(text))
        except:
            print("Ваш новый пароль: \n\n\n")

    else:
        print("Ошибка! Допустимые числа от 1 до 100\n\n\n")

else:

    print("Error! Enter the number under which the selected language is located.\n\n\n")
    language = int(input())


