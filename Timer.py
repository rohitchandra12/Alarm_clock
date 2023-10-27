def timer_counter(label):

    def count():
        global timer_running
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 66600:
                display = "Time is up"
                timer_running = False
                timer("reset")
            else:
                tt = datetime.datetime.fromtimestamp(timer_counter_num)
                string = tt.strftime("%H:%M:%S")
                display = string
                timer_counter_num -= 1
            label.config(text=display)
            label.after(1000, count)
    count()

def timer(work):
    if work=="start":
        global timer_running, timer_counter_num
        timer_running=True
        if timer_counter_num==66600:
            timer_time_str = timer_entry.get()
            hour, minute, second = timer_time_str.split(":")
            minute = int(minute) + int(hour) * 60
            second = (minute * 60) + int(second)
            timer_counter_num += second
        timer_counter(timer_label)
        timer_start.config(state="disable")
        timer_rest.config(state="enable")
        timer_stop.config(state="enable")
        timer_entry.config(state="disable")
    elif work=="stop":
        timer_running=False
        timer_start.config(state="enable")
        timer_rest.config(state="enable")
        timer_stop.config(state="disable")
    elif work=="reset":
        timer_running=False
        timer_counter_num=66600
        timer_label.config(text='00:00:00')
        timer_start.config(state="enable")
        timer_stop.config(state="disable")
        timer_rest.config(state="disable")
        timer_entry.config(state="enable")
        timer_entry.delete(0, END)
