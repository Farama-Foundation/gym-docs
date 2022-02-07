import gym
from rich.table import Table
from rich.console import Console
from rich import box
from tqdm import tqdm


def shortened_repr(lst):
    assert all((isinstance(item, int) for item in lst))
    assert len(set(lst)) == len(lst)
    lst = sorted(lst)

    if lst[-1] - lst[0] == len(lst) - 1 and len(lst) > 3:
        return f"`[{lst[0]}, ..., {lst[-1]}]`"
    elif len(lst) > 3 and lst[-2] - lst[0] == len(lst) - 2:
        return f"`[{lst[0]}, ..., {lst[-2]}, {lst[-1]}]`"
    return f"`{str(lst)}`"


current_atari_envs = sorted(
    [env_spec.id for env_spec in gym.envs.registry.all() if env_spec.id.startswith("ALE") and "ram" not in env_spec.id])

table = Table(title="Atari Flavors", box=box.ASCII)

table.add_column("Environment", no_wrap=True)
table.add_column("Valid Modes")
table.add_column("Valid Difficulties")
table.add_column("Default Mode")

for env_name in tqdm(current_atari_envs):
    env = gym.make(env_name)
    valid_modes = env.unwrapped.ale.getAvailableModes()
    valid_difficulties = env.unwrapped.ale.getAvailableDifficulties()
    difficulty = env.unwrapped.ale.cloneState().getDifficulty()
    assert (difficulty == 0), difficulty
    table.add_row(env_name.split("/")[1].split("-")[0], shortened_repr(valid_modes), shortened_repr(valid_difficulties),
                  f"`{env.unwrapped.ale.cloneState().getCurrentMode()}`")

console = Console()
console.print(table)
