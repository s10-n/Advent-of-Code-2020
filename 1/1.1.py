number_of_expenses = len(expenses)
for i in range(number_of_expenses):
    for j in range(i+1,number_of_expenses):
        if (expenses[i] + expenses[j]) == 2020:
            print(expenses[i] * expenses[j])
