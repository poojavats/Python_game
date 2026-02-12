"""
╔══════════════════════════════════════════════════════════════╗
║          🙏  CHAKRA PYTHON QUEST  🙏                        ║
║     Learn Python Through the 7 Chakras of Wisdom            ║
║     A Spiritual Journey from Beginner to Advanced           ║
╚══════════════════════════════════════════════════════════════╝

Journey through the 7 Chakras to master Python:
  1. Muladhara (Root)        → Python Basics
  2. Svadhisthana (Sacral)   → Data Types & Operators
  3. Manipura (Solar Plexus) → Control Flow
  4. Anahata (Heart)         → Functions
  5. Vishuddha (Throat)      → Data Structures
  6. Ajna (Third Eye)        → OOP & Classes
  7. Sahasrara (Crown)       → Advanced Python
"""

import pygame
import sys
import math
import random
import json
import os
import time

# ─── Initialize Pygame ───────────────────────────────────────
pygame.init()
pygame.mixer.init()

# ─── Screen Setup ─────────────────────────────────────────────
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chakra Python Quest - Learn Python Through Spiritual Wisdom")

# ─── Clock ────────────────────────────────────────────────────
clock = pygame.time.Clock()
FPS = 60

# ─── Colors ───────────────────────────────────────────────────
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GOLD        = (255, 215, 0)
DARK_GOLD   = (184, 134, 11)
SAFFRON     = (255, 153, 51)
DEEP_ORANGE = (255, 87, 34)
CREAM       = (255, 253, 240)
DARK_BG     = (15, 10, 30)
DARK_PANEL  = (25, 20, 45)
LIGHT_PANEL = (35, 30, 55)
GREEN       = (76, 175, 80)
DARK_GREEN  = (46, 125, 50)
RED_SOFT    = (229, 115, 115)
BLUE_SOFT   = (100, 181, 246)
SHADOW      = (10, 5, 20)
GREY        = (158, 158, 158)
SILVER      = (192, 192, 192)

# ─── Chakra Definitions ──────────────────────────────────────
CHAKRAS = [
    {
        "name": "Muladhara", "english": "Root Chakra",
        "topic": "Python Basics",
        "color": (220, 50, 50),       # Red
        "glow":  (255, 100, 100),
        "symbol": "LAM",
        "mantra": "I exist. I begin my Python journey.",
        "description": "Variables, Print, Input, Comments",
    },
    {
        "name": "Svadhisthana", "english": "Sacral Chakra",
        "topic": "Data Types & Operators",
        "color": (255, 140, 0),        # Orange
        "glow":  (255, 180, 80),
        "symbol": "VAM",
        "mantra": "I feel. I understand data.",
        "description": "Strings, Numbers, Booleans, Operators",
    },
    {
        "name": "Manipura", "english": "Solar Plexus",
        "topic": "Control Flow",
        "color": (255, 215, 0),        # Yellow
        "glow":  (255, 235, 100),
        "symbol": "RAM",
        "mantra": "I do. I control the flow.",
        "description": "If/Else, For, While, Break/Continue",
    },
    {
        "name": "Anahata", "english": "Heart Chakra",
        "topic": "Functions",
        "color": (76, 175, 80),        # Green
        "glow":  (130, 220, 130),
        "symbol": "YAM",
        "mantra": "I love. I create with functions.",
        "description": "def, return, args, lambda",
    },
    {
        "name": "Vishuddha", "english": "Throat Chakra",
        "topic": "Data Structures",
        "color": (66, 165, 245),       # Blue
        "glow":  (130, 200, 255),
        "symbol": "HAM",
        "mantra": "I speak. I structure knowledge.",
        "description": "Lists, Dicts, Sets, Tuples",
    },
    {
        "name": "Ajna", "english": "Third Eye",
        "topic": "OOP & Classes",
        "color": (103, 58, 183),       # Indigo
        "glow":  (160, 120, 230),
        "symbol": "OM",
        "mantra": "I see. I see the object within.",
        "description": "Classes, Inheritance, Polymorphism",
    },
    {
        "name": "Sahasrara", "english": "Crown Chakra",
        "topic": "Advanced Python",
        "color": (200, 140, 255),      # Violet
        "glow":  (230, 190, 255),
        "symbol": "AUM",
        "mantra": "I understand. I have mastered Python.",
        "description": "Decorators, Generators, Comprehensions",
    },
]

# ─── Questions Database ──────────────────────────────────────
QUESTIONS = {
    0: [  # Muladhara - Python Basics
        {
            "q": "What is the correct way to print\n'Hello World' in Python?",
            "options": ["echo 'Hello World'", "print('Hello World')", "printf('Hello World')", "System.out.print('Hello')"],
            "answer": 1,
            "explanation": "In Python, print() is the built-in\nfunction to display output.",
            "teaching": "print() sends text to the screen.\nExample: print('Namaste!')"
        },
        {
            "q": "How do you create a variable\nnamed 'age' with value 25?",
            "options": ["int age = 25", "var age = 25", "age = 25", "let age = 25"],
            "answer": 2,
            "explanation": "Python uses simple assignment.\nNo type declaration needed!",
            "teaching": "Variables store data.\nJust write: name = value"
        },
        {
            "q": "Which symbol is used for\nsingle-line comments in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": 1,
            "explanation": "The # symbol starts a comment.\nEverything after # is ignored.",
            "teaching": "Comments explain code:\n# This is a comment"
        },
        {
            "q": "What does input() do in Python?",
            "options": ["Displays output", "Takes user input", "Deletes data", "Creates a file"],
            "answer": 1,
            "explanation": "input() pauses the program and\nwaits for the user to type something.",
            "teaching": "name = input('Enter name: ')\nThis stores what the user types."
        },
        {
            "q": "What will print(type(10)) show?",
            "options": ["<class 'str'>", "<class 'float'>", "<class 'int'>", "<class 'num'>"],
            "answer": 2,
            "explanation": "10 is a whole number, so Python\nrecognizes it as an integer (int).",
            "teaching": "type() tells you what kind of\ndata a value is."
        },
    ],
    1: [  # Svadhisthana - Data Types & Operators
        {
            "q": "What is the result of\n10 / 3 in Python 3?",
            "options": ["3", "3.333...", "3.0", "Error"],
            "answer": 1,
            "explanation": "/ always returns a float in\nPython 3. Use // for integer division.",
            "teaching": "/ = true division (3.33)\n// = floor division (3)"
        },
        {
            "q": "Which is a valid string\nin Python?",
            "options": ["'hello'", "\"hello\"", "'''hello'''", "All of the above"],
            "answer": 3,
            "explanation": "Python accepts single quotes,\ndouble quotes, and triple quotes!",
            "teaching": "Strings hold text. You can use\n'single', \"double\", or '''triple'''."
        },
        {
            "q": "What does ** operator do?",
            "options": ["Multiplication", "Exponentiation", "Modulus", "Division"],
            "answer": 1,
            "explanation": "** is the power operator.\n2**3 = 8 (2 to the power of 3)",
            "teaching": "2 ** 3 = 8\n10 ** 2 = 100"
        },
        {
            "q": "What is bool('') in Python?",
            "options": ["True", "False", "None", "Error"],
            "answer": 1,
            "explanation": "An empty string is 'falsy' in\nPython. bool('') returns False.",
            "teaching": "Falsy values: 0, '', [], None, False\nEverything else is Truthy!"
        },
        {
            "q": "What does 'Hello' + ' ' + 'World' give?",
            "options": ["HelloWorld", "Hello World", "Error", "Hello+World"],
            "answer": 1,
            "explanation": "The + operator concatenates\n(joins) strings together.",
            "teaching": "String concatenation joins text:\n'Na' + 'ma' + 'ste' = 'Namaste'"
        },
    ],
    2: [  # Manipura - Control Flow
        {
            "q": "What keyword starts a\nconditional statement?",
            "options": ["switch", "if", "when", "case"],
            "answer": 1,
            "explanation": "Python uses if/elif/else\nfor conditional branching.",
            "teaching": "if age >= 18:\n    print('Adult')\nelse:\n    print('Minor')"
        },
        {
            "q": "What does 'for i in range(5)'\niterate through?",
            "options": ["1 to 5", "0 to 5", "0 to 4", "1 to 4"],
            "answer": 2,
            "explanation": "range(5) generates 0,1,2,3,4.\nIt starts at 0 and stops before 5.",
            "teaching": "range(5) = [0,1,2,3,4]\nrange(1,5) = [1,2,3,4]"
        },
        {
            "q": "Which keyword exits a\nloop immediately?",
            "options": ["stop", "exit", "break", "end"],
            "answer": 2,
            "explanation": "break exits the nearest\nenclosing loop immediately.",
            "teaching": "for i in range(10):\n    if i == 5: break\n# stops at 5"
        },
        {
            "q": "What does 'continue' do\ninside a loop?",
            "options": ["Stops the loop", "Skips to next iteration", "Restarts the loop", "Exits program"],
            "answer": 1,
            "explanation": "continue skips the rest of the\ncurrent iteration and moves to next.",
            "teaching": "for i in range(5):\n    if i == 2: continue\n# skips 2, prints 0,1,3,4"
        },
        {
            "q": "How do you write an\ninfinite loop?",
            "options": ["for(;;)", "loop:", "while True:", "repeat:"],
            "answer": 2,
            "explanation": "while True: creates a loop that\nruns forever until break is used.",
            "teaching": "while True:\n    cmd = input('> ')\n    if cmd == 'quit': break"
        },
    ],
    3: [  # Anahata - Functions
        {
            "q": "Which keyword is used to\ndefine a function?",
            "options": ["func", "function", "def", "define"],
            "answer": 2,
            "explanation": "Python uses 'def' to define\nfunctions. Short for 'define'.",
            "teaching": "def greet(name):\n    return 'Namaste, ' + name"
        },
        {
            "q": "What does 'return' do\nin a function?",
            "options": ["Prints output", "Sends back a value", "Stops the program", "Creates a variable"],
            "answer": 1,
            "explanation": "return sends a value back to\nwhere the function was called.",
            "teaching": "def add(a, b):\n    return a + b\nresult = add(3, 4)  # 7"
        },
        {
            "q": "What is a lambda function?",
            "options": ["A named function", "An anonymous function", "A class method", "A module"],
            "answer": 1,
            "explanation": "Lambda creates small anonymous\n(unnamed) functions in one line.",
            "teaching": "square = lambda x: x ** 2\nprint(square(5))  # 25"
        },
        {
            "q": "What are *args in a function?",
            "options": ["Required arguments", "Variable positional args", "Keyword arguments", "Default arguments"],
            "answer": 1,
            "explanation": "*args lets a function accept\nany number of positional arguments.",
            "teaching": "def add(*args):\n    return sum(args)\nadd(1,2,3)  # 6"
        },
        {
            "q": "What is a default parameter?",
            "options": ["Must be provided", "Has a preset value", "Is always None", "Is a global variable"],
            "answer": 1,
            "explanation": "Default parameters have values\nused when no argument is passed.",
            "teaching": "def greet(name='World'):\n    print('Hello', name)\ngreet()  # Hello World"
        },
    ],
    4: [  # Vishuddha - Data Structures
        {
            "q": "How do you create an\nempty list in Python?",
            "options": ["list = {}", "list = []", "list = ()", "list = <>"],
            "answer": 1,
            "explanation": "Square brackets [] create lists.\n{} is for dicts, () for tuples.",
            "teaching": "fruits = ['apple', 'mango']\nfruits.append('banana')"
        },
        {
            "q": "How do you access the value\nfor key 'name' in a dict?",
            "options": ["d.name", "d['name']", "d(name)", "d->name"],
            "answer": 1,
            "explanation": "Dictionary values are accessed\nusing square brackets with the key.",
            "teaching": "person = {'name': 'Arjun'}\nprint(person['name'])  # Arjun"
        },
        {
            "q": "What is special about a tuple?",
            "options": ["It's mutable", "It's immutable", "It's unordered", "It has no duplicates"],
            "answer": 1,
            "explanation": "Tuples cannot be changed after\ncreation. They are immutable.",
            "teaching": "point = (10, 20)\n# point[0] = 5  # ERROR!\n# Use lists if you need to change."
        },
        {
            "q": "What does set() remove\nfrom a collection?",
            "options": ["All items", "First item", "Duplicates", "None values"],
            "answer": 2,
            "explanation": "Sets only store unique values.\nDuplicates are automatically removed.",
            "teaching": "nums = [1,2,2,3,3]\nunique = set(nums)  # {1,2,3}"
        },
        {
            "q": "What does list slicing\nnums[1:4] return?",
            "options": ["Elements 1 to 4", "Elements 1 to 3", "Elements 0 to 3", "Elements 1 to 5"],
            "answer": 1,
            "explanation": "Slicing [1:4] gets elements at\nindex 1, 2, 3 (end is exclusive).",
            "teaching": "nums = [10,20,30,40,50]\nnums[1:4] = [20, 30, 40]"
        },
    ],
    5: [  # Ajna - OOP & Classes
        {
            "q": "Which keyword creates a\nclass in Python?",
            "options": ["struct", "object", "class", "type"],
            "answer": 2,
            "explanation": "The 'class' keyword defines\na new class (blueprint for objects).",
            "teaching": "class Dog:\n    def __init__(self, name):\n        self.name = name"
        },
        {
            "q": "What is __init__ in a class?",
            "options": ["Destructor", "Constructor", "Iterator", "Decorator"],
            "answer": 1,
            "explanation": "__init__ is called automatically\nwhen an object is created.",
            "teaching": "class Person:\n    def __init__(self, name):\n        self.name = name\np = Person('Krishna')"
        },
        {
            "q": "What is 'self' in a class?",
            "options": ["A global variable", "Reference to current instance", "The class name", "A keyword"],
            "answer": 1,
            "explanation": "'self' refers to the current\nobject instance of the class.",
            "teaching": "self.name stores 'name' as\nan attribute of THIS object."
        },
        {
            "q": "What is inheritance in OOP?",
            "options": ["Copying code", "Child class gets parent features", "Deleting a class", "Creating objects"],
            "answer": 1,
            "explanation": "Inheritance lets a child class\ninherit attributes and methods.",
            "teaching": "class Animal:\n    ...\nclass Dog(Animal):\n    # Dog inherits from Animal"
        },
        {
            "q": "What is polymorphism?",
            "options": ["Multiple inheritance", "Same interface, different behavior", "Hiding data", "Creating objects"],
            "answer": 1,
            "explanation": "Polymorphism means the same method\ncan behave differently in subclasses.",
            "teaching": "cat.speak() -> 'Meow'\ndog.speak() -> 'Woof'\nSame method, different results!"
        },
    ],
    6: [  # Sahasrara - Advanced Python
        {
            "q": "What is a decorator\nin Python?",
            "options": ["A design pattern", "A function that modifies another function", "A class method", "A comment style"],
            "answer": 1,
            "explanation": "Decorators wrap functions to\nextend behavior without modifying them.",
            "teaching": "@timer\ndef slow_func():\n    ...\n# @timer adds timing to the func"
        },
        {
            "q": "What does 'yield' do\nin a function?",
            "options": ["Returns and stops", "Pauses and produces a value", "Raises an error", "Creates a class"],
            "answer": 1,
            "explanation": "yield makes a function a generator.\nIt pauses and resumes execution.",
            "teaching": "def count(n):\n    for i in range(n):\n        yield i\n# Memory efficient iteration!"
        },
        {
            "q": "What is a list comprehension?",
            "options": ["A loop inside print()", "A concise way to create lists", "A type of sorting", "A class feature"],
            "answer": 1,
            "explanation": "List comprehensions create lists\nin a single, elegant line.",
            "teaching": "squares = [x**2 for x in range(5)]\n# [0, 1, 4, 9, 16]"
        },
        {
            "q": "What does 'with' statement do?",
            "options": ["Creates a loop", "Manages resources safely", "Defines a class", "Imports a module"],
            "answer": 1,
            "explanation": "'with' ensures resources like files\nare properly closed after use.",
            "teaching": "with open('data.txt') as f:\n    text = f.read()\n# File auto-closes!"
        },
        {
            "q": "What is the difference between\n'is' and '==' in Python?",
            "options": ["No difference", "'is' checks identity, '==' checks value", "'is' is faster", "'==' checks identity"],
            "answer": 1,
            "explanation": "'==' compares values.\n'is' checks if both are the SAME object.",
            "teaching": "a = [1,2]; b = [1,2]\na == b  # True (same value)\na is b  # False (different objects)"
        },
    ],
}

# ─── Save File Path ──────────────────────────────────────────
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chakra_save.json")

# ─── Fonts ────────────────────────────────────────────────────
def load_fonts():
    """Load fonts with fallbacks."""
    fonts = {}
    try:
        fonts["title"]   = pygame.font.SysFont("Georgia", 52, bold=True)
        fonts["heading"]  = pygame.font.SysFont("Georgia", 36, bold=True)
        fonts["medium"]   = pygame.font.SysFont("Segoe UI", 24)
        fonts["body"]     = pygame.font.SysFont("Segoe UI", 20)
        fonts["small"]    = pygame.font.SysFont("Segoe UI", 16)
        fonts["tiny"]     = pygame.font.SysFont("Segoe UI", 14)
        fonts["sanskrit"] = pygame.font.SysFont("Georgia", 28, bold=True)
        fonts["code"]     = pygame.font.SysFont("Consolas", 18)
        fonts["big_sym"]  = pygame.font.SysFont("Georgia", 72, bold=True)
    except Exception:
        default = pygame.font.SysFont(None, 24)
        for key in ["title","heading","medium","body","small","tiny","sanskrit","code","big_sym"]:
            fonts[key] = default
    return fonts

FONTS = load_fonts()

# ─── Particle System ─────────────────────────────────────────
class Particle:
    def __init__(self, x, y, color, speed=1.0, size=3):
        self.x = x
        self.y = y
        self.color = color
        self.base_speed = speed
        self.vx = random.uniform(-0.5, 0.5) * speed
        self.vy = random.uniform(-2, -0.5) * speed
        self.life = random.uniform(0.5, 2.0)
        self.max_life = self.life
        self.size = size

    def update(self, dt):
        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60
        self.life -= dt
        return self.life > 0

    def draw(self, surface):
        alpha = max(0, self.life / self.max_life)
        r, g, b = self.color
        color = (min(255, int(r * alpha + 255 * (1 - alpha))),
                 min(255, int(g * alpha + 255 * (1 - alpha))),
                 min(255, int(b * alpha + 255 * (1 - alpha))))
        size = max(1, int(self.size * alpha))
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), size)


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit(self, x, y, color, count=10, speed=1.0, size=3):
        for _ in range(count):
            self.particles.append(Particle(x, y, color, speed, size))

    def update(self, dt):
        self.particles = [p for p in self.particles if p.update(dt)]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)


particles = ParticleSystem()

# ─── Star Background ─────────────────────────────────────────
stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
          random.uniform(0.5, 2.5), random.uniform(0.5, 3.0))
         for _ in range(120)]

def draw_stars(surface, time_val):
    for x, y, size, speed in stars:
        brightness = int(130 + 80 * math.sin(time_val * speed + x))
        brightness = max(50, min(255, brightness))
        color = (brightness, brightness, min(255, brightness + 30))
        pygame.draw.circle(surface, color, (x, y), max(1, int(size)))


# ─── Drawing Helpers ──────────────────────────────────────────
def draw_gradient_rect(surface, rect, color1, color2, vertical=True):
    """Draw a rectangle with a gradient fill."""
    x, y, w, h = rect
    for i in range(h if vertical else w):
        ratio = i / (h if vertical else w)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if vertical:
            pygame.draw.line(surface, (r, g, b), (x, y + i), (x + w, y + i))
        else:
            pygame.draw.line(surface, (r, g, b), (x + i, y), (x + i, y + h))


def draw_om_symbol(surface, cx, cy, size, color, time_val):
    """Draw a stylized OM symbol using curves and lines."""
    alpha = int(180 + 50 * math.sin(time_val * 2))
    glow_size = size + int(8 * math.sin(time_val * 3))

    # Outer glow
    for r in range(glow_size, glow_size - 6, -1):
        a = max(10, alpha - (glow_size - r) * 30)
        glow_color = (min(255, color[0]), min(255, color[1]), min(255, color[2]))
        pygame.draw.circle(surface, glow_color, (cx, cy), r, 1)

    # Draw "OM" text as the symbol
    om_surf = FONTS["big_sym"].render("OM", True, color)
    om_rect = om_surf.get_rect(center=(cx, cy))
    surface.blit(om_surf, om_rect)


def draw_mandala(surface, cx, cy, radius, color, petals=12, time_val=0):
    """Draw a rotating mandala pattern."""
    rotation = time_val * 0.3

    for layer in range(3, 0, -1):
        r = radius * layer / 3
        layer_alpha = 0.4 + 0.2 * layer
        c = tuple(min(255, int(ch * layer_alpha)) for ch in color)

        for i in range(petals):
            angle = (2 * math.pi * i / petals) + rotation * layer
            x1 = cx + r * math.cos(angle)
            y1 = cy + r * math.sin(angle)

            # Petal shape
            angle2 = angle + math.pi / petals
            x2 = cx + r * 0.5 * math.cos(angle2)
            y2 = cy + r * 0.5 * math.sin(angle2)

            pygame.draw.line(surface, c, (cx, cy), (int(x1), int(y1)), 1)
            pygame.draw.circle(surface, c, (int(x1), int(y1)), max(2, int(4 * layer / 3)))

        pygame.draw.circle(surface, c, (cx, cy), int(r), 1)


def draw_lotus(surface, cx, cy, size, color, time_val):
    """Draw a lotus flower."""
    petals = 8
    for i in range(petals):
        angle = (2 * math.pi * i / petals) + math.sin(time_val) * 0.1
        px = cx + size * 0.6 * math.cos(angle)
        py = cy + size * 0.6 * math.sin(angle)

        # Petal (ellipse approximation)
        petal_points = []
        for j in range(20):
            t = j / 19 * math.pi
            lx = px + size * 0.4 * math.cos(angle) * math.sin(t)
            ly = py + size * 0.4 * math.sin(angle) * math.sin(t)
            lx += size * 0.15 * math.cos(angle + math.pi / 2) * math.cos(t)
            ly += size * 0.15 * math.sin(angle + math.pi / 2) * math.cos(t)
            petal_points.append((int(lx), int(ly)))

        if len(petal_points) > 2:
            pygame.draw.polygon(surface, color, petal_points, 2)

    # Center
    pygame.draw.circle(surface, GOLD, (cx, cy), int(size * 0.15))


def draw_chakra_symbol(surface, cx, cy, radius, chakra_idx, time_val, unlocked=True):
    """Draw a chakra circle with glow and symbol."""
    chakra = CHAKRAS[chakra_idx]
    color = chakra["color"] if unlocked else GREY
    glow = chakra["glow"] if unlocked else (100, 100, 100)

    # Outer glow rings
    if unlocked:
        for i in range(4, 0, -1):
            glow_r = radius + i * 4 + int(3 * math.sin(time_val * 2 + chakra_idx))
            alpha_color = tuple(min(255, max(0, c - i * 20)) for c in glow)
            pygame.draw.circle(surface, alpha_color, (cx, cy), glow_r, 2)

    # Main circle
    pygame.draw.circle(surface, color, (cx, cy), radius)
    pygame.draw.circle(surface, WHITE if unlocked else GREY, (cx, cy), radius, 2)

    # Inner symbol text
    sym_surf = FONTS["sanskrit"].render(chakra["symbol"], True, WHITE if unlocked else (80, 80, 80))
    sym_rect = sym_surf.get_rect(center=(cx, cy))
    surface.blit(sym_surf, sym_rect)


def draw_button(surface, rect, text, font, color, text_color=WHITE, hover=False, border_color=None):
    """Draw a rounded button."""
    x, y, w, h = rect
    r = 12  # border radius

    # Shadow
    shadow_rect = pygame.Rect(x + 3, y + 3, w, h)
    pygame.draw.rect(surface, SHADOW, shadow_rect, border_radius=r)

    # Button fill
    btn_color = tuple(min(255, c + 25) for c in color) if hover else color
    btn_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, btn_color, btn_rect, border_radius=r)

    # Border
    bc = border_color or tuple(min(255, c + 50) for c in color)
    pygame.draw.rect(surface, bc, btn_rect, 2, border_radius=r)

    # Text
    txt_surf = font.render(text, True, text_color)
    txt_rect = txt_surf.get_rect(center=(x + w // 2, y + h // 2))
    surface.blit(txt_surf, txt_rect)

    return btn_rect


def draw_text_wrapped(surface, text, font, color, x, y, max_width, line_spacing=5):
    """Draw text with word wrapping."""
    lines = text.split('\n')
    current_y = y
    for line in lines:
        words = line.split(' ')
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] > max_width and current_line:
                txt_surf = font.render(current_line.strip(), True, color)
                surface.blit(txt_surf, (x, current_y))
                current_y += font.get_height() + line_spacing
                current_line = word + ' '
            else:
                current_line = test_line
        if current_line.strip():
            txt_surf = font.render(current_line.strip(), True, color)
            surface.blit(txt_surf, (x, current_y))
            current_y += font.get_height() + line_spacing
    return current_y


def draw_progress_bar(surface, x, y, w, h, progress, color, bg_color=DARK_PANEL):
    """Draw a progress bar."""
    pygame.draw.rect(surface, bg_color, (x, y, w, h), border_radius=h // 2)
    if progress > 0:
        fill_w = max(h, int(w * progress))
        pygame.draw.rect(surface, color, (x, y, fill_w, h), border_radius=h // 2)
    pygame.draw.rect(surface, WHITE, (x, y, w, h), 1, border_radius=h // 2)


# ─── Game State ───────────────────────────────────────────────
class GameState:
    MENU = "menu"
    CHAKRA_MAP = "chakra_map"
    TEACHING = "teaching"
    QUIZ = "quiz"
    RESULT = "result"
    LEVEL_COMPLETE = "level_complete"
    GAME_COMPLETE = "game_complete"

class Game:
    def __init__(self):
        self.state = GameState.MENU
        self.current_chakra = 0
        self.current_question = 0
        self.score = 0
        self.total_answered = 0
        self.correct_answers = 0
        self.chakra_progress = [0] * 7  # 0 = locked, 1-5 = questions done, 6 = complete
        self.chakra_progress[0] = 0     # First chakra unlocked
        self.unlocked_chakras = {0}     # Set of unlocked chakra indices
        self.selected_answer = -1
        self.show_explanation = False
        self.answer_correct = False
        self.time_val = 0
        self.hover_btn = -1
        self.karma_points = 0
        self.transition_alpha = 0
        self.transitioning = False
        self.transition_target = None
        self.menu_anim_offset = 0
        self.notification = ""
        self.notification_timer = 0
        self.notification_color = GREEN

        # Load saved progress
        self.load_progress()

    def save_progress(self):
        data = {
            "chakra_progress": self.chakra_progress,
            "unlocked_chakras": list(self.unlocked_chakras),
            "karma_points": self.karma_points,
            "correct_answers": self.correct_answers,
            "total_answered": self.total_answered,
        }
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump(data, f)
        except Exception:
            pass

    def load_progress(self):
        try:
            if os.path.exists(SAVE_FILE):
                with open(SAVE_FILE, 'r') as f:
                    data = json.load(f)
                self.chakra_progress = data.get("chakra_progress", [0] * 7)
                self.unlocked_chakras = set(data.get("unlocked_chakras", [0]))
                self.karma_points = data.get("karma_points", 0)
                self.correct_answers = data.get("correct_answers", 0)
                self.total_answered = data.get("total_answered", 0)
        except Exception:
            pass

    def show_notification(self, text, color=GREEN):
        self.notification = text
        self.notification_timer = 3.0
        self.notification_color = color

    def start_quiz(self, chakra_idx):
        self.current_chakra = chakra_idx
        self.current_question = self.chakra_progress[chakra_idx]
        if self.current_question >= len(QUESTIONS.get(chakra_idx, [])):
            self.current_question = 0
        self.selected_answer = -1
        self.show_explanation = False
        self.state = GameState.TEACHING

    def answer_question(self, answer_idx):
        if self.show_explanation:
            return
        self.selected_answer = answer_idx
        self.show_explanation = True
        self.total_answered += 1

        q = QUESTIONS[self.current_chakra][self.current_question]
        if answer_idx == q["answer"]:
            self.answer_correct = True
            self.correct_answers += 1
            self.karma_points += 10
            self.show_notification("+10 Karma Points!", GOLD)
            particles.emit(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                          CHAKRAS[self.current_chakra]["color"], 30, 2.0, 4)
        else:
            self.answer_correct = False
            self.show_notification("Keep trying! Learn from this.", RED_SOFT)

    def next_question(self):
        if self.answer_correct:
            self.chakra_progress[self.current_chakra] = self.current_question + 1

        self.current_question += 1
        self.selected_answer = -1
        self.show_explanation = False

        total_q = len(QUESTIONS.get(self.current_chakra, []))

        if self.current_question >= total_q:
            # Level complete!
            self.chakra_progress[self.current_chakra] = total_q
            next_c = self.current_chakra + 1
            if next_c < 7:
                self.unlocked_chakras.add(next_c)
                self.state = GameState.LEVEL_COMPLETE
            else:
                self.state = GameState.GAME_COMPLETE
            self.save_progress()
        else:
            self.state = GameState.TEACHING

    def reset_game(self):
        self.chakra_progress = [0] * 7
        self.unlocked_chakras = {0}
        self.karma_points = 0
        self.correct_answers = 0
        self.total_answered = 0
        self.save_progress()


# ─── Screen Renderers ────────────────────────────────────────

def render_menu(game, mouse_pos, time_val):
    """Render the main menu."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    # Animated mandala in background
    draw_mandala(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30,
                 250, (40, 30, 70), 16, time_val)

    # Title section
    title_y = 80 + int(5 * math.sin(time_val * 0.8))

    # OM Symbol
    draw_om_symbol(screen, SCREEN_WIDTH // 2, title_y, 30, SAFFRON, time_val)

    # Title
    title_text = FONTS["title"].render("CHAKRA PYTHON QUEST", True, GOLD)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, title_y + 75))
    # Shadow
    shadow_text = FONTS["title"].render("CHAKRA PYTHON QUEST", True, (50, 40, 10))
    screen.blit(shadow_text, (title_rect.x + 3, title_rect.y + 3))
    screen.blit(title_text, title_rect)

    # Subtitle
    sub_text = FONTS["medium"].render("Learn Python Through the 7 Chakras of Wisdom", True, SAFFRON)
    sub_rect = sub_text.get_rect(center=(SCREEN_WIDTH // 2, title_y + 125))
    screen.blit(sub_text, sub_rect)

    # Decorative line
    line_y = title_y + 155
    pygame.draw.line(screen, DARK_GOLD, (SCREEN_WIDTH // 2 - 200, line_y),
                     (SCREEN_WIDTH // 2 + 200, line_y), 2)

    # Sanskrit quote
    quote = FONTS["small"].render(
        '"Yoga is the journey of the self, through the self, to the self." - Bhagavad Gita',
        True, (180, 160, 120))
    screen.blit(quote, quote.get_rect(center=(SCREEN_WIDTH // 2, line_y + 25)))

    # Menu buttons
    btn_w, btn_h = 300, 55
    btn_x = SCREEN_WIDTH // 2 - btn_w // 2
    btn_start_y = 340

    buttons = []

    # Start / Continue button
    has_progress = any(p > 0 for p in game.chakra_progress)
    btn_text = "Continue Journey" if has_progress else "Begin Journey"
    hover = pygame.Rect(btn_x, btn_start_y, btn_w, btn_h).collidepoint(mouse_pos)
    btn = draw_button(screen, (btn_x, btn_start_y, btn_w, btn_h), btn_text,
                      FONTS["medium"], (180, 100, 20) if hover else (140, 80, 10),
                      GOLD, hover, SAFFRON)
    buttons.append(("start", btn))

    # New Game button
    y2 = btn_start_y + 75
    hover2 = pygame.Rect(btn_x, y2, btn_w, btn_h).collidepoint(mouse_pos)
    btn2 = draw_button(screen, (btn_x, y2, btn_w, btn_h), "New Journey",
                       FONTS["medium"], (60, 40, 100) if hover2 else (40, 25, 70),
                       SILVER, hover2)
    buttons.append(("new", btn2))

    # Quit button
    y3 = btn_start_y + 150
    hover3 = pygame.Rect(btn_x, y3, btn_w, btn_h).collidepoint(mouse_pos)
    btn3 = draw_button(screen, (btn_x, y3, btn_w, btn_h), "Exit",
                       FONTS["medium"], (80, 30, 30) if hover3 else (60, 20, 20),
                       RED_SOFT, hover3)
    buttons.append(("quit", btn3))

    # Stats at bottom
    if game.total_answered > 0:
        accuracy = game.correct_answers / game.total_answered * 100
        stats_text = f"Karma: {game.karma_points}  |  Accuracy: {accuracy:.0f}%  |  Questions: {game.total_answered}"
    else:
        stats_text = "Your spiritual Python journey awaits..."
    stats_surf = FONTS["small"].render(stats_text, True, (120, 110, 140))
    screen.blit(stats_surf, stats_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)))

    # Mini chakras at bottom
    for i in range(7):
        cx = SCREEN_WIDTH // 2 - 120 + i * 40
        cy = SCREEN_HEIGHT - 25
        r = 8 if i in game.unlocked_chakras else 5
        c = CHAKRAS[i]["color"] if i in game.unlocked_chakras else GREY
        pygame.draw.circle(screen, c, (cx, cy), r)
        if game.chakra_progress[i] >= len(QUESTIONS.get(i, [])) and len(QUESTIONS.get(i, [])) > 0:
            pygame.draw.circle(screen, GOLD, (cx, cy), r + 3, 2)

    return buttons


def render_chakra_map(game, mouse_pos, time_val):
    """Render the chakra map / level select screen."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    # Title
    title = FONTS["heading"].render("The Path of Seven Chakras", True, GOLD)
    screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 40)))

    # Karma display
    karma_text = FONTS["body"].render(f"Karma Points: {game.karma_points}", True, SAFFRON)
    screen.blit(karma_text, (SCREEN_WIDTH - 250, 15))

    buttons = []

    # Draw the chakra path (vertical spine)
    spine_x = 160
    start_y = 600
    spacing = 80

    # Draw connecting line (the spine / Sushumna)
    for i in range(6):
        y1 = start_y - i * spacing
        y2 = start_y - (i + 1) * spacing
        color = CHAKRAS[i]["color"] if i in game.unlocked_chakras else (40, 40, 50)
        pygame.draw.line(screen, color, (spine_x, y1), (spine_x, y2), 3)

    # Draw each chakra node
    for i in range(7):
        cy = start_y - i * spacing
        cx = spine_x
        unlocked = i in game.unlocked_chakras
        chakra = CHAKRAS[i]
        total_q = len(QUESTIONS.get(i, []))
        progress = game.chakra_progress[i]
        complete = progress >= total_q and total_q > 0

        # Draw chakra circle
        draw_chakra_symbol(screen, cx, cy, 28, i, time_val, unlocked)

        # Completion star
        if complete:
            star_x = cx + 35
            star_y = cy - 20
            pygame.draw.polygon(screen, GOLD, [
                (star_x, star_y - 10), (star_x + 4, star_y - 3),
                (star_x + 10, star_y - 3), (star_x + 5, star_y + 2),
                (star_x + 7, star_y + 9), (star_x, star_y + 5),
                (star_x - 7, star_y + 9), (star_x - 5, star_y + 2),
                (star_x - 10, star_y - 3), (star_x - 4, star_y - 3),
            ])

        # Info panel to the right
        panel_x = 220
        panel_y = cy - 32
        panel_w = 530
        panel_h = 65

        # Panel background
        panel_color = (35, 30, 55) if unlocked else (25, 22, 38)
        is_hover = pygame.Rect(panel_x, panel_y, panel_w, panel_h).collidepoint(mouse_pos) and unlocked

        if is_hover:
            panel_color = (50, 42, 75)

        pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_w, panel_h), border_radius=10)
        border_c = chakra["color"] if unlocked else (60, 60, 70)
        pygame.draw.rect(screen, border_c, (panel_x, panel_y, panel_w, panel_h), 2, border_radius=10)

        # Chakra name
        name_color = chakra["color"] if unlocked else GREY
        name_text = FONTS["body"].render(f"{chakra['name']} — {chakra['english']}", True, name_color)
        screen.blit(name_text, (panel_x + 15, panel_y + 5))

        # Topic
        topic_color = WHITE if unlocked else (80, 80, 90)
        topic_text = FONTS["small"].render(f"Topic: {chakra['topic']} | {chakra['description']}", True, topic_color)
        screen.blit(topic_text, (panel_x + 15, panel_y + 30))

        # Progress bar
        bar_x = panel_x + panel_w - 120
        bar_y = panel_y + 8
        bar_w = 100
        bar_h = 12
        prog_ratio = progress / total_q if total_q > 0 else 0
        draw_progress_bar(screen, bar_x, bar_y, bar_w, bar_h, prog_ratio, chakra["color"])
        prog_label = FONTS["tiny"].render(f"{progress}/{total_q}", True, WHITE)
        screen.blit(prog_label, (bar_x + bar_w + 5, bar_y - 2))

        if unlocked:
            buttons.append(("chakra", i, pygame.Rect(panel_x, panel_y, panel_w, panel_h)))

    # Right side: decorative mandala
    draw_mandala(screen, 900, 350, 160, CHAKRAS[game.current_chakra]["color"], 12, time_val)

    # Mantra of current/highest unlocked chakra
    highest = max(game.unlocked_chakras)
    mantra = CHAKRAS[highest]["mantra"]
    mantra_surf = FONTS["small"].render(f'"{mantra}"', True, CHAKRAS[highest]["glow"])
    screen.blit(mantra_surf, mantra_surf.get_rect(center=(900, 520)))

    # Back button
    back_hover = pygame.Rect(20, 15, 100, 40).collidepoint(mouse_pos)
    back_btn = draw_button(screen, (20, 15, 100, 40), "< Back", FONTS["body"],
                           (60, 50, 80) if back_hover else (40, 30, 60), WHITE, back_hover)
    buttons.append(("back", back_btn))

    return buttons


def render_teaching(game, mouse_pos, time_val):
    """Render the teaching screen before a question."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    chakra = CHAKRAS[game.current_chakra]
    q_data = QUESTIONS[game.current_chakra][game.current_question]

    # Header with chakra info
    header_h = 80
    draw_gradient_rect(screen, (0, 0, SCREEN_WIDTH, header_h),
                       tuple(max(0, c // 4) for c in chakra["color"]),
                       DARK_BG)

    # Chakra name + question number
    total_q = len(QUESTIONS[game.current_chakra])
    header_text = f"{chakra['name']} — {chakra['topic']}  (Question {game.current_question + 1}/{total_q})"
    header_surf = FONTS["medium"].render(header_text, True, chakra["glow"])
    screen.blit(header_surf, (30, 15))

    # Progress bar
    prog = (game.current_question) / total_q
    draw_progress_bar(screen, 30, 50, SCREEN_WIDTH - 60, 14, prog, chakra["color"])

    # Teaching section
    teach_panel_y = 100
    teach_panel_h = 220
    pygame.draw.rect(screen, DARK_PANEL, (40, teach_panel_y, SCREEN_WIDTH - 80, teach_panel_h), border_radius=15)
    pygame.draw.rect(screen, chakra["color"], (40, teach_panel_y, SCREEN_WIDTH - 80, teach_panel_h), 2, border_radius=15)

    # Lotus decoration
    draw_lotus(screen, 100, teach_panel_y + 50, 40, chakra["color"], time_val)

    # Teaching title
    teach_title = FONTS["medium"].render("Wisdom Teaching", True, GOLD)
    screen.blit(teach_title, (160, teach_panel_y + 15))

    # Teaching content (the explanation for what's about to be asked)
    teaching_text = q_data.get("teaching", "Study this concept carefully...")
    draw_text_wrapped(screen, teaching_text, FONTS["code"], (200, 230, 200),
                      160, teach_panel_y + 55, SCREEN_WIDTH - 260)

    # Mantra
    mantra_surf = FONTS["small"].render(f'Mantra: "{chakra["mantra"]}"', True, chakra["glow"])
    screen.blit(mantra_surf, (160, teach_panel_y + teach_panel_h - 40))

    # Start quiz button
    btn_y = teach_panel_y + teach_panel_h + 40
    btn_w, btn_h = 280, 55
    btn_x = SCREEN_WIDTH // 2 - btn_w // 2
    hover = pygame.Rect(btn_x, btn_y, btn_w, btn_h).collidepoint(mouse_pos)
    btn = draw_button(screen, (btn_x, btn_y, btn_w, btn_h), "Test My Knowledge",
                      FONTS["medium"], chakra["color"] if hover else tuple(max(0, c - 40) for c in chakra["color"]),
                      WHITE, hover, chakra["glow"])

    # Decorative mandala
    draw_mandala(screen, SCREEN_WIDTH - 120, SCREEN_HEIGHT - 120, 80, chakra["color"], 8, time_val)

    buttons = [("quiz_start", btn)]

    # Back button
    back_hover = pygame.Rect(20, SCREEN_HEIGHT - 60, 100, 40).collidepoint(mouse_pos)
    back_btn = draw_button(screen, (20, SCREEN_HEIGHT - 60, 100, 40), "< Back",
                           FONTS["body"], (60, 50, 80), WHITE, back_hover)
    buttons.append(("back", back_btn))

    return buttons


def render_quiz(game, mouse_pos, time_val):
    """Render the quiz/question screen."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    chakra = CHAKRAS[game.current_chakra]
    q_data = QUESTIONS[game.current_chakra][game.current_question]

    # Header
    total_q = len(QUESTIONS[game.current_chakra])
    header_text = f"{chakra['name']} — Question {game.current_question + 1}/{total_q}"
    header_surf = FONTS["medium"].render(header_text, True, chakra["glow"])
    screen.blit(header_surf, (30, 15))

    # Progress
    prog = (game.current_question) / total_q
    draw_progress_bar(screen, 30, 50, SCREEN_WIDTH - 60, 12, prog, chakra["color"])

    # Karma
    karma_surf = FONTS["small"].render(f"Karma: {game.karma_points}", True, GOLD)
    screen.blit(karma_surf, (SCREEN_WIDTH - 150, 15))

    # Question panel
    q_panel_y = 80
    q_panel_h = 130
    pygame.draw.rect(screen, DARK_PANEL, (40, q_panel_y, SCREEN_WIDTH - 80, q_panel_h), border_radius=15)
    pygame.draw.rect(screen, chakra["color"], (40, q_panel_y, SCREEN_WIDTH - 80, q_panel_h), 2, border_radius=15)

    # Question mark decoration
    qm = FONTS["heading"].render("?", True, chakra["color"])
    screen.blit(qm, (60, q_panel_y + 15))

    # Question text
    draw_text_wrapped(screen, q_data["q"], FONTS["medium"], WHITE,
                      110, q_panel_y + 20, SCREEN_WIDTH - 200)

    # Answer options
    buttons = []
    opt_start_y = q_panel_y + q_panel_h + 25
    opt_w = SCREEN_WIDTH - 120
    opt_h = 55
    opt_spacing = 65

    for i, option in enumerate(q_data["options"]):
        opt_y = opt_start_y + i * opt_spacing
        opt_rect = pygame.Rect(60, opt_y, opt_w, opt_h)
        is_hover = opt_rect.collidepoint(mouse_pos)

        if game.show_explanation:
            if i == q_data["answer"]:
                # Correct answer - green
                color = DARK_GREEN
                border = GREEN
            elif i == game.selected_answer and not game.answer_correct:
                # Wrong selection - red
                color = (100, 30, 30)
                border = RED_SOFT
            else:
                color = (30, 28, 45)
                border = (60, 55, 80)
        else:
            if is_hover:
                color = (55, 48, 80)
                border = chakra["color"]
            else:
                color = (35, 30, 55)
                border = (70, 65, 90)

        pygame.draw.rect(screen, color, opt_rect, border_radius=10)
        pygame.draw.rect(screen, border, opt_rect, 2, border_radius=10)

        # Option letter
        letter = chr(65 + i)  # A, B, C, D
        letter_color = chakra["color"] if not game.show_explanation else border
        letter_surf = FONTS["medium"].render(f"{letter}.", True, letter_color)
        screen.blit(letter_surf, (75, opt_y + 14))

        # Option text
        opt_text_surf = FONTS["body"].render(option, True, WHITE)
        screen.blit(opt_text_surf, (115, opt_y + 17))

        if not game.show_explanation:
            buttons.append(("answer", i, opt_rect))

    # Explanation panel (shown after answering)
    if game.show_explanation:
        exp_y = opt_start_y + 4 * opt_spacing + 10
        exp_h = 120
        exp_color = (20, 50, 20) if game.answer_correct else (50, 20, 20)
        pygame.draw.rect(screen, exp_color, (40, exp_y, SCREEN_WIDTH - 80, exp_h), border_radius=12)

        result_text = "Correct! Your wisdom grows!" if game.answer_correct else "Not quite. Learn from this..."
        result_color = GREEN if game.answer_correct else RED_SOFT
        result_surf = FONTS["medium"].render(result_text, True, result_color)
        screen.blit(result_surf, (60, exp_y + 10))

        draw_text_wrapped(screen, q_data["explanation"], FONTS["body"],
                          (200, 200, 200), 60, exp_y + 45, SCREEN_WIDTH - 160)

        # Next button
        btn_w, btn_h = 220, 48
        btn_x = SCREEN_WIDTH // 2 - btn_w // 2
        btn_y = exp_y + exp_h + 10
        hover = pygame.Rect(btn_x, btn_y, btn_w, btn_h).collidepoint(mouse_pos)
        is_last = game.current_question >= total_q - 1
        btn_text = "Complete Level" if is_last else "Next Question"
        btn = draw_button(screen, (btn_x, btn_y, btn_w, btn_h), btn_text,
                          FONTS["medium"], chakra["color"] if hover else tuple(max(0, c - 40) for c in chakra["color"]),
                          WHITE, hover, chakra["glow"])
        buttons.append(("next", btn))

    # Mini chakra indicator at top right
    for i in range(7):
        cx = SCREEN_WIDTH - 30 - (6 - i) * 22
        cy = 20
        r = 6
        c = CHAKRAS[i]["color"] if i in game.unlocked_chakras else (50, 50, 60)
        pygame.draw.circle(screen, c, (cx, cy), r)
        if i == game.current_chakra:
            pygame.draw.circle(screen, WHITE, (cx, cy), r + 3, 2)

    return buttons


def render_level_complete(game, mouse_pos, time_val):
    """Render the level complete celebration screen."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    chakra = CHAKRAS[game.current_chakra]
    next_chakra = CHAKRAS[min(game.current_chakra + 1, 6)]

    # Celebration mandala
    draw_mandala(screen, SCREEN_WIDTH // 2, 200, 150, chakra["color"], 16, time_val)

    # Chakra symbol
    draw_chakra_symbol(screen, SCREEN_WIDTH // 2, 200, 45, game.current_chakra, time_val)

    # Particles
    if random.random() < 0.3:
        particles.emit(SCREEN_WIDTH // 2 + random.randint(-100, 100),
                      200 + random.randint(-50, 50),
                      chakra["color"], 3, 1.5, 3)

    # Title
    complete_text = FONTS["heading"].render(f"{chakra['name']} Chakra Awakened!", True, chakra["glow"])
    screen.blit(complete_text, complete_text.get_rect(center=(SCREEN_WIDTH // 2, 310)))

    # Stats
    total_q = len(QUESTIONS.get(game.current_chakra, []))
    stats_y = 360
    stats = [
        f"Topic Mastered: {chakra['topic']}",
        f"Questions Completed: {total_q}",
        f"Total Karma Points: {game.karma_points}",
    ]
    for i, stat in enumerate(stats):
        s = FONTS["body"].render(stat, True, WHITE)
        screen.blit(s, s.get_rect(center=(SCREEN_WIDTH // 2, stats_y + i * 35)))

    # Next chakra preview
    if game.current_chakra < 6:
        preview_y = 480
        pygame.draw.line(screen, GOLD, (SCREEN_WIDTH // 2 - 100, preview_y),
                        (SCREEN_WIDTH // 2 + 100, preview_y), 1)
        next_text = FONTS["medium"].render(f"Next: {next_chakra['name']} — {next_chakra['topic']}", True, next_chakra["color"])
        screen.blit(next_text, next_text.get_rect(center=(SCREEN_WIDTH // 2, preview_y + 30)))
        desc_text = FONTS["small"].render(next_chakra["description"], True, GREY)
        screen.blit(desc_text, desc_text.get_rect(center=(SCREEN_WIDTH // 2, preview_y + 60)))

    # Buttons
    buttons = []
    btn_w, btn_h = 250, 52

    if game.current_chakra < 6:
        btn_x = SCREEN_WIDTH // 2 - btn_w // 2
        btn_y = 570
        hover = pygame.Rect(btn_x, btn_y, btn_w, btn_h).collidepoint(mouse_pos)
        btn = draw_button(screen, (btn_x, btn_y, btn_w, btn_h), "Next Chakra",
                          FONTS["medium"], next_chakra["color"] if hover else tuple(max(0, c - 30) for c in next_chakra["color"]),
                          WHITE, hover, next_chakra["glow"])
        buttons.append(("next_level", btn))

    btn_y2 = 635
    btn_x2 = SCREEN_WIDTH // 2 - btn_w // 2
    hover2 = pygame.Rect(btn_x2, btn_y2, btn_w, btn_h).collidepoint(mouse_pos)
    btn2 = draw_button(screen, (btn_x2, btn_y2, btn_w, btn_h), "Chakra Map",
                       FONTS["medium"], (50, 40, 70) if hover2 else (35, 28, 55),
                       SILVER, hover2)
    buttons.append(("map", btn2))

    return buttons


def render_game_complete(game, mouse_pos, time_val):
    """Render the final game completion screen."""
    screen.fill(DARK_BG)
    draw_stars(screen, time_val)

    # Grand mandala
    for i in range(7):
        offset = i * 0.5
        draw_mandala(screen, SCREEN_WIDTH // 2, 250, 200 - i * 15,
                    CHAKRAS[i]["color"], 12, time_val + offset)

    # OM symbol at center
    draw_om_symbol(screen, SCREEN_WIDTH // 2, 250, 35, GOLD, time_val)

    # Celebration particles
    if random.random() < 0.4:
        c_idx = random.randint(0, 6)
        particles.emit(SCREEN_WIDTH // 2 + random.randint(-150, 150),
                      250 + random.randint(-80, 80),
                      CHAKRAS[c_idx]["color"], 5, 2.0, 4)

    # Title
    title = FONTS["title"].render("ENLIGHTENMENT!", True, GOLD)
    screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 420)))

    subtitle = FONTS["medium"].render("All 7 Chakras Awakened — You have mastered Python!", True, WHITE)
    screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH // 2, 470)))

    # Final stats
    accuracy = (game.correct_answers / game.total_answered * 100) if game.total_answered > 0 else 0
    stats = [
        f"Total Karma: {game.karma_points}",
        f"Accuracy: {accuracy:.0f}%",
        f"Questions Answered: {game.total_answered}",
    ]
    for i, s in enumerate(stats):
        surf = FONTS["body"].render(s, True, SAFFRON)
        screen.blit(surf, surf.get_rect(center=(SCREEN_WIDTH // 2, 520 + i * 30)))

    # Buttons
    buttons = []
    btn_w, btn_h = 250, 50

    btn_x = SCREEN_WIDTH // 2 - btn_w // 2
    btn_y = 620
    hover = pygame.Rect(btn_x, btn_y, btn_w, btn_h).collidepoint(mouse_pos)
    btn = draw_button(screen, (btn_x, btn_y, btn_w, btn_h), "Return to Menu",
                      FONTS["medium"], (140, 80, 10) if hover else (100, 60, 5),
                      GOLD, hover, SAFFRON)
    buttons.append(("menu", btn))

    return buttons


# ─── Main Game Loop ──────────────────────────────────────────
def main():
    game = Game()
    running = True
    buttons = []  # Persistent across frames so clicks can detect rendered buttons

    while running:
        dt = clock.tick(FPS) / 1000.0
        game.time_val += dt
        mouse_pos = pygame.mouse.get_pos()

        # Update particles
        particles.update(dt)

        # Update notification timer
        if game.notification_timer > 0:
            game.notification_timer -= dt

        # ─── Event Handling ───────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.save_progress()
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game.state == GameState.MENU:
                        running = False
                    else:
                        game.state = GameState.CHAKRA_MAP

                # Quick answer keys in quiz
                if game.state == GameState.QUIZ and not game.show_explanation:
                    if event.key == pygame.K_1 or event.key == pygame.K_a:
                        game.answer_question(0)
                    elif event.key == pygame.K_2 or event.key == pygame.K_b:
                        game.answer_question(1)
                    elif event.key == pygame.K_3 or event.key == pygame.K_c:
                        game.answer_question(2)
                    elif event.key == pygame.K_4 or event.key == pygame.K_d:
                        game.answer_question(3)

                if game.state == GameState.QUIZ and game.show_explanation:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        game.next_question()

                if game.state == GameState.TEACHING:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        game.state = GameState.QUIZ

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check button clicks based on current state
                for btn_info in buttons:
                    if btn_info[0] == "start":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.state = GameState.CHAKRA_MAP
                    elif btn_info[0] == "new":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.reset_game()
                            game.state = GameState.CHAKRA_MAP
                    elif btn_info[0] == "quit":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.save_progress()
                            running = False
                    elif btn_info[0] == "back":
                        if btn_info[1].collidepoint(mouse_pos):
                            if game.state == GameState.CHAKRA_MAP:
                                game.state = GameState.MENU
                            else:
                                game.state = GameState.CHAKRA_MAP
                    elif btn_info[0] == "chakra":
                        if btn_info[2].collidepoint(mouse_pos):
                            game.start_quiz(btn_info[1])
                    elif btn_info[0] == "quiz_start":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.state = GameState.QUIZ
                    elif btn_info[0] == "answer":
                        if btn_info[2].collidepoint(mouse_pos):
                            game.answer_question(btn_info[1])
                    elif btn_info[0] == "next":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.next_question()
                    elif btn_info[0] == "next_level":
                        if btn_info[1].collidepoint(mouse_pos):
                            next_c = game.current_chakra + 1
                            if next_c < 7:
                                game.start_quiz(next_c)
                    elif btn_info[0] == "map":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.state = GameState.CHAKRA_MAP
                    elif btn_info[0] == "menu":
                        if btn_info[1].collidepoint(mouse_pos):
                            game.state = GameState.MENU

        # ─── Render ──────────────────────────────────
        if game.state == GameState.MENU:
            buttons = render_menu(game, mouse_pos, game.time_val)
        elif game.state == GameState.CHAKRA_MAP:
            buttons = render_chakra_map(game, mouse_pos, game.time_val)
        elif game.state == GameState.TEACHING:
            buttons = render_teaching(game, mouse_pos, game.time_val)
        elif game.state == GameState.QUIZ:
            buttons = render_quiz(game, mouse_pos, game.time_val)
        elif game.state == GameState.LEVEL_COMPLETE:
            buttons = render_level_complete(game, mouse_pos, game.time_val)
        elif game.state == GameState.GAME_COMPLETE:
            buttons = render_game_complete(game, mouse_pos, game.time_val)

        # Draw particles on top
        particles.draw(screen)

        # Draw notification
        if game.notification_timer > 0 and game.notification:
            alpha = min(1.0, game.notification_timer)
            notif_surf = FONTS["medium"].render(game.notification, True, game.notification_color)
            notif_rect = notif_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80))
            # Background
            bg_rect = notif_rect.inflate(30, 15)
            pygame.draw.rect(screen, (20, 15, 35), bg_rect, border_radius=8)
            pygame.draw.rect(screen, game.notification_color, bg_rect, 2, border_radius=8)
            screen.blit(notif_surf, notif_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
