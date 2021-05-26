# Check_MK_Speedtest_Agent
Just my own little Check_MK_Agent extension to get Speedtest results to show up in Check_MK monitoring.<br>
It is not pretty, but it gets the job done for me.<br>

# Installation
Make sure you got Check_MK-agent up and running.<br>
Put the CronSpeed.py in a folder where anyone can execute it, and set it up in the Crontab to run at an interval of your choosing, I do it on the hour every hour. <br>
(On my server it takes about 20 sec. to execute it, remember it uses data and bandwidth!)<br>
Put the SpeedtestCSV.py in your Check_MK-agents "local" folder<br>
Remember to make both executable.<br>
Make sure you have Python 3.7 or higher installed.<br>
Make sure you got Speedtest-CLI installed.<br>
To add service in Check_MK, just do a Service Discovery on the agent.<br>

# Before first run
Update the location af the .csv file in both scripts.<br>
Update the thresholds for PING and Speed in the SpeedtestCSV.py<br>
Make sure that the user that executes the CronSpeed.py script has full rights to the .csv file and its folder, as it will be deleted and created every time the script runs.<br>

# After (every) reboot
Make sure you run the "Speedtest" and accept the license.<br>

# Existing problems and improvements
Get the inverted logic for Check_MK to work, so that a higher (speed) value is better. <br>
Move thresholds values to a variable instead of directly in the script.<br>
