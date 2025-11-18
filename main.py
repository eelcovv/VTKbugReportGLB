import vtk


def main():
    print("Hello from vtkbugreportglb!")
    # Create a reader for the GLB file
    reader = vtk.vtkGLTFReader()
    reader.SetFileName("suzanne.glb")
    reader.Update()

    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color

    # Create a render window
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 600)
    render_window.SetWindowName("Suzanne GLB Visualization")

    # Create a render window interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Set up the camera
    renderer.ResetCamera()

    # Start the interaction
    interactor.Initialize()
    interactor.Start()


if __name__ == "__main__":
    main()
