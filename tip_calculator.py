ask_question = True
while ask_question:
    total_bill = input('Total bill amount? ')
    try:
        total_float = float(total_bill)
        ask_question = False
        
    except ValueError:
        print("try again bucko")

ask_question = True
while ask_question:
    service_level = input('Level of service? ')
    service_lower = service_level.lower()
    if service_lower == 'good':
        tip = total_float * .2
        ask_question = False
    elif service_lower == 'fair':
        tip = total_float * .15
        ask_question = False
    elif service_lower == 'bad':
        tip = total_float * .1
        ask_question = False
    else:
        print('thats not an option: please enter good, fair, or bad')

ask_question = True
while ask_question:
    num_of_ppl = input('Split how many ways? ')
    try:
        num_int = int(num_of_ppl)
        ask_question = False

    except ValueError:
        print('please enter whole number') 

final_bill = total_float + tip
amount_per = final_bill / num_int

print('Tip amount: $%.2f \nTotal amount: $%.2f \nAmount per person: $%.2f' % (tip, final_bill, amount_per))
        
