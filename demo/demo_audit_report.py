import json

with open("logs/sample_audit_log.jsonl") as f:
    for line in f:
        entry = json.loads(line)
        print(entry)
