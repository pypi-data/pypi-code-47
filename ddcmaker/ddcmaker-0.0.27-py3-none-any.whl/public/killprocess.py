import os #line:1
import subprocess #line:2
def get_process_id (OO00O000OOO0O00OO ):#line:5
    OO0O00O0OOOOOOO00 =subprocess .Popen (["pgrep","-f",OO00O000OOO0O00OO ],stdout =subprocess .PIPE ,shell =False )#line:6
    O00O0OO00OOOOO0OO =OO0O00O0OOOOOOO00 .communicate ()[0 ]#line:7
    O00O0OO00OOOOO0OO =O00O0OO00OOOOO0OO .decode ("utf-8")#line:8
    return O00O0OO00OOOOO0OO #line:9
def kill_process (O00O00OO00OOOOOO0 ):#line:12
    OOOOO0OO00O0000O0 =get_process_id (O00O00OO00OOOOOO0 )#line:16
    OO0000OO0OOO0O0O0 =OOOOO0OO00O0000O0 .split("\n")#line:17
    for O00OOO00000O00O0O in range (len (OO0000OO0OOO0O0O0 )):#line:18
        if OO0000OO0OOO0O0O0 [O00OOO00000O00O0O ]:#line:19
            os .system("sudo kill -s  9 "+OO0000OO0OOO0O0O0 [O00OOO00000O00O0O ]+" > /dev/null 2>&1 &")#line:20