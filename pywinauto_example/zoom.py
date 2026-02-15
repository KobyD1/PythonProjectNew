import time
import pywinauto
from pywinauto import Desktop

app= pywinauto.application.Application(backend="uia")
app.start( "C://Users//dkdk1//AppData//Roaming//Zoom//bin//Zoom.exe")
dialog = Desktop(backend='uia').Zoom
dialog.print_control_identifiers(filename='outputs//output_zoom_4.txt')
join =dialog.child_window(title="Join a Meeting", control_type="Button")
join.click()
time.sleep(3)
dialog = Desktop(backend='uia').JoinMeeting
meeting_hystory =dialog.child_window(title="Meeting ID or Personal Link Name", control_type="Edit")
meeting_hystory.type_keys("123456")

meeting_name =dialog.child_window(title="Meeting history list", control_type="SplitButton")
for i in range(10):
    meeting_name.type_keys("{BACKSPACE}")  # clear only one digit
meeting_hystory.type_keys("eeeee")

close =dialog.child_window(title="Close", control_type="Button")
close.click()

time.sleep(3)

