from pathlib import Path
import vtk
import argparse


def main():
    """
    Main function to set up the VTK scene and render the GLB file.
    """
    print("Hello from vtkbugreportglb!")

    parser = argparse.ArgumentParser(description="VTK GLB Viewer")
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the rendering in an interactive window. If not specified, the rendering will be saved to a PNG file.",
    )
    parser.add_argument(
        "--filename", type=str, default="suzanne.glb", help="The GLB file to display."
    )
    parser.add_argument(
        "--colors",
        dest="colors",
        action="store_true",
        help="Show the model with its colors and textures (default).",
    )
    parser.add_argument(
        "--no-colors",
        dest="colors",
        action="store_false",
        help="Show the model as a grey mesh.",
    )
    parser.set_defaults(colors=True)
    args = parser.parse_args()

    # --- COMMON SETUP ---
    # Create a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.1, 0.2, 0.4)

    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 600)
    render_window.SetWindowName("Suzanne GLB Visualization")

    if not args.show:
        render_window.SetOffScreenRendering(1)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # --- MODEL LOADING ---
    # Load the model based on the colors flag
    if args.colors:
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
    # Reset camera, then set custom view
    renderer.ResetCamera()
    camera = renderer.GetActiveCamera()
    camera.SetPosition(3.0, 3.0, 3.0)
    camera.SetFocalPoint(0.0, 0.0, 0.0)
    camera.SetViewUp(0.0, 1.0, 0.0)
    renderer.ResetCameraClippingRange()
    render_window.Render()

    if args.show:
        interactor.Start()
    else:
        # Save to PNG
        window_to_image = vtk.vtkWindowToImageFilter()
        window_to_image.SetInput(render_window)
        window_to_image.SetInputBufferTypeToRGBA()  # Ensure correct color channels
        window_to_image.ReadFrontBufferOff()  # Read from the back buffer

        output_file = Path(args.filename).with_suffix(".png")
        png_writer = vtk.vtkPNGWriter()
        png_writer.SetFileName(str(output_file))
        png_writer.SetInputConnection(window_to_image.GetOutputPort())
        png_writer.Write()
        print(f"Rendering saved to {output_file}")


if __name__ == "__main__":
    main()
