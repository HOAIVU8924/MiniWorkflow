import csv
import json
import re

input_file = "emails.csv"
output_file = "leave_request.json"

pattern_leave = re.compile(r"\bleave\b|\btake\b.*\bday\s*off\b", re.IGNORECASE)

leave_requests = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text = (row["subject"] + " " + row["body"]).lower()

        if pattern_leave.search(text):
            leave_requests.append({
                "id": int(row["id"]),
                "sender": row["sender"],
                "type": "leave_request"
            })

with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(leave_requests, jsonfile, indent=4, ensure_ascii=False)

print(f"Đã xuất {len(leave_requests)} email nghỉ phép vào {output_file}")
