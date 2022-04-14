# Վարժություն 5
# Էկրանի վրա տպեք մի շարք բնական թվեր՝ նվազագույնից առավելագույնը քայլով:
# Օրինակ, եթե նվազագույնը 10 է, առավելագույնը՝ 35, քայլը՝ 5, ապա ելքը պետք է լինի՝ 10 15 20 25 30 35։
# Նվազագույնը, առավելագույնը և քայլը սահմանվում են օգտագործողի կողմից (ստանալ ստեղնաշարից)։

min_num = int(input("input minimum number: "))
max_num = int(input("input maximum number: "))
step_num = int(input("input step number: "))
for i in range(min_num, max_num + 1, step_num):
    print(i)
