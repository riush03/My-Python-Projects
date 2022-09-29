from tqdm import tqdm
import time

#show progress bar
bar = tqdm(range(10),bar_format="{percentage:3.0f}% |{bar}| {elapsed}/{remaining}")
desc = "Dimple bar"
tot = 0
for i in bar:
    time.sleep(2)
    tot += i
    bar.set_postfix({"total":tot})