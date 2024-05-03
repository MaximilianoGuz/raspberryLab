from tkinter.ttk import Button, Label, Entry, Frame
from tkinter import Tk, font

from machine import Pin
from time import sleep

class LedControl(Frame):
  def __init__(self, master=None, pin=17):
    Frame.__init__(self, master)
    self.led = Pin(pin, Pin.OUT)
    self.pack()
    self.ledState = False
    self.amountOfTimes = 0
    self.timeToSleep = 0
    self.create_widgets()


  def create_widgets(self):
    self.ledLabel = Label(self, text="LED State:", font=("Arial", 12))
    self.ledLabel.pack(pady=10)

    self.numberOfTimesLabel = Label(self, text="Ingresar el número de veces de encendido:", font=("Arial", 11))
    self.numberOfTimesLabel.pack()

    self.ledEntry = Entry(self,font=font.Font(family="Arial", size=11))
    self.ledEntry.pack(pady=5)
    self.ledEntry.insert(0, "0")

    self.timeToSleepLabel = Label(self, text="Ingresar el tiempo de encendido (seg):", font=("Arial", 11))
    self.timeToSleepLabel.pack()

    self.timeToSleepEntry = Entry(self,font=font.Font(family="Arial", size=11))
    self.timeToSleepEntry.pack(pady=5)
    self.timeToSleepEntry.insert(0, "0")

    self.ledButton = Button(self, text="Iniciar", command=self.toggleLed)
    self.ledButton.pack(pady=10)

    self.onButton = Button(self, text="ON", command=self.turnOnLed)
    self.onButton.pack(pady=10)

    self.offButton = Button(self, text="OFF", command=self.turnOffLed)
    self.offButton.pack(pady=10)

  def verifyValues(self, value):
    try:
      value = int(value)
      if value < 0:
        raise ValueError
    except ValueError:
      value = 0
      return None
    return value

  def toggleLed(self):
    self.amountOfTimes = self.verifyValues(self.ledEntry.get())
    self.timeToSleep = self.verifyValues(self.timeToSleepEntry.get())

    if not self.amountOfTimes:
      self.amountOfTimes = 0
      self.ledEntry.delete(0, "end")
      self.ledEntry.insert(0, "0")

    if not self.timeToSleep:
      self.timeToSleep = 0
      self.timeToSleepEntry.delete(0, "end")
      self.ledEntry.insert(0, "0")

    if self.amountOfTimes <= 0:
      self.amountOfTimes = 0
      return
    
    for i in range(self.amountOfTimes):
      if self.ledState:
        self.turnOffLed()
      else:
        self.turnOnLed()

  def turnOnLed(self):
    self.led.value(1)
    self.ledState = True
    self.ledLabel.config(text="LED State: ON")
    print(f"LED State: {self.ledState}")

    sleep(self.timeToSleep)

  def turnOffLed(self):
    self.led.value(0)
    self.ledState = False
    self.ledLabel.config(text="LED State: OFF")
    print(f"LED State: {self.ledState}")

    sleep(self.timeToSleep)

root = Tk()
root.title("Led Control")
root.geometry("400x250")

app = LedControl(master=root)
app.mainloop()