def name_Print():
    names=['Jason', 'Samme', 'Cody', 'Lane']
    message=f"Hello, {names[0].title()}! How are you today?\n"
    print(message)
    return None

def own_List():
    brand=['Honda', 'Subaru', 'Hyundai', 'Nissan', 'Ford', 'Chevy']
    transport=['motorcycle', 'car', 'truck', 'boat', 'mower']
    message=f"I would like to own a {brand[1].title()} {transport[1].title()} for my next vehicle.\n"
    print(message)
    return None

def motorcycles():
    cycles=['honda', 'suzuki', 'yamaha']
    cycles[0]='ducatti'
    print(cycles[0])
    return None

motorcycles()

own_List()

name_Print()