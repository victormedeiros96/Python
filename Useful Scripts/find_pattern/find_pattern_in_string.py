import re
# IF USE GROUPS INSIDE PATTERN, GET THEN WITH .groups() or .group(index_of_group) 
def find_pattern_in_string_using_search(text,pattern):
    # RETURNS INDEX POSITION OF PATTERN OCCURENCE
    m = re.search(pattern,text)
    return m
def find_pattern_in_string_using_find(text,pattern):
    # RETURNS THE PATTERN OCCURENCE 
    m = re.search(pattern,text)
    return m
