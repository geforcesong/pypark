s = 'a/b/c/d/e'

for i in range(len(s)):
    if(s[i] == '/'):
        print(s[:i])
print(s)