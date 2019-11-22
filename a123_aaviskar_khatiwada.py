#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height= -200
apple_letter_x_offset= -25
apple_letter_y_offset= -50

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")

screen_width=400
screen_height=400

font_setup = ("Arial", 74, "bold")
wn.tracer(False)
alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_choice = rand.choice(alphabet)
current_letter= "a"

current_letters= []
apple_list= []
number_of_apples= 5

# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  wn.update()

def drop_apple(letter):
  wn.tracer(True)
  index = current_letters.index(letter)
  current_letters.pop(index)
  active_apple = apple_list.pop(index) 
  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position= active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset, + active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font= font_setup)
  active_apple.setpos(remember_position)

def reset_apple(active_apple):
  global current_letter
  length_of_list= len(alphabet)
  if(length_of_list != 0):
    index= rand.randint(0, length_of_list)
    current_letter= alphabet.pop(index)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height/2)))
    draw_apple(active_apple,current_letter)
    current_letters.append(current_letter)

for i in range(number_of_apples):
  active_apple= trtl.Turtle(shape = apple_image)
  active_apple.penup()
  reset_apple(active_apple)
  apple_list.append(active_apple)


def check_letter_A():
  if ("a" in current_letters):
    drop_apple("a")
def check_letter_B():
  if ("b" in current_letters):
    drop_apple("b")
def check_letter_C():
  if ("c" in current_letters):
    drop_apple("c")
def check_letter_D():
  if ("d" in current_letters):
    drop_apple("d")
def check_letter_E():
  if ("e" in current_letters):
    drop_apple("e")
def check_letter_F():
  if ("f" in current_letters):
    drop_apple("f")
def check_letter_G():
  if ("g" in current_letters):
    drop_apple("g")
def check_letter_H():
  if ("h" in current_letters):
    drop_apple("h")
def check_letter_I():
  if ("i" in current_letters):
    drop_apple("i")
def check_letter_J():
  if ("j" in current_letters):
    drop_apple("j")
def check_letter_K():
  if ("k" in current_letters):
    drop_apple("k")
def check_letter_L():
  if ("l"in current_letters):
    drop_apple("l")
def check_letter_M():
  if ("m" in current_letters):
    drop_apple("m")
def check_letter_N():
  if ("n" in current_letters):
    drop_apple("n")
def check_letter_O():
  if ("o" in current_letters):
    drop_apple("o")
def check_letter_P():
  if ("o" in current_letters):
    drop_apple("o")
def check_letter_Q():
  if ("q" in current_letters):
    drop_apple("q")
def check_letter_R():
  if ("r" in current_letters):
    drop_apple()
def check_letter_S():
  if ("s" in current_letters):
    drop_apple("s")
def check_letter_T():
  if ("t" in current_letters):
    drop_apple("t")
def check_letter_U():
  if ("u" in current_letters):
    drop_apple("u")
def check_letter_V():
  if ("v" in current_letters):
    drop_apple("v")
def check_letter_W():
  if ("w" in current_letters):
    drop_apple("w")
def check_letter_X():
  if ("x" in current_letters):
    drop_apple("x")
def check_letter_Y():
  if ("y" in current_letters):
    drop_apple("y")
def check_letter_Z():
  if ("z" in current_letters):
    drop_apple("z")



wn.onkeypress(check_letter_A, "a")
wn.onkeypress(check_letter_B, "b")
wn.onkeypress(check_letter_C, "c")
wn.onkeypress(check_letter_D, "d")
wn.onkeypress(check_letter_E, "e")
wn.onkeypress(check_letter_F, "f")
wn.onkeypress(check_letter_G, "g")
wn.onkeypress(check_letter_H, "h")
wn.onkeypress(check_letter_I, "i")
wn.onkeypress(check_letter_J, "j")
wn.onkeypress(check_letter_K, "k")
wn.onkeypress(check_letter_L, "l")
wn.onkeypress(check_letter_M, "m")
wn.onkeypress(check_letter_N, "n")
wn.onkeypress(check_letter_O, "o")
wn.onkeypress(check_letter_P, "p")
wn.onkeypress(check_letter_Q, "q")
wn.onkeypress(check_letter_R, "r")
wn.onkeypress(check_letter_S, "s")
wn.onkeypress(check_letter_T, "t")
wn.onkeypress(check_letter_U, "u")
wn.onkeypress(check_letter_V, "v")
wn.onkeypress(check_letter_W, "w")
wn.onkeypress(check_letter_X, "x")
wn.onkeypress(check_letter_Y, "y")
wn.onkeypress(check_letter_Z, "z")

wn.listen()

trtl.mainloop()