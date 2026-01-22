haystack="sadbutsad"
needle="sad"
n = len(haystack)
m = len(needle)

if m == 0:
    print(0)

for i in range(n - m + 1):
     if haystack[i:i+m] == needle:
        print(i)
        exit(0)

print(-1)