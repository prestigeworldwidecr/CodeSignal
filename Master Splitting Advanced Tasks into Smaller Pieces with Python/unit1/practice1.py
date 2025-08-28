'''

Imagine you have a large mailbox that receives emails from various sources and you need to organize these emails. Your task involves implementing a Python function named organize_inbox(). This function will accept a string of emails as input and output a list of tuples. Each tuple contains two elements: the sender's email address and the total count of emails received from this sender.

Each email is represented by various metadata separated by commas, such as "Sender Email Address, Subject, Timestamp". The total string comprises these entries, separated by semicolons. Emails originate from distinct senders and can occur at any timestamp in the "HH:MM" format within a 24-hour range.

Here is the format of the string: "Sender Email Address1, Subject1, 09:00; Sender Email Address2, Subject2, 10:00; Sender Email Address1, Subject3, 12:00"

The function should return: [("Sender Email Address1", 2), ("Sender Email Address2", 1)].

For each input entry, the sender's email is a string containing up to 
20
20 characters. The timestamp follows the "HH:MM" format. The total number of email entries varies from 
1
1 to 
500
500, inclusive.

Your function must extract the sender's email address and count the number of emails received from each sender, outputting a list of tuples. Each tuple should contain the sender's email address, followed by the count of emails received from them. The tuples should be sorted by the descending order of these counts. If two senders have sent the same number of emails, the tuples should be listed in ascending order based on the senders' email addresses.

The sender's email address is always followed by a comma, a space, and the start of the subject line. The subject line is always followed by a comma, a space, and the timestamp. All emails are unique, meaning there will be no emails with the same subject and timestamp from the same sender.

'''

def organize_inbox(inbox_string) :
# {
    ## TODO: Implement this function
    i_s = inbox_string.split('; ')
    d_emails = {} # dict emails
    l_emails = [] # list emails

    for i in i_s :
    # {
        tmp = i.split(',')[0]
        d_emails[tmp] = d_emails.get(tmp, 0) + 1
    # }

    for key, value in d_emails.items() :
    # {
        # tmp = (key, value)
        # print(tmp)
        l_emails.append((key, value))
    # }

    # sorted_data = sorted(data, key=lambda x: (x[1], x[2]))

    return sorted(l_emails, key = lambda x: (x[1] * -1, x[0]))

# }

emails = "Sender Email Address1, Subject1, 09:00; Sender Email Address2, Subject2, 10:00; Sender Email Address1, Subject3, 12:00"

print(organize_inbox(emails))

# The function should return: [("Sender Email Address1", 2), ("Sender Email Address2", 1)].

'''

***** BONEYARD *****

# print(type(inbox_string))
    # for 
    # print(tmp[0], len(tmp[0]), str(tmp).split(',')[0].replace('[', ''))
    # for ()
    # print(len(tmp))

for book in returned_books :
# {
    # TODO: Update book_counts with the right counts for each book
    book_counts[book] = book_counts.get(book, 0) + 1
# }    

# print(t.split(',')[0])

'''