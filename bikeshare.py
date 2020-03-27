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
    city = input('Please input city name. Please choose from Chicago, New York City and Washington: ').lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("City is name is invalid! Please input another name: ").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Which month would you like to display: ").lower()

    while month not in months:
        month = input("Enter valid month: ").lower()
        if month in months:
            break
        else:
            return


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input("Please input day of week: ").lower()

    while day not in days:
        day = input("Enter valid day: ").lower()
        if day in days:
            break
        else:
            return

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode().values[0]
    print('The most popular month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode().values[0]
    print('The most popular day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().values[0]
    print('The most popular hour:', popular_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode().values[0]
    print('The most commonly used start station:', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode().values[0]
    print('The most commonly used end station:', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip:\n', most_frequent_combination)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    sum_seconds = total_travel_time%60
    sum_minutes = total_travel_time//60%60
    sum_hours = total_travel_time//3600%60
    sum_days = total_travel_time//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    mean_seconds = avg_travel_time%60
    mean_minutes = avg_travel_time//60%60
    mean_hours = avg_travel_time//3600%60
    mean_days = avg_travel_time//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print('Gender counts:\n', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
        most_common_year = df['Birth Year'].mode().values[0]
        print('The most common birth year:', most_common_year)

        most_recent = df['Birth Year'].max()
        print('The most recent birth year:', most_recent)

        earliest_year = df['Birth Year'].min()
        print('The most earliest birth year:', earliest_year)


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    while True:
        raw_data = input('\nWould you like to see the raw data? Please enter yes or no.\n> ')
        if (raw_data == 'yes'):
            print (df.iloc[i:i+5])
            i+=5
        elif (raw_data == 'no'):
            break
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
