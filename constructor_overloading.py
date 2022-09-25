import datetime

class LetOverride:
    name:str
    phone_num:str
    email:str
    d_o_b:str

    def __init__(self,*args):
        if len(args) == 2:
            self.name = args[0]
            self.phone_num = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.phone_num = args[1]
            self.email = args[2]
        elif len(args) == 4:
            self.name = args[0]
            self.phone_num = args[1]
            self.email = args[2]
            self.d_o_b = args[3]

if __name__ == "__main__":
    print("_________________________________________")
    f_name = LetOverride("Denis Muriungi","0791570615")
    print(f_name.name)
    print(f_name.phone_num)
    print("==========================================")
    s_name = LetOverride("Denis Muriungi", "0791570615","Dennzriush@gmail.com")
    print(s_name.name)
    print(s_name.phone_num)
    print(s_name.email)
    print("==========================================")
    t_name = LetOverride("Denis Muriungi", "0791570615", "Dennzriush@gmail.com","2000")
    print(t_name.name)
    print(t_name.phone_num)
    print(t_name.email)
    print(t_name.d_o_b)
