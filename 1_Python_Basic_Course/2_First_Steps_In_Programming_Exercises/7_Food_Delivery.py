chicken_menu = 10.35
fish_menu = 12.40
vegeterian_menu = 8.15
delivery_fee = 2.50

quantity_chicken_menu = int(input())
quantity_fish_menu = int(input())
quantity_vegeterian_menu = int(input())

chicken_menu_price = chicken_menu * quantity_chicken_menu
fish_menu_price = fish_menu * quantity_fish_menu
vegeterian_menu_price = vegeterian_menu * quantity_vegeterian_menu

desert_price = (chicken_menu_price + fish_menu_price + vegeterian_menu_price) * 0.20

final_price = chicken_menu_price + fish_menu_price + vegeterian_menu_price + desert_price + delivery_fee

print(f'{final_price:.2f}')