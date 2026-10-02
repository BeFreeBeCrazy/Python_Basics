deposit_sum = float(input())
time_of_deposit = int(input())
yearly_interest_rate = float(input())
yearly_interest_rate_percentage = yearly_interest_rate / 100

total_sum = deposit_sum + time_of_deposit * ((deposit_sum * yearly_interest_rate_percentage / 12))


print(total_sum)