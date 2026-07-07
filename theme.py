LIGHT_THEME = {
    "window_bg": "#f5f5f5",
    "frame_bg": "#ffffff",
    "title_bg": "#0d6efd",
    "title_fg": "white",
    "text": "#212529",
    "button_bg": "#0d6efd",
    "button_fg": "white",
}

DARK_THEME = {
    "window_bg": "#1e1e1e",
    "frame_bg": "#2d2d2d",
    "title_bg": "#111111",
    "title_fg": "white",
    "text": "white",
    "button_bg": "#444444",
    "button_fg": "white",
}

current_theme = LIGHT_THEME


def toggle_theme():

    global current_theme

    if current_theme == LIGHT_THEME:

        current_theme = DARK_THEME

    else:

        current_theme = LIGHT_THEME

    return current_theme


def get_theme():

    return current_theme
