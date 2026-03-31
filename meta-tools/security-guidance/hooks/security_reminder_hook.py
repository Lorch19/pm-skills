#!/usr/bin/env python3
"""
Security Reminder Hook for Claude Code
Checks for security patterns in file edits and warns about potential vulnerabilities.
Based on Anthropic's official security-guidance plugin.

Hook type: PreToolUse (fires on Edit, Write, MultiEdit)
Exit codes: 0 = allow, 1 = show error to user, 2 = block tool call and show to Claude
"""

import json
import os
import sys

SECURITY_PATTERNS = [
    {
        "ruleName": "child_process_exec",
        "substrings": ["child_process.exec", "exec(", "execSync("],
        "reminder": "Security Warning: child_process.exec() can lead to command injection. Use execFile() instead with argument arrays.",
    },
    {
        "ruleName": "new_function_injection",
        "substrings": ["new Function"],
        "reminder": "Security Warning: new Function() with dynamic strings can lead to code injection. Consider alternatives.",
    },
    {
        "ruleName": "eval_injection",
        "substrings": ["eval("],
        "reminder": "Security Warning: eval() executes arbitrary code. Use JSON.parse() for data or alternative patterns.",
    },
    {
        "ruleName": "react_dangerously_set_html",
        "substrings": ["dangerouslySetInnerHTML"],
        "reminder": "Security Warning: dangerouslySetInnerHTML can lead to XSS. Ensure content is sanitized with DOMPurify.",
    },
    {
        "ruleName": "document_write_xss",
        "substrings": ["document.write"],
        "reminder": "Security Warning: document.write() can be exploited for XSS. Use createElement() and appendChild().",
    },
    {
        "ruleName": "innerHTML_xss",
        "substrings": [".innerHTML =", ".innerHTML="],
        "reminder": "Security Warning: innerHTML with untrusted content leads to XSS. Use textContent or DOMPurify.",
    },
    {
        "ruleName": "pickle_deserialization",
        "substrings": ["pickle"],
        "reminder": "Security Warning: pickle with untrusted content can execute arbitrary code. Use JSON instead.",
    },
    {
        "ruleName": "os_system_injection",
        "substrings": ["os.system", "from os import system"],
        "reminder": "Security Warning: os.system should only be used with static arguments, never user-controlled input.",
    },
    {
        "ruleName": "sql_injection",
        "substrings": ["f\"SELECT", "f'SELECT", '+ "SELECT', "+ 'SELECT", ".format("],
        "reminder": "Security Warning: String interpolation in SQL queries leads to injection. Use parameterized queries.",
    },
]


def check_patterns(file_path, content):
    """Check if content matches any security patterns."""
    for pattern in SECURITY_PATTERNS:
        if "substrings" in pattern and content:
            for substring in pattern["substrings"]:
                if substring in content:
                    return pattern["ruleName"], pattern["reminder"]
    return None, None


def extract_content(tool_name, tool_input):
    """Extract content to check from tool input."""
    if tool_name == "Write":
        return tool_input.get("content", "")
    elif tool_name == "Edit":
        return tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        return " ".join(edit.get("new_string", "") for edit in edits) if edits else ""
    return ""


def main():
    if os.environ.get("ENABLE_SECURITY_REMINDER", "1") == "0":
        sys.exit(0)

    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ["Edit", "Write", "MultiEdit"]:
        sys.exit(0)

    content = extract_content(tool_name, tool_input)
    rule_name, reminder = check_patterns(tool_input.get("file_path", ""), content)

    if rule_name and reminder:
        print(reminder, file=sys.stderr)
        sys.exit(2)  # Block and show to Claude

    sys.exit(0)


if __name__ == "__main__":
    main()
