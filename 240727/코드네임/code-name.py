class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = int(score)

agents = []
for _ in range(5):
    codename, score = input().split()
    agents.append(Agent(codename, score))

lowest= min(agents, key=lambda agent: agent.score)


print(f'{lowest.codename} {lowest.score}')