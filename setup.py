from crontab import CronTab

cron = CronTab(user='root')
job = cron.new('python3 ./main.py')
job.dow.on('TUE', 'WED', 'THR', 'FRI', 'SAT')
job.hour.on(8)
cron.write()
