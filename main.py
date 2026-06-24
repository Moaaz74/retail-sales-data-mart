from transform.transform_all import run_all_transformations
from load.load_all_dimensions import load_all_dimensions


if __name__ == "__main__":
    dims = run_all_transformations()
    load_all_dimensions(dims)