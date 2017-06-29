@ECHO OFF
:onCrash
echo [%date% %time%] Starting AH Tool...
cd "C:\LegionDark\AH_Bot_old"
C:\python\python2 C:\LegionDark\AH_Bot_old\broker.py --verbose items.csv
@ECHO AH-Bot stopped or crashed!
@ECHO %date% %time%> .\Last_AH-tool_Stop.log
@ECHO ...
GOTO onCrash