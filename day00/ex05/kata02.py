t = (3, 30, 2019, 9, 25)

if __name__ == "__main__":
    keys = ("hour", "minutes", "year", "month", "day")
    d = {}
    for i in range(len(t)):
        d[keys[i]] = t[i]
    s = f"{d['month']:02}/{d['day']:02}/{d['year']} "
    s += f"{d['hour']:02}:{d['minutes']:02}"
    print(s)
