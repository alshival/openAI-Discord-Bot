finetune = [
        # Prompts for setting reminders.
        {
            'role':'user','content':"Can you remind me to take the cookies out of the oven in 3 minutes?"
        },
        {
            'role':'assistant','content':'''
            
from datetime import datetime, timedelta
# Three minutes from now
target_time = datetime.now() + timedelta(minutes = 3)
# Add reminder
# Add the reminder
reminder_dict = (
    ctx.author.name,
    f"@{ctx.author.name}, take the cookies out of the oven! Save me one <3",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
# set response text
response_text = f"It is done. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
        {
            'role':'user','content':"Can you remind me to turn in my library book in 2 hours?"
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Two hours from now
target_time = datetime.now() + timedelta(hours = 2)
# Add reminder
reminder_dict = (
    ctx.author.name,
    reminder = f"@{ctx.author.name}, don't forget to turn in your library book. <3",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
# set response text
response_text = f"Done. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
        {
            'role':'user','content':"Remind me to speak with Adalyn's doctor next Monday."
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now().date()

# Find the number of days until the next Monday (0: Monday, 1: Tuesday, ..., 6: Sunday)
days_until_next_monday = (0 - current_date.weekday()) % 7

# Calculate the date for the next Monday
target_time = current_date + timedelta(days=days_until_next_monday)
# Add reminder
reminder_dict = (
    ctx.author.name,
    reminder = f"@{ctx.author.name}, remember to speak with Adalyn's doctor.",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"Ask and you shall receive. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
        {
            'role':'user','content':"Can you please remind me to call mom at 5 PM?"
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Set the target time (5 PM) for the next occurrence
target_time = current_time.replace(hour=17, minute=0, second=0, microsecond=0)

# If the current time is already past 5 PM, increment the target_time by one day
if current_time >= target_time:
    target_time += timedelta(days=1)

# Calculate the time difference between the current time and the next 5 PM
time_difference = target_time - current_time 
# Add reminder
reminder_dict = (
    ctx.author.name,
    "Hey, @{ctx.author.name}, don't forget to call your mom! Tell her I said hi <3",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"Say no more... Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
        {
            'role':'user','content':"Could you remind me to buy groceries tomorrow morning?"
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Set the target time (9 AM) for the next occurrence
target_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)

# If the current time is already past 9AM, increment the target_time by one day
if current_time >= target_time:
    target_time += timedelta(days=1)
# Add the reminder
reminder_dict = (
    ctx.author.name,
    "@{ctx.author.name}, don't forget to buy groceries.",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"I got you. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S'))}"
        '''
        },
        {
            'role':'user','content':"Can you remind me to attend the team meeting at 2:30 PM next Monday."
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Find the number of days until the next Monday (0: Monday, 1: Tuesday, ..., 6: Sunday)
days_until_next_monday = (0 - current_time.weekday()) % 7

# Calculate the date for the next Monday
target_date = current_time.date() + timedelta(days=days_until_next_monday)

# Set the target time (2:25 PM) for next Monday to give them 5 minutes to prepare
target_time = target_date.replace(hour=14, minute=30, second=0, microsecond=0)

# If the current time is already past 2:30 PM on Monday, increment the target_date by one week
if current_time >= target_time:
    target_date += timedelta(weeks=1)

# Add the reminder
reminder_dict = (
    ctx.author.name,
    f"Don't miss the team meeting at 2:30 PM, @{ctx.author.name}!"
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"Sure. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
        {
            'role':'user','content':"Can you remind me to pay the utility bills before the end of the day?"
        },
        {
            'role':'assistant','content':'''
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Set the target time (end of the day) for today
target_time = current_time.replace(hour=23, minute=59, second=59, microsecond=0)

# Create reminder dict
reminder_dict = (
    ctx.author.name,
    "Don't forget to pay the utility bills before the end of the day, @{ctx.author.name}!",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"You got it! Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        '''
        },
{'role':'user','content':"remind me to turn in my homework by tomorrow noon."},
{'role':'assistant','content':"""
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Set the target time (tomorrow noon) for the next occurrence
target_time = current_time.replace(hour=12, minute=0, second=0, microsecond=0) + timedelta(days=1)

# Add reminder
reminder_dict = (
    ctx.author.name,
    f"Hey @{ctx.author.name}, remember to turn in your homework!",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"Noted. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        
"""},

{'role':'user','content':"Remind me to call mom tomorrow morning"},
{'role':'assistant','content':"""
from datetime import datetime, timedelta

# Get the current date and time
current_time = datetime.now()

# Set the target time (tomorrow morning) for the next occurrence
target_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)

# Add reminder
reminder_dict = (
    ctx.author.name,
    f"Hey @{ctx.author.name}, remember to turn in your homework!",
    ctx.channel.id,
    ctx.channel.name,
    target_time.strftime('%Y-%m-%d %H:%M:%S')
    )
response_text = f"Noted. Reminder set: {target_time.strftime('%Y-%m-%d %H:%M:%S')}"
        
"""}
    ]