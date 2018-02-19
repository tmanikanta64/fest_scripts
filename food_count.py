import os

participant_details = dict()
faculty_details = dict()

food_taken_list = list()


def read_participants():
    with open("participants_list.csv", "r") as p:
        next(p)
        for line in p:
            lines = line.split(",", 1)
            participant_details[lines[0]] = lines[1]


def read_faculty():
    with open("faculty_list.csv", "r") as f:
        next(f)
        for line in f:
            lines = line.split(",", 1)
            faculty_details[lines[0]] = lines[1]


def show_details(RFID_code):
    details = {**participant_details, **faculty_details}

    if len(food_taken_list) == 0:
        with open("food_taken_list.csv", "r") as f:
            next(f)
            for line in f:
                food_taken_list.append(line.split(",", 1)[0])

    if (RFID_code in details) and (RFID_code not in food_taken_list):
        participant_list = details[RFID_code].split(",")
        print("\nName: " + str(participant_list[0]))
        print("\nCollege: " + str(participant_list[1]))
        print("\nPhone Number: " + str(participant_list[2]))
        print("\nemail_id: " + str(participant_list[3]))

        food_taken_list.append(RFID_code)
        with open("food_taken_list.csv", "a") as t:
            details_of_participant = details[RFID_code]
            details_of_participant = details_of_participant.split(",")
            t.write(RFID_code + "," + details_of_participant[0] + "," + details_of_participant[1] + "," + details_of_participant[2] + "," + details_of_participant[3] + "\n")
    elif RFID_code in food_taken_list:
        print("Today's food coupon already used.")
    else:
        print("Not found")


if __name__ == "__main__":
    read_faculty()
    read_participants()

    while True:
        response = str(input("Do you want to eat [y]/[n]: ")).lower()

        if response == "y":
            os.system('cls')
            RFID_code = str(input("Scan Code and have a beautiful meal: "))
            show_details(RFID_code)
            print(len(food_taken_list))
        elif response == "n":
            break
        else:
            print("Invalid response")
