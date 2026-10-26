from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_middle_name():
    """Names like Benedict Estefan Halkin"""
    formatted_name = get_formatted_name('benedict', 'halkin', 'estefan')
    assert formatted_name == 'Benedict Estefan Halkin'

def test_different_cases():
    formatted_name = get_formatted_name('jANis', 'joPlin')
    assert formatted_name == 'Janis Joplin'
