import re
## https://github.com/CoreyMSchafer/code_snippets/tree/master/Regular-Expressions
print(r'\tTab')

urls= '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


emails= '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

text_to_search = '''
bcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
In the statement assert(False), these are just redundant parentheses around False, which evaluate to their contents. But with assert(False,) the parentheses are now a tuple, and a non-empty tuple evaluates to True in a boolean context.
111-333-555
123.123.124
123-123.124
123*123*124
800*123*124
900*123*124

cat
mat
pat
bat
'''
## re.compile is the function to compile the pattern into variable for latter search/filter usage:
#pattern = re.compile(r'text$')
#matches = pattern.finditer(text_to_search)

#for match in matches:
#	print(match)

#print(text_to_search)

### single character
#pattern =  re.compile(r'[^a-zA-Z]')## not a to z nor A to Z
#pattern =  re.compile(r'[^bcm]at') ## match *ct but not {b|c|m}at
#pattern =  re.compile(r'[89]00[*-.]\d\d\d[*-.]\d\d\d')

### groups
## multiple matches
#pattern =  re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') ## match *ct but not {b|c|m}at

## email 
print(re.search(r'[a-zA-Z]+@[a-zA-Z-]+\.(com|edu|net)',emails))
#print(re.search(r'[a-zA-Z]+@[a-zA-Z-]+\.(com|edu|net)',emails))
#print(re.findall(r'[a-zA-Z]+@[a-zA-Z-]+\.(com|edu|net)',emails))

#pattern =  re.compile(r'[a-zA-Z]+@[a-zA-Z-]+\.(com|edu|net)') ## match *ct but not {b|c|m}at
#pattern =  re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') ## match *ct but not {b|c|m}at
pattern =  re.compile(r'https?://(www\.)?(\w+)\.(\w+)',re.I) ## match *ct but not {b|c|m}at

matches = pattern.findall(urls) # only return the group[0]

matches = pattern.finditer(urls)
#for match in matches:
#	print(match.group(0))
#	print(match.group(1))
#	print(match.group(2))
# 	print(match.group(3))

## \2 is the group[2] and \3 is the group[3]
#https://www.kite.com/python/answers/how-to-use-re.sub()-in-python
sub_urls = pattern.sub(r'\2.\3',urls)
print(sub_urls)
