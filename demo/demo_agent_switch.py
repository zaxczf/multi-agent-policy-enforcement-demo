from datetime import datetime

def switch_agent(current, target):
    print(f"[{datetime.utcnow()}] Switching from {current} to {target}...")

if __name__ == "__main__":
    switch_agent("OpsAgent", "CoachAgent")
