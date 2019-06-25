name = '7z'

version = '19.0.0'

variants = [
    ['platform-windows', 'arch-AMD64'],
    ['platform-osx', 'arch-x86_64'],
    ['platform-linux', 'arch-x86_64']
]


def commands():
    env.PATH.append('{root}')
