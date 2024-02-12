import datetime
import sys
import inflect


def main():
    year, month, day = get_birth()
    total_minutes = date_to_minutes(year, month, day)
    print(make_sentence(total_minutes) + " minutes")


def get_birth():
    try:
        y, m, d = input("Date of Birth: ").strip().split("-")
        if int(m) < 0 or int(m) > 12 or int(d) < 0 or int(d) > 31:
            raise Exception
    except Exception:
        sys.exit("Usage: YYYY-MM-DD")
    return int(y), int(m), int(d)


def date_to_minutes(y, m, d):
    birth = datetime.datetime(y, m, d)
    now_y, now_m, now_d = str(datetime.datetime.now()).split()[0].split("-")
    now = datetime.datetime(int(now_y), int(now_m), int(now_d))
    return int(str((now - birth)).split()[0]) * 24 * 60


def make_sentence(min):
    infl = inflect.engine()
    return infl.number_to_words(min, andword="").capitalize()


if __name__ == "__main__":
    main()
