
'''client1_age = input('Client1 age: ')
cliente1_ticket = input('Client1 ticket: ')
client_discount_10 = False
client_discount_5 = False

client2_age = input('Client2 age: ')
cliente2_ticket = input('Client2 ticket: ')
client2_discount_10 = False
client2_discount_5 = False

client3_age = input('Client3 age: ')
cliente3_ticket = input('Client3 ticket: ')
client3_discount_10 = False
client3_discount_5 = False

client4_age = input('Client4 age: ')
cliente4_ticket = input('Client4 ticket: ')
client4_discount_10 = False
client4_discount_5 = False

client5_age = input('Client5 age: ')
cliente5_ticket = input('Client5 ticket: ')
client5_discount_10 = False
client5_discount_5 = False

client6_age = input('Client6 age: ')
cliente6_ticket = input('Client6 ticket: ')
client6_discount_10 = False
client6_discount_5 = False

client7_age = input('Client7 age: ')
cliente7_ticket = input('Client7 ticket: ')
client7_discount_10 = False
client7_discount_5 = False

client8_age = input('Client8 age: ')
cliente8_ticket = input('Client8 ticket: ')
client8_discount_10 = False
client8_discount_5 = False

client9_age = input('Client9 age: ')
cliente9_ticket = input('Client9 ticket: ')
client9_discount_10 = False
client9_discount_5 = False

client10_age = input('Client10 age: ')
cliente10_ticket = input('Client10 ticket: ')
client10_discount_10 = False
client10_discount_5 = False
'''


class Client:
    def __init__(self, age, sales, ticket):
        self.age = age
        self.sales = sales
        self.ticket = ticket

    def discount_10(self):
        if( 
            self.age >= 30 and self.age <= 45 and 
            self.sales >= 10 and self.ticket >= 50
        ):
            print('TRUE. 10% Discount approved')
        else:
            print('FALSE. 5% discount approved')
        return

client_1 = Client(40, 5, 45)
print(client_1.age)
print(client_1.sales)
print(client_1.ticket)
client_1.discount_10()
print()


client_2 = Client(49, 20, 200)
print(client_2.age)
print(client_2.sales)
print(client_2.ticket)
client_2.discount_10()
print()

client_3 = Client(47, 12, 34)
print(client_3.age)
print(client_3.sales)
print(client_3.ticket)
client_3.discount_10()
print()

client_4 = Client(34, 16, 150)
print(client_4.age)
print(client_4.sales)
print(client_4.ticket)
client_4.discount_10()
print()

client_5 = Client(48, 4, 23)
print(client_5.age)
print(client_5.sales)
print(client_5.ticket)
client_5.discount_10()
print()

client_6 = Client(38, 1, 42.23)
print(client_6.age)
print(client_6.sales)
print(client_6.ticket)
client_6.discount_10()
print()

client_7 = Client(42, 29, 45)
print(client_7.age)
print(client_7.sales)
print(client_7.ticket)
client_7.discount_10()
print()

client_8 = Client(49, 35, 123)
print(client_8.age)
print(client_8.sales)
print(client_8.ticket)
client_8.discount_10()
print()

client_9 = Client(46, 23, 95)
print(client_9.age)
print(client_9.sales)
print(client_9.ticket)
client_9.discount_10()
print()

client_10 = Client(22, 6, 35)
print(client_10.age)
print(client_10.sales)
print(client_10.ticket)
client_10.discount_10()
print()

client_11 = Client(54, 15, 60)
print(client_11.age)
print(client_11.sales)
print(client_11.ticket)
client_11.discount_10()
print()

client_12 = Client(34, 17, 71)
print(client_12.age)
print(client_12.sales)
print(client_12.ticket)
client_12.discount_10()
print()

