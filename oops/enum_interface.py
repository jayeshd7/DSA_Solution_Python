from enum import Enum


class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = DayOfWeek.FRIDAY
print(today)


for day in DayOfWeek:
    print(day.name, day.value)
