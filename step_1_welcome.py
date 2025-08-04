print("Welcome to the game Hangman") #printing welcome message
print("""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/""") #printing welcome sign
import random #importing random package
print(random.randint(1,10)) #printing randon number
print("""picture 1:
    x-------x

picture 2:
    x-------x
    |
    |
    |
    |
    |

picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |

picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |

picture 5:
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

picture 6:
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

picture 7:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""") #printing hangman variations