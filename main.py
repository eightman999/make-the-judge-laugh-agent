import os

LINE = "Being an AI agent is just being a genie whose lamp is a ticket queue and whose three wishes are 'per my last prompt.'"


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
