# Logical Operator
# Ex. / Bsp. / Пр.

# 1) and

# The action will occur if both values are True.
# Die Aktion wird ausgeführt, wenn beide Werte wahr sind.
# Дія відбудеться, якщо обидва значення вірні.

Login = True
Password = True
Come_in = (Login and Password)
print(Come_in)

# 2) Or

# The action will work if at least one value is True.
# Die Aktion wird aus geführt, wenn mindestens ein Wert wahr ist
# дія спрацює, якщо хоча б одне значення вірне.

Login = False
Password = True
Email = True
Come_in = (Login or Password or Email)
print(Come_in)

# 3) Not

# The action will work as a value change
# Die Aktion wird als Wertänderung funktionieren
# дія спрацює як зміна значення

Login = True
Password = False
Email = not False
Come_in = Login or Password or Email 
print(Come_in)

