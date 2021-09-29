token = input('Enter api: ')

f = open('result.txt', 'w')
f.write('')
f.close()

print("""
/$$    /$$ /$$   /$$        /$$$$$$  /$$                 /$$
| $$   | $$| $$  /$$/       /$$__  $$|__/                | $$
| $$   | $$| $$ /$$/       | $$  \__/ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$
|  $$ / $$/| $$$$$/ /$$$$$$| $$$$    | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
 \  $$ $$/ | $$  $$|______/| $$_/    | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
  \  $$$/  | $$\  $$       | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$
   \  $/   | $$ \  $$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$
    \_/    |__/  \__/      |__/      |__/|__/  |__/ \_______/ \_______/|__/

by kinobi""")

class vkid:
    val = 0
    count = 1
    def __init__(self, value, ncount):
        self.val = value
        self.count = ncount
    def changecount(self, ncount):
        self.count = ncount

from vklancer import api
from vklancer import utils

offset = 0
count = 0
array = []


vk = api.API(token=token, version='5.49')

array = []
ids = []

print("Enter group id, %%% if end, /file if from file, ~you can find group id at regvk.com/id/~")

while True:
        a = input()
        if '/file' in a:
            name = input("Enter file path with .txt")
            f = open(name, 'r')
            for l in f:
                ids.append(l[:-1])
            break
        if a != '%%%':
            ids.append(a)
        elif a == '%%%':
            break
        else:
            print('cannot understand')

print('this can take a while')

for id in ids:
    while True:
        resp = vk.groups.getMembers(group_id=id, offset=offset)["response"]
        array += resp["items"]
        offset += 1000
        if offset > resp["count"]:
            break

maxcount = len(ids)
verjnakan = []

for id in array:
    b = 0
    nid = vkid(int(id), 1)
    for oid in verjnakan:
        if oid.val == nid.val:
            oid.changecount(oid.count + 1)
            b = 1
            break
    if b == 0:
        verjnakan.append(nid)

userids = []

print('result in result.txt')

f2 = open('result.txt', 'a')

for oid in verjnakan:
    if oid.count == maxcount:
        f2.write(str(oid.val) + '\n')
