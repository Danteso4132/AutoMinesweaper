import tkinter as tk
import random


import requests
def getting_info():
    def typer(s):
        if 'OneHandWeapons' in s:
            return 1
        if 'TwoHandWeapons' in s:
            return 2
        if 'Ring' in s:
            return 3
        if 'Amulet' in s:
            return 4
        if 'Belts' in s:
            return 5
        if '/Shield' in s:
            return 6
        if 'Helmet' in s:
            return 7
        if 'BodyArmours' in s:
            return 8
        if 'Gloves' in s:
            return 9
        if 'Boots' in s:
            return 10

    def getting_type(i):
        helper = ['OneHandWeapons', 'TwoHandWeapons', 'Ring', 'Amulet', 'Belts', 'Shield', 'Helmet', 'BodyArmours', 'Gloves', 'Boots']
        return(helper[i-1])



    cookies = {'POESESSID':'df56b5ccec3aed0a0b1c8e7d0a7d2cea'}
    r = requests.post("https://www.pathofexile.com/character-window/get-stash-items?league=Standard&realm=pc&accountName=monser4132&tabs=0&tabIndex=0", cookies=cookies)

    s = r.text
    s += '"verified"'
    item_id = []
    positions_x = []
    positions_y = []
    item_size_x = []
    item_size_y = []

    item_type = []

    #Splitting to items
    for i in range(len(s)-8):
        if s[i:i+10] == '"verified"':
            item_id.append(i)
    items_s = []
    for i in range(len(item_id)-1):
        items_s.append(s[item_id[i]:item_id[i+1]])


    #Getting the position
    for i in range(len(items_s)):
        all_numbers = '0123456789'
        x_find = items_s[i].index('"x":')
        coord_s = items_s[i][x_find:x_find+13]
        flag = True
        x_pos = ''
        y_pos = ''
        for j in range(len(coord_s)):
            if coord_s[j] in all_numbers:
                if flag:
                    x_pos += coord_s[j]
                else:
                    y_pos += coord_s[j]
            if coord_s[j] == ',':
                flag = False
        x_pos = int(x_pos)+1
        y_pos = int(y_pos)+1
        positions_x.append(x_pos)
        positions_y.append(y_pos)

        type_s = typer(items_s[i])
        #print(getting_type(type_s))

        item_type.append(type_s)

        item_width = int(items_s[i][21])
        item_height = int(items_s[i][27])

        item_size_x.append(item_width)
        item_size_y.append(item_height)







    for i in range(len(positions_x)):
        print('x=',positions_x[i], 'y=', positions_y[i], '/type=', getting_type(item_type[i]), 'w', item_size_x[i], 'h', item_size_y[i])
        #print(items_s[i])
    #print(item_type)

    info = [0]*len(positions_x)
    for i in range(len(positions_x)):
        info[i] = [positions_x[i], positions_y[i], item_type[i], item_size_x[i], item_size_y[i]]

    print(items_s[0])

    return info


def weapon(info):
    weps = 0
    s = []
    for i in range(len(info)):
        if info[i][2] == 1 or info[i][2] == 6:
            weps += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if info[i][2] == 2:
            weps += 2
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if weps >= 2:
            info[i][2] = 99
            return s
    else:
        return False
def armour(info):
    arm = 0
    s = []
    for i in range(len(info)):
        if info[i][2] == 8:
            arm+=1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if arm >= 1:
            info[i][2] = 99
            return s
    else:
        return False


def helmet(info):
    helms = 0
    s = []
    for i in range(len(info)):
        if info[i][2] == 7:
            helms+=1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if helms >= 1:
            info[i][2] = 99
            return s
    else:
        return False

def boots(info):
    boots = 0
    s = []
    for i in range(len(info)):
        if info[i][2] == 10:
            boots += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if boots >= 1:
            info[i][2] = 99
            return s
    else:
        return False

def gloves(info):
    s = []
    glv = 0
    for i in range(len(info)):
        if info[i][2] == 9:
            glv += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if glv >= 1:
            info[i][2] = 99
            return s
    else:
        return False

def ring(info):
    rings = 0
    s = []
    for i in range(len(info)):
        if info[i][2] == 3:
            rings += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if rings >= 2:
            info[i][2] = 99
            return s
    else:
        return False

def amulet(info):
    s = []
    amuls = 0
    for i in range(len(info)):
        if info[i][2] == 4:
            amuls += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if amuls >= 1:
            info[i][2] = 99
            return s
    else:
        return False

def belt(info):
    s = []
    blt = 0
    for i in range(len(info)):
        if info[i][2] == 5:
            blt += 1
            s.append([info[i][0], info[i][1], info[i][3], info[i][4]])
        if blt >= 1:
            info[i][2] = 99
            return s
    else:
        return False

def fielding(s):
    global field
    if type(s[0]) != int:
        s = s[0]
    print(s)
    for i in range(s[2]):
        for j in range(s[3]):
            field[s[0] + i-1][s[1] + j-1] = 1
    return
def creating_rec(info):
    recept = [0]*10
    global field
    k = 0
    if weapon(info) != False and armour(info) != False and amulet(info) != False and ring(info) != False and gloves(info) != False and boots(info) != False and gloves(info) != False and belt(info) != False :

        field = []
        for jj in range(24):
            field.append([0] * 24)

        s = weapon(info)
        s1 = armour(info)
        s2 = amulet(info)
        s3 = ring(info)
        s4 = gloves(info)
        s5 = boots(info)
        s6 = belt(info)
        s7 = helmet(info)

        if len(s) == 2:
            s_1 = s[0]
            fielding(s_1)
            s_2 = s[1]
            fielding(s_2)
        else:
            fielding(s)

        fielding(s3[0])
        fielding(s3[1])
        fielding(s1[0])
        fielding(s2[0])
        fielding(s4[0])
        fielding(s5[0])
        fielding(s6[0])
        fielding(s7[0])

        for i in range(24):
            print(field[i])

        return(field)



    else:
        print('Not Possible')





















colours = ['red', 'blue', 'green', 'yellow']

def gen_set(field):
    for i in range(24):
        for j in range(24):
            if field[i][j] == 1:
                colour = 'red'
            else:
                colour = 'blue'
            #colour = colours[random.randint(0, 3)]
            tk.Label(root, bg=colour).place(x=i * 21, y=j * 21, width=21, height=21)
    # root.quit()
    return

info = 0
final_field = 0

def generate():
    # print('1')
    global final_field
    print('Generating')
    if info != 0:
        final_field = creating_rec(info)
        gen_set(final_field)
    return

def update_s():
    global info
    info = getting_info()



def clear_s():
    tk.Label(root, bg='red').place(x=0, y=0, width=504, height=504)

root = tk.Tk()
root.title("Сетка")
root.geometry("504x504")
root.wm_attributes('-transparentcolor', 'red')
root.wm_attributes('-topmost', '1')
root.wm_attributes('-alpha', 0.3)

control = tk.Tk()
control.title("COntrol")
control.wm_attributes('-topmost', '1')
control.wm_attributes('-transparentcolor', 'red')
tk.Label(control, bg='red').place(x=0, y=0, width=504, height=504)
control.geometry("200x100")

btn_gen = tk.Button(control, text="Generate", command=generate).place(x=10, y=10)
btn_clear = tk.Button(control, text='Clear', command=clear_s).place(x=80, y=10)
btn_update = tk.Button(control, text='Update', command=update_s).place(x=150, y=10)

root.mainloop()



