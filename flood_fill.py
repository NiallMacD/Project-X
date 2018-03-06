# Flood fill start

import numpy as np
size = 17

test = np.zeros((size,size), dtype = float)
test_with_walls = np.pad(test, (1), 'constant', constant_values=(1))
test_with_walls[:, int(size/2)] =  1.0
test_with_walls[int(size/2), :] =  1.0

test_with_walls_after_fill = np.copy(test_with_walls)

def floodfill(matrix, x, y):
    #"hidden" stop clause - not reinvoking for numbers less than a value.
    if matrix[x][y] < 1:  
        matrix[x][y] = 2 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y)
        if y > 0:
            floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1)
            
floodfill(test_with_walls_after_fill, 1, 5 )
            
def floodfill_3d(matrix, x, y, z):
    #"hidden" stop clause - not reinvoking for numbers less than a value.
    if matrix[x][y][z] < 1:  
        matrix[x][y][z] = 2 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill_3d(matrix,x-1,y, z)
        if x < len(matrix[y]) - 1:
            floodfill_3d(matrix,x+1,y, z)
        if y > 0:
            floodfill_3d(matrix,x,y-1, z)
        if y < len(matrix) - 1:
            floodfill_3d(matrix,x,y+1, z)
        if z > 0:
            floodfill_3d(matrix,x,y, z-1)
        if z < len(matrix) - 1:
            floodfill_3d(matrix,x,y, z+1)




test_3d = np.zeros((size, size, size), dtype = float)
test_3d_with_walls = np.pad(test_3d, (1), 'constant', constant_values=(1))
test_3d_with_walls[:, int(size/2)] =  1.0
test_3d_with_walls[int(size/2), :] =  1.0

test_3d_with_walls_after_fill = np.copy(test_3d_with_walls)

floodfill_3d(test_3d_with_walls_after_fill, 1, 3 ,4)

npoints = size + 2
import vtk; import numpy as  np
# creating vti image file 
filename = "3d_test.vti"
imageData = vtk.vtkImageData()
imageData.SetDimensions(npoints, npoints, npoints )
imageData.SetOrigin( (-npoints+1)/2, (-npoints+1)/2, 0 )
if vtk.VTK_MAJOR_VERSION <= 5:
    imageData.SetNumberOfScalarComponents(1)
    imageData.SetScalarTypeToDouble()
else:
    imageData.AllocateScalars(vtk.VTK_DOUBLE, 1)
dims = imageData.GetDimensions()
# Fill every entry of the image data
for z in range(dims[2]):
    for y in range(dims[1]):
        for x in range(dims[0]):
            imageData.SetScalarComponentFromDouble(x, y, z, 0, test_3d_with_walls[x,y,z])
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(filename)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()



