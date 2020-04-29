class SimpleDate:

    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def __eq__(self,other):
        if (self.day == other.day and self.month == other.month and self.year == other.year):
            return True

        return False

    def __str__(self):
        return str(self.day) + "." + str(self.month) + "." + str(self.year)

    def before(self, other):
        # first compare years
        if (self.year < other.year):
            return True

        # if the years are the same, compare months
        if (self.year == other.year and self.month < other.month):
            return True

        # the years and the months are the same, compare days
        if (self.year == other.year and self.month == other.month and self.day < other.day):
            return True

        return False

    # implement your method here
