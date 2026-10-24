from datetime import datetime

CONFIG_FILE = "cloud_config.txt"
REPORT_FILE = "cloud_audit_report.txt"


checks = []

with open(CONFIG_FILE, "r") as file:
    config = {}

    for line in file:
        key, value = line.strip().split("=", 1)
        config[key] = value.lower()

if config.get("IAM_PUBLIC_ACCESS") == "true":
    checks.append("[HIGH] IAM allows public access")

if config.get("STORAGE_ENCRYPTION") == "false":
    checks.append("[HIGH] Storage encryption is disabled")

if config.get("FIREWALL_ENABLED") == "false":
    checks.append("[HIGH] Firewall protection is disabled")

if config.get("LOGGING_ENABLED") == "false":
    checks.append("[MEDIUM] Security logging is disabled")

if config.get("MFA_ENABLED") == "false":
    checks.append("[HIGH] Multi-factor authentication is disabled")

if config.get("BACKUP_ENABLED") == "false":
    checks.append("[MEDIUM] Backup protection is disabled")

report = [
    "CLOUD SECURITY AUDIT REPORT",
    "=" * 40,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    f"Security issues detected: {len(checks)}",
    "",
    "FINDINGS",
    "-" * 40
]

if checks:
    report.extend(checks)
else:
    report.append("No security issues detected.")

with open(REPORT_FILE, "w") as file:
    file.write("\n".join(report))

print("\n".join(report))
print(f"\nReport saved to: {REPORT_FILE}")
