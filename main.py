from prettytable import PrettyTable


class MusicBar():
    def __init__(self):
        self.list_song = []

    def addon(self, song):
        self.list_song.append(song)

    def writeall(self):
        th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
        td = []
        for i in range(len(self.list_song)):
            td.append(self.list_song[i].name)
            td.append(self.list_song[i].artist)
            td.append(self.list_song[i].link)
            td.append(self.list_song[i].rate)
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print(table)

    def sortbyrate(self):
        temp = self.list_song
        for i in range(len(temp) - 1):
            for j in range(len(temp) - i - 1):
                if int(temp[j].rate) < int(temp[j + 1].rate):
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
        th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
        td = []
        for i in range(len(temp)):
            td.append(temp[i].name)
            td.append(temp[i].artist)
            td.append(temp[i].link)
            td.append(temp[i].rate)
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print(table)

    def find_songs_of_artist(self, info):
        temp = []
        for i in range(len(self.list_song)):
            if self.list_song[i].artist == info:
                temp.append(self.list_song[i])
        if len(temp) == 0:
            print('За вашим запитом нічого не знайдено')
        else:
            th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
            td = []
            for i in range(len(temp)):
                td.append(temp[i].name)
                td.append(temp[i].artist)
                td.append(temp[i].link)
                td.append(temp[i].rate)
            columns = len(th)
            table = PrettyTable(th)
            td_data = td[:]
            while td_data:
                table.add_row(td_data[:columns])
                td_data = td_data[columns:]

            print(table)

    def find_songs_of_name(self, info):
        temp = []
        for i in range(len(self.list_song)):
            if self.list_song[i].name == info:
                temp.append(self.list_song[i])
        if len(temp) == 0:
            print('За вашим запитом нічого не знайдено')
        else:
            th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
            td = []
            for i in range(len(temp)):
                td.append(temp[i].name)
                td.append(temp[i].artist)
                td.append(temp[i].link)
                td.append(temp[i].rate)
            columns = len(th)
            table = PrettyTable(th)
            td_data = td[:]
            while td_data:
                table.add_row(td_data[:columns])
                td_data = td_data[columns:]

            print(table)

    def find_songs_of_link(self, info):
        temp = []
        for i in range(len(self.list_song)):
            if self.list_song[i].link == info:
                temp.append(self.list_song[i])
        if len(temp) == 0:
            print('За вашим запитом нічого не знайдено')
        else:
            th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
            td = []
            for i in range(len(temp)):
                td.append(temp[i].name)
                td.append(temp[i].artist)
                td.append(temp[i].link)
                td.append(temp[i].rate)
            columns = len(th)
            table = PrettyTable(th)
            td_data = td[:]
            while td_data:
                table.add_row(td_data[:columns])
                td_data = td_data[columns:]

            print(table)

    def find_songs_of_rate(self, info):
        temp = []
        if info.isdigit():
            for i in range(len(self.list_song)):
                if abs(int(self.list_song[i].rate) - int(info)) < 10000:
                    temp.append(self.list_song[i])
            if len(temp) == 0:
                print('За вашим запитом нічого не знайдено')
            else:
                th = ['Назва', 'Група-Виконавець', 'посилання на аудіо- або відео-файл', 'особистий рейтинг пісні']
                td = []
                for i in range(len(temp)):
                    td.append(temp[i].name)
                    td.append(temp[i].artist)
                    td.append(temp[i].link)
                    td.append(temp[i].rate)
                columns = len(th)
                table = PrettyTable(th)
                td_data = td[:]
                while td_data:
                    table.add_row(td_data[:columns])
                    td_data = td_data[columns:]
                print(table)
        else:
            print('Не ввірний ввод рейтінгу')
            #  quit()


class Song():
    def __init__(self, name, artist, link, rate):
        if rate.isdigit() and link.rfind('https://') != -1 and len(name) != 0 and len(artist) != 0 and len(link) != 0\
                and len(rate) != 0:
            self.flag = True
            self.name = name
            self.artist = artist
            self.link = link
            self.rate = rate
        else:
            self.flag = False

    def checker(self):
        if self.flag is False:
            return False
        else:
            return True



            #  quit()


def main():
    # Стартові значення
    MB = MusicBar()
    S1 = Song('Californication', 'Red Hot Chili Peppers', 'https://www.youtube.com/watch?v=YlUKcNNmywk', '780422615')
    MB.addon(S1)
    S1 = Song('Stressed Out', 'twenty one pilots', 'https://www.youtube.com/watch?v=pXRviuL6vMY', '2191418613')
    MB.addon(S1)
    S1 = Song('Dark Necessities', 'Red Hot Chili Peppers', 'https://www.youtube.com/watch?v=Q0oIoR9mLwc', '304262727')
    MB.addon(S1)
    while True:
        print('\nДля додавання пісні в музичну скриньку введіть - 1\n')
        print('Для виведення списку пісень введіть            - 2\n')
        print('Для визначення топ-списку пісень введіть       - 3\n')
        print('Для пошуку пісень группи-виконавця введіть     - 4\n')
        print('Для пошуку пісні через назву введіть           - 5\n')
        print('Для пошуку пісні через рейтинг введіть         - 6\n')
        print('Для пошуку пісні через посилання введіть       - 7\n')
        print('Для завершення програми введіть                - 0\n')
        x = input('')
        if x == '1':
            name = input('Задайте назву пісні\n')
            artist = input('Задайте назву виконавця\n')
            link = input('Задайте посилання пісні\n')
            rate = input('Задайте  особистий  рейтинг  пісні\n')
            S = Song(name, artist, link, rate)
            if S.checker() is True:
                MB.addon(S)
            else:
                print('Не вірний ввод данних')
        if x == '2':
            MB.writeall()
        if x == '3':
            MB.sortbyrate()
        if x == '4':
            art = input('Задайте назву группи / виконавця для пошуку\n')
            MB.find_songs_of_artist(art)
        if x == '5':
            name = input('Задайте назву пісні для пошуку\n')
            MB.find_songs_of_name(name)
        if x == '6':
            rate = input('Задайте рейтинг пісня для пошуку\n')
            MB.find_songs_of_rate(rate)
        if x == '7':
            link = input('Задайте посилання на пісню для пошуку\n')
            MB.find_songs_of_link(link)
        if x == '0':
            quit()


main()