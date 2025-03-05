import logging
import sys


def _init_logger():
    import logging
    logger = logging.getLogger('app')
    # Set the threshold logging level of the logger to INFO
    logger.setLevel(logging.INFO)
    # Create a stream-based handler that writes the log entries#into the standard output stream
    handler = logging.StreamHandler(sys.stdout)
    # Create a formatter for the logs
    formatter = logging.Formatter('%(created)f:%(levelname)s:%(name)s:%(module)s:%(message)s')
    # Set the created formatter as the formatter of the handlerhandler.setFormatter(formatter)
    # Add the created handler to this logger
    logger.addHandler(handler)


_init_logger()
_logger = logging.getLogger('app')
