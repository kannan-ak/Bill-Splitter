import random


def main():
    try:
        people = int(input("Enter the number of friends joining (including you): \n"))
        if people > 0:
            print("Enter the name of every friend (including you), each on a new line: ")
            friends = [input() for _i in range(people)]
            bill = int(input("Enter the total bill value: \n"))
            friends_dict = dict.fromkeys(friends, round(bill / len(friends), 2))
            lucky(friends_dict, bill)
        else:
            print("No one is joining for the party")
            exit()
    except ValueError:
        print("No one is joining for the party")
        exit()


def lucky(current_friends_dict, bill):
    lucky_draw = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: \n')
    if lucky_draw.lower() == "yes":
        lucky_person = random.choice(list(current_friends_dict))
        print(f"\n{lucky_person} is the lucky one!")
        updated_bill = round(bill / (len(current_friends_dict) - 1), 2)
        updated_friends_dict = dict.fromkeys(current_friends_dict.keys(), updated_bill)
        updated_friends_dict[lucky_person] = 0
        print(updated_friends_dict)
    else:
        print("\nNo one is going to be lucky")
        print(current_friends_dict)


main()











