groups = int(input())

destination = ""
percentage = 0
all_people = 0

everest = 0
k2 = 0
kilimandjaro = 0
mondblande = 0
musala = 0
printing_everest = 0
printing_k2 = 0
printing_kilimandjaro = 0
printing_mondblande = 0
printing_musala = 0

for _ in range(groups):
    people = int(input())
    all_people += people
    if people >= 41:
        everest += people
    elif people >= 26:
        k2 += people
    elif people >= 13:
        kilimandjaro += people
    elif people >= 6:
        mondblande += people
    else:
        musala += people

printing_everest += (everest / all_people) * 100
printing_k2 += (k2 / all_people) * 100
printing_kilimandjaro += (kilimandjaro / all_people) * 100
printing_mondblande += (mondblande / all_people) * 100
printing_musala += (musala / all_people) * 100

print(f"{printing_musala:.2f}%")
print(f"{printing_mondblande:.2f}%")
print(f"{printing_kilimandjaro:.2f}%")
print(f"{printing_k2:.2f}%")
print(f"{printing_everest:.2f}%")
