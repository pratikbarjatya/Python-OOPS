class English:
    @staticmethod
    def greet(self):
        print("Good Morning", name)


class French:
    @staticmethod
    def greet(self):
        print("Bonjour", name)


class German:
    @staticmethod
    def greet(self):
        print("Guten Morgan", name)


def greetings(language, name):
    language.greet(name)


print("1.English\n2.French\n3.German\n4.Enter 4 to quit")

name = input('Enter ur name...')

language = input('Enter in which language to greet you...')

if language.lower() == 'english':
    english = English()
    greetings(english, name)

if language.lower() == 'french':
    french = French()
    greetings(french, name)

if language.lower() == 'german':
    german = German()
    greetings(german, name)
