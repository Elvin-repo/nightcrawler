import sys, logging


def not_implemented_func(message):
    """
    Log a message indicating that the specified function is not implemented yet and exit the script.

    This function is intended to be used as a placeholder for parts of the code that have not been implemented yet.
    It is often used during development to mark areas where additional functionality is required.

    The function logs a custom message and exits the script with an exit code of 1.

    Parameters:
        message (str): The custom message to be logged.

    Usage:
        not_implemented_func("This feature is not implemented yet.")
    """
    logger = logging.getLogger(__name__)
    logger.error(message)
    sys.exit(1)


def setup_logging(log_file):
    """
    Configure logging settings.

    Parameters:
        log_file (str): The name of the log file.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
