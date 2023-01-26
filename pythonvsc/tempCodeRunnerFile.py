
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None