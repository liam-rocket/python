def convert_secs_to_hours(time_in_seconds):
    seconds_per_minute = 60
    minutes_per_hour = 60
    time_in_minutes = time_in_seconds / seconds_per_minute
    time_in_hours = time_in_minutes / minutes_per_hour
    return time_in_hours

def calc_years_to_hug_all_hk_people(hug_duration_preference):
    # set variables for the fixed values you will be referring to
    hours_in_a_day = 24
    non_hugging_hours = 9

    # population size is approx 7 mil people
    population_size = 7000000
    days_in_a_year = 365
    
    # calculate the number of hours each day that are available for hugging
    hours_per_day_for_hugging = hours_in_a_day - non_hugging_hours

    # convert the users hug_duration_preference from seconds to hours
    hug_duration_preference = convert_secs_to_hours(hug_duration_preference)

    # calculate how many hugs you can give during the hugging hours
    max_hug_given_per_day = hours_per_day_for_hugging / hug_duration_preference

    # culculate how long it would take to pug the population
    days_taken_for_hug_population = population_size / max_hug_given_per_day

    # convert answers to years
    years_to_hug_population = days_taken_for_hug_population / days_in_a_year

    # return years_to_hug_population to 2 decimal place
    return round(years_to_hug_population, 2)

def main(input):
    years_to_hug_all_hk_people = calc_years_to_hug_all_hk_people(input)
    output = "It will take ${years} yrs to hug all Sgpeans if your preferred hug duration is ${input} secs".format(years=years_to_hug_all_hk_people, input=input )
    return output

# Well done ! Don't foreget to give yourself a hug too !

convert_secs_to_hours(30)