"""Part II Task 4: basic static security regression checks for a sample app policy."""
checks={
"Permission minimisation":True,
"Token stored in private/Keystore-protected storage":True,
"HTTPS required":True,
"Certificate validation enabled":True,
"Update signer verified":True,
"Sensitive payload excluded from notification":True
}
for name,passed in checks.items(): print(("PASS" if passed else "FAIL"),name)
print("This is a policy checklist example; it does not inspect an APK or prove security.")
