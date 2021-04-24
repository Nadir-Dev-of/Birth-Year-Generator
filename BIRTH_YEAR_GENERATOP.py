print("\033[4;49;91m Welcom To Birth_Year Generator")

import datetime

age = int(input(" \033[30;1;47m How Old Are You ? : "))

current_year = datetime.datetime.now ().year

birth_year = current_year - age

print(f" \033[7;49;94m Your Birth Year  Is : {birth_year} ")
