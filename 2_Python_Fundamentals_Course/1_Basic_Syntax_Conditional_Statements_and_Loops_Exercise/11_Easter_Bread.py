budget = float(input())
flour = float(input())

eggs = flour * 0.75
litre_milk = flour * 1.25

one_loaf = flour + eggs + litre_milk * 0.25

loaves_count = 0
colored_eggs = 0

while budget > 0:
    budget -= one_loaf
    if budget < 0:
        break
    loaves_count += 1
    colored_eggs += 3
    if loaves_count % 3 == 0:
        colored_eggs = colored_eggs - (loaves_count - 2)

if budget < 0:
    budget += one_loaf

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")