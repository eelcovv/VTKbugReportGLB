import vtk

GLB_FILE = "suzanne.glb"
SHOW_COLORS = True


def setup_grey_actor(filename):
    """
    Sets up a grey actor from the GLB file using vtkGLTFReader.
    """
    reader = vtk.vtkGLTFReader()
    reader.SetFileName(filename)

    polydata_filter = vtk.vtkCompositeDataGeometryFilter()
    polydata_filter.SetInputConnection(reader.GetOutputPort())

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(polydata_filter.GetOutputPort())
    mapper.SetScalarVisibility(False)  # This makes the actor grey

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor


def setup_colored_scene(filename, render_window):
    """
    Sets up the scene with colors and textures using vtkGLTFImporter.
    """
    importer = vtk.vtkGLTFImporter()
    importer.SetFileName(filename)
    importer.SetRenderWindow(render_window)
    importer.Update()


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
    # Load the model based on the show_colors flag
    if SHOW_COLORS:
        # vtkGLTFImporter populates the renderer directly
        setup_colored_scene(filename=GLB_FILE, render_window=render_window)
    else:
        # vtkGLTFReader provides an actor that we must add to the renderer
        actor = setup_grey_actor(filename=GLB_FILE)
        renderer.AddActor(actor)

    # --- FINALIZATION ---
    # Reset camera, render, and start interaction
    renderer.ResetCamera()
    render_window.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
