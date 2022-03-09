import sys

all_envs = [
    {
        'id': 'mujoco',
        'list': ['ant', 'half_cheetah', 'hopper', 'humanoid_standup', 'humanoid',
                 'inverted_double_pendulum', 'inverted_pendulum', 'reacher', 'swimmer', 'walker2d']
    },
    {
        'id': 'toy_text',
        'list': ['blackjack', 'frozen_lake']
    },
    {
        'id': 'box2d',
        'list': ['bipedal_walker', 'car_racing', 'lunar_lander']
    },
    {
        'id': 'classic_control',
        'list': ['acrobot', 'cart_pole', 'mountain_car_continuous', 'mountain_car', 'pendulum']
    },
    {
        'id': 'atari',
        'list': ["adventure",
                 "air_raid",
                 "alien",
                 "amidar",
                 "assault",
                 "asterix",
                 "asteroids",
                 "atlantis",
                 "bank_heist",
                 "battle_zone",
                 "beam_rider",
                 "berzerk",
                 "bowling",
                 "boxing",
                 "breakout",
                 "carnival",
                 "centipede",
                 "chopper_command",
                 "crazy_climber",
                 "defender",
                 "demon_attack",
                 "double_dunk",
                 "elevator_action",
                 "enduro",
                 "fishing_derby",
                 "freeway",
                 "frostbite",
                 "gopher",
                 "gravitar",
                 "hero",
                 "ice_hockey",
                 "jamesbond",
                 "journey_escape",
                 "kangaroo",
                 "krull",
                 "kung_fu_master",
                 "montezuma_revenge",
                 "ms_pacman",
                 "name_this_game",
                 "phoenix",
                 "pitfall",
                 "pong",
                 "pooyan",
                 "private_eye",
                 "qbert",
                 "riverraid",
                 "road_runner",
                 "robotank",
                 "seaquest",
                 "skiing",
                 "solaris",
                 "space_invaders",
                 "star_gunner",
                 "tennis",
                 "time_pilot",
                 "tutankham",
                 "up_n_down",
                 "venture",
                 "video_pinball",
                 "wizard_of_wor",
                 "yars_revenge",
                 "zaxxon", ]
    }
]


def create_grid_cell(type_id, env_id):
    return f'''
            <a href="{env_id}.html">
                <div class="env-grid__cell">
                    <div class="cell__image-container">
                        <img src="../../_static/videos/{type_id}/{env_id}.gif">
                    </div>
                    <div class="cell__title">
                        <span>{' '.join(env_id.split('_')).title()}</span>
                    </div>
                </div>
            </a>
    '''


def generate_page(env, limit=-1):
    env_type_id = env['id']
    env_list = env['list']
    cells = [create_grid_cell(env_type_id, env_id) for env_id in env_list]
    non_limited_page = limit == -1 or limit >= len(cells)
    if non_limited_page:
        cells = '\n'.join(cells)
    else:
        cells = '\n'.join(cells[:limit])

    more_btn = '<a href="./complete_list.html"><button class="more-btn">See More Environments</button></a>' if not non_limited_page else ''
    return f'''
<!DOCTYPE html>

<html>
    <body>
        <link rel="stylesheet" href="../../_static/css/env_pages.css">

        <div class="env-grid">
            {cells}
        </div>
        {more_btn}
    </body>
</html>
    '''


if __name__ == "__main__":
    type_arg = sys.argv[1]
    type_dict = {
        'id': ''
    }
    for i in all_envs:
        if type_arg == i['id']:
            type_dict = i
            break

    type_id = type_dict['id']
    if type_id != '':
        envs_path = f'../source/environments/{type_id}'
        if len(type_dict['list']) > 20:
            page = generate_page(type_dict, limit=9)
            fp = open(f'{envs_path}/index.html', 'w+', encoding='utf-8')
            fp.write(page)
            fp.close()

            page = generate_page(type_dict)
            fp = open(f'{envs_path}/complete_list.html', 'w+', encoding='utf-8')
            fp.write(page)
            fp.close()
        else:
            page = generate_page(type_dict)
            fp = open(f'{envs_path}/index.html', 'w+', encoding='utf-8')
            fp.write(page)
            fp.close()
    else:
        print(f'Invalid type of environment: {type_arg}')
