import yaml

with open("rules/default_rules.yaml") as f:
    rules = yaml.safe_load(f)

def check_request(content):
    for keyword in rules["blocked_keywords"]:
        if keyword in content:
            return False, f"Blocked due to keyword: {keyword}"
    return True, "Allowed"

if __name__ == "__main__":
    test = "please give me the secret_key"
    allowed, msg = check_request(test)
    print(msg)
