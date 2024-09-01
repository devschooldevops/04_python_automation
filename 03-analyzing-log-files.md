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
- which user checked their balance the most?
- how many payments does a user make on average?


To get the log file, run the 03-generate.py script.  
! **Be careful**  
When using data that was read from a file, you should take care to strip whitespace and convert it to the datatype you actually want!
### Homework
- which user spent the most?
- which user received the most?
- assuming everyone started with 0 money, calculate everyone's balance.

<details>
    <summary>Spoiler warning</summary>
    <p>
    ## Breakdown
    Let's start by defining some helper variables, since we know the format of the log lines.
    ```python
    SEPARATOR = ';'
    USER = 0
    ACTION = 1
    TIMESTAMP - 2
    ```
    </p>
</details>