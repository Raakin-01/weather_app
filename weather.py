from logging import config
import tkinter as tk
import requests
import time

def getweather(canvas):
    city=textField.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b94490d58feb72297beb7f434a32df4e"
    json_data=requests.get(api).json()
    condition= json_data['weather'][0]['main']
    
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    presssure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime('%I:%M:%S',time.gmtime(json_data['sys']['sunrise']-21600))
    sunset=time.strftime('%I:%M:%S',time.gmtime(json_data['sys']['sunset']-21600))
    final_info= condition+'\n'+str(temp)+'c'
    fianl_data='\n'+'max temp: '+str(max_temp)+'\n'+'min temp: '+str(min_temp)+'\n'+'pressure: '+str(presssure)+'\n'+'humidity:'+str(humidity)+'\n'+'windspeed: '+str(wind)+'\n'+'sunrise:'+sunrise+'\n'+'sunset: '+sunset
    Label1.config(text=final_info)
    Label2.config(text=fianl_data)
    


canvas=tk.Tk()
canvas.geometry("600x500")
canvas.title("weather app")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textField=tk.Entry(canvas, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>',getweather)


Label1=tk.Label(canvas, font = t)
Label1.pack()
Label2=tk.Label(canvas,font = f)
Label2.pack()
canvas.mainloop()


