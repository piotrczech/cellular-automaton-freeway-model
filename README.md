# A cellular automation model for freeway traffic

## About

Implementation of the cellular automaton model for freeway traffic discussed in the paper by Kai Nagel and Michael Schreckenberg (HAL Id:
jpa-00246697).

## Usage

```bash
python main.py [-h] [-L SITES] [-v V_MAX] [-d DENSITY] [-p PROBABILITY] [-s STEPS] [-m DISPLAY_MODE {console,scatter,line}]
```

where options are:

- `-h`, `--help` - show help message and exit
- `-L`, `--sites` - number of sites on the road (default: 70)
- `-v`, `--v_max` - maximum velocity of vehicles (default: 5)
- `-d`, `--density` - density of vehicles on the road (default: 0.25)
- `-p`, `--probability` - probability of randomization (default: 0.4)
- `-s`, `--steps` - number of simulation steps (default: 50)
- `-m`, `--display-mode` - display mode for simulation data (default: console) (enum of: console, scatter, line)

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

#### Examples

##### Console

The default display mode is the console, as it is fast and presents numerical values compared to other types of plots. However, it is important to note that the console is efficient only when one row of the road containing `L` sites can be displayed in a single console row. Otherwise, this implementation loses its purpose, so we suggest adjusting smaller values for the `--sites` and `--steps` parameters.

Examples of console usage on a 1920x1080 resolution:

```bash
python main.py --sites 80 --steps 40
```

```bash
python main.py --sites 80 --steps 40 --v_max 7 --density 0.4
```

##### Plots

Displaying data as a plot is more computationally complex, but at the same time requires a much larger amount of data to achieve nice results. The data points must be so close together that they almost overlap. This approach is recommended for patient users.

Examples of plotting without resizing the plot window:

```bash
python main.py --display-mode scatter --sites 350 --steps 600
```

```bash
python main.py --display-mode line --sites 250 --steps 600 --density 0.4
```

```bash
python main.py --display-mode scatter --sites 350 --steps 600 --v_max 15 --probability 0.7
```

###### Note

At the moment, the scatter implementation performs significantly better than the line plot, so we recommend using it.

## Testing

Unit tests can be conducted using pytest. To run the tests, make sure you have pytest installed in your environment. You can install it using pip:

```bash
pip install pytest
```

Once pytest is installed, you can run the tests by navigating to the project directory and executing:

```bash
pytest .
```
