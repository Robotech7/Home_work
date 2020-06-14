from itertools import filterfalse, dropwhile
import datetime as dt


class User:

    def __init__(self, username, register_date):
        self.username = username
        self.register_date = register_date

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username


user_iter = [User(username='Mila', register_date=dt.datetime(2018, 6, 23, 15, 53, 46, 964019)),
             User(username='John', register_date=dt.datetime(2018, 6, 22, 15, 53, 46, 963948)),
             User(username='Sara', register_date=dt.datetime(2021, 6, 21, 15, 53, 46, 963580)),
             User(username='Ailce', register_date=dt.datetime(2018, 6, 19, 15, 53, 46, 964008))
             ]


def register_year_ago(x):
    if dt.datetime.now() - x.register_date < dt.timedelta(days=365):
        return True


result = list(filterfalse(register_year_ago, user_iter))

print(result)
