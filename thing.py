import requests
import re
#steps 1-4
print("hello")
name = "andrew"
print("my name is", name)
nCats = 0

# step 5
if nCats == 1:
    print("i have {} cat".format(nCats))
else:
    print("i have {} cats".format(nCats))
# 6 - 9
if nCats < 1:
    print("im getting a cat")
    nCats = 1
else:
    if nCats == 1:
        nCats = 2
        print("now my cat has a friend")
    else:
        if nCats == 2:
            print("i have a duo of cats")
        else:
            if nCats > 2:
                print("i have an army of cats")

# 10  an d 11
print("i have {} cats but i want more".format(nCats))
nCats *=9
print("now i have {} cats".format(nCats))

# 12
if nCats %2 == 0:
    print("even cats")
else:
    print("odd cats")
# this list i used for the cat pictures obtained from the cat api
catList = []
# 13 - 17
for i in range(1,nCats+1):
    if i % 2 == 0 and i %3 == 0:
        print(i)
    else:
        if i %2 == 0:
            print("{} meow".format(i))
        else:
            if i %3 == 0:
                print("{} cat".format(i))
            else:
                print(i)
    #this part web scrapes the cat api, an api that provides random pictures of cats
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    #the request returns something that looks like this:
    # [{'breeds': [], 'id': 'tMtdYyf0N', 'url': 'https://cdn2.thecatapi.com/images/tMtdYyf0N.jpg', 'width': 1265, 'height': 951}]
    #so removing all of this and just getting the link to the cat is better
    # i did this by converting the response to string and using regex:
    catLink = re.sub(r'.*\'url\': \'', '', str(response.json()))
    catLink = re.sub(r'\'\,.*', '', catLink)
    print("this is cat #{}".format(i), catLink)
    catList.append(catLink)

print('list of all my cats:')
print(catList)
