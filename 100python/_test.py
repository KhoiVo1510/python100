class Room():
    def __init__(self, number):
        self.capacity = 0
        self.number = number
    def add(self, num):
        self.capacity += num

class Motel():
    def __init__(self, max_rooms):
        self.max_rooms = max_rooms
        self.all_rooms = [Room(i) for i in range(1, self.max_rooms + 1)]
        self.room_have_0 = [i for i in range(0, self.max_rooms)]
        self.room_have_1 = []

    def update_status_0(self, num):
        if self.all_rooms[num].capacity == 1:
            self.room_have_1.append(num)
        self.room_have_0.remove(num)
    
    def update_status_1(self, num):
        self.room_have_1.remove(num)

class Group():
    def __init__(self, members):
        self.remain_members = members

    def room_arrangement_1(self):
        self.remain_members -= 1
    def room_arrangement_2(self):
        self.remain_members -= 2

motel = Motel(5)
doankhach = [2,3,2]
group = [Group(mem) for mem in doankhach]
for grp in range(len(group)):
    while group[grp].remain_members != 0:
        if len(motel.room_have_0):
            if group[grp].remain_members > 1:

                group[grp].room_arrangement_2()

                motel.all_rooms[motel.room_have_0[0]].add(2)
                motel.update_status_0(motel.room_have_0[0])

            elif group[grp].remain_members == 1:

                group[grp].room_arrangement_1()

                motel.all_rooms[motel.room_have_0[0]].add(1)
                motel.update_status_0(motel.room_have_0[0])
            else:
                break

        elif len(motel.room_have_1):
            group[grp].room_arrangement_1()

            motel.all_rooms[motel.room_have_1[0]].add(1)
            motel.update_status_1(motel.room_have_1[0])

        else:
            break
        
for z in range(0, 5):
    print(f"Phòng {motel.all_rooms[z].number}: có {motel.all_rooms[z].capacity} người")    
