def min_to_day(min):
    min_per_day = 24 * 60
    d = min // min_per_day
    h = (min - (d * min_per_day)) // 60
    m = min - (d * min_per_day + h * 60)
    return d,h,m

def min_to_day_dic(min):
    min_per_day = 24 * 60
    d = min // min_per_day
    h = (min - (d * min_per_day)) // 60
    m = min - (d * min_per_day + h * 60)
    return {'day':d,'hour':h,'min':m}

if __name__ == "__main__" :
    print(min_to_day(70))
    print(min_to_day_dic(90))