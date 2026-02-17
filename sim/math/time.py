from datetime import datetime


def calculate_julian_date(date: datetime):
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second

    julian_date = (1_721_013.5 + 367*year -
                   int((7/4)*(year + int((month + 9)/12)) +
                    int((275*month)/9) + day +
                    (60*hour + minute + (second/60))/1440))
    return julian_date


def calculate_gmst_angle(date: datetime):
    hour = date.hour
    minute = date.minute
    second = date.second

    julian_date = calculate_julian_date(date)

    # calculate centuries since J2000
    T0 = (julian_date - 2_451_545)/36_525

    gmst_angle = (24_110.54841 + 8_640_184.812866*T0 + 0.093104*(T0**2) -
                  (6.2*(10**-6))*T0**3 +
                  1.002737909350795*(3600*hour + 60*minute + second))
    return gmst_angle
