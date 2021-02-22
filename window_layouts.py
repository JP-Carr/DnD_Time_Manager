import PySimpleGUI as sg
from time import sleep
from os import listdir, mkdir
from database_class import db, pickler
from sys import exit
import custom_themes
import condition_lists
from database_class import time_increment

QT_ENTER_KEY1 =  'special 16777220'
QT_ENTER_KEY2 =  'special 16777221'

icon_path="dnd_logo.ico"

def alert_box(text="TEXT HERE", window_name="ALERT", button_text="OK", sound=True, theme=None):
    lines=text.split("\n")
    
    sg.theme(theme)
    layout=[[sg.Text("  "+lines[i]+"  ")] for i in range(len(lines))]+[
          #  [sg.Text("  "+text+"  ")],
            [sg.Button(button_text)]
            ]
    window=sg.Window(window_name, layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=True, return_keyboard_events=True, )
    if sound==True:
        print("\a")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return False
        elif event==button_text or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            window.close()
            return True
            

def choice_box(text, window_name="", theme=None):
    sg.theme(theme)
    layout=[
            [sg.Text(text)],
            [sg.Button("Yes"), sg.Button("No")]
            ]
    window=sg.Window(window_name, layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=True, return_keyboard_events=True, )
    print("\a")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return False
        elif event=="No":
            window.close()
            return False
        elif event=="Yes" or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            window.close()
            return True
        
def create_campaign(first=False, theme=None):
    sg.theme(theme)
    layout=[
            [sg.Text("New Campaign")],
            [sg.HorizontalSeparator(color="gray")],
            [sg.Text("Name"), sg.InputText("", size=(25,1), key="campaign_name")],
            [sg.Button("Create")]
            ]
    window=sg.Window("New...", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=False, return_keyboard_events=True, )

    while True:
        event, values = window.read()
        focused_enter=None
     #   print(event)
        if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            active_element=window.FindElementWithFocus()          #Dectects if the enter key has been pressed and checks which element is active
            print(active_element)
            
            if active_element==window["campaign_name"]:
                focused_enter="campaign_name"

        
        if event == sg.WIN_CLOSED and first==False:
            window.close()
            return 
        elif event == sg.WIN_CLOSED and first==True:
            window.close()
            exit()
            return
        
        elif event=="Create" or focused_enter=="campaign_name":
            name=window["campaign_name"].Get()
            
            try:
                if name in listdir("campaigns"):
                    alert_box(text="Campaign \"{}\" already exists".format(name))
                    pass
                else:
                    _dir="campaigns/{}".format(name)
                    
                    new_db=db()
                    mkdir(_dir)
                    pickler(_dir+"/{}.pkl".format(name), new_db)
                    
                    window.close()
                    return name
            except:
                alert_box(text="\"{}\" is not a valid campaign name".format(name))
                pass
                
def pref_window(pref, theme=None, using_RAW=False):
    sg.theme(theme)
  #  themes=["Default", "Black", "DarkRed1", "SandyBeach"]
    #themes=["Black", "BlueMono", "BluePurple", "BrightColors", "BrownBlue", "Dark", "Dark2", "DarkAmber", "DarkBlack", "DarkBlack1", "DarkBlue", "DarkBlue1", "DarkBlue10", "DarkBlue11", "DarkBlue12", "DarkBlue13", "DarkBlue14", "DarkBlue15", "DarkBlue16", "DarkBlue17", "DarkBlue2", "DarkBlue3", "DarkBlue4", "DarkBlue5", "DarkBlue6", "DarkBlue7", "DarkBlue8", "DarkBlue9", "DarkBrown", "DarkBrown1", "DarkBrown2", "DarkBrown3", "DarkBrown4", "DarkBrown5", "DarkBrown6", "DarkGreen", "DarkGreen1", "DarkGreen2", "DarkGreen3", "DarkGreen4", "DarkGreen5", "DarkGreen6", "DarkGrey", "DarkGrey1", "DarkGrey2", "DarkGrey3", "DarkGrey4", "DarkGrey5", "DarkGrey6", "DarkGrey7", "DarkPurple", "DarkPurple1", "DarkPurple2", "DarkPurple3", "DarkPurple4", "DarkPurple5", "DarkPurple6", "DarkRed", "DarkRed1", "DarkRed2", "DarkTanBlue", "DarkTeal", "DarkTeal1", "DarkTeal10", "DarkTeal11", "DarkTeal12", "DarkTeal2", "DarkTeal3", "DarkTeal4", "DarkTeal5", "DarkTeal6", "DarkTeal7", "DarkTeal8", "DarkTeal9", "Default", "Default1", "DefaultNoMoreNagging", "Green", "GreenMono", "GreenTan", "HotDogStand", "Kayak", "LightBlue", "LightBlue1", "LightBlue2", "LightBlue3", "LightBlue4", "LightBlue5", "LightBlue6", "LightBlue7", "LightBrown", "LightBrown1", "LightBrown10", "LightBrown11", "LightBrown12", "LightBrown13", "LightBrown2", "LightBrown3", "LightBrown4", "LightBrown5", "LightBrown6", "LightBrown7", "LightBrown8", "LightBrown9", "LightGray1", "LightGreen", "LightGreen1", "LightGreen10", "LightGreen2", "LightGreen3", "LightGreen4", "LightGreen5", "LightGreen6", "LightGreen7", "LightGreen8", "LightGreen9", "LightGrey", "LightGrey1", "LightGrey2", "LightGrey3", "LightGrey4", "LightGrey5", "LightGrey6", "LightPurple", "LightTeal", "LightYellow", "Material1", "Material2", "NeutralBlue", "Purple", "Reddit", "Reds", "SandyBeach", "SystemDefault", "SystemDefault1", "SystemDefaultForReal", "Tan", "TanBlue", "TealMono", "Topanga"]
    themes=custom_themes.themes
    theme_len=0
    for i in themes:
        if len(i)>theme_len:
            theme_len=len(i)
    
    
    layout=[
            [sg.Text("Appearance")],
            [sg.HorizontalSeparator()],
            [sg.Text("Theme (requires restart)"), sg.Combo(themes, key="themes", size=(theme_len+2, 1), default_value=theme, readonly=True)],
            [sg.Text("RAW Weather"),sg.Checkbox("", default=using_RAW, key="RAW_weather")],
            [sg.Button("Save"), sg.Button("Cancel")],
            ]
    window=sg.Window("Preferences", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=False)
  
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Cancel":
            save=False
            break
        
        elif event=="Save":
            save=True
            if window["themes"].Get() in themes:
                pref["new_theme"]=window["themes"].Get()
            using_RAW=window["RAW_weather"].get()
                
            
            
                
            print(pref["theme"])
            break
        
    window.close()        
    return pref, save, using_RAW
            
    
def rename_window(old_name, theme=None):
    sg.theme(theme)
    layout=[
            [sg.Text("Rename Campaign - "+old_name)],
            [sg.HorizontalSeparator(color="gray")],
            [sg.Text("New name"), sg.InputText("", size=(25,1), key="campaign_name")],
            [sg.Button("Confirm"), sg.Button("Cancel")]
            ]
    
    window=sg.Window("Rename", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=False, return_keyboard_events=True)
  
    while True:
        event, values = window.read()
        
        focused_enter=None
     #   print(event)
        if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            active_element=window.FindElementWithFocus()          #Dectects if the enter key has been pressed and checks which element is active
            print(active_element)
            
            if active_element==window["campaign_name"]:
                focused_enter="campaign_name"
        
        if event == sg.WIN_CLOSED or event=="Cancel":
            window.close()
            return 

        elif event=="Confirm" or focused_enter=="campaign_name":
            name=window["campaign_name"].Get()
            if name!="" and name not in listdir():
                window.close()
                return name
            else:
                if name in listdir():                 
                    alert_box(text="Campaign \"{}\" already exists".format(name))
                    pass
                
                
def set_reminder(time_data, pref, theme=None): 
    sg.theme(theme)
    
    hour, day, month, year=time_data
    hour=int(hour.split(":")[0])
    day=int(day)
    month=int(month.split(".")[0])
    year=int(year)

    radio_date=(pref["set_reminder_option"]=="date")
    
    layout= [
            [sg.Text("Text: "), sg.InputText("", size=(47,1), key="reminder_text")],
            [sg.HorizontalSeparator(color="gray")],
            [sg.Text("Alert Time")],
            [sg.Radio("", group_id="rd0", default=radio_date, enable_events=True, key="select_date"), sg.VerticalSeparator(color="gray"),  sg.Combo([str(i)+":00" for i in range(0,24)], default_value=hour,size=(6,1), readonly=True,key="hour", tooltip="Time - 24 hour"),   sg.Combo(list(range(1,31)), default_value=day, size=(3,1), readonly=True,key="day", tooltip="Day of the month"), sg.Combo(["{}. {}".format(condition_lists.months.index(i)+1,i) for i in condition_lists.months], default_value=time_data[2], size=(30,1), readonly=True,key="month", tooltip="Month"),   sg.InputText(year, size=(5,1), readonly=False,key="year", tooltip="Year - DR",  use_readonly_for_disable=False)],
            [sg.HorizontalSeparator(color="gray")],
            [sg.Radio("", group_id="rd0", default=not radio_date, enable_events=True, key="select_time"), sg.VerticalSeparator(color="gray"), sg.Text(" Hour:"), sg.InputText("0",size=(5,1), key="hour_input", tooltip="Time - 24 hour"),  sg.Text(" Day:"), sg.InputText("0", size=(5,1),key="day_input", tooltip="Day of the month"), sg.Text(" Month:"), sg.InputText("0", size=(5,1), key="month_input", tooltip="Month"),  sg.Text(" Year:"), sg.InputText("0", size=(5,1), key="year_input", tooltip="Year - DR"), sg.Text("")],
            [sg.Button("Confirm"), sg.Button("Cancel")],
            ]
    
    window=sg.Window("Set Reminder", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True, disable_minimize=False, return_keyboard_events=True)

    if radio_date==True:
        for j in ("hour_input","day_input","month_input","year_input"):
            window[j].update(disabled=True)
    else:
        for i in ("hour","day","month","year"):
            window[i].update(disabled=True)
            
    while True:
        event, values = window.read()
        focused_enter=None
        if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            active_element=window.FindElementWithFocus()          #Dectects if the enter key has been pressed and checks which element is active
    #        print(active_element)
            
            if active_element==window["reminder_text"]:
                focused_enter="reminder_text"
        
        if event == sg.WIN_CLOSED or event=="Cancel":
            window.close()
            return False
        
        elif event=="select_time":
            for i in ("hour","day","month","year"):
                window[i].update(disabled=True)
            for j in ("hour_input","day_input","month_input","year_input"):
                window[j].update(disabled=False)
        elif event=="select_date":
            for i in ("hour","day","month","year"):
                window[i].update(disabled=False)
            for j in ("hour_input","day_input","month_input","year_input"):
                window[j].update(disabled=True)
        
        elif event=="Confirm" or focused_enter=="reminder_text":
            text=window["reminder_text"].get()
            if text=="":
                print("\a")
                continue
            
            if values["select_date"]==True:
                hour=int(window["hour"].get().split(":")[0])
                day=int(window["day"].get())
                month=int(window["month"].get().split(".")[0])
                year=int(window["year"].get())
                pref["set_reminder_option"]="date"
            
            elif values["select_time"]==True:
               d_hour=(window["hour_input"]).get()
               d_day=(window["day_input"]).get()
               d_month=(window["month_input"]).get()
               d_year=(window["year_input"]).get()
               pref["set_reminder_option"]="time"
               
               for i in (d_hour,d_day,d_month,d_year):
                   try:
                       _=int(i)
                   except ValueError:
                       alert_box(text="Please enter integer values", theme=theme)
                       continue

            
               d_hour,d_day,d_month,d_year=int(d_hour),int(d_day),int(d_month),int(d_year)
               hour, day, month, year=time_increment(start_time=(hour, day, month, year), increment=(d_hour,d_day,d_month,d_year))
            
            window.close()
            return (text, (hour,day,month,year)),pref
        
        
                
        else:
                print(event)

def view_reminders(db, time_data, theme=None):
    sg.theme(theme)
    
    if db.reminders==[]:
        if choice_box("No reminders found. Would you like to create one?", window_name="Alert", theme=theme)==True:
            return "set_reminder"
        else:
            return
            
    else:
    
        reminder_list=[" "+i[0]+" | {}:00  {}/{}/{}".format(i[1][0],i[1][1],i[1][2],i[1][3]) for i in db.reminders]
        list_box_width=30
        list_box_height=7
        for i in reminder_list:
            if len(i)>list_box_width:
                list_box_width=len(i)
    
        
       
        
        
       # print(reminder_list)
        layout=[
                [sg.Text("Reminders")],
                [sg.HorizontalSeparator(color="gray")],
                [sg.Listbox(reminder_list, select_mode="LISTBOX_SELECT_MODE_SINGLE", key="list_box", size=(list_box_width,list_box_height), enable_events=True)]  , 
                [sg.Button("Delete", disabled=True)]
                ]
        
        window=sg.Window("View Reminders", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=False)
      
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event=="list_box" and len(db.reminders)!=0:
                window["Delete"].update(disabled=False)
            
            if event=="Delete":
                try:
                    index=window["list_box"].GetIndexes()[0]
                except IndexError:
                    continue
                else:
                    db.reminders.pop(index)
                    print(db.reminders)
                    reminder_list=[" "+i[0]+" | {}:00  {}/{}/{}".format(i[1][0],i[1][1],i[1][2],i[1][3]) for i in db.reminders]
                    window["list_box"].Update(values=reminder_list)
                    
                    if len(db.reminders)==0:
                        window["Delete"].update(disabled=True)
            else:
                print(event)
        window.close()         
    
                
def test_window(theme=None):
    sg.theme(theme)
  #  c1=[sg.Button("Confirm"), sg.Button("Cancel")]
    layout=[
            [sg.Text("test")],
            [sg.HorizontalSeparator(color="gray")],
            [sg.Text("New name"), sg.InputText("", size=(25,1), key="campaign_name")],
            #[sg.Button("Confirm"), sg.Button("Cancel")],
            [sg.Listbox(["aaaaa","bbbbb","ccccc","ddddd","eeeee","fffff","ggggg","hhhhh"], size=(15,6), key="list")],
            [sg.Button("x")]
            ]
    
    window=sg.Window("Preferences", layout, finalize=True, icon=icon_path, element_justification="center", force_toplevel=True,disable_minimize=False)
  
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event=="x":
           print( window["tab"].read())
    window.close()
    
if __name__=="__main__":  
    test_window()