import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new_york_city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    stop = 0
    while stop < 3:

        while stop == 0:
            city = input('which city you wanna look at : [chicago, new_york_city, washington]').lower()
            c_options = ['chicago', 'new_york_city', 'washington']
            if city.lower() not in c_options:
                print('looks like you entered wrong city name type it as shown with no extra spaces')
                continue
            else:
                stop = 1
        while stop == 1:
            month = input('which month you wanna look at : [all, january, february, ... , june]').lower()
            m_options = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            if month.lower() not in m_options:
                print('looks like you entered wrong option')
                continue
            else:
                stop = 2
        while stop == 2:
            day = input('which day of the week you wanna look at : [all, monday, tuesday, ... sunday]').lower()
            d_options = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
            if day.lower() not in d_options:
                print('looks like you entered wrong option')
                continue
            else:
                stop = 3

    print('-' * 40)
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular month :', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular day of week:', popular_day)

    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start = df['Start Station'].mode()
    print('most commonly used start station : ', com_start)
    # TO DO: display most commonly used end station
    com_end = df['End Station'].mode()
    print('most commonly used end station : ', com_end)
    # TO DO: display most frequent combination of start station and end station trip
    f_comb = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('most frequent combination of start station and end station trip :\n                   start    ------    '
          'end\n', f_comb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time : ', total_time)
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time : ', mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types :\n', user_types)
    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('counts of gender :\n', genders)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('earliest year : ', earliest)
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year of birth : ', most_common_year)
        most_recent = df['Birth Year'].max()
        print('most recent year : ', most_recent)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)
    except :
        print('!! Sorry: no gender or years data for washington !!')
def data_show(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_show(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks...')
            break


if __name__ == "__main__":
    main()
