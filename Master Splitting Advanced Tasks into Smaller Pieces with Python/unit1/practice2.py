'''

There is a school hosting an online programming competition. Each problem is assigned a unique level of difficulty. Every time a student successfully solves a problem, their score is updated based on the problem's difficulty level. However, if a student makes an unsuccessful attempt, they incur a penalty. The competition logs every action of each student in a string.

Your task is to create a Python function named analyze_competition(). It will take a string of logs as input and output a list of tuples, representing the students' score, the number of successful attempts, and the total penalties. The tuples should be sorted by the decreasing order of scores of their respective students. It is guaranteed that there will be no students with the same positive score. Don't include students in the output who haven't solved any problem.

For example, if you have logs like this:
"1 solve 09:00 50, 2 solve 10:00 60, 1 fail 11:00, 3 solve 13:00 40, 2 fail 14:00, 3 solve 15:00 70",
your function should return: [(3, 110, 2, 0), (2, 60, 1, 1), (1, 50, 1, 1)].

All log entries are separated by a comma and a space. It is guaranteed that the log entries are sorted in chronological order.

'''

def analyze_competition(logs) :
# {
    # TODO: implement the function
    l_gs = logs.split(", ")
    d_logs = {} # dict logs
    l_logs = [] # list logs
    result = []

    for l in l_gs :
    # {
        log_id = int(l.split(' ')[0])
        log_solvefail = l.split(' ')[1]
        log_time = l.split(' ')[2]

        if(log_solvefail == "solve") :
        # {
            log_score = int(l.split(' ')[3])

            try :
            # {
                d_logs[log_id] is None # test is log_id recorded

                d_logs[log_id] = {"total_score" : d_logs[log_id]["total_score"] + log_score,
                                "total_pass" : d_logs[log_id]["total_pass"] + 1,
                                "total_penalty" : d_logs[log_id]["total_penalty"],
                                "time" : log_time
                                }
            # }

            except KeyError :
            # {
                d_logs[log_id] = {"total_score" : log_score,
                                "total_pass" : 1,
                                "total_penalty" : 0,
                                "time" : log_time
                                }
            # }
            
        # }

        elif (log_solvefail == "fail") :
        # {
            try :
            # {
                d_logs[log_id] is None # test is log_id recorded

                d_logs[log_id] = {"total_score" : d_logs[log_id]["total_score"],
                                "total_pass" : d_logs[log_id]["total_pass"],
                                "total_penalty" : d_logs[log_id]["total_penalty"] + 1,
                                "time" : log_time
                                }
                
            # }

            except KeyError :
            # {
                d_logs[log_id] = {"total_score" : 0,
                                "total_pass" : 0,
                                "total_penalty" : 1,
                                "time" : log_time
                                }
            # }

        # }

        else :
        # {
            None
        # }

    # }

    for key, val in d_logs.items() :
    # {
        if (val["total_pass"] > 0) :
        # {
            l_logs.append((key, val["total_score"], val["total_pass"], val["total_penalty"], val["time"]))
        # }

        else :
        # {
            None
        # }

    # }

    l_logs = sorted(l_logs, key = lambda x : x[1] * -1)

    for l in l_logs :
    # {
        result.append((l[0], l[1], l[2], l[3]))
    # }

    return result
# }

logs = "1 solve 09:00 50, 2 solve 10:00 60, 1 fail 11:00, 3 solve 13:00 40, 2 fail 14:00, 3 solve 15:00 70"
print(analyze_competition(logs))

# should return: [(3, 110, 2, 0), (2, 60, 1, 1), (1, 50, 1, 1)]

'''

***** BONEYARD *****

    max_time = "00:00"

    # tmp = (key, value)
        # print(key, val["total_score"])
        # if (l_logs[0][4])
        
        # print(l_logs[0][4])
    # print(d_logs.values()[3])
    # print(dict(sorted(d_logs.items(), key = lambda x: x[1])))

# print(log_id, log_score, log_time)

            
student_scores = {'Alex': 88, 'Ben': 75, 'Cyrus': 93, 'Denver': 85}
sorted_by_values = dict(sorted(student_scores.items(), key=lambda item: item[1]))
print(sorted_by_values)



# d_logs[log_id] = {"total_penalty" : d_logs[log_id]["total_penalty"] + 1 }
            None

            # print("#")
            
        # print(log_id)

            # d_logs[log_id] = {"total_score" : 0,
            #                   "total_pass" : 0
            #                  }

            # d_logs[log_id] = d_logs[log_id].get("total_score", 0) + 1

            # d_logs[log_id] = {"total_score" : d_logs[log_id]["total_score"] + log_score,
            #                        "total_pass" : d_logs[log_id]["total_pass"] + 1

data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        }
    }
}

# Accessing the user's name (key exists)
name = data.get("user", {}).get("profile", {}).get("name", "Unknown")
print(f"Name: {name}")

# Attempting to access a non-existent key (e.g., "address")
address = data.get("user", {}).get("contact", {}).get("address", "N/A")
print(f"Address: {address}")


        # log_penalty = 0


        # 

# d_logs[tmp] = d_emails.get(tmp, 0) + 1

{
                    "book1" : {
                                "title" : "title1",
                                "author" : "author1",
                                "year_published" : 2001
                                }, 

'''