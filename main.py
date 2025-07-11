### Gmail account only
### Set up Gmail API through Google Cloud Console
import ezgmail as ezgmail
from apscheduler.schedulers.background import BackgroundScheduler
import random_time
import subject_body
ezgmail.init()

valentine_email = "valentine_email@gmail.com"
def send_scheduled_email(valentine_email, subject, body):
    for _ in range(random_time.email_time):
        ezgmail.send(
            valentine_email,
            subject[_],
            body[_]
        )
        print(f"Email successfully sent to valentine at {random_time.email_time[_]})

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    for time in random_time.email_time:
    scheduler.add_job(
        send_scheduled_email,
        hour = random_time.email_time()
        minute = random_time.email_time()
        args = [valentine_email, subject, body]
    )

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler shut down.")