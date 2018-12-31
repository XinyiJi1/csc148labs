if __name__ == '__main__':
    from typing import Any
    from lab1 import Runner, Raceregistry
    race = Raceregistry()
    race.register('gerhard@mail.utoronto.ca (with time under 40 minutes)')
    race.register('tom@mail.utoronto.ca (with time under 30 minutes)')
    race.register('toni@mail.utoronto.ca (with time under 20 minutes)')
    race.register('margot@mail.utoronto.ca(with time under 30 minutes)')
    race.register("gerhard@mail.utoronto.ca (with time under 30 minute \
    he's gotten faster))")
    print(race.under30)

