import tkinter as tk

text_input = [[]]
cursor_row = 0
cursor_column = 0

def update_canvas():
    canvas.delete('all')
    text = "\n".join("".join(row) for row in text_input)
    canvas.create_text(10, 10, anchor='nw', text=text, font=("Consolas", 12))

def keypress(event):
    global cursor_row, cursor_column
    if event.char:  # Ignore special keys
        if cursor_column <= 40:
            text_input[cursor_row].insert(cursor_column, event.char)
            cursor_column += 1
        elif cursor_column > 40:
            cursor_row += 1
            cursor_column = 0
            text_input.append([])
        update_canvas()

window = tk.Tk()
window.title('Vic Text Editor')

canvas = tk.Canvas(window, width=550, height=400, background='gray75')
canvas.focus_set()
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the keypress event to the canvas
canvas.bind("<KeyPress>", keypress)

def backspace(event):
    global cursor_row, cursor_column
    if cursor_column > 0:
        text_input[cursor_row].pop(cursor_column - 1)
        cursor_column -= 1 
    elif cursor_column == 0 and cursor_row > 0:
        text_input.pop(cursor_row)
        cursor_row -= 1
        cursor_column = 41
    update_canvas()

def delete(event):
    global cursor_row, cursor_column
    if cursor_column < len(text_input[cursor_row]):
        text_input[cursor_row].pop(cursor_column)
    elif cursor_column == 40:
        text_input[cursor_row][cursor_column] = text_input[cursor_row + 1][cursor_column]
        text_input[cursor_row + 1].pop()
        if len(text_input[cursor_row + 1]) == 0:
            text_input[cursor_row + 1].pop()
    update_canvas()

canvas.bind("<BackSpace>", backspace)
canvas.bind("<Delete>", delete)

def left_movement(event):
    global cursor_row, cursor_column
    if cursor_column > 0:
        cursor_column -= 1
    elif cursor_column == 0 and cursor_row > 0:
        cursor_column == 40
        cursor_row -= 1
    update_canvas()

def right_movement(event):
    global cursor_row, cursor_column
    if cursor_column < len(text_input[cursor_row]):
        cursor_column += 1
    elif cursor_column == 40:
        cursor_row +=1
    update_canvas()

canvas.bind("<Left>", left_movement)
canvas.bind("<Right>", right_movement)

window.mainloop()