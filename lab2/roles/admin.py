import redis

def admin_menu():
    print(10 * "-", "ADMIN MENU", 10 * "-")
    print("1. Show Top senders")
    print("2. Show Top spamers")
    print("3. Show Users online")
    print("4. Quit")
    print(40 * "-")
    return int(input("Select option: "))

def main():
    isProgramRunning = True
    connection = redis.Redis(charset="utf-8", decode_responses=True)

    while isProgramRunning:
        selectedOptions = admin_menu();

        if selectedOptions == 1:
            top_senders_count = int(input("Select amount of senders: "))
            senders = connection.zrange("sent:", 0, top_senders_count-1, desc=True, withscores=True)
            print("Top %s senders" % top_senders_count)
            for index, sender in enumerate(senders):
                print(index + 1, ".", sender[0], "-", int(sender[1]), "message(s)")

        elif selectedOptions == 2:
            top_spamers_count = int(input("Select amount of spamers: "))
            spamers = connection.zrange("spam:", 0, top_spamers_count -1 , desc=True, withscores=True)
            print("Top %s spamers" % top_spamers_count)
            for index, spamer in enumerate(spamers):
                print(index + 1, ". ", spamer[0], " - ", int(spamer[1]), " spammed message(s)")

        elif selectedOptions == 3:
            users_online = connection.smembers("online:")
            print("Online users list:")
            for user in users_online:
                print(user)

        elif selectedOptions == 4:
            print("Exiting...")
            isProgramRunning = False
        else:
            print("Error. Invalid option.")


if __name__ == '__main__':
    main()
