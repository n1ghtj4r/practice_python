distance_mi = 0
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif distance_mi <= 1 and is_raining != True:
    print('True')
elif distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == True:
    print('True')
elif distance_mi > 6 and (has_ride_share_app == True or has_car == True):
    print('True')
else:
    print('False')