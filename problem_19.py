# You are given the following information, but you may prefer to do some research for yourself.
#
#  - 1 Jan 1900 was a Monday.
#  - Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#  - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#########################################################
days_in_month = [31,  28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #0 - 11
days_per_year = 365 #sum(days_in_month)

# defines
SUNDAY = 0
TUESDAY = 2
DAYS_IN_WEEK = 7
FEB = 1
FIRST_YEAR = 1901
LAST_YEAR = 2000

# counts the sundays
ans_count = 0

month_count = 0

#########################################################
def get_month():
    return (month_count % 12) + 1

#########################################################
def get_year():
    return FIRST_YEAR + (month_count / 12)

#########################################################
def is_leap_year():
    year = get_year()
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#########################################################
def get_days_in_month():
    month_id = month_count % 12
    if(month_id == FEB):
        if(is_leap_year()):
            return days_in_month[month_id] + 1
        else:
            return days_in_month[month_id]
    else:
        return days_in_month[month_id]

#########################################################
def euler_problem_19():
    global month_count
    global ans_count
    

    # initial data
    today = TUESDAY # Jan 1st, 1901    
    while(get_year() <= LAST_YEAR):
        print("checking date: %d/%d/%d" % (1, get_month(), get_year()))
        
        if(today == SUNDAY):
            ans_count += 1            
            print "\tThis is a Sunday"
            
        days = get_days_in_month()
        today  = (today + days) % DAYS_IN_WEEK
        month_count += 1
      
    print("ans: %d" %(ans_count))

euler_problem_19();
