import vtk

GLB_FILE = "suzanne.glb"
SHOW_COLORS = False


def main():
    """
    Main function to set up the VTK scene and render the GLB file.
    """
    print("Hello from vtkbugreportglb!")

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
    # Load the model based on the SHOW_COLORS flag
    if SHOW_COLORS:
        # Use vtkGLTFImporter to load the scene with textures and materials.
        # This importer works on the render window level and populates the renderer.
        importer = vtk.vtkGLTFImporter()
        importer.SetFileName(GLB_FILE)
        importer.SetRenderWindow(render_window)
        importer.Update()
    else:
        # Use vtkGLTFReader for more granular control over the geometry.
        # This provides the geometry that we can put into an actor.
        reader = vtk.vtkGLTFReader()
        reader.SetFileName(GLB_FILE)

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
