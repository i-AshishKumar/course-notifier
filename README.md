# Get notified Instantly!
Looking forward to take classes with your favorite prof. This tool notifies you to be ahead of the competetion and register fast before the seats get filled out.Do not missout on registering for your favourite course.

###### Note: You have to be logged in to your Dal Online account for this to work properly

## Instructions for setting up

`git clone https://github.com/i-AshishKumar/course-notifier.git`

`cd course-notifier`

`pip install -r requirements.txt`

![Course release notification](https://i.ibb.co/GR2Hz2s/course-release-notification.jpg)

### Make sure to edit the below code fields in `main.py`

```
email_sender = 'xxxxx@gmail.com'
email_receiver = 'xxxxx@gmail.com'
email_password = 'xxxxx'
```
```
desired_course = "XXXX" ** The course number you would like to get notified for upon release**
```
Schedule this python script to run in Windows Task Scheduler at the frequency of your liking.
![Task Scheduler](https://i.ibb.co/r2RGVYq/course-task-scheduler.png)

That's all you have to do. Good luck with your course :)