"""
Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list 
- parkingSpaces -> list
- currentTicket -> dictionary
"""



class Parking():

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTicket = {'paid': False}
        self.flag = 'staying'
         
        

    def takeTicket(self):
        # print(self.tickets, self.parkingSpaces)  # for checking purposes
        self.tickets.pop()          # decreases number of tickets
        self.parkingSpaces.pop()    # decreases number of spaces
        # print(self.tickets, self.parkingSpaces) # for checking purposes

    def payForParking(self):
        # print(self.currentTicket)           #for checking purposes
        if self.flag == 'staying':
            pay_parking = input("Enter an amount to pay for your parking:\n")
            if pay_parking != '':
                print('Your ticket has been paid and you have 15mins to leave.')
                self.currentTicket['paid'] = True
                # print(self.currentTicket)   #for checking purposes
            else:
                print('Invalid entry, try again')

        if self.flag == 'leaving':
            # print(self.tickets, self.parkingSpaces) # for checking purposes
            while True:
                pay_parking = input("Enter an amount to pay for your parking:\n")
                if pay_parking != '':
                    print("Thank You, have a nice day!")
                    self.tickets.append(len(self.tickets)+ 1)
                    self.parkingSpaces.append(len(self.parkingSpaces)+1)
                    # print(self.tickets, self.parkingSpaces) # for checking purposes
                    break
                else:
                    print('Invalid Entry, try again.')


    def leaveGarage(self):
        # print(self.tickets, self.parkingSpaces)         # for checking purposes
        while True: 
            if self.currentTicket['paid'] == True:
                print("Thank You, have a nice day!")
                self.tickets.append(len(self.tickets)+ 1)
                self.parkingSpaces.append(len(self.parkingSpaces)+1)
                # print(self.tickets, self.parkingSpaces) # for checking purposes
                break
            else:
                self.flag = 'leaving'
                self.payForParking()
                break
    

my_parking = Parking()
def welcome():
    while True:
        user_input = input('Hello welcome to the parking garage. Please type "enter" to recieve a ticket:\n')
        if user_input.lower() == 'enter':
            my_parking.takeTicket()
            new_input = input('Would you like to pay now? Enter Y/N:\n')
            if new_input.upper() == 'Y':
                my_parking.payForParking()
                break
            if new_input.upper() == 'N':
                print('You have 15 minutes to leave. You can pay before you exit.')
                break
            else:
                print('Invalid Entry')
                break
        else:
            print('Invalid entry')
            continue
        
    
def goodbye():
    while True:
        scan_input = input('Please enter "s" to scan your ticket:\n')
        if scan_input.lower() == 's':
            my_parking.leaveGarage()
            break
        else:
            print('Invalid entry, please try again')

welcome()

while True:
    exit_input = input('when you are ready to leave enter "exit":\n')
    if exit_input.lower() == 'exit':
        goodbye()
        break
    else:
        print('Invalid entry')
    
