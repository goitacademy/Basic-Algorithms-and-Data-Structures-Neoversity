from time import sleep

try:
    while True:
        print("Process file")
        sleep(0.2)
except KeyboardInterrupt:
    print("Finish file processing")

