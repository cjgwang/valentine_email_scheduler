import numpy as np

wake_up_time = 10
bedtime = 22
num_emails = 10
## email time is a list of randomly generated times between wake_up_time and bedtime
email_time = []
for _ in range(num_emails):
    hour = np.random.integers(wake_up_time, bedtime)
    minute = np.random.random_integers(0, 59)
    email_time.append(f"{hour}:{minute}")
