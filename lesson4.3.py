num_1 = 7
num_2 = 2

num_3 = num_1 / num_2
num_4 = num_1 // num_2
num_5 = num_1 % num_2

print(num_3, num_4, num_5)
 
# Exampele 
# Beispiel 

pack_weight = 1000

# Gram in a pack
# Gram pro Portion
 
portion = 18

# How many full cups of coffee will we get?
# Wie viele volle Tassen Kaffee bekomen wir?

total_cups = pack_weight // portion

# How many gram will remain in the pack?
# Wie viele Gramm bleiben in der Packung übrig?

Leftover_gram = pack_weight % portion

# Exact number of portions (for analyticks)
# Genaue Anzahl der Portionen (für die Analytik)

theoretical_yield = pack_weight / portion

print(total_cups, Leftover_gram, theoretical_yield)



