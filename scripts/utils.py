def place_options_vertical(options, option_pos, x, y, y_gap):
    for i in range(len(options)):
        option_pos.append((x, y + i * y_gap))
