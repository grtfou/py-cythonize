from elephant.monkey import coffee
from lion import hello


def run():
    output = hello.say_hi('Micky Mouse test')
    print(output)
    print(coffee.get_coffee(cup=2))
    return 1


if __name__ == '__main__':
    run()
