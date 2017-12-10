import webbrowser;
import time;


totalbreaks = 1
breakcount = 0

print ("This program started at " + time.ctime())

while ( breakcount < totalbreaks):
    time.sleep(60*60*20)
    webbrowser.open("https://www.youtube.com/watch?v=fJ9rUzIMcZQ")
    breakcount = breakcount + 1
print ("Take a brake Kiddo")
