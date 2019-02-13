import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='testCartPoleEnvm2l05-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm2l05',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='testCartPoleEnvm4l05-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm4l05',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='testCartPoleEnvm2l15-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm2l15',
    max_episode_steps=500,
    reward_threshold=475.0,
)


register(
    id='testCartPoleEnvm4l15-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm4l15',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='testCartPoleEnvm2l25-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm2l25',
    max_episode_steps=500,
    reward_threshold=475.0,
)


register(
    id='testCartPoleEnvm4l25-v0',
    entry_point='cartpole_test.envs:TestCartPoleEnvm4l25',
    max_episode_steps=500,
    reward_threshold=475.0,
)
