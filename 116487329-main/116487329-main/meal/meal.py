def main(time):
    # time = input("prompt")
    time = time.strip()
    # time = time[0] + time[1]
    if (time[0] + time[1]) == "12" or time == "13:00":
        print("lunch time")
    if (time[0] + time[1]) == "18" or time == "19:00":
        print("dinner time")
    # time = time[0]
    if time[0] == "7" or time == "8:00":
        print("breakfast time")



def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    time = input("prompt")
    main(time)