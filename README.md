# Exercise 5.15 Dating app

With the exercise base the class `SimpleDate` is supplied. The date is stored with the help of the object variables `year`, `month`, and `day`:

```python
class SimpleDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # ...
```

In this exercise set we will expand this class.

## Next day

Implement the method `def advance()` that moves the date by one day. In this exercise we assume that each month has 30 day. NB! In *certain* situations you need to change the values of month and year.

## Advance specific number of days

Implement the method `def advance(self, how_many_days)` that moves the date by the number of days that is given. Use the method `advance()` that you implemented in the previous section to help you in self.

## Passing of time

Let's add the possibility to advance time to the `SimpleDate` class. Create the method `after_number_of_days(self, days)` for the class. It creates a **new** `SimpleDate` object whose date is the specified number of days greater than the object that the method was called on. You may still assume that each month has 30 days. Notice that the old date object must remain unchanged!

Since the method must create **a new object**, the structure of the code should be somewhat similar to this:

```python
def after_number_of_days(self, days):
    newDate = SimpleDate( ... )

    # do something..

    return newDate
```

Here is an example of how the method works.

```python
def main():
    date = SimpleDate(13, 2, 2015)
    print("The date is " + str(date))

    newDate = date.after_number_of_days(7)
    week = 1
    while (week <= 7):
        print("Friday after " + str(week) + " weeks is " + str(newDate))
        newDate = newDate.after_number_of_days(7)

        week = week + 1


    print("The date after 790 days from the examined Friday is ... try it out yourself!")
    #    print("Try " + date.after_number_of_days(790))
```

The program prints:

```plaintext
Friday of the examined week is 13.2.2015
Friday after 1 weeks is 20.2.2015
Friday after 2 weeks is 27.2.2015
Friday after 3 weeks is 4.3.2015
Friday after 4 weeks is 11.3.2015
Friday after 5 weeks is 18.3.2015
Friday after 6 weeks is 25.3.2015
Friday after 7 weeks is 2.4.2015
The date after 790 days from the examined Friday is ... try it out yourself!
```

**NB!** Instead of modifying the state of the old object we return a new one. Imagine that the `SimpleDate` class has a method `advance` that works similarly to the method we programmed, but it modifies the state of the old object. In that case the next block of code would cause problems.

```python
now = SimpleDate(13, 2, 2015)
after_one_week = now
after_one_week.after_number_of_days(7)

print("Now: " + str(now))
print("After one week: " + str(after_one_week))
```

The output of the program should be like this:

```plaintext
Now: 20.2.2015
After one week: 20.2.2015
```

This is because a normal assignment only copies the reference to the object. So the objects `now` and `after_one_week` in the program now refer to the **one and same** `SimpleDate` object.
