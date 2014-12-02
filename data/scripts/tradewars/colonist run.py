# Enter script code
# From home sector (in space), pick up colonists
#  at earth and assign them to fuel on planet in
#  nav point 1
#pickup_from_earth = "1\relt\r"
get_ore = "ltnt1\rq"
transwarp = "lcb991\ry"
sell_ore = "9\rept\r\r0\r"
pickup_from_earth = "1\relt\r"
drop_at_nav_1 = "n1elsnl1\r\r"
#keyboard.send_keys(get_ore)
#keyboard.send_keys(transwarp)
#keyboard.send_keys(sell_ore)
keyboard.send_keys(pickup_from_earth)
keyboard.send_keys(drop_at_nav_1)
# take off and show status
keyboard.send_keys("q/")