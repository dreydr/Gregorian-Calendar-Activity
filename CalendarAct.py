class Calendar:
    def __init__(self):
        self.events = {}

    def is_leap_year(self, year):
        return year % 4 == 0

    def get_days_in_month(self, month, year):
        match month:
            case 1:
                return 31
            case 2:
                if self.is_leap_year(year):
                    return 29
                else:
                    return 28
            case 3:
                return 31
            case 4:
                return 30
            case 5:
                return 31
            case 6:
                return 30
            case 7:
                return 31
            case 8:
                return 31
            case 9:
                return 30
            case 10:
                return 31
            case 11:
                return 30
            case 12:
                return 31
            case _:
                return -1

    def get_month_name(self, month):
        match month:
            case 1:
                return "January"
            case 2:
                return "February"
            case 3:
                return "March"
            case 4:
                return "April"
            case 5:
                return "May"
            case 6:
                return "June"
            case 7:
                return "July"
            case 8:
                return "August"
            case 9:
                return "September"
            case 10:
                return "October"
            case 11:
                return "November"
            case 12:
                return "December"
            case _:
                return "Unknown"\

    def is_valid_date(self, day, month, year):
        if year < 2026 or year > 2028:
            print("[ERROR] Year must be between 2026 and 2028 only!")
            return False

        if month < 1 or month > 12:
            print("[ERROR] Month must be between 1 and 12 only!")
            return False

        max_days = self.get_days_in_month(month, year)
        if day < 1 or day > max_days:
            print(f"[ERROR] Day must be between 1 and {max_days} for {self.get_month_name(month)} {year}!")
            return False

        return True

    def make_date_key(self, day, month, year):
        return f"{year}-{month:02d}-{day:02d}"

    def add_event(self, day, month, year, event_name):
        key = self.make_date_key(day, month, year)

        if key in self.events:
            self.events[key].append(event_name)
        else:
            self.events[key] = [event_name]

        print(f"\n[SUCCESS] Event '{event_name}' added on {self.get_month_name(month)} {day}, {year}!")

    def view_events_on_date(self, day, month, year):
        key = self.make_date_key(day, month, year)
        if key in self.events:
            print(f"\nEvents on {key}:")
            for event in self.events[key]:
                print(f"- {event}")
        else:
            print("\nNo events found on this date.")

    def view_all_events(self):
        if not self.events:
            print("\nNo events available.")
            return

        print("\nAll Events:")
        for date, events in self.events.items():
            print(f"{date}:")
            for event in events:
                print(f"  - {event}")

    def delete_event(self, day, month, year, event_name):
        key = self.make_date_key(day, month, year)

        if key in self.events and event_name in self.events[key]:
            self.events[key].remove(event_name)
            print("\n[SUCCESS] Event deleted.")
        else:
            print("\n[ERROR] Event not found.")


def main():
    calendar = Calendar()

    while True:
        print("\n---- MAIN MENU ----")
        print("1. Add an Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Delete an Event")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- ADD AN EVENT ---")
            try:
                year = int(input("Year (2026-2028): "))
                month = int(input("Month (1-12): "))
                day = int(input("Day: "))
            except ValueError:
                print("[ERROR] Please enter valid numbers.")
                continue

            if not calendar.is_valid_date(day, month, year):
                continue

            event_name = input("Enter event name: ")
            calendar.add_event(day, month, year, event_name)

        elif choice == "2":
            try:
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
            except ValueError:
                print("[ERROR] Invalid input.")
                continue

            calendar.view_events_on_date(day, month, year)

        elif choice == "3":
            calendar.view_all_events()

        elif choice == "4":
            try:
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
            except ValueError:
                print("[ERROR] Invalid input.")
                continue

            event_name = input("Enter event name to delete: ")
            calendar.delete_event(day, month, year, event_name)

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("[ERROR] Invalid choice.")


if __name__ == "__main__":
    main()