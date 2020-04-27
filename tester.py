##
##
##
import exercises_dataset
import warmups_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

spacing = '----------------------------'

##working on this 7:08am 4/25

# 'bear crawls' : {
#     'categories': ['snatches', 'cleans','deadlifts','presses','gymanstics upper','gymnastics lower', 'kettlebells'],
#     'time': 2,
#     'reps': '2 min',
#     'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',

#
# 'clean': {
#     'category': 'cleans',
#     'intensity': 'high',
#     'loaded': 'barbell'
# },

### THIS WORKS TO PRINT A VIDEO
focus_of_wod = ['floor press']

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
                elif v['category'] == 'cleans':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                elif v['category'] == 'snatches':
                    print('Do this',w,'warmup:')
                    print(v['reg_warm'])
                else:
                    print('nowww')

loaded_video_adder()
print()
# for k,v in exercises.items():
#     exercises[k]['reg_warm'] = 'https://www.youtube.com/watch?v=pCEpcIo-O4I'
#
# print(exercises)
