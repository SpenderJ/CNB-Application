from CNB_application.exceptions import APIError


class UserError(APIError):
    def __init__(self, message, status_code=None):
        APIError.__init__(self, 'Users', message, status_code)


class EmailAddressAlreadyTaken(UserError):
    def __init__(self):
        UserError.__init__(self, 'An account with this email address already exists', 401)


class UserNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No account associated with this email address', 404)


class MembershipNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No membership found with this id', 404)


class RentNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No rent found with this id', 404)


class FamilyNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No family found with this combination', 404)


class ProgramNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No program found with this id', 404)


class AddressNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No address found with this id', 404)


class DrinkNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No drink found with this id', 404)


class PontonNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No ponton found with this id', 404)


class InvalidLink(UserError):
    def __init__(self):
        UserError.__init__(self, "This link is invalid or has expired", 404)


class AccountAlreadyActivated(UserError):
    def __init__(self):
        UserError.__init__(self, "Your account is already activated", 403)


class EmailRequired(UserError):
    def __init__(self):
        UserError.__init__(self, "Email is required", 400)


class FirstNameRequired(UserError):
    def __init__(self):
        UserError.__init__(self, "First name is required", 400)


class LastNameRequired(UserError):
    def __init__(self):
        UserError.__init__(self, "Last name is required", 400)


class InvalidDateFormat(UserError):
    def __init__(self):
        UserError.__init__(self, "Date format is invalid", 400)


class NoMembershipForSelectedDate(UserError):
    def __init__(self):
        UserError.__init__(self, "No active membership at the given date for the family", 400)


class AddressAlreadyCreatedForThisAccount(UserError):
    def __init__(self):
        UserError.__init__(self, 'Address already created for this family', 400)


class DrinkCardAlreadyCreatedForThisAccount(UserError):
    def __init__(self):
        UserError.__init__(self, 'DrinkCard already created for this family', 400)


class InvalidRentingType(UserError):
    def __init__(self):
        UserError.__init__(self, "Renting type is invalid", 400)


class EmailNotConfirmed(UserError):
    def __init__(self):
        UserError.__init__(self, "An account with this email address already exists and hasn't been activated", 401)
