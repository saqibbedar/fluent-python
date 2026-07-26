with open("00_enumerate.py") as f:
    if not f:
        print("Unable to read file")
    else:
        print(f"{"Line No.":<10} | Contents")
        for line_no, line_contents in enumerate(f, start=1):
            print(f"{line_no:<10} | {line_contents}")
