from PyQt6.QtCore import QDate

now = QDate.currentDate()

d = QDate(1946, 5, 7)


print(f'Days in month: {d.daysInMonth()}')
print(f'Days in year: {d.daysInYear()}')
