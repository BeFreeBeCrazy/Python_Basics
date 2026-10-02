plastic_envelope = 1.50
paint = 14.50
paint_thinner = 5
more_paint_thinner = paint_thinner + 2
envelope = 0.40


quantity_plastic_envelope = int(input())
quantity_paint = int(input())
quantity_paint_thinner = int(input())
hours_needed = int(input())
more_paint = quantity_paint * 0.10

plastic_envelope_price = (quantity_plastic_envelope + 2) * plastic_envelope
paint_price = (quantity_paint + more_paint) * paint 
paint_thinner_price = paint_thinner * quantity_paint_thinner
one_hour_work = (plastic_envelope_price + paint_price + paint_thinner_price + envelope)
total_hours_needed = hours_needed * (one_hour_work * 0.30)

final_price = plastic_envelope_price + paint_price + paint_thinner_price + total_hours_needed + envelope

print(f'{final_price:.2f}')