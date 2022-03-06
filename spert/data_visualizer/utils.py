import argparse


def create_arguments(): 
    parser = argparse.ArgumentParser(
        description='Convert json prediction to BERT visualizer format')
    parser.add_argument('--o', dest='origen', nargs='+',
                        help='Path to JSON file') 
    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Destination of BERT File')
    args = parser.parse_args()
    return args


def center(win): 
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
    win.update_idletasks()
