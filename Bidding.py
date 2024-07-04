from replit import clear

print("WELCOME TO THE BIDDING GROUND !!!")

def aution():
    bids = {}
    flag = "yes"
    while flag == "yes":
        name =  input("Please tell your Name::")
        bid = int(input("Please place your bid($)::"))
        bids[name] = bid
        flag = input("Does anyone else want to pplace a bid?:")
        if flag == 'yes':
            clear()
        
    max_key = max(bids, key=bids.get)  
    print(f'{max_key} Won the bid')


aution()


