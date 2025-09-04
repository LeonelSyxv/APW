from Functions.watchReportResolved import resolved_watcher
from Functions.watchNewReport import latest_watcher
import threading
import time
from threading import Lock

# Lock to ensure only one WhatsApp-related action is executed at a time
whatsapp_lock = Lock()

# Shared dictionary to track recently resolved channels
recently_resolved_channels = {}

# Start background thread to monitor resolved reports
threading.Thread(
    target=resolved_watcher,
    args=(15, whatsapp_lock, recently_resolved_channels),
    daemon=True
).start()

# Start background thread to monitor new reports
threading.Thread(
    target=latest_watcher,
    args=(15, whatsapp_lock, recently_resolved_channels),
    daemon=True
).start()

print("Script started. Watchers are running in background threads.")
while True:
    time.sleep(60)  # Keep main thread alive, watchers run in background
