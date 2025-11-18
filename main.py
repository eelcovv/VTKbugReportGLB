import vtk


def main():
    print("Hello from vtkbugreportglb!")
    # Create a reader for the GLB file
    reader = vtk.vtkGLTFReader()
    reader.SetFileName("suzanne.glb")
    reader.Update()

    # As the vtkGLTFReader can output a vtkMultiBlockDataSet, we need to
    # use a vtkCompositeDataGeometryFilter to extract the polygonal data.
    polydata_filter = vtk.vtkCompositeDataGeometryFilter()
    polydata_filter.SetInputConnection(reader.GetOutputPort())
    polydata_filter.Update()

    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(polydata_filter.GetOutputPort())
    mapper.SetScalarVisibility(False)

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

    # Render and start interaction
    render_window.Render()
    interactor.Initialize()
    interactor.Start()


if __name__ == "__main__":
    main()
