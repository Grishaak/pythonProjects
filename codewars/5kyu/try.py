def foo(lenght: int = -1):
    return [i for i in range(2, lenght, 2)]


print(foo())


def convert_to_time(time_in_sec: int) -> str:
    seconds = time_in_sec % 60
    minutes = (time_in_sec // 60) % 60
    hours = (time_in_sec // 3600) % 24
    days = (time_in_sec // (3600 * 24)) % 365
    text = ((f" {days} days" if days > 1 or days == 0 else f" {days} day")
            + (f" {hours} hours" if hours > 1 or hours == 0 else f" {hours} hour")
            + (f" {minutes} minutes" if minutes > 1 or minutes == 0 else f" {minutes} minute")
            + (f" {seconds} seconds" if seconds > 1 or seconds == 0 else f" {seconds} second"))
    return text


print(convert_to_time(12030))
