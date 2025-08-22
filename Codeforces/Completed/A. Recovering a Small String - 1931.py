def find_smallest_word(n):
    for i in range(1, 27):
        for j in range(1, 27):
            k = n - i - j
            if 1 <= k <= 26:
                return chr(i + 96) + chr(j + 96) + chr(k + 96)
    return ""

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(find_smallest_word(n))
    
    for result in results:
        print(result) 