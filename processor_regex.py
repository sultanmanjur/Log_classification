import re


def classify_with_regex(log_messages):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action",
    }
    for pattern,label in regex_patterns.items():
        if re.search(pattern, log_messages, re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    test_logs = [
        "User User123 logged in.",
        "Backup started at 2023-10-01 02:00:00.",
        "System updated to version 1.2.3.",
        "Disk cleanup completed successfully.",
        "File report.pdf uploaded successfully by user User456.",
        "Account with ID 789 created by admin.",
        "Unrecognized log message."
    ]
    
    for log in test_logs:
        classification = classify_with_regex(log)
        print(f"Log: '{log}' => Classification: '{classification}'")