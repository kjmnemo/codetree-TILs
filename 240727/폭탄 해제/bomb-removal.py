class People:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

a,b,c = input().split()
person = People(a,b,c)
print(f'code : {person.code}')
print(f'color : {person.color}')
print(f'second : {person.sec}')