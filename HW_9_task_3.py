from random import randint
class Ghost():
    def __init__(self):
        a=randint(1,4)
        if a==1:
            color="white"
        if a==2:
            color="yellow"
        if a==3:
            color="purple"
        if a==4:
            color="red"
        self.color=color

ghost = Ghost()
print(ghost.color)