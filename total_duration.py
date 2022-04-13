durations = ["3:10:30", "1:22:23", "3:46:22", "1:14:29", "2:47:56",
             "5:00:17", "4:41:24", "1:25:37", "1:56:16", "2:46:22"]

total_hours = 0
total_minutes = 0
total_seconds = 0

for duration in durations:
    hours, minutes, seconds = duration.split(":")
    hours = int(hours
    minutes = int(minutes)
    seconds = int(seconds)
    total_hours += hours
    total_minutes += minutes
    total_seconds += seconds

print(f"{total_hours}:{total_minutes}:{total_seconds}")


def calculate_total_time(h, m, s):
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60

    return f"{h}:{m}:{s}"


total = calculate_total_time(total_hours, total_minutes, total_seconds)
print(total)
