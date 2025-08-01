

try:
    file = open('movies.txt','r')
    print(file.read())
except:
    print('error')


with open('friends.csv','r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')