# Import GLB in VTK

This project demnostrates an example of a erouneous import of glb into vtk

## How to run

To run the script with default settings (showing colors for `suzanne.glb`):
```bash
python main.py
```

To run the script without colors:
```bash
python main.py --no-show-colors
```

To specify a different GLB file:
```bash
python main.py --filename path/to/your/file.glb
```