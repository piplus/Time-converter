def sec_to_hour(sec):
    sec_per_day = 60*60*24
    d = sec // sec_per_day
    h = (sec - (d * sec_per_day)) // 3600
    m = (sec - ((d * sec_per_day)+h*3600)) // 60
    s = sec - (d * sec_per_day + h * 3600 + m * 60)
    return d,h,m,s

print(sec_to_hour(6500))
    