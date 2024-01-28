import sys

def cat_visit_log(cat_records):
    # Check if a command line argument is provided
    if not cat_records:
        sys.exit("Missing Command Line Argument!")

    try:
        # Read the content of the log file
        with open(cat_records, "r") as log_file:
            file_lines = log_file.readlines()

    except FileNotFoundError:
        # Handle file not found error
        sys.exit(f"Can't Open File!: {cat_records}")

    # Initialize variables to keep track of statistics
    our_cat_visits = 0
    other_cats_doused = 0
    total_minutes = 0
    shortest_visit_time = float('inf')
    longest_visit_time = 0

    # Process each line in the log file
    for line in file_lines:
        if not line.strip():
            continue
        # Exit loop when encountering 'END'
        if line.strip() == "END":
            break

        try:
            # Split each line into event, entry time, and exit time
            event, entry_time, exit_time = line.strip().split(",")
            entry_time, exit_time = int(entry_time),int(exit_time)

            # Calculate the duration of the visit in minutes
            duration = exit_time - entry_time

            # Update statistics based on the event
            if event == "OURS":
                our_cat_visits += 1
                 # Update total visit duration and track shortest and longest visits
                total_minutes += duration
                shortest_visit_time = min(shortest_visit_time, duration)
                longest_visit_time = max(longest_visit_time, duration)
                # Calculate average visit duration by our cat
                average_visit_duration = total_minutes // our_cat_visits if our_cat_visits else 0
            else:
                other_cats_doused += 1

        except ValueError:
            # Handle invalid format error
            print(f"Error: Invalid Format. {line}")

    # Calculate hours and remaining minutes from total visit duration
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    

    # Print the log file analysis results
    print("*****************")
    print("Log File Analysis")
    print("*****************")
    print(f"Our Cat Visits: {our_cat_visits}")
    print(f"Intruding Cats Doused With Water: {other_cats_doused}")
    print(f"Total Time in House: {hours} Hours, {remaining_minutes} Minutes")
    print(f"Average Visit Length By Our Cat: {average_visit_duration} Minutes")
    print(f"Longest Visit Length: {longest_visit_time} Minutes")
    print(f"Shortest Visit Length: {shortest_visit_time} Minutes")

# Run the log analysis with the provided command line argument
cat_visit_log(sys.argv[1] if len(sys.argv) > 1 else "")
