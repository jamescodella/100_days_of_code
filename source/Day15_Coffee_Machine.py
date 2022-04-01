# Day 15: coffee machine

import os

# Define global variables
machine_resources = {
    'water' : 500,
    'milk' : 250,
    'coffee' : 60,
    'money' : 0
    }

coins = {
    'quarter' : 0.25,
    'dime' : 0.1,
    'nickel': 0.05,
    'penny': 0.01
}

coffee_drinks = {
    'espresso' : {
        'water' : 50,
        'milk' : 0,
        'coffee' : 18,
        'money' : 1.50
    },
    'latte' : {
        'water' : 200,
        'milk' : 150,
        'coffee' : 24,
        'money' : 2.50
    },
    'cappuccino' : {
        'water' : 250,
        'milk' : 100,
        'coffee' : 24,
        'money' : 3.00
    }
}

def welcome():
    '''
    Prints a welcome message in ASCII art.
    '''
    print('''

            
        ██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗███████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
        ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██╔════╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
        ██████╔╝ ╚████╔╝ ██║     ███████║█████╗  █████╗      ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
        ██╔═══╝   ╚██╔╝  ██║     ██╔══██║██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
        ██║        ██║   ╚██████╗██║  ██║██║     ███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
        ╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                                    )
        
        ''')


def check_resources(order, machine_resources):
    '''
    Checks to ensure coffee machine has enough water, milk, and coffee for the order.
    '''

    for k, v in list(machine_resources.items())[:-1]:  # not checking money
        
        if machine_resources[k] < coffee_drinks[order][k]:
            print(f'Sorry, there is not enough {k}.')
            return False
     
    return True

def check_transaction(payment, amount_due):
    '''
    Checks payment with amount due to determine if the payment is sufficient and if change is needed.
    '''

    global machine_resources

    total_payment = 0
    for k, v in payment.items():
        total_payment += payment[k] * coins[k]
    
    if total_payment < amount_due:
        print(' Sorry, that''s not enough money. Money refunded.')
        return False
    
    elif total_payment == amount_due:
        print('Thank you for exact change.')
        machine_resources['money'] += total_payment
    
    elif total_payment > amount_due:
        print(f'Here is ${( total_payment - amount_due):.2f} in change.')
    
    return True


def make_coffee(order):
    '''
    Makes coffee, uses resources, and serves the coffee to the customer.
    '''

    for k,v, in coffee_drinks[order].items():
        machine_resources[k] -= v
    
    print(f'Here is your {order}. ☕️ Enjoy!')

def print_report():
    print('\nPyCafe Machine Resource Report')
    for k,v in machine_resources.items():
        print('|- ' + k + ' : ' + str(v))
    
    print('\n')

def coffee_machine():
    '''
    Main function for coffee machine application
    '''
    
    os.system('cls' if 'Win' in os.name else 'clear')
    welcome()

    order = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if order == 'off':
        quit()
    elif order == 'report':
        print_report()
    elif order in ['espresso', 'latte', 'cappuccino']:
        sufficient = check_resources(order, machine_resources=machine_resources)
        if sufficient:
            price = coffee_drinks[order]['money']
            print(f'The price is: ${price:.2f}')
            payment = {}
            payment['quarter'] = int(input('Please enter the amount of quarters: '))
            payment['nickel'] = int(input('Please enter the amount of nickels: '))
            payment['dime'] = int(input('Please enter the amount of dimes: '))
            payment['penny'] = int(input('Please enter the amount of pennies: '))

            successful_transaction = check_transaction(payment, price)

            if successful_transaction:
                make_coffee(order)

    else:
        print('Invalid option.')

    another = input('Would you like to place another order? Type y or n: ').lower()

    if another == 'n' or another == 'no':
        quit()
    else:
        coffee_machine()

if __name__ == '__main__':
    coffee_machine()