import os
import logging
import zipfile


def setup_logger(log_file):
    # Create the log folder if it doesn't exist
    log_folder = os.path.dirname(log_file)
    os.makedirs(log_folder, exist_ok=True)

    # Create a logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger


def create_apps_zip(archive_dir, egg_filename):
    # Get the absolute path to the parent directory of the scripts folder
    parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    # Replace these variables with your actual settings
    python_source_dir = os.path.join(parent_dir, "src")

    # Ensure the Python source directory exists
    os.makedirs(python_source_dir, exist_ok=True)

    # Create the zip archive using Python's zipfile module
    with zipfile.ZipFile(os.path.join(archive_dir, egg_filename), "w") as zipf:
        for root, dirs, files in os.walk(python_source_dir):
            for file in files:
                # Calculate the relative path of the file from the PYTHON_SOURCE_DIR
                relative_path = os.path.relpath(os.path.join(root, file), python_source_dir)
                # Construct the arcname to include the "apps" parent folder
                arcname = os.path.join("src", relative_path)
                # Add the file to the zip archive using the constructed arcname
                zipf.write(os.path.join(root, file), arcname=arcname)

    print(f"{egg_filename} created in the {archive_dir} directory.")


if __name__ == "__main__":
    # Set the log file name and location
    log_file = "./log/zip_src.log"

    # Create the logger
    logger = setup_logger(log_file)

    try:
        # Replace these variables with your actual settings
        archive_dir = "./archive"
        egg_filename = "src.zip"

        # Create the Python zip archive using the create_apps_zip function
        create_apps_zip(archive_dir, egg_filename)

        # Log a message to the log file to verify it is working
        logger.info("Zip file created successfully!")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
