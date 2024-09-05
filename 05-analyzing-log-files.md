# Putting it all together

You are a data analyst for a bank. Your task is to analyze the logs of a banking application to figure out how top customers use your service.  
You are given a logfile that contains all the actions that customers have performed for a stretch of time.(0 - 1200)  
The log file consists of a few hundred lines having the following format:  
```
<userId>; <action>; <timestamp>
```
Unfortunately for you, the log lines have been shuffled, so they are not ordered by timestamp.  
The possible actions are:
- `logged in`
- `logged out`
- `performed a payment of X`
- `received X`
- `checked their balance`  

You have the guarantee that each user logged in and out exactly once.

Your task is to find out the following:

- how many and which users were active in the logfile you're analyzing? (how many unique userIds in the file)
- which user was logged in the longest?
- how many times did each user check their balance?
- how many payments does a user make on average?


To get the log file, run the 05-generate.py script.  
! **Be careful**  
When using data that was read from a file, you should take care to strip whitespace and convert it to the datatype you actually want!
### Homework
- which user spent the most?
- which user received the most?
- assuming everyone started with 0 money, calculate everyone's balance.
<details>
  <summary>Spoiler warning</summary>
  
  ## Breakdown
  Let's start by defining some helper variables, since we know the format of the log lines
  
  ```python
    SEPARATOR = ';'
    USER = 0
    ACTION = 1
    TIMESTAMP = 2
  ```
  Next, let's open the log file and read its content:

  ```python
  logs = []
  with open('log.txt') as file:
    logs = [line for line in file]
  print(logs[0:10]) # test print the first few lines to make sure we have them read ok.
  ```

  Now let's initialize a set of users, and go through all the lines, adding the first element to the set:
  ```python
  users = set() #empty set
  for log in logs:
    parts = log.split(SEPARATOR)
    user = parts[USER] # USER is 0
    users.add(user) 
  print(f"There are {len(users)} users: {users}")
  ```

  This can also be done in a single less readable line with a set comprehension:
  ```python
  users = { log.split(SEPARATOR)[USER] for log in logs }
  ```
  For the second task, we'll need to look for the 'logged in' and 'logged out' action for each user.  
  Let's use dictionary comprehensions to initialize 2 dictionaries:
  ```python
  logins = {user: -1 for user in users}
  logouts = {user: -1 for user in users}
  ```
  Now let's go through the logs and populate those entries:
  ```python
  for log in logs:
    # The following is a shorter way of saying
    # parts = log.split(SEPARATOR)
    # user = parts[0]
    # action = parts[1]
    # timestamp = parts[2]
    user, action, timestamp = log.split(SEPARATOR) # we know for sure that log.split(SEPARATOR) will give exactly 3 elements in that order
    action = action.strip() # making sure there's no whitespace to confuse the check
    timestamp = int(timestamp.strip()) # turning it to a number
    if action == 'logged in':
        logins[user] = timestamp
    elif action == 'logged out':
        logouts[user] = timestamp
  ```

  And now let's compute the amout of time each user was logged in for:
  ```python
time_logged_in = {}
for user in users:
    time_logged_in[user] = logouts[user] - logins[user]
print(time_logged_in)
  ```

  The above can of course be shortened to:
  ```python
  time_logged_in = {user: logouts[user] - logins[user] for user in users}
  ```
  Now let's find out who spent the most time logged in:

  ```python
max_time, max_user = 0, None
for user, time in time_logged_in.items():
    if time > max_time:
        max_time = time
        max_user = user
print(f"{max_user} was logged in the longest: {max_time}")
  ```

  For the next task, let's look at how many times each user has checked their balance:
  ```python
balance_check_no = {user: 0 for user in users} # init at 0
for log in logs:
    user, action, _ = log.split(SEPARATOR) # we no longer care about the timestamp here, so just name it _
    if action.strip() == 'checked their balance':
        balance_check_no[user] += 1
for user, number_of_checks in balance_check_no.items():
    print(f"{user} checked their balance {number_of_checks} times")
  ```
  For payments, you can do the same, but can no longer check for equality with 'performed a payment' instead you can do `'performed a payment' in action`.

</details>
