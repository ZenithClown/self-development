<h1 align = "center">DeepQ Learning Projects</h1>

<p align = "justify">The repository features a collection of projects associated with <code>Q-Learning</code>. As defined in <a href = "https://en.wikipedia.org/wiki/Q-learning">WiKiPedia</a>, <q>Q-learning is a model-free reinforcement learning algorithm to learn the value of an action in a particular state. <code>Q</code> refers to the function that the algorithm computes – the expected rewards for an action taken in a given state.</q> A very good introduction is available at <a href = "https://www.novatec-gmbh.de/en/blog/introduction-to-q-learning/">novatech-gmbh.de/blog</a> which explains about the <code><q>agent</q></code> and <code><q>environment</q></code> which correlates with <code>state, rewards, and action</code>.</p>

<img src = "https://www.novatec-gmbh.de/wp-content/uploads/1_mPGk9WTNNvp3i4-9JFgD3w.png" alt = "Q-Learning Agent-Environment">

<p align = "justify">The repository is built to develop understanding of Reinforcement Learning by practical implementation on developing an agent, creating an environment and all other features. The following projects are currently available:</p>

 1. [AI Learns to Play Snake Game](./projects/Snake-Game.md)

## Getting Started

<p align = "justify">The program is developed in <code>py38</code> with all the required libraries listed in <a href = "./requirements.txt"><code>requirements.txt</code></a>. It is recomended to create a virtual environment (below an example is shown with <code>virtualenv</code>), and then proceed.</p>

```python
dpramanik$ python virtualenv
dpramanik$ source activate venv/bin/activate
dpramanik$ pip install -r requirements.txt
dpramanik$ python agent.py
```

For details on `agent` check individual project documentations.

## Acknowledgement
Project favicon/logo is avaiable [here](https://www.pngegg.com/en/png-wfvfy).
