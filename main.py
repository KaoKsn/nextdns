import os, json
from pathlib import Path
import time
import sys
import requests
from dotenv import load_dotenv


def init():
    load_dotenv()

    profile_id = os.getenv("PID", "")
    key = os.getenv("API_KEY", "")

    if not profile_id or not key:
        raise RuntimeError("API_KEY or PID not set")
    return profile_id, key


def main():
    start = time.time()

    try:
        profile_id, key = init()
    except RuntimeError as e:
        print(e, file=sys.stderr)
        return 1

    url = f"https://api.nextdns.io/profiles/"
    headers = {"X-Api-Key": key}

    configuration_file = "./configs/config.json"
    try:
        with open(configuration_file, "r", encoding="utf-8") as f:
            configuration_requested = json.load(f)
    except (FileNotFoundError, OSError) as e:
        print(f"Configuration file missing. error: {e}", file=sys.stderr)
        return 1

    try:
        response = requests.post(
            url, headers=headers, json=configuration_requested, timeout=30
        )
    except requests.exceptions as e:
        print(e, file=sys.stderr)
        return 1

    outfile = "./results/"
    print(json.dumps(response.json(), indent=2))

    if response.status_code == 200:
        outfile += "success.json"
        print(f"Profile creation successfull, details saved to {outfile}")
    else:
        outfile += "failure.json"
        print(f"Profile creation failed! Details saved to {outfile}")

    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, indent=2)
    except Exception as e:
        print(f"Unable to write request status. error: {e}", file=sys.stderr)
        return 1
    print(f"Took: {time.time() - start:.2f}s")


if __name__ == "__main__":
    sys.exit(main())
