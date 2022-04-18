# Gym-docs

This repo contains the [NEW website](http://www.gymlibrary.ml) for [Gym](https://github.com/openai/gym). This site is currently in Beta and we are in the process of adding/editing information. 

Please see instructions below on how to contribute.

If you are modifying a non-environment page or an atari environment page, please PR this repo. Otherwise, follow the steps below:

## Instructions for modifying environment pages

### Editing an environment page

If you are editing an Atari environment, directly edit the md file in this repository. 

Otherwise, fork Gym and edit the docstring in the environment's Python file. Then, pip install your Gym fork and run `docs/scripts/gen_mds.py` in this repo. This will automatically generate a md documentation file for the environment.

### Adding a new environment

#### Atari env

For Atari envs, add a md file into `pages/environments/atari` then complete the **other steps**.

#### Non-Atari env

Ensure the environment is in Gym (or your fork). Ensure that the environment's Python file has a properly formatted markdown docstring. Pip install Gym (or your fork) then run `docs/scripts/gen_mds.py`. This will automatically generate an md page for the environment. Then complete the [other steps](#other-steps).

#### Other steps

- Add the corresponding gif into the `docs/source/_static/videos/{ENV_TYPE}` folder, where `ENV_TYPE` is the category of your new environment (e.g. mujoco). Follow snake_case naming convention. Alternatively, run `docs/scripts/gen_gifs.py`.
- Edit `docs/source/environments/{ENV_TYPE}/index.md`, and add the name of the file corresponding to your new environment to the `toctree`.

## Build the Documentation

Install the required packages and Gym (or your fork):

```
pip install -r requirements.txt
pip install gym
```

To build the documentation once:

```
cd docs
make dirhtml
```

To rebuild the documentation automatically everytime a change is made:

```
cd docs
sphinx-autobuild -b dirhtml ./source build/html
```
