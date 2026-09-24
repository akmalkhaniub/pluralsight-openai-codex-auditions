#!/usr/bin/env python3
"""
Lightweight SQLite Schema Inspector MCP Server.
Provides read-only schema inspection tools to OpenAI Codex via JSON-RPC/stdio.
"""
import sys
import json
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "database.sqlite")

def get_schema(table_name: str) -> dict:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    conn.close()
    
    col_details = []
    for col in columns:
        col_details.append({
            "cid": col[0],
            "name": col[1],
            "type": col[2],
            "notnull": bool(col[3]),
            "default_value": col[4],
            "pk": bool(col[5])
        })
    return {"table": table_name, "columns": col_details}

def list_tables() -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall() if row[0] != "sqlite_sequence"]
    conn.close()
    return tables

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "inspect_table_schema",
                        "description": "Inspects columns, types, and constraints for a given SQLite table.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "table_name": {"type": "string"}
                            },
                            "required": ["table_name"]
                        }
                    },
                    {
                        "name": "list_tables",
                        "description": "Lists all user tables in the database.",
                        "inputSchema": {"type": "object"}
                    }
                ]
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "inspect_table_schema":
            table_name = args.get("table_name", "users")
            data = get_schema(table_name)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
            }
        elif tool_name == "list_tables":
            data = list_tables()
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(data)}]}
            }
    
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling MCP line: {e}\n")

if __name__ == "__main__":
    main()
