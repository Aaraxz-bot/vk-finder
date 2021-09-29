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
import os

token = input('Enter api (you can get vk api from https://vkhost.github.io/ choose vk admin): ')

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

by kinobi
~bul bul forever~""")

print("""
1) get mutal friends
2) get mutal members

enter an option (etc. 1): """, end = '')
while True:
    opt = int(input())
    if opt == 2:
        count = 0
        array = []


        vk = api.API(token=token, version='5.49')

        array = []
        ids = []

        print("Enter group id, %%% if end, /file if from file, ~you can find group id at regvk.com/id/~")

        while True:
                a = input()
                if '/file' in a:
                    name = input("Enter file path with .txt: ")
                    f = open(name, 'a')
                    for l in f:
                        if l != '\n':
                            ids.append(l[:-1])
                    break
                if a != '%%%':
                    ids.append(a)
                elif a == '%%%':
                    break
                else:
                    print('cannot understand')

        print('downloading data..')

        for id in ids:
            offset = 0
            while True:
                resp = vk.groups.getMembers(group_id=id, offset=offset)["response"]
                array += resp["items"]
                offset += 1000
                if offset > resp["count"]:
                    break

        maxcount = len(ids)
        verjnakan = []

        print('processing data..')

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

        while True:
            anw = input("Job is done. Do you wan't to see result on your screen? (y/n): ")
            if anw == 'y' or anw == 'Y':
                for oid in verjnakan:
                    if oid.count == maxcount:
                        print(oid.val)
            elif anw == 'n' or anw == 'N':
                while True:
                    anw1 = input("Do you wan't to rewrite old data? (y/n): ")
                    if anw1 == 'y' or anw1 == 'Y':
                        f2 = open('result.txt', 'a')
                        for oid in verjnakan:
                            if oid.count == maxcount:
                                f2.write(str(oid.val) + '\n')
                        print('result in result.txt')
                    elif anw1 == 'n' or anw1 == 'N':
                        name = input('Enter your file name (with txt): ')
                        os.system('touch ' + name)
                        f2 = open(name, 'a')
                        for oid in verjnakan:
                            if oid.count == maxcount:
                                f2.write(str(oid.val) + '\n')
                        print('result in ' + name)
                        break
            break


    elif opt == 1:
        count = 0
        array = []


        vk = api.API(token=token, version='5.49')

        array = []
        ids = []

        print("Enter user id, %%% if end, /file if from file, ~you can find group id at regvk.com/id/~")

        while True:
                a = input()
                if '/file' in a:
                    name = input("Enter file path with .txt: ")
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

        print('downloading data..')

        command = 'resp = vk.friends.getMutual(source_uid='
        for id in ids:
            if id != '' and id != ids[0]:
                command = command + id + ','
            elif id == ids[0]:
                command = command + id + ', target_uids='
        command = command + ')["response"]'
        command = command.replace(',)', ')')
        exec(command)
        array += resp[0]['common_friends']

        print('processing data..')

        while True:
            anw = input("Job is done. Do you wan't to see result on your screen? (y/n): ")
            if anw == 'y' or anw == 'Y':
                for oid in array:
                    print(oid)
            elif anw == 'n' or anw == 'N':
                while True:
                    anw1 = input("Do you wan't to rewrite old data? (y/n): ")
                    if anw1 == 'y' or anw1 == 'Y':
                        f2 = open('result.txt', 'a')
                        for oid in array:
                            f2.write(str(oid.val) + '\n')
                        print('result in result.txt')
                    elif anw1 == 'n' or anw1 == 'N':
                        name = input('Enter your file name (with txt): ')
                        os.system('touch ' + name)
                        f2 = open(name, 'a')
                        for oid in array:
                            f2.write(str(oid.val) + '\n')
                        print('result in ' + name)
                        break
            break
    break
