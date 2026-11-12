for b in range(1,25):
    for k in range(1, 25):
        for t in range(1, 25):
            if 10*b + 5*k + 0.5*t == 100 and b>=1 and k>=1 and t>=1:
                print(f"быков:{b}, коров: {k}, телят: {t}")