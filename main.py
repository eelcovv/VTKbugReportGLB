import vtk


def main():
    print("Hello from vtkbugreportglb!")

    # Create a renderer and a render window
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color

    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 600)
    render_window.SetWindowName("Suzanne GLB Visualization")

    # Create a render window interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Use vtkGLTFImporter to load the scene
    importer = vtk.vtkGLTFImporter()
    importer.SetFileName("suzanne.glb")
    importer.SetRenderWindow(render_window)
    importer.Update()

    # Reset camera to frame the scene
    renderer.ResetCamera()

    # Render and start interaction
    render_window.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
