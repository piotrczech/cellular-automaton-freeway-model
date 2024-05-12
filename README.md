# A cellular automation model for freeway traffic

## About

Implementation of the cellular automaton model for freeway traffic discussed in the paper by Kai Nagel and Michael Schreckenberg (HAL Id:
jpa-00246697).

## Usage

```bash
python main.py [-h] [-L SITES] [-v V_MAX] [-d DENSITY] [-p PROBABILITY] [-s STEPS]
```

where options are:

- `-h`, `--help` - show help message and exit
- `-L`, `--sites` - number of sites on the road (default: 70)
- `-v`, `--v_max` - maximum velocity of vehicles (default: 5)
- `-d`, `--density` - density of vehicles on the road (default: 0.25)
- `-p`, `--probability` - probability of randomization (default: 0.4)
- `-s`, `--steps` - number of simulation steps (default: 50)

<br>

Additional information you can get by providing

```bash
python main.py --help
```

### Basic run

To simply run basic model implementation provide

```bash
python main.py
```
