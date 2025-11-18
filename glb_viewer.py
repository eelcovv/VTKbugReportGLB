import vtk
import argparse


def main():
    """
    Main function to set up the VTK scene and render the GLB file.
    """
    print("Hello from vtkbugreportglb!")

    parser = argparse.ArgumentParser(description="VTK GLB Viewer")
    parser.add_argument(
        "--filename", type=str, default="suzanne.glb", help="The GLB file to display."
    )
    parser.add_argument(
        "--show-colors",
        dest="show_colors",
        action="store_true",
        help="Show the model with its colors and textures (default).",
    )
    parser.add_argument(
        "--no-show-colors",
        dest="show_colors",
        action="store_false",
        help="Show the model as a grey mesh.",
    )
    parser.set_defaults(show_colors=True)
    args = parser.parse_args()

    # --- COMMON SETUP ---
    # Create a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.1, 0.2, 0.4)

    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 600)
    render_window.SetWindowName("Suzanne GLB Visualization")

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # --- MODEL LOADING ---
    # Load the model based on the show_colors flag
    if args.show_colors:
        # Use vtkGLTFImporter to load the scene with textures and materials.
        # This importer works on the render window level and populates the renderer.
        importer = vtk.vtkGLTFImporter()
        importer.SetFileName(args.filename)
        importer.SetRenderWindow(render_window)
        importer.Update()
    else:
        # Use vtkGLTFReader for more granular control over the geometry.
        # This provides the geometry that we can put into an actor.
        reader = vtk.vtkGLTFReader()
        reader.SetFileName(args.filename)

        polydata_filter = vtk.vtkCompositeDataGeometryFilter()
        polydata_filter.SetInputConnection(reader.GetOutputPort())

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(polydata_filter.GetOutputPort())
        mapper.SetScalarVisibility(False)  # This makes the actor grey

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        renderer.AddActor(actor)

    # --- FINALIZATION ---
    # Reset camera, render, and start interaction
    renderer.ResetCamera()
    render_window.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
