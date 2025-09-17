from tkinter import *

잔여시간 = 0
cnt = 0
timer_job = None     # after() id 저장
running = False      # 타이머 동작 여부

def start_timer(): # 중복 예약 방지: 기존 타이머 취소
    global 잔여시간, time_job, running, cnt
    if timer_job is not None:
        tk.after_cancel(timer_job)
    잔여시간 = 5
    cnt = 0
    Ib,comfig(text = '현재 횟수:0')
    timer_label.config(text = f'time left: (잔여시간) seconds')
    bt1.config(state=NoRMAL, command = clicke)
    start
    running=True
    update_timer()

    
def update_timer():
    global 잔여시간, time_job, running, cnt
    timer_label.config(text = f'time left: (잔여시간) seconds')
    if 잔여 시간 <=0:
        running=False
        bt1.config(state=DISABLED)
        Ib.config(text='최종 횟수: '+str(cnt))
        timer_label.config(text='Time OVER')
        start_button.config(state=NORMAL)
        timer_job = None
        return
    잔여시간
def click():
    global cnt
    if running:
        cnt += 1
        lb.config(text='현재 횟수: ' + str(cnt))

def reset():
    global cnt
    cnt = 0
    lb.config(text='현재 횟수: 0')

tk = Tk()
tk.geometry('500x220')
tk.title('주어진 시간동안 최대한 많이 클릭하세요!')

timer_label = Label(tk, text="Time left: 0 seconds", font=("Arial", 20), fg="black")
timer_label.pack(pady=10)

start_button = Button(tk, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

lb = Label(tk, text='현재 횟수: 0', fg='blue', font=("Arial", 16))
lb.pack()

bt1 = Button(tk, text='Button', command=click, state=DISABLED)
bt1.pack(padx=10, pady=6)

bt2 = Button(tk, text='reset', command=reset)
bt2.pack(padx=10, pady=6)

tk.mainloop()
