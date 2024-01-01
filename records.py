# %%
#run these once then never again to not lose your work
#best_known_sets = [[] for _ in range(20)]
#best_known_functions = [None for i in range(20)]
# %%
#run this every time you change your function
for i in range(3,10):
    try:
        out = greedy_solve(i,f)
        if len(out) > len(best_known_sets[i]):
            print(f"Best cap set for n = {i} improved from {len(best_known_sets[i])} to {len(out)}!")
            best_known_sets[i] = out
            best_known_functions[i] = f
        else:
            print(f"n={i}: {len(out)} (best {len(best_known_sets[i])})")
    except:
        pass