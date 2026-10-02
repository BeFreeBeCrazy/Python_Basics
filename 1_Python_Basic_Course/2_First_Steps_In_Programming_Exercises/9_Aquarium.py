length = int(input())
width = int(input())
heigth = int(input())
percent = float(input())

volume = length * width * heigth
litres_volume = volume / 1000
space_taken = percent / 100
needed_litres = litres_volume * (1 - space_taken)

print(needed_litres)