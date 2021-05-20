from crontab import CronTab

cron = CronTab(user='root')
job = cron.new('python3 ./src/main.py')
job.dow.on('TUE', 'WED', 'THU', 'FRI', 'SAT')
job.hour.on(8)
cron.write()
