def is_leap(year):
    """Check if the give year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(month, year):
    """Return the number of days for a give month and year.
       It also checks the year for leapyear.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]

# https://quasar.as.utexas.edu/BillInfo/JulianDatesG.html
def julian_day(year: int, month: int, day: int):
    """Calculates the julian day of a give date"""
    if month < 3:
        year -= year
        month += 12
    A = year // 100
    B = A // 4
    C = 2 - A + B
    E = int(365.25 * (year + 4716))
    F = int(30.6001 * (month + 1))
    return C + day + E + F - 1524.5

def gregorian_date(julian_day: float):
    """Calculate a gregorian date dd.mm.yyyy from a give julian day."""
    Q = julian_day + 0.5
    Z = int(Q)
    W = (Z - 1867216.25) // 36524.25
    X = W // 4
    A = Z + 1 + W - X
    B = A + 1524
    C = (B - 122.1) // 365.25
    D = int(365.25 * C)
    E = (B - D) // 30.6001
    F = int(30.6001 * E)
    day = int(B - D - F + (Q - Z))
    month = int(E - 1)
    if month > 12:
        month = E - 13
    if month < 3:
        year = int(C - 4715)
    else:
        year = int(C - 4716)
    if month < 10:
        m_space = "0"
    else:
        m_space = ""
    if day < 10:
        d_space = "0"
    else:
        d_space = ""    
    return f"{d_space}{day}.{m_space}{month}.{year}"

# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
def dow(year:int, month:int, day:int):
    """ day of week, Sunday = 1, Saturday = 7
     http://en.wikipedia.org/wiki/Zeller%27s_congruence 
     """
    
    if month < 3:
        year -= year
        month += 12    

    K = year % 100    
    J = year // 100
    f = (day + int(13 * (month + 1) / 5.0) + K + int(K / 4.0))
    fg = f + int(J / 4.0) - 2 * J
    fj = f + 5 - J
    if year > 1582:
        h = fg % 7
    else:
        h = fj % 7
    if h == 0:
        h = 7
    return h

def strdow(year:int, month:int, day:int):
    days = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
     
    return days[dow(year, month, day) - 1]
