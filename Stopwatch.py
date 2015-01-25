# "Stopwatch: The Game"

import simplegui

# define global variables

#Keeps track of the time  in tenths of seconds
time=0

# Track attempts and successful stops
attempts=0
successful_stops= 0

timer_running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
      
    d=t%10
    
    a=(t-d)/600
    
    remainder=((t-d)/10)%60
    
    c=remainder%10
    
    b=(remainder-c)/10    
    
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer, timer_running
    timer.start()
    timer_running=True
    
def stop_handler():
    global timer, time, timer_running, attempts, successful_stops
    
    timer.stop()
    if timer_running:       
    
        attempts+=1
    
        if time%10==0:
            successful_stops+=1
            
        timer_running=False
        
        

def reset_handler():
    global timer, time, timer_running, attempts, successful_stops
    
    timer.stop()
    time=0   
    attempts=0
    successful_stops= 0
    timer_running=False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    
    global time
    
    time+=1
    
    

# define draw handler
def draw_handler(canvas):
    global time, attempts, successful_stops
    canvas.draw_text(format(time), (150, 150), 24, 'Green')
    canvas.draw_text(str(successful_stops)+"/"+str(attempts), (230, 30), 24, 'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)

start_button = frame.add_button('Start', start_handler, 50)
stop_button  = frame.add_button('Stop',  stop_handler,  50)
reset_button = frame.add_button('Reset', reset_handler, 50)


# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer = simplegui.create_timer(100, timer_handler)

