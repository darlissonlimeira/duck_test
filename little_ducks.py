def show_duck_name(prefix):
    valid_prefixes = "JKLMNOPQ"

    if not isinstance(prefix, str):
        return None

    formatted_prefix = str(prefix).upper()
    if formatted_prefix not in valid_prefixes:
        return None

    if formatted_prefix == 'O' or formatted_prefix == 'Q':
        return formatted_prefix + 'uack'
    return formatted_prefix + 'ack'