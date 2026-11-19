"""Part II Task 1: Android OS/lifecycle validation commands and test checklist."""
tests=["Foreground / resume","Move to background","Memory pressure","Reopen app","Rotate screen","Force-stop / process death"]
expected=["Activity resumed","Paused/stopped; process may stay cached","Trim or process killed","Restore or cold launch","Activity recreated; restore state","Process may not be restarted automatically"]
for t,e in zip(tests,expected): print(f"TEST: {t}\n EXPECT: {e}\n")
commands=["adb shell uname -a","adb shell cat /proc/version","adb shell ps -A | grep zygote","adb shell service list","adb shell dumpsys activity","adb shell pm list packages -3"]
print("Useful device commands:")
for c in commands: print(c)
