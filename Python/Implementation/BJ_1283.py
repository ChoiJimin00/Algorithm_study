import sys
input = sys.stdin.readline

def get_shortcut(word):
    global shortcuts
    
    # 단어의 첫 글자
    word_s = word.split()
    for i in range(len(word_s)):
        l = word_s[i][0].lower()
        if l not in shortcuts:
            shortcuts.append(l)
            
            for j in range(len(word_s)):
                if i == j : print(f"[{word_s[j][0]}]{word_s[j][1:]} ",end='')
                else: print(f"{word_s[j]} ",end='')
            print()
            return  
        
    # 단어의 앞 부터
    for i in range(len(word)):
        l = word[i].lower()
        if word[i] == ' ':
            continue
        if l not in shortcuts :
            shortcuts.append(l)
            print(f"{word[:i]}[{word[i]}]{word[i+1:]}")
            return 
        
    print(word)


if __name__ == '__main__':
    N = int(input())
    shortcuts = []
    words = []
    
    for _ in range(N): 
        word = input().rstrip()
        get_shortcut(word)