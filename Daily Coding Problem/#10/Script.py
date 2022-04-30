def job_scheduler(func, milli):
   from time import sleep

   sec = milli / 1000
   sleep(sec)

   func()

def samplefunc():
   print("agagaga")

job_scheduler(samplefunc, int(input()))
