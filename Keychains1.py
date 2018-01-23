
def add_keychains():
    kChains = 0
    print('You Have',kChains,'keychains',end='')
    kChains = int(input('How Many To add?'))
    print('You now have',kChains,'Keychains.')
    return kChains

def remove_heychains(chains):
    print('You have',chains,end='')
    rem = int(input('How many to remove?'))
    print('you now have',chains-rem,'Keychains.')
    return chains-rem

def view_oreder(chain):
    print('You have',chain,'Keychains.')
    print('Keychains cost $10 each.')
    print('Total Cost',chain*10)

def checkout():
    print('CHEECKOUT')

def menu():
    print('1.Add keychains to order ')
    print('2.Remove keychains fromorder')
    print('3.View Current Order')
    print('4.Checkout')

holder = 0
order = 0
while True:
    menu()
    print()
    user = int(input('Please Enter Your Choice:'))
    if user == 1:
        holder = add_keychains()
        print()
    elif user == 2:
        order = remove_heychains(holder)
        print()
    elif user == 3:
        view_oreder(order)
        print()
    else:
        checkout()
        break















