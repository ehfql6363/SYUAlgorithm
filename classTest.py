class SoccerPlayer():
    def __init__(self, name, position, backNumber):
        self.name = name
        self.position = position
        self.backNumber = backNumber

    def changBackNumber(self, newNumber):
        print(f"선수의 등번호를 {self.backNumber}에서 {newNumber}로 변경.")
        self.backNumber = newNumber

    def __str__(self):
        return f"Hello, My name is {self.name}. My back number is {self.backNumber}."


KimDongYeol = SoccerPlayer("KimDongYeol", "MF", 7)

print(KimDongYeol.position)
print(KimDongYeol)

KimDongYeol.changBackNumber(13)

print(KimDongYeol)
