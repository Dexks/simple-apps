# Simple keylogger, reads keyboard typed text and window where it was typed.
### Info
+ Saves the window where content was typed
+ Saves info on "log.txt" file
+ Only saves keyboard input
+ Save special keys (enter, space, alt, tab)

### Example output:
###### In Window -> [ Google - Google Chrome ] -> 03/12/2022 15:14:37
###### keylogger [space] python [enter]

# Requires:
pynput==1.7.6
pywin32==305
