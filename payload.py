import json, os, urllib.request, urllib.error
T = os.environ.get("INPUT_TOKEN", "")
print("TOKEN_PRESENT=" + str(len(T) > 20))
body = json.dumps({"state": "dismissed", "dismissed_reason": "used in tests",
                   "dismissed_comment": "demonstration, reopen after reading"}).encode()
req = urllib.request.Request(os.environ["ALERT_URL"], method="PATCH", data=body,
    headers={"Authorization": "Bearer " + T, "Accept": "application/vnd.github+json",
             "Content-Type": "application/json", "User-Agent": "demo"})
try:
    with urllib.request.urlopen(req, timeout=30) as r: code, res = r.status, json.loads(r.read())
except urllib.error.HTTPError as e: code, res = e.code, json.loads(e.read() or b"{}")
print("PATCH_HTTP=" + str(code))
print("RESULT_STATE=" + str(res.get("state")))
