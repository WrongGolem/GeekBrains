class Date:
    #def __init__(self, line):
    #    self.line = line.split('-')

    #def get_data(self):
     #   print(int(self.line[0]), int(self.line[1]), int(self.line[2]))

    @classmethod
    def get_date(cls, line):
        line = line.split('-')
        print(int(line[0]), int(line[1]), int(line[2]))

    @staticmethod
    def validate_date(line):
        line = line.split('-')
        if 1<=int(line[0])<=31 and 1<=int(line[1])<=12 and 1<=int(line[2]):
            print('Дата имеет место быть!')
        elif int(line[0])<1 or int(line[0])>31:
            print('Количество дней в дате указано неверно!')
        elif int(line[1])<1 or int(line[1])>12:
            print('Количество ммесяцев в дате указано неверно!')
        else:
            print('Год указан неверно!')



gd = Date()
gd.get_date('15-7-1967')
gd.validate_date('15-7-1967')
gd.validate_date('45-7-1967')
gd.validate_date('15-14-1967')

