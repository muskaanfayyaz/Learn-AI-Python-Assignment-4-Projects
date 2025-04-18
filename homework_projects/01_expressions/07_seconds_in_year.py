def main():
    # Constants for the time units
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    # Calculate the number of seconds in a year
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    
    # Print the result in a nice format
    print(f"There are {seconds_in_year} seconds in a year!")

if __name__ == '__main__':
    main()
