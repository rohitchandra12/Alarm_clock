def stopwatch_counter(label):
    def counter():
        if stopwatch_running:
            global  stopwatch_counter_num
            tt = datetime.datetime.fromtimestamp(stopwatch_counter_num)
            string = tt.strftime("%H:%M:%S")
            display = string
            label.config(text=display)
            label.after(1000,counter)
            stopwatch_counter_num+=1
    counter()

def stopwatch(work):
    global stopwatch_running
    if work=="start":
        stopwatch_running=True
        stopwatch_start.config(state="disabled")
        stopwatch_stop.config(state="enabled")
        stopwatch_rest.config(state="enabled")
        stopwatch_counter(stopwatch_label)
    elif work=="stop":
        stopwatch_running = False
        stopwatch_start.config(state="enabled")
        stopwatch_stop.config(state="disabled")
        stopwatch_rest.config(state="enabled")
    else:
        global  stopwatch_counter_num
        stopwatch_running = False
        stopwatch_counter_num=66600
        stopwatch_start.config(state="enabled")
        stopwatch_stop.config(state="disabled")
        stopwatch_rest.config(state="disabled")
        stopwatch_label.config(text="00:00:00")