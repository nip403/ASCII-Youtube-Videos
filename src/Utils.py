import argparse
import logging
import os

valid_ext = [
    ".mp4"
]

parser = argparse.ArgumentParser(
    prog="Vid2ASCII.py",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Valid file types: " + " | ".join(valid_ext)
)

mode = parser.add_argument_group("Video selection")
mode.add_argument(
    "--yt", 
    "--url",
    dest="video",
    default=None,
    help="YT URL or video name, will select the top video from search results if not using URL",
)

mode.add_argument(
    "--fp", 
    "--file",
    dest="file",
    default=None,
    help="Full filepath to video",
    metavar="filepath"
)

other = parser.add_argument_group("Other options")
other.add_argument(
    "--fullplayback",
    "-f",
    dest="playback",
    type=int,
    choices=[0, 1],
    default=0,
    help="""Playback mode:
      (DEFAULT) 0: Play ASCII video as each frame loads (variable fps) 
                1: Play ASCII video once whole video is processed (slower but reliable fps)
""",
    metavar="bool"
)

other.add_argument(
    "--logger",
    "-l", 
    dest="log",
    type=int,
    choices=[0, 1],
    default=1,
    help="""Toggle logger:
                0: Only display errors/warnings
      (DEFAULT) 1: Display all logs
""",
    metavar="bool"
)

def validate_args(args):
    assert bool(args.video is None) ^ bool(args.file is None), "Input only one video source, use -h or --help for more details."
    
    if args.file is not None:
        assert os.path.exists(args.file), f"File {args.file} not found."
        assert os.path.splitext(args.file)[-1] in valid_ext, "File in invalid format. See help options for valid file types."

def setup_logger(logger):
    logger.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(name)s.%(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S")
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logger(logging.getLogger("Root"))
