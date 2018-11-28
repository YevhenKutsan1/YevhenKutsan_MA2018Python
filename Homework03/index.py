import simplegui

current_time = 0
interval = 100
total_attempts = 0
successfull_attempts = 0
timer_started = False

def format_time(val):
    milliseconds = str(val % 10);
    seconds = str(val % 600 // 10);
    if len(seconds) == 1:
        seconds = "0" + seconds;
    minutes = str(val // 600);
    return minutes + ":" + seconds + "." + milliseconds;    

def start():
    global timer_started
    if not(timer_started):
        timer.start()
        timer_started = True
    
def stop():
    global total_attempts, successfull_attempts, timer_started
    if timer_started:          
        timer.stop()
        total_attempts += 1
        if (current_time % 10) == 0:
            successfull_attempts += 1
        timer_started = False       
    
def reset():
    global current_time, total_attempts, successfull_attempts, timer_started
    timer.stop()
    current_time = 0
    total_attempts = 0
    successfull_attempts = 0
    timer.start()
    timer_started = True
    
def tick():
    global current_time
    current_time += 1

def draw(canvas):
    canvas.draw_text(format_time(current_time), [130, 150], 35, "Green")
    canvas.draw_text(str(successfull_attempts) + "/" + str(total_attempts), [250, 40], 20, "Green")

frame = simplegui.create_frame("Homework03", 300, 300)
frame.set_draw_handler(draw)

start_button = frame.add_button("Start", start, 100)
stop_button  = frame.add_button("Stop",  stop,  100)
reset_button = frame.add_button("Reset", reset, 100)

frame.start()
timer = simplegui.create_timer(interval, tick)