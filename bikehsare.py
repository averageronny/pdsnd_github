import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    options = ('chicago', 'new york city', 'washington')
    while True:
        try:
            city = input('Please enter the city you want to analyze. Possible options are Chicago, New York City and Washington: ').lower()
            if city in options:
                break
            else:
                raise ValueError
        except ValueError:
            print("That was no valid city.  Try again...")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    yesno = ('yes', 'no')
    while True:
        try:
            filter_month = input('Do you want to filter the Month? Type: Yes or No: ').lower()
            if filter_month in yesno:
                break
            else:
                raise ValueError
        except ValueError:
            print("That was no valid input.  Try again...")
            continue
    month_options = ('jan', 'feb', 'mar', 'apr', 'may', 'jun')
    if filter_month == 'yes':
        while True:
            try:
                month = input('For which month do you want to filter. Please type the first 3 letters of the month (e.g. mar): ').lower()
                if month in month_options:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That was no valid month.  Try again...")
                continue
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            filter_day = input('Do you want to filter the Day? Type: Yes or No: ').lower()
            if filter_day in yesno:
                break
            else:
                raise ValueError
        except ValueError:
            print("That was no valid input.  Try again...")
            continue
    day_options = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
    if filter_day == 'yes':
        while True:
            try:
                day = input('For which weekday do you want to filter. Please type the first three letters of the weekday (e.g. wed): ').lower()
                if day in day_options:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That was no valid weekday.  Try again...")
                continue
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if month != 'all':
        m = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6}
        month = m[month]
        df = df[df['month'] == month]
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday
    if day != 'all':
        d = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}
        day = d[day]
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    m={1: 'January', 2: 'February', 3: 'March', 4: 'April', 5:'May', 6:'June'}
    month = m[df['month'].mode()[0]]
    print('The most common month is {}.'.format(month))


    # TO DO: display the most common day of week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday
    d={0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5:'Saturday', 6:'Sunday'}
    day = d[df['day_of_week'].mode()[0]]
    print('The most common weekday is {}.'.format(day))

    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    hour = df['hour'].mode()[0]
    print('The most common hour is {} o\'clock.'.format(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination is between start station "{}" and end station "{}".'.format(combination[0], combination[-1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in minutes is {},\nin hours it is {},\nin days it would be {}\nand in years it would be {}.'.format(total_travel_time/60, total_travel_time/360, total_travel_time/8640, total_travel_time/3153600))


    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time in minutes is {}'.format(avg_travel_time/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby('User Type')['Start Time'].nunique()
    print(user_types.to_string(),'\n')


    # TO DO: Display counts of gender
    gender = df.groupby('Gender')['Start Time'].nunique()
    print(gender.to_string(),'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_by = df['Birth Year'].min()
    print('The earliest birth year is {}.'.format(int(earliest_by)))

    recent_by = df['Birth Year'].max()
    print('The most recent birth year is {}.'.format(int(recent_by)))

    most_common_by = df['Birth Year'].mode()[0]
    print('The most common birth year is {}.'.format(int(most_common_by)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_raw(df):
    while True:
        try:
            print_init = input('Do you want to print a sample? Yes or No: ').lower()
            if print_init in ('yes', 'y'):
                i = 0
                while True:
                    print(df.iloc[i:i+5])
                    i += 5
                    more_data = input('Would you like to see more data? Please enter Yes or No: ').lower()
                    if more_data not in ('yes', 'y'):
                        break
                break
            elif print_init in ('no', 'n'):
                break
            else:
                raise ValueError
        except ValueError:
            print("That was no valid input.  Try again...")
            continue
            




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        print_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
