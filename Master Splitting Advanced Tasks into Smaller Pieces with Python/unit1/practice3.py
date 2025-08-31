'''

You are provided with log data from a library's digital system, stored in string format. The log represents books' borrowing activities, including the book ID and the time a book is borrowed and returned. The structure of a log entry is as follows: <book_id> borrow <time>, <book_id> return <time>.

The time is given in the HH:MM 24-hour format, and the book ID is a positive integer between 1 and 500. The logs are separated by a comma, followed by a space (", ").

Your task is to create a Python function named solution(). This function will take as input a string of logs and output a list of tuples representing the books with the longest borrowed duration. Each tuple contains two items: the book ID and the book's borrowed duration. By 'borrowed duration,' we mean the period from when the book was borrowed until it was returned. If a book has been borrowed and returned multiple times, the borrowed duration is the total cumulative sum of those durations. If multiple books share the same longest borrowed duration, the function should return all such books in ascending order of their IDs.

For example, if we have a log string as follows: "1 borrow 09:00, 2 borrow 10:00, 1 return 12:00, 3 borrow 13:00, 2 return 15:00, 3 return 16:00",
the function will return: [(2, '05:00')].

Note: You can safely assume that all borrowing actions for a given book will have a corresponding return action in the log, and vice versa. Also, the logs are sorted by the time of the action.

'''

from datetime import datetime, timedelta
from operator import itemgetter

def hours_minutes_to_time_delta(time) :
# {
    td = datetime.strptime(time, "%H:%M").time()
    td = timedelta(hours = td.hour, minutes = td.minute)

    return td
# }

def time_delta_to_hours_minutes(time) :
# {
    hours, remainder = divmod(time.seconds, 3600)
    minutes = (time.seconds // 60) % 60
    hm = f"{hours:02d}:{minutes:02d}"

    return hm
# }

def solution(logs) :
# {
    # TODO: your code goes here
    l_gs = logs.split(", ")
    l_logs = []
    d_logs = {}
    result = []
    max_duration = hours_minutes_to_time_delta("00:00")

    for l in l_gs :
    # {
        book_id = int(l.split(' ')[0])
        book_borrow_return = l.split(' ')[1]
        book_time = l.split(' ')[2]
        book_time = hours_minutes_to_time_delta(book_time)

        if (book_borrow_return == "borrow") :
        # {
            # try if book exists in d_logs
            try :
            # {
                d_logs[book_id] is None

                d_logs[book_id] = { "book_time" : book_time,
                                    "borrowed_duration" : d_logs[book_id]["borrowed_duration"]
                                    }
            # }

            except :
            # {
                d_logs[book_id] = { "book_time" : book_time,
                                    "borrowed_duration" : timedelta(0)
                                    }
                
                # print(type(d_logs[book_id]["borrowed_duration"]))

            # }

        # }

        elif (book_borrow_return == "return") :
        # {
            # print(book_time, d_logs[book_id]["book_time"], d_logs[book_id]["borrowed_duration"])

            d_logs[book_id] = {"book_time" : book_time,
                                "borrowed_duration" : book_time - d_logs[book_id]["book_time"] + d_logs[book_id]["borrowed_duration"]
                                }
            
            # print(type(d_logs[book_id]["borrowed_duration"]))

        # }

        else :
        # {
            None
        # }

    # }

    for key, val in d_logs.items() :
    # {
        l_logs.append((key, val["borrowed_duration"]))
        # print(type)
    # }

    max_duration = max(l_logs, key = itemgetter(1))[1]

    for l in l_logs :
    # {
        if (l[1] >= max_duration) :
        # {
            result.append((l[0], time_delta_to_hours_minutes(l[1])))
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

logs = "1 borrow 09:00, 2 borrow 10:00, 1 return 12:45, 3 borrow 13:00, 2 return 15:00, 3 return 16:00"
# [(2, '05:00')]

print(solution(logs))

'''

***** BONEYARD *****


            # print(type(d_logs[book_id]["borrowed_duration"]))

# print(type(val["borrowed_duration"]))
        
        # print(max_duration)
        # print(type(l[1]), type(max_duration))


# print(max(l_logs, lambda x: x[2]))
    # print(max_by_second_element)

# print(max(d_logs, lambda x: x[2]))

    

from operator import itemgetter

    my_list = [(1, 5), (3, 2), (2, 8)]
    max_by_second_element = max(my_list, key=itemgetter(1))
    print(max_by_second_element)

for l in l_logs :
    # {
        tmp = l[1]
        tmp = datetime.strptime(tmp, "%H:%M").time()
        tmp = timedelta(hours = tmp.hour, minutes = tmp.minute)
        print(tmp, max_duration)
        
        if (tmp >= max_duration) :
        # {
            result.append(l)
        # }

        else :
        # {
            None
        # }

    # }

# print(book_time, d_logs[book_id]["book_time"], d_logs[book_id]["borrowed_duration"])

# print(hours_minutes_to_time_delta("00:00"))

if (tmp4 >= max_duration) :
# {
    max_duration = tmp4
# }

else :
# {
    None
# }

# tmp1 = datetime.strptime(d_logs[book_id]["book_time"], "%H:%M").time()
            # tmp1 = timedelta(hours = tmp1.hour, minutes = tmp1.minute)
            # tmp2 = datetime.strptime(book_time, "%H:%M").time() 
            # tmp2 = timedelta(hours = tmp2.hour, minutes = tmp2.minute)
            # tmp3 = datetime.strptime(d_logs[book_id]["borrowed_duration"], "%H:%M").time()
            # tmp3 = timedelta(hours = tmp3.hour, minutes = tmp3.minute)
            # tmp4 = tmp2 - tmp1 + tmp3
            # hours, remainder = divmod(tmp4.seconds, 3600)
            # minutes = (tmp4.seconds // 60) % 60
            # tmp5 = f"{hours:02d}:{minutes:02d}"

# print('1', tmp4, max_duration)


        # max_duration = datetime.strptime("00:00", "%H:%M").time()
    # max_duration = timedelta(hours = max_duration.hour, minutes = max_duration.minute)
        # tmp_borrowed_duration = datetime.strptime(book_time, "%H:%M").time()
        # tmp_borrowed_duration = timedelta(hours = tmp_book_time.hour, minutes = tmp_book_time.minute)
    # max_duration = max(l_logs, key = lambda x : x[1])[1] 
    # print(l_logs)   

# "book_time" : datetime.strptime(book_time, "%H:%M").time(),
                                

# tmp4 =  str(f"{int(sum_hours):02d}:{int(sum_minutes):02d}")

hours, remainder = divmod(tmp4.total_seconds(), 3600)
            minutes, _ = divmod(remainder, 60)

            

# book_time = datetime.strptime(l.split(' ')[2], "%H:%M").time()

from datetime import timedelta

# Example: add 1 hour 30 min and 2 hours 15 min
td1 = timedelta(hours=1, minutes=30)
td2 = timedelta(hours=2, minutes=15)
total = td1 + td2  # This is a timedelta object

# To format as 'HH:MM':
hours, remainder = divmod(total.seconds, 3600)
minutes = (total.seconds // 60) % 60
result = f"{hours:02d}:{minutes:02d}"


# print("")
# print(type(b_d))
# print(type(d_logs[book_id]["borrowed_duration"]), d_logs[book_id]["borrowed_duration"])

# tmp = datetime.strptime(d_logs[book_id]["book_time"], "%H:%M").time()
# print(type(d_logs[book_id]["book_time"]))
# tmp = d_logs[book_id]["book_time"]


# print(type(book_time))

# print(tmp)

# add previous time


# sorted(l_logs, key = lambda x : x[1] * -1)




# print("h1", max_duration)
    #print(l[1] >= max_duration)


# print("20:00" + "01:45")
        # print(key, val["borrowed_duration"])

# print(logs)

            # datetime.combine(date.min,book_time) - datetime.combine(date.min,logs[book_id][book_time])
            # print(d_logs[book_id]["book_time"])
            
        # print(book_time - book_time)

        # print(l, book_id, book_time, book_borrow_return)

            # print(int(sum_hours), int(sum_minutes))

from datetime import datetime, timedelta

# Create datetime objects (you can set a dummy date if only time is relevant)
time1 = datetime.strptime("01:30", "%H:%M").time()
time2 = datetime.strptime("00:45", "%H:%M").time()

# Convert to timedelta for calculations
td1 = timedelta(hours=time1.hour, minutes=time1.minute)
td2 = timedelta(hours=time2.hour, minutes=time2.minute)

# Perform operations
sum_td = td1 + td2
difference_td = td1 - td2

# Extract hours and minutes from timedelta
sum_hours, remainder = divmod(sum_td.total_seconds(), 3600)
sum_minutes, _ = divmod(remainder, 60)

print(f"Sum using timedelta: {int(sum_hours):02d}:{int(sum_minutes):02d}")

dt1 = datetime.fromtimestamp(start_ts)
print('Datetime Start:', dt1)
dt2 = datetime.fromtimestamp(end_ts)
print('Datetime End:', dt2)

# Difference between two timestamps
# in hours:minutes:seconds format
delta = dt2 - dt1
print('Difference is:', delta)

# start time and end time
start_time = datetime.strptime("2:13:57", "%H:%M:%S")
end_time = datetime.strptime("11:46:38", "%H:%M:%S")

# get difference
delta = end_time - start_time

sec = delta.total_seconds()
print('difference in seconds:', sec)

min = sec / 60
print('difference in minutes:', min)

# get difference in hours
hours = sec / (60 * 60)
print('difference in hours:', hours)

print(datetime.combine(date.min, end) - datetime.combine(date.min, start))

'''