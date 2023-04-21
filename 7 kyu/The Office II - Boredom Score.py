#Every now and then people in the office moves teams or departments. Depending what people are doing with their time they can become more or less boring. Time to assess the current team.
#You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.
def boredom(staff):
    bored_object = {
        "accounts" : 1,
        "finance" : 2,
        "canteen" : 10,
        "regulation" : 3,
        "trading" : 6,
        "change" : 6,
        "IS" : 8,
        "retail" : 5,
        "cleaning" : 4,
        "pissing about" : 25}
    boring_score = sum(bored_object[job] for job in staff.values())
    if boring_score <= 80:
        sentiment_for_return = 'kill me now'
    elif 80 < boring_score < 100:
        sentiment_for_return = 'i can handle this'
    else:
        sentiment_for_return = 'party time!!'
    return  sentiment_for_return    