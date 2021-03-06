import tkinter
import time
import random
import numpy

root = tkinter.Tk()
root.geometry('1540x800')
root.title('Multi Color Puzzle')
canvas = tkinter.Canvas(root, width=1540, height=800, bg="gold")
canvas.place(x=0, y=0)

index = 0
key = ""


def key_down(e):
    global key, index
    key = e.keysym
    if index == 0:
        if key == "space":
            canvas.delete("all")
            label.place_forget()
            index += 1
            main_two()


def square(canvas):
    canvas.create_rectangle(x1, y1, x1 + 50, y1 + 50, fill=color)
    canvas.create_rectangle(x1 + 30, y1 + 5, x1 + 45, y1 + 10, fill="white", outline="white", width=0)
    canvas.create_rectangle(x1 + 40, y1 + 10, x1 + 45, y1 + 20, fill="white", width=0)
    canvas.create_rectangle(x1 + 40, y1 + 25, x1 + 45, y1 + 30, fill="white", outline="black", width=1)
    canvas.create_line(x1 + 30, y1 + 5, x1 + 45, y1 + 5, x1 + 45, y1 + 5, x1 + 45, y1 + 20, x1 + 40, y1 + 20, x1 + 45,
                       y1 + 20, fill="black", width=1)
    canvas.create_line(x1 + 30, y1 + 5, x1 + 30, y1 + 10, x1 + 30, y1 + 10, x1 + 40, y1 + 10, x1 + 40, y1 + 10, x1 + 40,
                       y1 + 20, fill="black", width=1)


def now_square(canvas):
    canvas.create_rectangle(x3, y3, x3 + 70, y3 + 70, fill="#E6E6FA", outline="navy", width=4)


x2 = 250
y2 = 70


def main_one():
    global index, key, label
    if index == 0:
        label = tkinter.Label(text="SPACE KEY を押してスタート", font=("system", 30), bg="gold")
        label.place(x=550, y=200)


def block():
    global block_number, brn
    block_number = random.randint(1, 24)
    brn = block_number


list_move = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]

numlist = []


def block_move_sub():
    global label2, index, label5, numlist
    canvas.delete("all")
    label2 = tkinter.Label(text="GAMEOVER", font=("system", 500), bg="gold")
    label2.place(x=550, y=200)
    label3.place_forget()
    index += 1
    numlist.extend([score])
    label5 = tkinter.Label(text="最高得点は" + str(max(numlist)), font=("system", 50))
    label5.place(x=10, y=720)
    label6.place_forget()
    label7.place_forget()
    label8.place_forget()
    label9.place_forget()
    label10.place_forget()
    label11.place_forget()
    label12.place_forget()
    label13.place_forget()
    label14.place_forget()
    label15.place_forget()
    label16.place_forget()
    label17.place_forget()
    label18.place_forget()
    label19.place_forget()
    label20.place_forget()
    label21.place_forget()
    label22.place_forget()
    label23.place_forget()
    label24.place_forget()
    label25.place_forget()
    label26.place_forget()
    label27.place_forget()
    label28.place_forget()
    label29.place_forget()
    root.after(5000, main_two_sub)


def block_move(e):
    global x1, y1, exlist, point_x, point_y, eylist, exlistArray, eylistArray, pos_x, pos_y, score, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, label16, label17, label18, label19, label20, label21, label22, label23, label24, label25, label26, label27, label28, label29
    if index == 1:
        point_x = e.x
        point_y = e.y
        exlist = [495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045]
        exlistArray = numpy.array(exlist)
        pos_x = (numpy.abs(exlistArray - point_x)).argmin()
        eylist = [125, 175, 225, 275, 325, 375, 375, 425, 475, 525, 575, 625, 675]
        eylistArray = numpy.array(eylist)
        pos_y = (numpy.abs(eylistArray - point_y)).argmin()
        exnumber = exlistArray[pos_x] - 25
        eynumber = eylistArray[pos_y] - 25
        list_number = int(((exnumber - 470) / 50 + (eynumber - 100) / 50 * 12) + 12)
        if list_move[list_number] == 0:
            if point_x >= 470 and point_x <= 1070 and point_y >= 100 and point_y <= 700:
                x1 = exnumber
                y1 = eynumber
                square(canvas)
                list_move[list_number] = brn
                if list_move[list_number - 1] == brn or list_move[list_number + 1] == brn or list_move[
                    list_number - 12] == brn or list_move[list_number + 12] == brn:
                    root.after(500, block_move_sub)
                else:
                    score += 3
                    score_pack()
                    label6.place_forget()
                    label7.place_forget()
                    label8.place_forget()
                    label9.place_forget()
                    label10.place_forget()
                    label11.place_forget()
                    label12.place_forget()
                    label13.place_forget()
                    label14.place_forget()
                    label15.place_forget()
                    label16.place_forget()
                    label17.place_forget()
                    label18.place_forget()
                    label19.place_forget()
                    label20.place_forget()
                    label21.place_forget()
                    label22.place_forget()
                    label23.place_forget()
                    label24.place_forget()
                    label25.place_forget()
                    label26.place_forget()
                    label27.place_forget()
                    label28.place_forget()
                    label29.place_forget()
                    color_determine()
    else:
        pass


a1 = 6
a2 = 6
a3 = 6
a4 = 6
a5 = 6
a6 = 6
a7 = 6
a8 = 6
a9 = 6
a10 = 6
a11 = 6
a12 = 6
a13 = 6
a14 = 6
a15 = 6
a16 = 6
a17 = 6
a18 = 6
a19 = 6
a20 = 6
a21 = 6
a22 = 6
a23 = 6
a24 = 6


def color_determine():
    global x1, y1, color, score, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, label16, label17, label18, label19, label20, label21, label22, label23, label24, label25, label26, label27, label28, label29
    block()
    w = "white"
    x1 = x3 + 10
    y1 = y3 + 10
    if index == 1:
        if brn == 1 and a1 != 0:
            a1 -= 1
            color = "red"
        elif brn == 2 and a2 != 0:
            a2 -= 1
            color = "blue"
        elif brn == 3 and a3 != 0:
            a3 -= 1
            color = "gold"
        elif brn == 4 and a4 != 0:
            a4 -= 1
            color = "limegreen"
        elif brn == 5 and a5 != 0:
            a5 -= 1
            color = "deeppink"
        elif brn == 6 and a6 != 0:
            a6 -= 1
            color = "purple"
        elif brn == 7 and a7 != 0:
            a7 -= 1
            color = "cyan"
        elif brn == 8 and a8 != 0:
            a8 -= 1
            color = "orange"
        elif brn == 9 and a9 != 0:
            a9 -= 1
            color = "ivory"
        elif brn == 10 and a10 != 0:
            a10 -= 1
            color = "navy"
        elif brn == 11 and a11 != 0:
            a11 -= 1
            color = "violet"
        elif brn == 12 and a12 != 0:
            a12 -= 1
            color = "indianred"
        elif brn == 13 and a13 != 0:
            a13 -= 1
            color = "gainsboro"
        elif brn == 14 and a14 != 0:
            a14 -= 1
            color = "mistyrose"
        elif brn == 15 and a15 != 0:
            a15 -= 1
            color = "skyblue"
        elif brn == 16 and a16 != 0:
            a16 -= 1
            color = "khaki"
        elif brn == 17 and a17 != 0:
            a17 -= 1
            color = "coral"
        elif brn == 18 and a18 != 0:
            a18 -= 1
            color = "greenyellow"
        elif brn == 19 and a19 != 0:
            a19 -= 1
            color = "tan"
        elif brn == 20 and a20 != 0:
            a20 -= 1
            color = "snow"
        elif brn == 21 and a21 != 0:
            a21 -= 1
            color = "maroon"
        elif brn == 22 and a22 != 0:
            a22 -= 1
            color = "olive"
        elif brn == 23 and a23 != 0:
            a23 -= 1
            color = "crimson"
        elif brn == 24 and a24 != 0:
            a24 -= 1
            color = "green"
        else:
            block()
            root.after(1, color_determine)

        label6 = tkinter.Label(text="＝" + str(a1), font=(10), bg=w)
        label6.place(x=45, y=285)
        label7 = tkinter.Label(text="＝" + str(a2), font=(10), bg=w)
        label7.place(x=145, y=285)
        label8 = tkinter.Label(text="＝" + str(a3), font=(10), bg=w)
        label8.place(x=245, y=285)
        label9 = tkinter.Label(text="＝" + str(a4), font=(10), bg=w)
        label9.place(x=45, y=325)
        label10 = tkinter.Label(text="＝" + str(a5), font=(10), bg=w)
        label10.place(x=145, y=325)
        label11 = tkinter.Label(text="＝" + str(a6), font=(10), bg=w)
        label11.place(x=245, y=325)
        label12 = tkinter.Label(text="＝" + str(a7), font=(10), bg=w)
        label12.place(x=45, y=365)
        label13 = tkinter.Label(text="＝" + str(a8), font=(10), bg=w)
        label13.place(x=145, y=365)
        label14 = tkinter.Label(text="＝" + str(a9), font=(10), bg=w)
        label14.place(x=245, y=365)
        label15 = tkinter.Label(text="＝" + str(a10), font=(10), bg=w)
        label15.place(x=45, y=405)
        label16 = tkinter.Label(text="＝" + str(a11), font=(10), bg=w)
        label16.place(x=145, y=405)
        label17 = tkinter.Label(text="＝" + str(a12), font=(10), bg=w)
        label17.place(x=245, y=405)
        label18 = tkinter.Label(text="＝" + str(a13), font=(10), bg=w)
        label18.place(x=45, y=445)
        label19 = tkinter.Label(text="＝" + str(a14), font=(10), bg=w)
        label19.place(x=145, y=445)
        label20 = tkinter.Label(text="＝" + str(a15), font=(10), bg=w)
        label20.place(x=245, y=445)
        label21 = tkinter.Label(text="＝" + str(a16), font=(10), bg=w)
        label21.place(x=45, y=485)
        label22 = tkinter.Label(text="＝" + str(a17), font=(10), bg=w)
        label22.place(x=145, y=485)
        label23 = tkinter.Label(text="＝" + str(a18), font=(10), bg=w)
        label23.place(x=245, y=485)
        label24 = tkinter.Label(text="＝" + str(a19), font=(10), bg=w)
        label24.place(x=45, y=525)
        label25 = tkinter.Label(text="＝" + str(a20), font=(10), bg=w)
        label25.place(x=145, y=525)
        label26 = tkinter.Label(text="＝" + str(a21), font=(10), bg=w)
        label26.place(x=245, y=525)
        label27 = tkinter.Label(text="＝" + str(a22), font=(10), bg=w)
        label27.place(x=45, y=565)
        label28 = tkinter.Label(text="＝" + str(a23), font=(10), bg=w)
        label28.place(x=145, y=565)
        label29 = tkinter.Label(text="＝" + str(a24), font=(10), bg=w)
        label29.place(x=245, y=565)

        square(canvas)
        score_pack()


def canvas_delete_all():
    canvas.delete("all")
    main_tree()


def main_two():
    global score
    canvas.create_rectangle(0, 0, 1540, 1540, fill="black")
    score = 0
    root.after(3000, canvas_delete_all)


def main_two_sub():
    global index, list_move, score, label2, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24
    label2.place_forget()
    score = 0
    score_pack()
    index -= 1
    list_move = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
    a1 = 6
    a2 = 6
    a3 = 6
    a4 = 6
    a5 = 6
    a6 = 6
    a7 = 6
    a8 = 6
    a9 = 6
    a10 = 6
    a11 = 6
    a12 = 6
    a13 = 6
    a14 = 6
    a15 = 6
    a16 = 6
    a17 = 6
    a18 = 6
    a19 = 6
    a20 = 6
    a21 = 6
    a22 = 6
    a23 = 6
    a24 = 6
    if __name__ == "__main__":
        main_two()


score = 0


def score_pack():
    global label4
    label4.place_forget()
    label4 = tkinter.Label(text="SCORE＝" + str(score), font=("systm", 50))
    label4.place(x=10, y=170)


def main_tree():
    global x3, y3, label3, label4
    label3 = tkinter.Label(text="LEVEL1", font=("system", 70))
    label3.place(x=10, y=10)
    label4 = tkinter.Label(text="SCORE＝" + str(score), font=("systm", 50))
    label4.place(x=10, y=170)
    canvas.create_rectangle(470, 100, 470 + 600, 100 + 600, fill="#E6E6FA", width=0)
    canvas.create_rectangle(420, 50, 470, 750, fill="#006400", width=0)
    canvas.create_rectangle(420, 50, 1120, 100, fill="#006400", width=0)
    canvas.create_rectangle(1070, 50, 1120, 750, fill="#006400", width=0)
    canvas.create_rectangle(420, 700, 1120, 750, fill="#006400", width=0)
    for i in range(13):
        y = i * 50 + 100
        canvas.create_line(470, y, 1070, y, fill="black")
        x = i * 50 + 470
        canvas.create_line(x, 100, x, 700, fill="black")
    (x3, y3) = 1200, 200
    now_square(canvas)
    canvas.create_rectangle(10, 280, 300, 600, fill="white")
    canvas.create_rectangle(20, 290, 40, 310, fill="red")
    canvas.create_rectangle(120, 290, 140, 310, fill="blue")
    canvas.create_rectangle(220, 290, 240, 310, fill="gold")
    canvas.create_rectangle(20, 330, 40, 350, fill="limegreen")
    canvas.create_rectangle(120, 330, 140, 350, fill="deeppink")
    canvas.create_rectangle(220, 330, 240, 350, fill="purple")
    canvas.create_rectangle(20, 370, 40, 390, fill="cyan")
    canvas.create_rectangle(120, 370, 140, 390, fill="orange")
    canvas.create_rectangle(220, 370, 240, 390, fill="ivory")
    canvas.create_rectangle(20, 410, 40, 430, fill="navy")
    canvas.create_rectangle(120, 410, 140, 430, fill="violet")
    canvas.create_rectangle(220, 410, 240, 430, fill="indianred")
    canvas.create_rectangle(20, 450, 40, 470, fill="gainsboro")
    canvas.create_rectangle(120, 450, 140, 470, fill="mistyrose")
    canvas.create_rectangle(220, 450, 240, 470, fill="skyblue")
    canvas.create_rectangle(20, 490, 40, 510, fill="khaki")
    canvas.create_rectangle(120, 490, 140, 510, fill="coral")
    canvas.create_rectangle(220, 490, 240, 510, fill="greenyellow")
    canvas.create_rectangle(20, 530, 40, 550, fill="tan")
    canvas.create_rectangle(120, 530, 140, 550, fill="snow")
    canvas.create_rectangle(220, 530, 240, 550, fill="maroon")
    canvas.create_rectangle(20, 570, 40, 590, fill="olive")
    canvas.create_rectangle(120, 570, 140, 590, fill="crimson")
    canvas.create_rectangle(220, 570, 240, 590, fill="green")
    color_determine()
    canvas.bind("<1>", block_move)


if __name__ == "__main__": main_one()

root.bind("<Key>", key_down)
root.mainloop()
