
def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

import rjdate
#print (is_leap(2020))
#print(format_name("rOLF", "JAHNEL"))

#m_year = int(input("Give a year (nnnn): "))
#m_month = int(input("Gibe a month :"))
#print (f"It has {days_in_month(m_month, m_year)} days.")

print(rjdate.julian_day(1582, 10, 15))
print(rjdate.gregorian_date(2299160.5+20))
print(rjdate.strdow(1998, 4, 14))
