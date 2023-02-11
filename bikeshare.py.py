
# this is the beginning of the bikeshare project code
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

included_cities=['chicago','new york city','washington']
included_months=['january', 'february', 'march', 'april', 'may', 'june','all']
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    while True:                                                                         # user input for city, month and day
        city=input('Out of chicago, new york city,and washington, which city would you like to see data of?\n>').lower()
        if city not in included_cities:
            print('Informathion for what you entered is unavailable. Please choose from chicago, new york city, or washington')
        else:
            break

    while True:
        month=input('Out of january, ...june, which month do you want? or all these months?\n>').lower()
        if month not in included_months:
            print('Informathion for what you entered is unavailable. Please choose from  january, february, march, april, may, june or all')
        else:
            break

    while True:
        day=input('Out of the days of the week, which day do you want (monday, tuesday, ..sunday)?\n>').lower()
        if day not in days:
            print('Informathion for what you entered is unavailable. Please choose from sunday, ... friday, saturday or all')
        else:
            break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):                                                        #loading the data for the city, month and day
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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):                                                            #most common month, day and start hr statistics
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("most common month: \n{}\n".format(df['month'].mode()[0]))
    print("most common day of the week:\n{}\n".format(df['day_of_week'].mode()[0]))
    print("most common start hour:\n{}\n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):                      #3, most commonly used start station, end station and frequent combination of both

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_startstation = df['Start Station'].mode()[0]
    print('most commonly used start station:', common_startstation)

    common_endstation=df['End Station'].mode()[0]
    print('most commonly used start end station:', common_endstation)

    trip_combination=df.groupby(['Start Station','End Station'])
    print('most frequent combination of start station and end station trip:\n{}\n'.format(trip_combination.size().sort_values(ascending=False).head(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):                                                          # total and mean of trip durations
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time)

    travel_time_mean = df['Trip Duration'].mean()
    print('mean travel time:', travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city):                                                              #counts of user types and gender
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print(user_types)


    if city != 'washington':
       gender = df['Gender'].value_counts()
       print('gender count =', gender)



    if city != 'washington':                                            #earliest, most recent and most common birthyear
       most_recent_birth_year = df['Birth Year'].max()
       earliest_birth_year = df['Birth Year'].min()
       most_common_birth_year = df['Birth Year'].mode()[0]
       print('Earliest birth from the fitered data is: {}\n'.format(earliest_birth_year))
       print('Most recent birth from the fitered data is: {}\n'.format(most_recent_birth_year))
       print('Most common birth from the fitered data is: {}\n'.format(most_common_birth_year))


       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)


def display_data(df):
    print(df.head())

    start_loc = 0
    while True:
       view_data = input('\nWould you like to view next five rows of raw data? Choose by entering yes or no.\n')
       if view_data.lower() != 'yes':
           return

       start_loc = start_loc + 5
       print(df.iloc[start_loc:start_loc+5])



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
