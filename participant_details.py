import os

event_ids = {
    '1': "Code N Code",
    '2': "Ensemble",
    '3': "Model Presentation",
    '4': "Circuitry",
    '5': "Trouble Shooting",
    '6': "Technical Quiz",
    '7': "Photography and Short films",
    '8': "Paper Presentation"
}

RFID_codes = list()

details = dict()


def read_details():
    with open("participants_list.csv", "r") as p:
        next(p)
        for line in p:
            lines = line.split(",", 1)
            details[lines[0]] = lines[1]


def show_details(RFID_code):
    if RFID_code in details:
        participant_list = details[RFID_code].split(",")
        print("\nName: " + str(participant_list[0]))
        print("\nCollege: " + str(participant_list[1]))
        print("\nPhone Number: " + str(participant_list[2]))
        print("\nemail_id: " + str(participant_list[3]))
        print("----------------------------")
        print("\nEvents participated:\n")
        for event in participant_list[4: len(participant_list)]:
            print(event)
    else:
        print("participant not found")


if __name__ == "__main__":
    while True:
        response = str(input("Do you want to search a participant [y]/[n]: ")).lower()
        if response == "y":
            os.system('cls')
            read_details()
            # print(details)
            RFID_code = str(input("Enter the code: "))
            print(show_details(RFID_code))
        elif response == "n":
            break
        else:
            print("Invalid option")
