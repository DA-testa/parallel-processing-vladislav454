def parallel_processing(n, m, data):
    output = []

    for i in range(n):
        output.append((i, 0))
    
    for i in range(n, m):
        sec = output[i-n][1] + int(data[i-n])
        output.append((i % n, sec))

    return output

def main():
    first_line = input().split()
    n = int(first_line[0])
    m = first_line[1]
    m = int(m.replace("\\r\\n",""))

    second_line = input().split()
    data = []
    data = second_line

    result = parallel_processing(n,m,data)

    for i,j in result:
        print(i,j)

if __name__ == "__main__":
    main()
