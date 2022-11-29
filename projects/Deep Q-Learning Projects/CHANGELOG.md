# Changelog

<p align = "justify">All notable changes to this <code><b>repository</b></code> will be documented here. The format is based on <a href = "https://keepachangelog.com/en/1.0.0/">Keep a Changelog</a>, and this project adheres to <a href = "https://semver.org/spec/v2.0.0.html">Semantic Versioning</a>.</p>

## Snake Game Engine
<p align = "justify">To test and learn/implement Deep-Q Learning Algorithms, special engines are being developed, such that a neural network can be built to train to play certain types of games. The <b><code>Snake Game Engine</code></b> provides a playable as well as configurable engine for AI modeling. The games are mostly planned to be developed using python library <code>pygame</code> and is intended for systems with <code>py38</code> or later.</p>

### [v1.0.1]()
* added boundary wall for better visualization.
* *bug fix* import font file via `abspath` such that engine can be initialized from submodule.
* initialize `pygame` at the beginning (as suggested [here](https://stackoverflow.com/a/58868533/6623589)).

### [v1.0.0]()
A basic snake game logic, where eating "food" awards score, and hit the boundary and you die!
