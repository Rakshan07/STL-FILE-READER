# STL Weight and Price Calculator

This Python script estimates the weight and material cost of every STL model in a selected folder. It assumes the models are designed in millimeters and made from PLA.

## How It Works

1. Imports Python's `os` module for listing files and building file paths, and the `trimesh` package for loading and measuring 3D models.
2. Sets `folder` to the directory containing the STL files.
3. Sets PLA density to `1.24 g/cm^3`. Change this value if you are estimating a different material.
4. Lists the files in the configured folder and processes files whose names end in `.stl` (uppercase or lowercase).
5. Loads each STL as a 3D mesh with `trimesh` and reads its volume. The volume is converted from cubic millimeters to cubic centimeters by dividing by `1000`.
6. Estimates each model's weight using:

	`weight in grams = volume in cm^3 * material density in g/cm^3`

7. Prints each filename and estimated weight, then adds the weights and displays the total.
8. Estimates the total price at `3` currency units per gram and prints it with a rupee symbol. Change `price = total_weight * 3` to use a different rate.

## Requirements

- Python
- `trimesh`

Install the package with:

```powershell
python -m pip install trimesh
```

## Run

Update the `folder` setting in `weight.py` if your STL files are stored elsewhere, then run:

```powershell
python weight.py
```

## Notes

- Only `.stl` files are processed. Other formats, including `.3mf`, are skipped.
- The volume conversion assumes the STL dimensions are in millimeters.
- Weight is an estimate based on the selected material density. Actual print weight can differ because of infill, shells, supports, and printer settings.
- For a reliable volume measurement, each STL should describe a closed, valid solid mesh.
