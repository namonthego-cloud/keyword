#snack vending machine

#part 1: a function that works out change and sends it back with return
def calculate_change (paid, price):
    change = paid -price
    return change

#part 2: set the snack price and greet the customer
snack_price = 25
print("=======SNACK VENDING MACHINE======")
print(f"this snack costs {snack_price}unit.")
print("accpeted coins 1,5,10, 25\n")

total_inseted = 0
coins_inseted = 0

# part 3: keep accepting coins until enougg money is inserted
while True:
    coin = int(input ("insert a coin (1, 5, 10 or 25):"))

    #PART4:REJECT ANY COIN THAT ISN'T A VAILD VALUE
    if coin != 1 and coin  != 5 and coin!= 10 and coin != 25:
        print("invaild coin, try again!\n")
        continue

    #part 5: add the vaild coin to the running total
    total_inseted += coin
    coins_inseted += 1
    print (f"Inserted {coin}. Total so far: {total_inseted}\n")

    #part 6: stop asking coins once enough has ben inserted
    if total_inseted >= snack_price:
        print("enough money inseted!\n")
        break

#part 7: work out the change using the value returned by caluclate_change
change_due = calculate_change(total_inseted, snack_price)

print("dispensing your snack...")

# part8: nothing extra when the change is zero
if change_due == 0:
    pass
else:
    print(f"here is your change: {change_due}unit.")

#part9:print a short summary of the purchase
print("\n=====PURCHASE SUMMARY====")
print("snack price:",snack_price)
print("coins inserted:",coins_inseted)
print("total paid:",total_inseted)
print("change given:",change_due)
print("=============================")
print("thanks for the purchase!")
#end the program    


