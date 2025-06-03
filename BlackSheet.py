cheat_sheet = {
    "8":   {"2": "K", "3": "K", "4": "K", "5": "K", "6": "K", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "9":   {"2": "K", "3": "V", "4": "V", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "10":  {"2": "V", "3": "V", "4": "V", "5": "V", "6": "V", "7": "V", "8": "V", "9": "V", "10": "K", "A": "K"},
    "11":  {"2": "V", "3": "V", "4": "V", "5": "V", "6": "V", "7": "V", "8": "V", "9": "V", "10": "V", "A": "K"},
    "12":  {"2": "K", "3": "K", "4": "P", "5": "P", "6": "P", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "13":  {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "14":  {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "15":  {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "K", "8": "K", "9": "K", "10": "U/K", "A": "K"},
    "16":  {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "K", "8": "K", "9": "U/K", "10": "U/K", "A": "U/K"},
    "17":  {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "P", "8": "P", "9": "P", "10": "P", "A": "P"},
    "A,2": {"2": "K", "3": "K", "4": "K", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "A,3": {"2": "K", "3": "K", "4": "K", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "A,4": {"2": "K", "3": "K", "4": "V", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "A,5": {"2": "K", "3": "K", "4": "V", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "A,6": {"2": "K", "3": "V", "4": "V", "5": "V", "6": "V", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "A,7": {"2": "P", "3": "V", "4": "V", "5": "V", "6": "V", "7": "P", "8": "P", "9": "K", "10": "K", "A": "K"},
    "A,8": {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "P", "8": "P", "9": "P", "10": "P", "A": "P"},
    "A,9": {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "P", "8": "P", "9": "P", "10": "P", "A": "P"},
    "2,2": {"2": "S/K", "3": "S/K", "4": "S", "5": "S", "6": "S", "7": "S", "8": "K", "9": "K", "10": "K", "A": "K"},
    "3,3": {"2": "S/K", "3": "S/K", "4": "S", "5": "S", "6": "S", "7": "S", "8": "K", "9": "K", "10": "K", "A": "K"},
    "4,4": {"2": "K", "3": "K", "4": "K", "5": "S/K", "6": "S/K", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "5,5": {"2": "V", "3": "V", "4": "V", "5": "V", "6": "V", "7": "V", "8": "V", "9": "V", "10": "K", "A": "K"},
    "6,6": {"2": "S/K", "3": "S", "4": "S", "5": "S", "6": "S", "7": "K", "8": "K", "9": "K", "10": "K", "A": "K"},
    "7,7": {"2": "S", "3": "S", "4": "S", "5": "S", "6": "S", "7": "S", "8": "K", "9": "K", "10": "K", "A": "K"},
    "8,8": {"2": "S", "3": "S", "4": "S", "5": "S", "6": "S", "7": "S", "8": "S", "9": "S", "10": "S", "A": "S"},
    "9,9": {"2": "S", "3": "S", "4": "S", "5": "S", "6": "S", "7": "P", "8": "S", "9": "S", "10": "P", "A": "P"},
    "10,10": {"2": "P", "3": "P", "4": "P", "5": "P", "6": "P", "7": "P", "8": "P", "9": "P", "10": "P", "A": "P"},
    "A,A": {"2": "S", "3": "S", "4": "S", "5": "S", "6": "S", "7": "S", "8": "S", "9": "S", "10": "S", "A": "S"},
}

action_map = {
    "V": "(V) Verdubbelen",
    "K": "(K) Kaart nemen",
    "P": "(P) Passen",
    "S": "(S) Splitsen",
    "S/K": "(S/K) Splitsen als het kan om te verdubbelen, anders een kaart nemen",
    "U/K": "(U/K) Uitbetalen als het kan, anders een kaart nemen"
}

def normalize_card(card):
    card = card.upper()
    if card in ["J", "Q", "K"]:
        return "10"
    return card

def hand_to_key(card1, card2):
    if card1 == card2:
        if card1 == "A":
            return "A,A"
        else:
            return f"{card1},{card2}"
        
    if card1 == "A" or card2 == "A":
        other = card2 if card1 == "A" else card1
        return f"A,{other}"
    
    total = int(card1) + int(card2)
    return str(total)

def lookup_blackjack_action(player_hand, dealer_card):
    try:
        return cheat_sheet[player_hand][dealer_card]
    except KeyError:
        return "Ongeldige hand of dealer kaart"

def get_blackjack_action(player_card1, dealer_card, player_card2):
    player_card1 = normalize_card(player_card1)
    dealer_card = normalize_card(dealer_card)
    player_card2 = normalize_card(player_card2)
    player_hand = hand_to_key(player_card1, player_card2)
    action_code = lookup_blackjack_action(player_hand, dealer_card)
    return action_map.get(action_code, f"Onbekende actie ({action_code})")

while True:
    try:
        player_card1 = input("Speler eerste kaart: ")
        dealer_card = input("Dealer eerste kaart: ")
        player_card2 = input("Speler tweede kaart: ")

        action = get_blackjack_action(player_card1, dealer_card, player_card2)
        print(f"Uitkomst: {action}\n")
    except KeyboardInterrupt:
        break
