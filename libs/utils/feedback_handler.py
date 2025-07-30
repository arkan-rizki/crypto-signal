def collect_feedback(signal, result):
    with open("storage/logs/feedback.log", "a") as f:
        f.write(f"{signal} => {result}\n")
