import subprocess

print("Content-type: text/html")
print("<br> Gonna show you the time by exceuting the unix date command in a shell, nothing could go wrong here<br>")
print(subprocess.check_output("date", shell=True))
print("<br> done")


