def name_Print():
    #we select an item from the list in this case index 0 = Jason and we add it to the message
    names=['jason', 'samme', 'cody', 'lane']
    #.title is just a way to format a element of a string to be capital. 
    message=f"Hello, {names[0].title()}! How are you today?\n"
    print(message)
    return None

def own_List():
    #here we combine multiple elements from different lists to forma  sentance. Still using our title formatting
    brand=['Honda', 'Subaru', 'Hyundai', 'Nissan', 'Ford', 'Chevy']
    transport=['motorcycle', 'car', 'truck', 'boat', 'mower']
    message=f"I would like to own a {brand[1].title()} {transport[1].title()} for my next vehicle.\n"
    print(message)
    return None
#adding to a list
def motorcycles():
    cycles=['honda', 'suzuki', 'yamaha']
    #here, we change index 0 to equal the ducatti instead
    cycles[0]='ducatti'
    print(cycles[0].title())
    return None

#here, I'm appending a list rather than replacing a index by using the append function
def cycles_revisited():
    cyclez=['honda', 'suzuki', 'yamaha']
    cyclez.append('ducati')
    print(cyclez)
    return None

#for this, rather than just adding a element to our list at the end using apend, we're going to designate a place for it somewhere in between using insert.\
#this operation shifts every other value in the list one position to the right.
def Legumes():
    beans=['kidney', 'pinto', 'black', 'navy']
    beans.insert(2, 'black-eyed')
    print(beans)
    return None

#wait, why is pasta in here? That clearly is not a fruit. Here we use 'del' to delete it and the index that it's located at. It will print without the pasta in the list.
def fruits():
    type_fruits=['Apple', 'Grape', 'Orange', 'Pasta', 'Cranberry']
    #how we delete elements from a list
    del type_fruits[3]
    print(type_fruits)
    return None

#Here we will use the pop function which similarly does what delete does. However, instead of removing it and being done with it, it removes the last item in a list and lets us work with that item.
def pop_Practice():
    soda=['Pepsi', 'Fanta', 'Coke', 'Sprite']
    popped_soda= soda.pop()
    print(soda)
    #this will print 'sprite' from our list that was removed before
    print(popped_soda)
    return None

def pop_Round2():
    soda=['Pepsi', 'Fanta', 'Coke', 'Sprite']
    popped_soda= soda.pop(0)
    print(soda)
    #selected which item we popped from before
    print(popped_soda)
    return None


#this is where we print out those functions. I like to use functions because it helps me keep things organized.
motorcycles()

fruits()

Legumes()

own_List()

name_Print()

cycles_revisited()

pop_Practice()

pop_Round2()