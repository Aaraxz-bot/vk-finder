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

print("""\033[1;32;40m
\033[1;32;40m/$$    /$$ /$$   /$$        /$$$$$$  /$$                 /$$
\033[1;32;40m| $$   | $$| $$  /$$/       /$$__  $$|__/                | $$
\033[1;32;40m| $$   | $$| $$ /$$/       | $$  \__/ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$
\033[1;32;40m|  $$ / $$/| $$$$$/ /$$$$$$| $$$$    | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
\033[1;32;40m \  $$ $$/ | $$  $$|______/| $$_/    | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
\033[1;32;40m  \  $$$/  | $$\  $$       | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$
\033[1;32;40m   \  $/   | $$ \  $$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$
\033[1;32;40m    \_/    |__/  \__/      |__/      |__/|__/  |__/ \_______/ \_______/|__/

\033[1;32;40m by kinobi
\033[1;32;40m ~bul bul forever~""")

print("""
1) get mutal friends
2) get mutal members
3) get user info

enter an option (for ex. 1): """, end = '')
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

        moreinfoids = []

        while True:
            anw = input("Job is done. Do you want to see result on your screen? (y/n): ")
            if anw == 'y' or anw == 'Y':
                i = 1
                for oid in verjnakan:
                    if oid.count == maxcount:
                        print(str(i) + ') ' + str(oid.val))
                        i += 1
                        moreinfoids.append(oid.val)
            elif anw == 'n' or anw == 'N':
                while True:
                    anw1 = input("Do you want to rewrite old data? (y/n): ")
                    if anw1 == 'y' or anw1 == 'Y':
                        f = open('result.txt', 'w')
                        f.write('')
                        f.close()
                        f2 = open('result.txt', 'a')
                        for oid in verjnakan:
                            if oid.count == maxcount:
                                f2.write(str(oid.val) + '\n')
                                moreinfoids.append(oid.val)
                        print('result in result.txt')
                    elif anw1 == 'n' or anw1 == 'N':
                        name = input('Enter your file name (with txt): ')
                        os.system('touch ' + name)
                        f2 = open(name, 'a')
                        for oid in verjnakan:
                            if oid.count == maxcount:
                                f2.write(str(oid.val) + '\n')
                                moreinfoids.append(oid.val)
                        print('result in ' + name)
                        break
            break

        while True:
            getusers = input("Do you want to get more information about users? (y/n): ")
            if getusers == 'y' or getusers == 'Y':
                g = 0
                userstxtname = ''
                while True:
                    anw2 = input('Do you want to save data to txt? (y/n): ')
                    if anw2 == 'y' or anw2 == 'Y':
                        userstxtname = input('Enter txt file name (with .txt): ')
                        os.system('touch ' + userstxtname)
                        break
                    elif anw2 == 'n' or anw2 == 'N':
                        g = 1
                        break
                while True:
                    insertid = input('Enter users number (for ex. 1) * if all %%% if end: ')
                    if insertid == '%%%':
                        break
                    elif int(insertid) >= 1 and int(insertid) <= len(moreinfoids):
                        resp = vk.users.get(user_ids=moreinfoids[int(insertid)-1], fields = 'photo_id, verified, sex, bdate, city, country, home_town, has_mobile, contacts, site, education, universities, schools, status, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, interests, about, can_post, can_see_all_posts, timezone, career, military')['response']
                        try:
                            print('first name: /' + str(resp[0]['first_name']) + '/')
                        except:
                            print("can't find first name")
                        try:
                            print('last name:  /' + str(resp[0]['last_name']) + '/')
                        except:
                            print("can't find last name")
                        try:
                            print('sex:        /' + str(resp[0]['sex']) + '/')
                        except:
                            print("can't find sex")
                        try:
                            print('nickname:   /' + str(resp[0]['nickname']) + '/')
                        except:
                            print("can't find nickname")
                        try:
                            print('bdate:      /' + str(resp[0]['bdate']) + '/')
                        except:
                            print("can't find bdate")
                        try:
                            print('city:       /' + str(resp[0]['city']['title']) + '/')
                        except:
                            print("can't find city")
                        try:
                            print('country:    /' + str(resp[0]['country']['title']) + '/')
                        except:
                            print("can't find county")
                        try:
                            print('photo:      /' + str(resp[0]['photo_id']) + '/')
                        except:
                            print("can't find photo")
                        try:
                            print('skype:      /' + str(resp[0]['skype']) + '/')
                        except:
                            print("can't find skype")
                        try:
                            print('interests:  /' + str(resp[0]['interests']) + '/')
                        except:
                            print("can't find interests")
                        try:
                            print('about:      /' + str(resp[0]['about']) + '/')
                        except:
                            print("can't find about")
                        try:
                            print('mobile:     /' + str(resp[0]['mobile_phone']) + '/')
                        except:
                            print("can't find mobile number")
                        try:
                            print('site:       /' + str(resp[0]['site']) + '/')
                        except:
                            print("can't find size")
                        try:
                            print('status:     /' + str(resp[0]['status']) + '/')
                        except:
                            print("can't find status")
                        try:
                            print('followers:  /' + str(resp[0]['followers_count']) + '/')
                        except:
                            print("can't find followers")
                        try:
                            print('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/')
                        except:
                            print("can't find occupation")
                        try:
                            print('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/')
                        except:
                            print("can't find personal info")
                        try:
                            print('relatives:  /' + str(resp[0]['relatives']) + '/')
                        except:
                            print("can't find relatives")
                        if g == 0:
                            f4 = open(userstxtname, 'a')
                            f4.write('USER ID :: --' + str(moreinfoids[int(insertid)-1]) + '--\n\n')
                            try:
                                f4.write('first name: /' + str(resp[0]['first_name']) + '/\n')
                            except:
                                f4.write("can't find first name\n")
                            try:
                                f4.write('last name:  /' + str(resp[0]['last_name']) + '/\n')
                            except:
                                f4.write("can't find last name\n")
                            try:
                                f4.write('sex:        /' + str(resp[0]['sex']) + '/\n')
                            except:
                                f4.write("can't find sex\n")
                            try:
                                f4.write('nickname:   /' + str(resp[0]['nickname']) + '/\n')
                            except:
                                f4.write("can't find nickname\n")
                            try:
                                f4.write('bdate:      /' + str(resp[0]['bdate']) + '/\n')
                            except:
                                f4.write("can't find bdate\n")
                            try:
                                f4.write('city:       /' + str(resp[0]['city']['title']) + '/\n')
                            except:
                                f4.write("can't find city\n")
                            try:
                                f4.write('country:    /' + str(resp[0]['country']['title']) + '/\n')
                            except:
                                f4.write("can't find county\n")
                            try:
                                f4.write('photo:      /' + str(resp[0]['photo_id']) + '/\n')
                            except:
                                f4.write("can't find photo\n")
                            try:
                                f4.write('skype:      /' + str(resp[0]['skype']) + '/\n')
                            except:
                                f4.write("can't find skype\n")
                            try:
                                f4.write('interests:  /' + str(resp[0]['interests']) + '/\n')
                            except:
                                f4.write("can't find interests\n")
                            try:
                                f4.write('about:      /' + str(resp[0]['about']) + '/\n')
                            except:
                                f4.write("can't find about\n")
                            try:
                                f4.write('mobile:     /' + str(resp[0]['mobile_phone']) + '/\n')
                            except:
                                f4.write("can't find mobile number\n")
                            try:
                                f4.write('site:       /' + str(resp[0]['site']) + '/\n')
                            except:
                                f4.write("can't find size\n")
                            try:
                                f4.write('status:     /' + str(resp[0]['status']) + '/\n')
                            except:
                                f4.write("can't find status\n")
                            try:
                                f4.write('followers:  /' + str(resp[0]['followers_count']) + '/\n')
                            except:
                                f4.write("can't find followers\n")
                            try:
                                f4.write('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/\n')
                            except:
                                f4.write("can't find occupation\n")
                            try:
                                f4.write('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/\n')
                            except:
                                f4.write("can't find personal info\n")
                            try:
                                f4.write('relatives:  /' + str(resp[0]['relatives']) + '/\n')
                            except:
                                print("can't find relatives\n")
                            f4.write('\n\n\n')
                            print('result saved to ' + userstxtname)
                if insertid == '%%%':
                    break
            elif getusers == 'n' or getusers == 'N':
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

        moreinfoids = []

        while True:
            anw = input("Job is done. Do you want to see result on your screen? (y/n): ")
            i = 1
            if anw == 'y' or anw == 'Y':
                for oid in array:
                    print(str(i) + ') ' + str(oid))
                    moreinfoids.append(oid)
                    i += 1
                while True:
                    anw1 = input("Do you want to rewrite old data? (y/n): ")
                    if anw1 == 'y' or anw1 == 'Y':
                        f = open('result.txt', 'w')
                        f.write('')
                        f.close()
                        f2 = open('result.txt', 'a')
                        for oid in array:
                            f2.write(str(oid) + '\n')
                        print('result in result.txt')
                        break
                    elif anw1 == 'n' or anw1 == 'N':
                        name = input('Enter your file name (with txt): ')
                        os.system('touch ' + name)
                        f2 = open(name, 'a')
                        for oid in array:
                            f2.write(str(oid) + '\n')
                        print('result in ' + name)
                        break
            elif anw == 'n' or anw == 'N':
                while True:
                    anw1 = input("Do you want to rewrite old data? (y/n): ")
                    if anw1 == 'y' or anw1 == 'Y':
                        f = open('result.txt', 'w')
                        f.write('')
                        f.close()
                        f2 = open('result.txt', 'a')
                        for oid in array:
                            f2.write(str(oid) + '\n')
                            moreinfoids.append(oid)
                            i += 1
                        print('result in result.txt')
                    elif anw1 == 'n' or anw1 == 'N':
                        name = input('Enter your file name (with txt): ')
                        os.system('touch ' + name)
                        f2 = open(name, 'a')
                        for oid in array:
                            f2.write(str(oid) + '\n')
                            moreinfoids.append(oid)
                            i += 1
                        print('result in ' + name)
                        break
            break
        while True:
            getusers = input("Do you want to get more information about users? (y/n): ")
            if getusers == 'y' or getusers == 'Y':
                g = 0
                userstxtname = ''
                while True:
                    anw2 = input('Do you want to save data to txt? (y/n): ')
                    if anw2 == 'y' or anw2 == 'Y':
                        userstxtname = input('Enter txt file name (with .txt): ')
                        os.system('touch ' + userstxtname)
                        break
                    elif anw2 == 'n' or anw2 == 'N':
                        g = 1
                        break
                while True:
                    insertid = input('Enter users number (for ex. 1) %%% if end: ')
                    if insertid == '%%%':
                        break
                    elif int(insertid) >= 1 and int(insertid) <= len(moreinfoids):
                        resp = vk.users.get(user_ids=moreinfoids[int(insertid)-1], fields = 'photo_id, verified, sex, bdate, city, country, home_town, has_mobile, contacts, site, education, universities, schools, status, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, interests, about, can_post, can_see_all_posts, timezone, career, military')['response']
                        try:
                            print('first name: /' + str(resp[0]['first_name']) + '/')
                        except:
                            print("can't find first name")
                        try:
                            print('last name:  /' + str(resp[0]['last_name']) + '/')
                        except:
                            print("can't find last name")
                        try:
                            print('sex:        /' + str(resp[0]['sex']) + '/')
                        except:
                            print("can't find sex")
                        try:
                            print('nickname:   /' + str(resp[0]['nickname']) + '/')
                        except:
                            print("can't find nickname")
                        try:
                            print('bdate:      /' + str(resp[0]['bdate']) + '/')
                        except:
                            print("can't find bdate")
                        try:
                            print('city:       /' + str(resp[0]['city']['title']) + '/')
                        except:
                            print("can't find city")
                        try:
                            print('country:    /' + str(resp[0]['country']['title']) + '/')
                        except:
                            print("can't find county")
                        try:
                            print('photo:      /' + str(resp[0]['photo_id']) + '/')
                        except:
                            print("can't find photo")
                        try:
                            print('skype:      /' + str(resp[0]['skype']) + '/')
                        except:
                            print("can't find skype")
                        try:
                            print('interests:  /' + str(resp[0]['interests']) + '/')
                        except:
                            print("can't find interests")
                        try:
                            print('about:      /' + str(resp[0]['about']) + '/')
                        except:
                            print("can't find about")
                        try:
                            print('mobile:     /' + str(resp[0]['mobile_phone']) + '/')
                        except:
                            print("can't find mobile number")
                        try:
                            print('site:       /' + str(resp[0]['site']) + '/')
                        except:
                            print("can't find size")
                        try:
                            print('status:     /' + str(resp[0]['status']) + '/')
                        except:
                            print("can't find status")
                        try:
                            print('followers:  /' + str(resp[0]['followers_count']) + '/')
                        except:
                            print("can't find followers")
                        try:
                            print('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/')
                        except:
                            print("can't find occupation")
                        try:
                            print('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/')
                        except:
                            print("can't find personal info")
                        try:
                            print('relatives:  /' + str(resp[0]['relatives']) + '/')
                        except:
                            print("can't find relatives")
                        if g == 0:
                            f4 = open(userstxtname, 'a')
                            f4.write('USER ID :: --' + str(moreinfoids[int(insertid)-1]) + '--\n\n')
                            try:
                                f4.write('first name: /' + str(resp[0]['first_name']) + '/\n')
                            except:
                                f4.write("can't find first name\n")
                            try:
                                f4.write('last name:  /' + str(resp[0]['last_name']) + '/\n')
                            except:
                                f4.write("can't find last name\n")
                            try:
                                f4.write('sex:        /' + str(resp[0]['sex']) + '/\n')
                            except:
                                f4.write("can't find sex\n")
                            try:
                                f4.write('nickname:   /' + str(resp[0]['nickname']) + '/\n')
                            except:
                                f4.write("can't find nickname\n")
                            try:
                                f4.write('bdate:      /' + str(resp[0]['bdate']) + '/\n')
                            except:
                                f4.write("can't find bdate\n")
                            try:
                                f4.write('city:       /' + str(resp[0]['city']['title']) + '/\n')
                            except:
                                f4.write("can't find city\n")
                            try:
                                f4.write('country:    /' + str(resp[0]['country']['title']) + '/\n')
                            except:
                                f4.write("can't find county\n")
                            try:
                                f4.write('photo:      /' + str(resp[0]['photo_id']) + '/\n')
                            except:
                                f4.write("can't find photo\n")
                            try:
                                f4.write('skype:      /' + str(resp[0]['skype']) + '/\n')
                            except:
                                f4.write("can't find skype\n")
                            try:
                                f4.write('interests:  /' + str(resp[0]['interests']) + '/\n')
                            except:
                                f4.write("can't find interests\n")
                            try:
                                f4.write('about:      /' + str(resp[0]['about']) + '/\n')
                            except:
                                f4.write("can't find about\n")
                            try:
                                f4.write('mobile:     /' + str(resp[0]['mobile_phone']) + '/\n')
                            except:
                                f4.write("can't find mobile number\n")
                            try:
                                f4.write('site:       /' + str(resp[0]['site']) + '/\n')
                            except:
                                f4.write("can't find size\n")
                            try:
                                f4.write('status:     /' + str(resp[0]['status']) + '/\n')
                            except:
                                f4.write("can't find status\n")
                            try:
                                f4.write('followers:  /' + str(resp[0]['followers_count']) + '/\n')
                            except:
                                f4.write("can't find followers\n")
                            try:
                                f4.write('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/\n')
                            except:
                                f4.write("can't find occupation\n")
                            try:
                                f4.write('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/\n')
                            except:
                                f4.write("can't find personal info\n")
                            try:
                                f4.write('relatives:  /' + str(resp[0]['relatives']) + '/\n')
                            except:
                                print("can't find relatives\n")
                            f4.write('\n\n\n')
                            print('result saved to ' + userstxtname)
                if insertid == '%%%':
                    break
            elif getusers == 'n' or getusers == 'N':
                break
    elif opt == 3:
        vk = api.API(token=token, version='5.49')
        g = 0
        userstxtname = ''
        while True:
            anw2 = input('Do you want to save data to txt? (y/n): ')
            if anw2 == 'y' or anw2 == 'Y':
                userstxtname = input('Enter txt file name (with .txt): ')
                os.system('touch ' + userstxtname)
                break
            elif anw2 == 'n' or anw2 == 'N':
                g = 1
                break
        while True:
            insertid = input('Enter users id %%% if end: ')
            if insertid == '%%%':
                break
            else:
                resp = vk.users.get(user_ids=int(insertid), fields = 'photo_id, verified, sex, bdate, city, country, home_town, has_mobile, contacts, site, education, universities, schools, status, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, interests, about, can_post, can_see_all_posts, timezone, career, military')['response']
                try:
                    print('first name: /' + str(resp[0]['first_name']) + '/')
                except:
                    print("can't find first name")
                try:
                    print('last name:  /' + str(resp[0]['last_name']) + '/')
                except:
                    print("can't find last name")
                try:
                    print('sex:        /' + str(resp[0]['sex']) + '/')
                except:
                    print("can't find sex")
                try:
                    print('nickname:   /' + str(resp[0]['nickname']) + '/')
                except:
                    print("can't find nickname")
                try:
                    print('bdate:      /' + str(resp[0]['bdate']) + '/')
                except:
                    print("can't find bdate")
                try:
                    print('city:       /' + str(resp[0]['city']['title']) + '/')
                except:
                    print("can't find city")
                try:
                    print('country:    /' + str(resp[0]['country']['title']) + '/')
                except:
                    print("can't find county")
                try:
                    print('photo:      /' + str(resp[0]['photo_id']) + '/')
                except:
                    print("can't find photo")
                try:
                    print('skype:      /' + str(resp[0]['skype']) + '/')
                except:
                    print("can't find skype")
                try:
                    print('interests:  /' + str(resp[0]['interests']) + '/')
                except:
                    print("can't find interests")
                try:
                    print('about:      /' + str(resp[0]['about']) + '/')
                except:
                    print("can't find about")
                try:
                    print('mobile:     /' + str(resp[0]['mobile_phone']) + '/')
                except:
                    print("can't find mobile number")
                try:
                    print('site:       /' + str(resp[0]['site']) + '/')
                except:
                    print("can't find size")
                try:
                    print('status:     /' + str(resp[0]['status']) + '/')
                except:
                    print("can't find status")
                try:
                    print('followers:  /' + str(resp[0]['followers_count']) + '/')
                except:
                    print("can't find followers")
                try:
                    print('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/')
                except:
                    print("can't find occupation")
                try:
                    print('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/')
                except:
                    print("can't find personal info")
                try:
                    print('relatives:  /' + str(resp[0]['relatives']) + '/')
                except:
                    print("can't find relatives")
                if g == 0:
                    f4 = open(userstxtname, 'a')
                    f4.write('USER ID :: --' + str(insertid) + '--\n\n')
                    try:
                        f4.write('first name: /' + str(resp[0]['first_name']) + '/\n')
                    except:
                        f4.write("can't find first name\n")
                    try:
                        f4.write('last name:  /' + str(resp[0]['last_name']) + '/\n')
                    except:
                        f4.write("can't find last name\n")
                    try:
                        f4.write('sex:        /' + str(resp[0]['sex']) + '/\n')
                    except:
                        f4.write("can't find sex\n")
                    try:
                        f4.write('nickname:   /' + str(resp[0]['nickname']) + '/\n')
                    except:
                        f4.write("can't find nickname\n")
                    try:
                        f4.write('bdate:      /' + str(resp[0]['bdate']) + '/\n')
                    except:
                        f4.write("can't find bdate\n")
                    try:
                        f4.write('city:       /' + str(resp[0]['city']['title']) + '/\n')
                    except:
                        f4.write("can't find city\n")
                    try:
                        f4.write('country:    /' + str(resp[0]['country']['title']) + '/\n')
                    except:
                        f4.write("can't find county\n")
                    try:
                        f4.write('photo:      /' + str(resp[0]['photo_id']) + '/\n')
                    except:
                        f4.write("can't find photo\n")
                    try:
                        f4.write('skype:      /' + str(resp[0]['skype']) + '/\n')
                    except:
                        f4.write("can't find skype\n")
                    try:
                        f4.write('interests:  /' + str(resp[0]['interests']) + '/\n')
                    except:
                        f4.write("can't find interests\n")
                    try:
                        f4.write('about:      /' + str(resp[0]['about']) + '/\n')
                    except:
                        f4.write("can't find about\n")
                    try:
                        f4.write('mobile:     /' + str(resp[0]['mobile_phone']) + '/\n')
                    except:
                        f4.write("can't find mobile number\n")
                    try:
                        f4.write('site:       /' + str(resp[0]['site']) + '/\n')
                    except:
                        f4.write("can't find size\n")
                    try:
                        f4.write('status:     /' + str(resp[0]['status']) + '/\n')
                    except:
                        f4.write("can't find status\n")
                    try:
                        f4.write('followers:  /' + str(resp[0]['followers_count']) + '/\n')
                    except:
                        f4.write("can't find followers\n")
                    try:
                        f4.write('occupation: /' + str(resp[0]['occupation']['name']) + '/ /' + str(resp[0]['occupation']['type']) + '/\n')
                    except:
                        f4.write("can't find occupation\n")
                    try:
                        f4.write('personal:   /alcohol: ' + str(resp[0]['personal']['alcohol']) + '/ /inspiret by: ' + str(resp[0]['personal']['inspired_by']) + '/ /lanuages: ' + str(resp[0]['personal']['langs']) + '/\n')
                    except:
                        f4.write("can't find personal info\n")
                    try:
                        f4.write('relatives:  /' + str(resp[0]['relatives']) + '/\n')
                    except:
                        print("can't find relatives\n")
                    f4.write('\n\n\n')
                    print('result saved to ' + userstxtname)
        if insertid == '%%%':
            break
    break
