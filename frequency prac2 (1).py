import re

text = "Contact us at alice123@example.com or bob_smith@domain.org"

# Username part before '@'
emails = re.findall(r'([A-Za-z0-9._%+-]+)@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
print(emails)  # ['alice123', 'bob_smith']

text = "Loving the vibes! #summer #AI #Python3"

hashtags = re.findall(r'#\w+', text)
print(hashtags)  # ['#summer', '#AI', '#Python3']

text = "Important dates: 29/04/2026, 2026-04-29, April 29, 2026"

dates = re.findall(r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}|[A-Za-z]+\s\d{1,2},\s\d{4})\b', text)
print(dates)  # ['29/04/2026', '2026-04-29', 'April 29, 2026']

text = "Call me at +91-9876543210 or (123) 456-7890"

phones = re.findall(r'\+?\d{1,3}[-.\s]?\(?\d{2,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{4}', text)
print(phones)  # ['+91-9876543210', '(123) 456-7890']
