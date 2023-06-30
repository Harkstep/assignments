import re


pattern = r'(.*)://(.*)'

text = 'http://example.com'
matches = re.findall(pattern, text, re.MULTILINE)
print('Output:')
print(f'Pattern: {pattern}\nText: {text}\nMatches: {matches}\n')