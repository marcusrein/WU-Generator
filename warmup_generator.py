#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 06:31:13 2020

@author: MarcusMBP
"""
##TESTERRRR




# import fuzz
import re
from random import choice
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import exercises_dataset
import warmups_dataset

spacing = ('---------------------------')
big_spacing = ('\n---------------------------------\n')

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()


### GET THE TIME FOR YOUR WARMUP

def welcome():
    print()
    print('<<<Welcome to the Warmup Generator!>>>')
    print(big_spacing)


welcome()

### GET WARMUP TIME AVAILABLE TO USER

time_prompt = 0


def time_prompt_func():
    '''Updates the time_prompt global variable. Asks the 'how much time' question and cleans it up'''
    global time_prompt
    time_prompt_q = input('What is the max amount of minutes you can warmup today?\n>>>')
    re.sub('[abcdefghijklmnopqrstuvwzyz: ]', '', time_prompt_q)
    time_prompt_q = re.sub('[abcdefghijklmnopqrstuvwzyz: ]', '', time_prompt_q)
    if time_prompt_q.isdigit():
        time_prompt = int(time_prompt_q)
    else:
        print('You didn\'t enter your max minutes. Try again!')
        time_prompt_func()
    return time_prompt


time_prompt_func()
print()

### GET THE MOVEMENTS IN THE WOD

todays_wod = []

wod_prompt = (input(
    f'What is one movement is in your workout today? \n\t(Press Enter to add another movement to The Warmup '
    f'Generator) \n\t(Type \'done\' when finished\n>>>'))
print()

wod_prompt_new = ''

while wod_prompt != 'done':
    wod_prompt = wod_prompt.lower().strip()
    wod_prompt_new = wod_prompt.replace('kb', 'kettlebells')
    for j in list(exercises.keys()):
        if (fuzz.ratio(wod_prompt_new, j)) > 80:
            todays_wod.append(j)
            # elif (fuzz.ratio(wod_prompt,j)) < 80 and (fuzz.ratio(wod_prompt,j)) > 50:
        #     possible_misspelled.append(wod_prompt)
        # TO USE THIS I"LL HAVE TO MAKE THIS WHOLE THING A FUNCTION. DONT WANNA DO TAHT NOW



    wod_prompt = input(
        'Please enter another movement in your workout...\n\t(Press Enter to add another movement to The Warmup '
        'Generator) \n\t(Type \'done\' when finished) \n>>>')
    print()

print()
print(f'The movements in todays wod are {todays_wod}')
print()
print(spacing)
print()


### CHECK IF THERES ENOUGH TIME TO WWARMUP FOR LOADED MOVEMENTS:

def loaded_time_checker():
    for i in todays_wod:
        for k, v in exercises.items():
            if i == k:
                if v['loaded'] == 'kb' and time_prompt <= 5:
                    print('Theres not enough time to safely warmup for your kettlebell lift. Please enter 5min or more.')
                    time_prompt_func()
                    loaded_time_checker()
                if v['loaded'] == 'barbell' and time_prompt <= 10:
                    print('Theres not enough time to safely warmup for your barbell lift. Please enter 10min or more.')
                    time_prompt_func()
                    loaded_time_checker()

loaded_time_checker()

### Check if theres enough time to warmup for bodyweight movements

def unloaded_time_checker():
    if time_prompt < 5:
        print()
        print('More than 5min is recommended for your workout.')
        print()
        time_prompt_func()


unloaded_time_checker()

## FIGURE OUT WHICH MOVEMENT WILL BE THE FOCUS OF THE WOD:


focus_of_wod = []


def what_focus():
    '''Asks user what their focus of the workout will be'''
    focus = input(
        f'Of your inputted movements: ({todays_wod}), which one movement would you like to warm up the most thoroughly?\n>>>')
    for j in list(exercises.keys()):
        if (fuzz.ratio(focus, j)) > 80:
            focus_of_wod.append(j)



def check_length_of_wod():
    '''Checks is the lenght of wod is >1. If so, runs 'what focus'.'''
    if len(todays_wod) > 1:
        what_focus()
        print()
        print(f'The focus of your workout from your inputted movements {todays_wod} will be {focus_of_wod}')
    else:
        focus = todays_wod[0]
        focus_of_wod.append(focus)
    print()
    input('Press Enter to run The Warmup Generator!')


check_length_of_wod()

### IDENTIFY IF FOCUS IS LOADED OR NOT, IF TRUE, ADD 10 or 15:
print()

focus_item1 = (focus_of_wod[0])

## CHANGE THESE VARS TO BE BETTER. FUTURE UPDATE WILL HAVE A BB AND KB WARMUP OUTPUT BASED ON THE TYPE OF INPUTTED exercises. Oly lift. Strength lift. etc.
add_time = 0
added_time = False

if exercises[focus_item1]['loaded'] == 'barbell':
    add_time += 10
    added_time = True
elif exercises[focus_item1]['loaded'] == 'kb':
    add_time += 5
    added_time = True
else:
    add_time = 0
    added_time = False


### GET THE CATEGORIES OF exercises

mov_cat = []


def search_for_cat():
    '''searches the movement database to find categories of exercises'''
    for w in todays_wod:
        for k, v in exercises.items():
            if w.lower() == k.lower():
                mov_cat.append(v['category'])


    print(f'The categories of their movement are {mov_cat}')
    print()
    print(spacing)


search_for_cat()

### IDENTIFY WHICH WARMUPS COULD WORK

todays_warmups = []


def find_warmups_from_cat():
    '''Searches through 'Warmups' dataset using categories and identifies possible warmups to use'''
    for cat in mov_cat:
        for k, v in warmups.items():
            if cat in v['categories']:
                todays_warmups.append(k)

    print()
    print(f'The possible bodyweight warmups for today\'s workout are: \n{todays_warmups}')
    print()
    print(spacing)
    print()


find_warmups_from_cat()

# # ### TALLIES UP WARMUPS TO IDENTIFY WHICH WOULD BE MOST LIKELY TO WORK

tally_of_warmups = {}


def warmup_counter():
    '''Tallies warmups and puts them in an unordered dictionary called tally_of_warmups'''
    for todays_warm in todays_warmups:
        if todays_warm in tally_of_warmups:
            tally_of_warmups[todays_warm] += 1
        else:
            tally_of_warmups[todays_warm] = 1
    print('The tally of todays warmups unordered are:')
    print(tally_of_warmups)
    print()
    print(spacing)
    print()


warmup_counter()

# # ### ORDERS THE TALLY FROM HIGHEST TALLY TO LOWEST TALLY:


ordered_tally = {k: v for k, v in sorted(tally_of_warmups.items(), key=lambda item: item[1], reverse=True)}

print('The tally of todays warmups ordered are:')
print(ordered_tally)

print()
print(spacing)
print()

### Create a new dictionary of k:v pairs with the ordered talley as key and random warmup reps as value. Get those reps!


dict_of_ordered_wu_rand_reps = {}


def rand_warmup_sets_for_ordered_wu():
    global dict_of_ordered_wu_rand_reps
    list_of_ordered_tally = list(ordered_tally.keys())
    real_rand_warm_reps_list = []
    for k, v in ordered_tally.items():  ## THIS IS CORRECTLY A LIST. Vaules but too many cause it has all rep variations
        for r in warmups.keys():
            if k == r:
                get_warmup_values = warmups.get(str(k))
                get_warmup_reps = get_warmup_values.get('reps')
                rand_warmup_reps = choice(get_warmup_reps)
                real_rand_warm_reps_list.append(rand_warmup_reps)
    dict_of_ordered_wu_rand_reps = dict(zip(list_of_ordered_tally, real_rand_warm_reps_list))
    return dict_of_ordered_wu_rand_reps


rand_warmup_sets_for_ordered_wu()

# # ## ADD UP TOTAL TIME OF ORDERED TALLY

total_bw_time_list = []


def list_of_warmup_times():
    '''Lists times of selected warmups'''
    for k, v in ordered_tally.items():
        for k2, v2 in warmups.items():
            if k == k2:
                total_bw_time_list.append(v2['time'])



list_of_warmup_times()

print('The list of warmup times is:')
print(total_bw_time_list)
print()
print(spacing)

# ### ADDS UP LIST OF BW TIMES CREATED.

sum_bw_warmup_times = sum(total_bw_time_list)

print()
print('The sum of potential bodyweight warmup times found from the dataset is:')
print(sum_bw_warmup_times, 'min')
print(spacing)

####

### RANDOM WARMUP METCON GENERATOR

get_rand_warm_metcon_key = []
get_rand_warm_metcon_values = []
get_rand_warm_metcon_reps = []
random_metcon_reps = []


def get_random_metcon_warmup():
    global get_rand_warm_metcon_key
    global get_rand_warm_metcon_values
    global get_rand_warm_metcon_reps
    global get_rand_warm_metcon_time
    global random_metcon_reps
    get_rand_warm_metcon_key = random.choice(list(warmup_metcons.keys()))
    for r in warmup_metcons.keys():
        if r == get_rand_warm_metcon_key:
            get_rand_warm_metcon_values = warmup_metcons.get(str(r))
            get_rand_warm_metcon_reps = get_rand_warm_metcon_values.get('reps')
            get_rand_warm_metcon_time = get_rand_warm_metcon_values.get('time')
            random_metcon_reps = random.choice(get_rand_warm_metcon_reps)


    # return get_rand_warm_metcon_key
    # return get_rand_warm_metcon_values
    # return get_rand_warm_metcon_reps
    # return get_rand_warm_metcon_time
    # return random_metcon_reps


print()
print('The new dictionary created to find a randomly generated metcon warmup is this one:\n\n',
      dict_of_ordered_wu_rand_reps)
print()
print(spacing)


def loaded_time_adder():
    if add_time != 0:
        print()
        print(spacing)
        print()
        print(f'Now take {add_time} min to warmup your focused lift: {focus_of_wod}')
        print()


def loaded_video_adder():
    for w in focus_of_wod:
        for k, v in exercises.items():
            if w.lower() == k.lower():
                if k['categories'] == 'cleans':
                    print('yep')
                else:
                    print('nowww')




''' THIS IS THE BIG CALCULATOR AND OUTPUTTER'''


### Notice the places where everything is identical
def print_end_message():
    print()
    print(spacing)
    print()
    print('You are now warmed up for your workout! Have fun!')
    print()
    print('<<<Thank You for Using The Warmup Generator!>>>')


def print_run_warmup():
    print('Start your warmup with a 200m run.\n')
    input("Press Enter to continue...")


def print_welcome_output():
    print(
        f'<<<The Warmup Generator has Completed Processing>>>\n\nIt has created a tailored warmup for you that fits within your given time of {time_prompt} minutes\n')
    if time_prompt >= 12 and add_time == 10:
        print('The structure of your warmup will be:\n')
        print(f'1: Short metabolic warmup ({get_rand_warm_metcon_time} minutes). \n2: Bodyweight warmups ({sum(total_bw_time_list) - 3} to {sum(total_bw_time_list)} minutes).\n3: Barbell warmup for your focused lift of {focus_of_wod} (10 minutes).\n')
    elif time_prompt >= 12 and add_time == 5:
        print('The structure of your warmup will be:\n')
        print(f'1: Short metabolic warmup ({get_rand_warm_metcon_time} minutes). \n2: Bodyweight warmups ({sum(total_bw_time_list) - 3} to {sum(total_bw_time_list)} minutes).\n3: Kettlebell warmup for your focused lift of {focus_of_wod} (5 minutes).\n')
    elif time_prompt >= 12 and add_time == 0:
        print('The structure of your warmup will be:\n')
        print(f'1: Short metabolic warmup ({get_rand_warm_metcon_time} minutes). \n2: Bodyweight warmups ({sum(total_bw_time_list) - 3} to {sum(total_bw_time_list)} minutes).\n')
    else:
        print(f'1: Bodyweight warmups ({sum(total_bw_time_list) - 2} to {sum(total_bw_time_list)} minutes).\n')

    input('Press enter to begin your warmup...')


def print_bodyweight_warmups():
    n = 0
    #  {list(ordered_tally.keys())}\n')
    for k, v in dict_of_ordered_wu_rand_reps.items():
        n += 1
        print(f'Warmup', n, ': ', k.title(), 'for', v)


##Your full warmup should take {new_loaded} minutes.\n\n
##\n After you are done with your bodyweight warmup, take {add_time} minutes to warm up your {focus_of_wod}.\n')
##f'Your {get_rand_warm_metcon_key} should have taken around 1-{get_rand_warm_metcon_time} minutes.\n\n
# def print_loaded_times(new_sum_loaded, total_bw_time_list, add_time):
#     print(f'Next, lets move on to your bodyweight portion of the warmup.')


def videos_for_user():
    print()
    yn = input('Would you like videos for your bodyweight warmups? Type \'yes\' or \'no\':\n\n>>>')
    if yn.lower() == 'yes':
        for warm in dict_of_ordered_wu_rand_reps:
            for k, v in warmups.items():
                if warm == k:
                    print()
                    print(f'{warm.title()}:')
                    print(v['url'])
        print()
        input('Press Enter when done with your bodyweight warmup...')
    else:
        print()
        input('Press Enter when done with your bodyweight warmup...')


def check_time_add_wu_metcon():
    if time_prompt >= 12:
        print('Perform:',get_rand_warm_metcon_key.title(), 'for', random_metcon_reps)
        print()
        input('Press enter to move onto your bodyweight warmups...')



def loaded_video_adder():
    for w in focus_of_wod:
        for k, v in exercises.items():
            if w.lower() == k.lower():
                if v['category'] == 'cleans':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'presses':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'jerks':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'deadlifts':
                    print('Do this', w, 'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'kettlebells':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'squats':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'snatches':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                else:
                    print('nowww')


def check_pop_loaded():
    new_sum_loaded = 0
    get_random_metcon_warmup()
    if sum_bw_warmup_times + add_time + get_rand_warm_metcon_time > time_prompt:
        # print('pooo')
        dict_of_ordered_wu_rand_reps.popitem()
        total_bw_time_list.pop()
        new_sum_loaded = add_time + sum(total_bw_time_list) + get_rand_warm_metcon_time
        if new_sum_loaded >= time_prompt:
            # print('peee')
            pop_check2()
        else:
            print_welcome_output()
            # print('jeez')
            check_time_add_wu_metcon()
            print(big_spacing)
            # print_loaded_times(new_sum_loaded, total_bw_time_list, add_time)
            print_bodyweight_warmups()
            videos_for_user()
            loaded_time_adder()
            loaded_video_adder()
            print_end_message()
    else:
        # print('fart')
        new_sum_loaded = add_time + sum(total_bw_time_list)
        print_welcome_output()
        check_time_add_wu_metcon()
        print(big_spacing)
        # print_loaded_times(new_sum_loaded, total_bw_time_list, add_time)
        print_bodyweight_warmups()
        videos_for_user()
        loaded_time_adder()
        loaded_video_adder()
        print_end_message()


def check_pop_unloaded():
    new_sum_unloaded = 0
    get_random_metcon_warmup()
    if sum_bw_warmup_times > time_prompt:
        # print('pyeeasdf')
        dict_of_ordered_wu_rand_reps.popitem()
        total_bw_time_list.pop()
        new_sum_unloaded = sum(total_bw_time_list)
        if new_sum_unloaded >= time_prompt:
            # print('seeeee')
            pop_check2()
        else:
            # print('doooo')
            new_sum_unloaded = sum(total_bw_time_list)
            print_welcome_output()
            check_time_add_wu_metcon()
            print(big_spacing)
            print_bodyweight_warmups()
            videos_for_user()
            print_end_message()
    else:
        # print('yaaak')
        new_sum_unloaded = sum(total_bw_time_list)
        print_welcome_output()
        check_time_add_wu_metcon()
        print(big_spacing)
        print_bodyweight_warmups()
        videos_for_user()
        print_end_message()


def pop_check2():
    if added_time == True:
        check_pop_loaded()
    else:
        check_pop_unloaded()


pop_check2()
