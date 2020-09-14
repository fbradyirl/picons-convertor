import cairosvg
import os
from shutil import copyfile
import logging, coloredlogs

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(name)s   : %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger("convert")
coloredlogs.install(level=os.getenv("LOG_LEVEL", "INFO"))

source_dir = "picons-source/build-source/logos/"
output_dir = "picons"

for subdir, dirs, files in os.walk(source_dir):
    log.info("Found {} files in {}. Converting...".format(len(files), source_dir))

    for file in files:
        raw_name = file.replace(".default.svg", "")
        raw_name = raw_name.replace(".default.png", "")
        output_file = "{}/{}.png".format(output_dir, raw_name)
        if file.endswith("png"):
            log.debug("Already a png {}. saving to {}...".format(file, output_file))
            copyfile("picons-source/build-source/logos/{}".format(file), output_file)

        elif file.endswith("svg"):

            log.debug("Converting {} and saving to {}...".format(file, output_file))
            try:
                cairosvg.svg2png(url="picons-source/build-source/logos/{}".format(file),
                                 write_to=output_file)
            except Exception as e:
                log.error("There was a problem converting {}".format(file))
        else:
            log.error("WARNING unknown format? {}...".format(file))

    log.info("Conversion done for {} files".format(len(files)))
