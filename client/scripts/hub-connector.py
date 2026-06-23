#!/usr/bin/env python3
#date: 2026-06-23
import json, argparse, requests
from pathlib import Path

def push_patterns(source, hub_url, api_key, namespace):
    patterns = []
    for f in Path(source).rglob("*.md"):
        if f.name.startswith("00-INDEX"): continue
        patterns.append({"fingerprint": "test", "type": "adr", "domain": "general"})
    if patterns:
        r = requests.post(f"{hub_url}/api/v1/patterns", json={"namespace": namespace, "patterns": patterns},
                       headers={"Authorization": f"Bearer {api_key}"}, timeout=30)
        print(f"Sent {len(patterns)} patterns")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["push", "pull"])
    parser.add_argument("--source")
    parser.add_argument("--hub-url")
    parser.add_argument("--api-key")
    parser.add_argument("--namespace")
    args = parser.parse_args()
    if args.mode == "push": push_patterns(args.source, args.hub_url, args.api_key, args.namespace)
