class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        try:
            if not isinstance(account, Account):
                raise TypeError
            if not self.fix_account(account):
                raise ValueError
            self.account.append(account)
        except TypeError:
            print("Not a valid account")
        except ValueError:
            print("Corrupted account. Recuperation was not possible.")

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return: True if success, False if an error occured
        """
        try:
            origin_account = self.__get_account(origin)
            dest_account = self.__get_account(dest)
            if origin_account.value < amount or amount < 0:
                raise ValueError
            dest_account.transfer(amount)
            origin_account.transfer(-amount)
        except (ValueError, AttributeError):
            print("Insufficient funds to make transfer.")
        pass

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return: True if success, False if an error occured
        """
        try:
            if not isinstance(account.id, int):
                raise TypeError
            elif not isinstance(account.name, str):
                raise TypeError
            elif not any(i.startswith(("zip", "addr")) for i in vars(account)):
                raise AttributeError("Address information not found.")
            elif not all(i in vars(account) for i in ("id", "name", "value")):
                raise AttributeError("Mandatory info not found.")
            battr = [i for i in vars(account) if i.startswith("b")]
            for i in battr:
                delattr(account, i)
            if len(vars(account)) % 2 == 0:
                raise AttributeError("Even number of attributes")
        except (TypeError, AttributeError) as e:
            print(str(e))
            return False
        else:
            return True

    def __get_account(self, identifier):
        try:
            if isinstance(identifier, int):
                ac = [i for i in self.account if identifier == i.id]
            elif isinstance(identifier, str):
                ac = [i for i in self.account if identifier == i.name]
                if len(ac) > 1:
                    raise AttributeError
            else:
                raise TypeError
            return ac[0]
        except TypeError:
            print("Data type not allowed. Search for account name or ID.")
        except AttributeError:
            print("Possible duplicate entries. Search for account ID.")
        except IndexError:
            print("Account not found.")


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
            Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount
