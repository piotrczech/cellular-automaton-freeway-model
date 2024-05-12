# A cellular automation model for freeway traffic

## About

Implementation of the cellular automaton model for freeway traffic discussed in the paper by Kai Nagel and Michael Schreckenberg (HAL Id:
jpa-00246697).

## Usage

```bash
python main.py [-h] [-L SITES] [-v V_MAX] [-d DENSITY] [-p PROBABILITY] [-s STEPS]
```

where options are:

- -h, --help show this help message and exit
- -L SITES, --sites SITES
- -v V_MAX, --v_max V_MAX
- -d DENSITY, --density DENSITY
- -p PROBABILITY, --probability PROBABILITY
- -s STEPS, --steps STEPS.

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
