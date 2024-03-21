from django.core.exceptions import ValidationError
import re

def validate_subject_format(name):
    error_message = 'Subject must be in title case format.'
    regex = r'^[A-Z][a-z]+( [A-Z][a-z]+)*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError(error_message, params={'Current Value':name})

def validate_professor_name(name):
    error_message = 'Professor name must be in the format "Professor Adam".'
    regex = r'^Professor [A-Z][a-z]+$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError(error_message, params={'Current Value':name})