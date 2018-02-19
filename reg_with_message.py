import way2sms
import os

# event_id dictionary
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

# login ids for way2sms
login_ids = [
    "8332098992-83320",
    "7660993932-766099",
    "8919381090-891938"
]


def send_message(id, phone_number, Message):
    details = login_ids[id].split("-")
    q = way2sms.sms(details[0], details[1])
    q.send(phone_number, Message)
    return q


def enter_details():
    RFID_code = str(input("Enter the code: "))

    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    college = str(input("Enter college: "))

    # ensuring the entered names are not numbers
    while first_name.isnumeric() or last_name.isnumeric() or college.isnumeric():
        print("Entered credentials are numeric, please enter name and college\n")
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        college = str(input("Enter college: "))

    phone_number = str(input("Enter phone number: "))

    # ensuring the entered phone number is a 10 digit string
    while (len(phone_number) != 10) or not (phone_number.isnumeric()):
        print("Please enter a valid phone number\n")
        phone_number = str(input("Enter phone number: "))
    email_id = str(input("Enter email: "))

    return [RFID_code, first_name, last_name, college, phone_number, email_id]


def enter_events():
    print("-------------------------------")
    print("Events:")
    print("-------------------------------")
    print("[1] Code N Code.")
    print("[2] Ensemble.")
    print("[3] Model Presentation.")
    print("[4] Circuitry.")
    print("[5] Trouble Shooting.")
    print("[6] Technical Quiz.")
    print("[7] Photography and Short films.")
    print("[8] Paper Presentation.")
    print("--------------------------------")

    def read_events():
        events = str(input("Enter any three event options: "))
        return list(events.split())

    events = read_events()
    while events[0] == events[1] or events[1] == events[2] or events[2] == events[0]:
        print("event repeated\n")
        print("Enter three different events")
        events = read_events()

    print("The events interested are: ")
    for event in events:
        try:
            print(event_ids[event])
        except KeyError:
            print("Enter valid event number")
            events = read_events()
    return events


if __name__ == "__main__":
    count = 0
    id = 0
    while True:
        response = str(input("Do you want to add a participant[y]/[n]: "))
        if response == "y":
            os.system('cls')
            details = list(enter_details())
            events = list(enter_events())
            with open("participants_list.csv", "a+") as o:
                o.write(details[0] + "," + details[1] + " " + details[2] + "," + details[3] + "," + details[4] + "," + details[5] + "," + event_ids[events[0]] + "," + event_ids[events[1]] + "," + event_ids[events[2]] + "\n")
            # this logic is awesome
            with open(str(events[0]) + ".csv", "a+") as one:
                one.write(details[0] + "," + details[1] + " " + details[2] + "," + details[3] + "," + details[4] + "," + details[5] + "," + event_ids[events[0]] + "\n")

            with open(str(events[1]) + ".csv", "a+") as two:
                two.write(details[0] + "," + details[1] + " " + details[2] + "," + details[3] + "," + details[4] + "," + details[5] + "," + event_ids[events[1]] + "\n")

            with open(str(events[2]) + ".csv", "a+") as three:
                three.write(details[0] + "," + details[1] + " " + details[2] + "," + details[3] + "," + details[4] + "," + details[5] + "," + event_ids[events[2]] + "\n")

            message = "Hi " + str(details[1] + " " + details[2]) + "\n" + " You have been successfully registered for:\n" + str(event_ids[events[0]]) + "\n" + str(event_ids[events[1]]) + "\n" + str(event_ids[events[2]])
            try:
                if count > 96:
                    id += 1
                    count = 1

                if send_message(id, details[4], message):
                    print("message sent successfully\n")
                print(count)
                count += 1
            except ConnectionError:
                raise
        else:
            print("invalid response")
