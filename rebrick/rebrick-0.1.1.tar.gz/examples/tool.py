#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import rebrick

# Before you can start this example be sure to fill in following variables with
# your specific values:

API_KEY = "key"
USER_TOKEN = "token"
USER_NAME = "username"
USER_PASSWORD = "password"

# init Rebrick tool
rb = rebrick.Rebrick(API_KEY, USER_TOKEN, silent=True)

# if user token is not provided on init you can get it later to access user data
rb.login(USER_NAME, USER_PASSWORD)

print("Get element:")
data = rb.get_element(300121)
print(data)
print()

print("Get element ids:")
data = rb.get_element_ids(3001, 4)
print(data)
print()

print("Get element image:")
data = rb.get_element_image(300121)
print(data)
print()

print("Get color:")
data = rb.get_color(4)
print(data)
print()

print("Get colors:")
data = rb.get_colors()
print(data)
print()

print("Get part:")
data = rb.get_part(3001)
print(data)
print()

print("Get parts:")
data = rb.get_parts('Bilbo')
print(data)
print()

print("Get part colors:")
data = rb.get_part_colors(3001)
print(data)
print()

print("Get part color sets:")
data = rb.get_part_color_sets(3001, 4)
print(data)
print()

print("Get part category:")
data = rb.get_part_category(11)
print(data)
print()

print("Get part categories:")
data = rb.get_part_categories()
print(data)
print()

print("Get set:")
data = rb.get_set(6608)
print(data)
print()

print("Get sets:")
data = rb.get_sets(min_year=1982, max_year=1982, min_pieces=20, max_pieces=25)
print(data)
print()

print("Get set elements:")
data = rb.get_set_elements(6608)
print(data)
print()

print("Get set themes:")
data = rb.get_set_themes(6608)
print(data)
print()

print("Get set image:")
data = rb.get_set_image(6608)
print(data)
print()

print("Get set MOCs:")
data = rb.get_set_alternates(79003)
print(data)
print()

print("Get theme:")
data = rb.get_theme(73)
print(data)
print()

print("Get themes:")
data = rb.get_themes()
print(data)
print()

print("Get MOC:")
data = rb.get_moc(24522)
print(data)
print()

print("Get MOC elements:")
data = rb.get_moc_elements(24522)
print(data)
print()

print("Get lost elements:")
data = rb.get_lost_elements()
print(data)
print()

print("Get part lists:")
data = rb.get_partlists()
print(data)
print()

print("Get part list:")
data = rb.get_partlist(21261)  # provide your own list ID
print(data)
print()

print("Get part list elements:")
data = rb.get_partlist_elements(21261)  # provide your own list ID
print(data)
print()
