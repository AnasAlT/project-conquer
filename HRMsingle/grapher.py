from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from fpdf import FPDF
import datetime as dt
import time


plt.style.use('fast')

pdf = FPDF()

with open("./resources/bpmdata.txt", "w") as hr:
    hr.write("0")
    
xval1 = []
yval1 = []

xval2 = []
yval2 = []

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ueData = pd.read_csv(r'D:\UE Projects\project-conquer\Data\reportMetric.csv')

def animate(i):
    with open("./resources/bpmdata.txt") as hr:
        currentHR = hr.read()
    
    xval1.append(dt.datetime.fromtimestamp(time.time()))
    yval1.append(currentHR)
    
    
    ax1.cla()
    ax1.set_title("Heart Rate")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("BPM")
    ax1.plot(xval1, yval1)
    
    ueData = pd.read_csv(r'D:\UE Projects\project-conquer\reportMetric.csv')
    # columns first, rows second
    yval2.append(ueData.values[0][1])
    ax2.cla() 
    ax2.set_title("User Engagement")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Points")
    ax2.plot(xval1, yval2)
    

ani = FuncAnimation(plt.gcf(), animate, frames=60, interval = 1000)   

plt.tight_layout(pad = 1)
fig.set_figheight(8)
fig.set_figwidth(15)
plt.show()
ani.save(filename= r'D:\UE Projects\HRMsingle\mytest.png')

pdf.add_page() 
#header 
pdf.image("./resources/header.png", 0, 0, w=210)
#title
pdf.set_font("Arial", '', 23)
pdf.ln(20)

pdf.image("mytest.png", 3, 45, w= 200, h=150)
pdf.write(5, f"Experience Report")

#interactions
pdf.ln(180)
pdf.write(5, f"found {ueData.values[1][1]} out of {ueData.values[1][2]} lamps during experiement")

#footer 
pdf.image("./resources/footer.png", 0, 264, w=212)
pdf.output('report.pdf')

