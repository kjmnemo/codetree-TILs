class Game:
    def __init__(self, Id, lv):
        self.Iden = Id
        self.lv = int(lv)  # lv를 정수로 변환

first = Game('codetree', 10)
a, b = input().split()
second = Game(a, b)  # b를 입력받을 때 자동으로 문자열로 받아짐

print(f'user {first.Iden} lv {first.lv}')
print(f'user {second.Iden} lv {second.lv}')