import types


class Strategy:
    def __init__(self, function=None):
        self.name = "strategy method"
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("Do nothing")


def strategy_one(self):
    print('strategy one')


def strategy_two(self):
    print('strategy two')


s = Strategy()
s1 = Strategy(strategy_one)
s2 = Strategy(strategy_two)
s.execute()
s1.execute()
s2.execute()
