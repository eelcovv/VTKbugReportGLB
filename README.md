# Import GLB in VTK

This project demnostrates an example of a erouneous import of glb into vtk

## How to run

To run the script with default settings (showing colors for `suzanne.glb`):
```bash
python glb_viewer.py
```

To run the script without colors:
```bash
python glb_viewer.py --no-show-colors
```

To specify a different GLB file:
```bash
python glb_viewer.py --filename path/to/your/file.glb
```