# gym-docs

This repository used to house the documentation website for [Gym](https://github.com/openai/gym).

Gym has been unmaintained since 2022. [Gymnasium](https://gymnasium.farama.org) is the
maintained drop-in replacement from the original Gym team, and the documentation now lives there.

This repo is archived. All it does now is serve a single static page that forwards visitors to
Gymnasium.

## Contents

- `index.html` — the standalone notice / forward page
- `404.html` — redirects any old deep link back to `index.html`
- `assets/` — the Gym logos and favicon used by the page

## Hosting

No build step is required. Point GitHub Pages (or any static host) at the repository root
and it will serve `index.html` directly.
