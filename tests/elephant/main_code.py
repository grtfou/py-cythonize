import lion.hello


def run():
    output = lion.hello.say_hi('Micky Mouse test')
    print(output)
    return 1


if __name__ == '__main__':
    run()
