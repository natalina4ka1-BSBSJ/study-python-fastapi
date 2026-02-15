# Comparison Operators in Python

# Ex/ Bsp/ Пр. 

# 1) Equality

clean_p1 = 10
dirty_p2 = 10

# If the number of clean plates is equal to the total number of plates

# Wenn die Anzahl der sauberen Teller gleich der Gesamtzahl der Teller ist

# якщо кількість чистих тарілок дорівнює сумарній кількості тарілок 

num_3 = clean_p1 == dirty_p2
print(num_3)

#----------------

# 2) Inequality

clean_p1 = 10
dirty_p2 = 5

# If the number of washed plates is 5 out of 10, 
# then the dishes are not fully washed.

# Wenn die Anzahl der gewaschenen Teller 5 von 10 ist,
# dann ist das Geschirr nicht fertig abgespült.

# Якщо кількість помитих тарілок 5 з 10, то це, не дорівнює, перемитий посуд.

num_3 = dirty_p2 != clean_p1
print(num_3)

#-----------------

# 3) Less than

clean_p1 = 5
dirty_p2 = 10

# If the number of plates is significantly less than the total number of plates.

# Wenn die Anzahl der Teller deutlich geringer ist als die Gesamtzahl der Teller.

# якщо кількість чистих тарілок значно менше, ніж кількість гязних тарілок.

num_3 = clean_p1 < dirty_p2
print(num_3)

#-----------------

# 4) Greater than

clean_p1 = 10
dirty_p2 = 5

# If the number of plates is significantly greater than the total number of plates.

# Wenn die Anzahl der Teller größer ist als die Gesamtzahl der Teller.

# якщо кількість чистих тарілок більше ніж кількість грязних тарілок

num_3 = clean_p1 > dirty_p2
print(num_3)