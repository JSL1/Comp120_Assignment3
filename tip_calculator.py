bill = input('Enter the bill total(numbers only)')

tip = 0

service = input('How was the service? enter "great", "fine" or "poor"')

if (service == 'great' or service == 'Great'):
    tip = bill * 0.15
elif (service == 'fine' or service == 'Fine'):
    tip = bill * 0.1
elif (service == 'poor' or service == 'Poor'):
    tip = 0
else:
    tip = 1
