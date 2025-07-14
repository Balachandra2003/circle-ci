import datetime

def main():
    now = datetime.datetime.now()
    message = f"✅ Python script ran successfully at {now}"
    
    # Print to console
    print(message)

    # Write to a log file
    with open("log.txt", "w") as f:
        f.write(message + "\n")

if __name__ == "__main__":
    main()
