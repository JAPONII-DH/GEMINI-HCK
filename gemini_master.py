import os, g4f, re, arabic_reshaper
G, R, Y, C, W, B = "\033[1;32m", "\033[1;31m", "\033[1;33m", "\033[1;36m", "\033[0m", "\033[1;34m"
def fix_display(text):
    if any("\u0600" <= char <= "\u06FF" for char in text):
        try:
            reshaped = arabic_reshaper.reshape(text)
            return "\n".join([line[::-1] for line in reshaped.split("\n")])
        except: return text
    return text
def get_ai_response(prompt):
    try:
        return g4f.ChatCompletion.create(model=g4f.models.default,
            messages=[{"role": "system", "content": "Tech expert. Use `` for commands."},
                      {"role": "user", "content": prompt}])
    except: return "Connection Error"
def execute_logic(ai_text):
    for cmd in re.findall(r"`(.*?)`", ai_text):
        print(f"{Y}┌─[ EXEC ]\n└─╼ {G}{cmd}{W}"); os.system(cmd)
def draw_interface():
    os.system("clear")
    print(f"{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n{C}┃{R}   ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗██╗ {C}┃\n{C}┃{R}  ██╔════╝ ██╔════╝████╗ ████║██║████╗  ██║██║ {C}┃\n{C}┃{R}  ██║  ███╗█████╗  ██╔████╔██║██║██╔██╗ ██║██║ {C}┃\n{C}┃{R}  ██║   ██║██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║ {C}┃\n{C}┃{R}  ╚██████╔╝███████╗██║ ╚═╝ ██║██║██║ ╚████║██║ {C}┃\n{C}┃{R}   ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ {C}┃\n{C}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n{C}┃{W}  TOOL: {G}GEMINI HCK{W}   |   DEV: {G}JAPONI{W}   | {Y}V21 {C}┃\n{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{W}")
draw_interface()
while True:
    try:
        user_in = input(f"\n{C}┌──({G}GEMINI-HCK{C})─[{B}Master{C}]\n{C}└─{G}$ {W}").strip()
        if not user_in: continue
        if user_in.lower() in ["exit", "خروج"]: break
        if user_in in ["clear", "مسح"]: draw_interface(); continue
        print(f"{Y} [!] Analyzing...{W}", end="\r")
        reply = get_ai_response(user_in)
        print(f"\n{C}┏━━━━ {G}AI RESPONSE {C}━━━━━\n{C}┃{W} {fix_display(reply)}")
        execute_logic(reply)
        print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━{W}")
    except Exception as e: print(f"\n{R}[!] ERROR: {str(e)}{W}")
