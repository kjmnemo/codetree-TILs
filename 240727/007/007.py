class Cipher:
    def __init__(self, name, code, time):
        self.name = name
        self.code = code
        self.time = time


a,b,c = input().split()
person = Cipher(a,b,c)
print(f'secret code : {person.name}')
print(f'meeting point : {person.code}')
print(f'time : {person.time}')