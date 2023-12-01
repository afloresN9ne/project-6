"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    #takes care of case where control_dist_km is larger then the brevet distance
    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km
    #holds times
    total_hrs = 0
    total_mins = 0
    
    #loop
    tf = True
    while (tf):
        # case brevet = 200
        if control_dist_km <= 200 and control_dist_km <= brevet_dist_km * 1.2:
            
            #calculates hr and decimal which will be turn to mins
            hr, total = control_dist_km // 34, control_dist_km / 34
            mins = ((total - hr) * 60)
            
            #adds time calculated to overall time 
            total_hrs +=hr
            total_mins +=mins
            
            #ends looping
            tf = False

        elif control_dist_km <= 400 and control_dist_km <= brevet_dist_km * 1.2:
            
            #calculates based of a range of 0-200 as the first 200 km will use the previous calculations 
            range_control = control_dist_km - 200
            
            hr, total = range_control // 32, range_control / 32
            mins = ((total - hr )* 60)
            
            total_hrs +=hr
            total_mins  +=mins


            #creates new control for next calculation
            control_dist_km -= range_control

        elif control_dist_km <= 600 and control_dist_km <= brevet_dist_km * 1.2:
            range_control = control_dist_km - 400
            hr, total = range_control // 30, range_control / 30
            mins = ((total - hr)* 60)

            
            total_hrs +=hr
            total_mins +=mins
            control_dist_km -= range_control

        elif control_dist_km <= 1000 and control_dist_km <= brevet_dist_km * 1.2:
            range_control = control_dist_km - 600
            hr, total = range_control // 28, range_control / 28
            mins = ((total - hr) * 60)

            total_hrs +=hr
            total_mins +=mins
            control_dist_km -= range_control
    
    #special casee for open time  
    if control_dist_km == brevet_dist_km and control_dist_km == 200:
        hr = 5
        mins = 53
    elif control_dist_km == brevet_dist_km and control_dist_km == 300:
        hr = 9
        mins = 0
    elif control_dist_km == brevet_dist_km and control_dist_km == 400:
        hr = 12
        mins = 8
    elif control_dist_km == brevet_dist_km and control_dist_km == 600:
        hr = 6
        mins = 48

    elif control_dist_km == brevet_dist_km and control_dist_km == 1000:
        hr = 33
        mins = 5

    #rounds minutes to whole number creates arrow object and then shifts it by the time calculated by the algorithm
    rounded_mins = round(total_mins)
    opn_time = arrow.get(brevet_start_time)
    opn = opn_time.shift(hours=total_hrs,minutes=rounded_mins)
    
    

    return opn


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    #takes care of case where control_dist_km is larger then the brevet distance
    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km
              
    #cases
    if control_dist_km <=60:
        hr ,total = 1 + control_dist_km // 20, 1+ control_dist_km / 20
        mins = (total -hr) *60 
    
    elif control_dist_km <= 200:
        hr, total = control_dist_km // 15, control_dist_km / 15
        mins = ((total-hr) * 60 )
        

    elif control_dist_km <= 300:
        hr, total = control_dist_km // 15, control_dist_km / 15
        mins =  ((total-hr) * 60)

    elif control_dist_km <= 400:
        hr, total = control_dist_km // 15, control_dist_km / 15
        mins = ((total-hr) * 60)

    elif control_dist_km <= 600:
        hr, total = control_dist_km // 15, control_dist_km / 15
        mins = ((total-hr) * 60)

    elif control_dist_km <= 1000:
        hr, total = control_dist_km // 15, control_dist_km / 15
        mins = ((total-hr) * 60)


    #special cases
    if control_dist_km == brevet_dist_km and control_dist_km == 200:
        hr = 13
        mins = 30
    elif control_dist_km == brevet_dist_km and control_dist_km == 400:
        hr = 27
        mins = 0
    elif control_dist_km == brevet_dist_km and control_dist_km == 1000:
        hr = 75
        mins = 0

     
    #rounds and shifts arrow object
    rounded_mins = round(mins)
    close_time = arrow.get(brevet_start_time)
    
    
    close = close_time.shift(hours=hr,minutes=rounded_mins)
    
    
    """
    close time should use the slowest speed.
    """

    return close
