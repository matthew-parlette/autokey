# Enter script code
# From home sector (in space), pick up ore from planet
#  and sell it nearby
pickup_from_planet = "ltnt1\rq"
#go_to_sector = "260\r"
#go_to_sector = "395\r"
#go_to_sector = "883e"
#go_to_sector = "927e"
go_to_sector = "39\re"
sell_ore = "pt\r\r0\r"
#return_to_nav_1 = "n1"
return_to_nav_1 = "n1e"
keyboard.send_keys(pickup_from_planet)
keyboard.send_keys(go_to_sector)
keyboard.send_keys(sell_ore)
keyboard.send_keys(return_to_nav_1)

# show status
keyboard.send_keys("/")