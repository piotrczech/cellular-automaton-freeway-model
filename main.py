#!/usr/bin/env python3
import argparse, sys

from lib.cellural_traffic_model import circle_freeway_model
from lib.utils.display.core import DisplaySimulationContext
from lib.utils.display.strategies import ConsoleDisplayStrategy, ScatterPlotDisplayStrategy, LinePlotDisplayStrategy

def define_parser():
    """
    Defines the command-line arguments parser.

    Returns
    -------
    argparse.ArgumentParser
        The configured argument parser.
    """
    parser = argparse.ArgumentParser(
                    prog='A cellular automation model for freeway traffic',
                    description="""Implementation of the cellular automaton model for freeway
                        traffic discussed in the paper by Kai Nagel and Michael Schreckenberg
                        (HAL Id: jpa-00246697).
                    """,
                    epilog='Project carried out as part of a project for applied mathematics studies at Wrocław University of Science and Technology.')

    parser.add_argument(
        '-L', '--sites',
        default=70, type=int,
        help='Number of sites on the road (default: 70)'
    )
    parser.add_argument(
        '-v', '--v_max',
        default=5, type=int,
        help='Maximum velocity of vehicles (default: 5)'
    )
    parser.add_argument(
        '-d', '--density',
        default=0.25, type=float,
        help='Density of vehicles on the road (default: 0.25)'
    )
    parser.add_argument(
        '-p', '--probability',
        default=0.4, type=float,
        help='Probability of randomization (default: 0.4)'
    )
    parser.add_argument(
        '-s', '--steps',
        default=50, type=int,
        help='Number of simulation steps (default: 50)'
    )
    parser.add_argument(
        '-m', '--display-mode',
        default='console', choices=['console', 'scatter', 'line'],
        help='Display mode for simulation data (default: console)'
    )

    return parser

def main():
    """
    Main function to execute the program.
    """
    parser = define_parser()
    args = parser.parse_args()

    road_history = circle_freeway_model.simulate_with_history(
        L = args.sites,
        v_max = args.v_max,
        density = args.density,
        p = args.probability,
        steps = args.steps
    )

    display_context = DisplaySimulationContext(ConsoleDisplayStrategy) 
    if args.display_mode == 'scatter':
        display_context = DisplaySimulationContext(ScatterPlotDisplayStrategy)
    elif args.display_mode == 'line':
        display_context = DisplaySimulationContext(LinePlotDisplayStrategy)
    
    display_context.display(road_history)

if __name__ == "__main__":
    main()
