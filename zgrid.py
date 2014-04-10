#! /usr/bin/env python3

from vasppy import grid
import argparse

def parse_command_line_arguments():
    # command line arguments
    parser = argparse.ArgumentParser( description='z-projection of a VASP (grid format) file' )
    parser.add_argument( 'gridfile', help="filename of the VASP (grid format) file to be processed" )
    args = parser.parse_args()
    return( args )

if __name__ == "__main__":
    args = parse_command_line_arguments()
    grid = grid.Grid()
    grid.read_from_filename( args.gridfile )
    [ print( i ) for i in grid.z_average() ]
