#!/usr/bin/env python3
import argparse, sys

from lib.cellural_traffic_model import circle_freeway_model
from lib.utils.display.core import DisplaySimulationContext
from lib.utils.display.strategies import ConsoleDisplayStrategy 

def define_parser():
    parser = argparse.ArgumentParser(
                    prog='A cellular automation model for freeway traffic',
                    description="""Implementation of the cellular automaton model for freeway
                        traffic discussed in the paper by Kai Nagel and Michael Schreckenberg
                        (HAL Id: jpa-00246697).
                    """,
                    epilog='Text at the bottom of help')

    parser.add_argument('-L', '--sites', default=70) 
    parser.add_argument('-v', '--v_max', default=5) 
    parser.add_argument('-d', '--density', default=0.25) 
    parser.add_argument('-p', '--probability', default=0.4) 
    parser.add_argument('-s', '--steps', default=50) 

    return parser

def main():
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
    display_context.display(road_history)

if __name__ == "__main__":
    main()
