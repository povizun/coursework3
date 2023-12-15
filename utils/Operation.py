class Operation:
    def __init__(self, dictionary):
        self.date = dictionary["date"]
        self.description = dictionary["description"]
        try:
            self.from_ = dictionary["from"]
        except KeyError:
            self.from_ = None
        self.to = dictionary["to"]
        self.amount = dictionary["operationAmount"]["amount"]
        self.currency = dictionary["operationAmount"]["currency"]["name"]

    def get_date(self):
        final_date = f"{self.date[8:10]}.{self.date[5:7]}.{self.date[0:4]}"
        return final_date

    @staticmethod
    def get_encrypted_from(account):
        if account is None:
            return ""
        elif "Счет" in account:
            encrypted = f"Счет **{account[-4:]}"
        else:
            card_number = f"{account[-16:-12]} {account[-12:-10]}** **** {account[-4:]}"
            encrypted = f"{account[0:-16]}{card_number}"
        return encrypted

    def get_message(self):
        message = f"""{self.get_date()} {self.description}
{self.get_encrypted_from(self.from_)}{" -> " if self.from_ is not None else ""}{self.get_encrypted_from(self.to)}
{self.amount} {self.currency}

"""
        return message
