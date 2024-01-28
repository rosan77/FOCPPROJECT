import sys

def analyze_log(filename):
    """Analyzes the cat shelter log file and prints the required statistics."""

    try:
        with open(filename, 'r') as file:
            our_cat_visits = 0
            intruders_doused = 0
            total_time_in_house = 0
            visit_durations = []

            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace

                if line == "END":  # Skip the "END" marker
                    continue

                try:
                    cat_type, entry_time, exit_time = line.split(',')
                    entry_time, exit_time = int(entry_time), int(exit_time)

                    if cat_type == 'OURS':
                        our_cat_visits += 1
                        visit_duration = exit_time - entry_time
                        total_time_in_house += visit_duration
                        visit_durations.append(visit_duration)
                    else:
                        intruders_doused += 1

                except ValueError:
                    print(f"Invalid line format: {line}")  # Log error for invalid lines

            # Calculate average, longest, and shortest visit durations
            if visit_durations:
                average_visit = sum(visit_durations) / len(visit_durations)
                longest_visit = max(visit_durations)
                shortest_visit = min(visit_durations)
            else:
                average_visit = longest_visit = shortest_visit = 0

            # Format total time in hours and minutes
            hours = total_time_in_house // 60
            minutes = total_time_in_house % 60

            print("\nLog File Analysis\n==================")
            print(f"Cat Visits: {our_cat_visits}")
            print(f"Other Cats: {intruders_doused}")
            print(f"Total Time in House: {hours} Hours, {minutes} Minutes")
            print(f"Average Visit Length: {average_visit} Minutes")
            print(f"Longest Visit: {longest_visit} Minutes")
            print(f"Shortest Visit: {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f"Cannot open {filename}!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        filename = sys.argv[1]
        analyze_log(filename)
