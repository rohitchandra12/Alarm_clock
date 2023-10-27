import datetime


def alarm():
    main_time=datetime.datetime.now().strftime("%H:%M %p")
    main_time1,main_time2=main_time.split(' ')
    main_hour1,main_minute=main_time1.split(":")
    alarm_time=alarm_input.get()
    alarm_time1,alarm_time2=alarm_time.split(' ')
    alarm_hour,alarm_minute=alarm_time1.split(":")
    if int(main_hour1)>12 and int(main_hour1)<=24:
        main_hour=str(int(main_hour1)-12)
    else:
        main_hour=main_hour1
    if int(main_hour)==int(alarm_hour) and int(main_minute)==int(alarm_minute) and main_time2==alarm_time2:
        alarm_status.config(text="Weak Up")
        alarm_button.config(state="enabled")
        alarm_input.config(state="enabled")

    else:
        alarm_status.config(text="Alarm has started")
        alarm_button.config(state="disabled")
        alarm_input.config(state="disabled")
    alarm_status.after(1000,alarm)