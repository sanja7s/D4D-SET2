'''
Created on Nov 21, 2012

@author: sscepano
'''

import logging
import traceback
from read_in_data import user_movements_v2 as rd
from analyze_data import calculate_statistics as pd
from analyze_data import find_home_by_night as fhn
from visualize import graph_statistics as gs

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

    data = rd.read_in_seq_usr_mov()
    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            #reload(pd)
            #reload(fhn)
            reload(gs)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            #fhn.find_home(pd.find_usr_call_fq(data))  
            gs.num_visited_locations(data)
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == "__main__":
    main()