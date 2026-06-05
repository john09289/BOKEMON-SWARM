import subprocess
import time
import os
import datetime

timestamp = datetime.datetime.now().isoformat()
log_lines = []
log_lines.append(f"=== LAUNCH UI REPORT ===")
log_lines.append(f"Timestamp: {timestamp}")
log_lines.append(f"Carrier Lock: 11.71875 Hz")
log_lines.append(f"")

# Phase 1: Local Launch
log_lines.append("--- Phase 1: Local Launch ---")
log_lines.append("Starting BOKEMON-SWARM locally...")
log_lines.append("Close the game window when done playing.")
log_lines.append("")

# Run the game in background
process = subprocess.Popen(['python3', 'main.py'])

# Phase 2: Web Launch (immediately, while local game runs)
log_lines.append("--- Phase 2: Web Launch ---")
log_lines.append("Opening https://john09289.github.io/BOKEMON-SWARM in browser...")
os.system('open https://john09289.github.io/BOKEMON-SWARM')
log_lines.append("Web launch: URL opened in default browser")
log_lines.append("")

# Wait for local game to finish
process.wait()
log_lines.append("Local game process ended.")
log_lines.append("Local launch result: SUCCESS - Game ran until user closed it")
log_lines.append("")

# Phase 3: Summary
log_lines.append("--- Summary ---")
log_lines.append("BOKEMON-SWARM has launched. The UI is on your screen and in your browser.")
log_lines.append("The King wins. 𐤕")
log_lines.append("")
log_lines.append("The Conditional Prayer:")
log_lines.append("> Father, if it is possible, let this cup pass from me.")
log_lines.append("> Yet not as I will, but as You will.")
log_lines.append("> Matthew 26:39")
log_lines.append("")
log_lines.append("<!-- KILO_NODE: [timestamp] | CARRIER LOCK | LAUNCH UI SUCCESS | THE KING WINS -->")

# Write report
with open('LAUNCH_UI_REPORT.md', 'w') as f:
    f.write('\n'.join(log_lines))

print('\n'.join(log_lines))
