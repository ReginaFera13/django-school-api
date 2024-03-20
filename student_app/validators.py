from django.core.exceptions import ValidationError
import re

def validate_name(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^[A-Z][a-z]* [A-Z]. [A-Z][a-z]*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError(error_message, params={'Current Value':name})

def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^[A-Za-z]+@school.com$'
    good_email = re.match(regex, email)
    if good_email:
        return email
    raise ValidationError(error_message, params={'Current Value':email})

def validate_combination(combination):
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^\d{2}-\d{2}-\d{2}$'
    good_combination = re.match(regex, combination)
    if good_combination:
        return combination
    raise ValidationError(error_message, params={'Current Value':combination})