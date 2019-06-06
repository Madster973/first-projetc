#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(distance_in_kms>0 and distance_in_kms<=3):
        amount=0
    elif(distance_in_kms>3 and distance_in_kms<=6):
        amount=(distance_in_kms-3)*3
    elif(distance_in_kms>6):
        amount=(distance_in_kms-6)*6+9
    else:
        print(-1)
        
    #write your logic here
    if(food_type=="V" and quantity_ordered>0):
        famount=quantity_ordered*120
        bill_amount=famount+amount
    elif(food_type=="N" and quantity_ordered>0):
        famount=quantity_ordered*150
        bill_amount=famount+amount
    else:
        print(-1)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,3)
print(bill_amount)
