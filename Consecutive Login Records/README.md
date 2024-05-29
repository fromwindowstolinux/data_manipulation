# Consecutive Login Records

- Given a list of time stamps that is generated by the provided seed.py, where the timestamps represent login time

- Length is defined as the number of days of consecutive logins, NOT the number of consecutive logins

- Output a table with time stamps sorted by consecutive logins, sorted by descending length

- For example, if given the following timestamps
    - ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

- DO NOT use the example above as input

- Since the longest period of consecutive logins occur from 2021-03-16 to 2021-03-18, the answer would be

| START | END | LENGTH
| --- | --- | --- |
| 2021-03-16 | 2021-03-18 | 3
| 2021-03-13 | 2021-03-13 | 1

- The problem stems from needing to award badges for consecutive logins

### Remarks

- current known issue : the code produces incorrect answers while testing