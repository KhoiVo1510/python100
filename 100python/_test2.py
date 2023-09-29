def parse_ex100(N):
    result = []
    for a in range(1, int(N/2)+1):
        tmp_sum = a
        for b in range(a + 1, int(N/2) + 2):
            tmp_sum += b
            if tmp_sum < N:
                continue
            if tmp_sum == N:
                result.append((a, b))
            break
    return result

with open("./rwf/bieudienso.inp", "r") as rf:
    with open("./rwf/bieudienso.out", "w") as wf:
        out = parse_ex100(int(rf.readline()))
        out = sorted(out, key = lambda a: a[1] - a[0])
        wf.write(str(len(out)) + '\n')
        for x, y in out:
            lst = []
            for num in range(x, y+1):
                lst.append(num)
            wf.write(str(" + ".join(map(str,lst)) + '\n'))
