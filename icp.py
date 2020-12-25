#from __future__ import print_function
import vtk
import math
from vtk import *

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]) + (p1[2] - p2[2])*(p1[2] - p2[2]))
    
# ============ create source points ==============
print("Creating source points...")
sourcePoints = vtk.vtkPoints()
sourceVertices = vtk.vtkCellArray()

id = sourcePoints.InsertNextPoint(1.0, 0.1, 10.0)
sourceVertices.InsertNextCell(1)
sourceVertices.InsertCellPoint(id)

id = sourcePoints.InsertNextPoint(0.1, 1.1, 10.0)
sourceVertices.InsertNextCell(1)
sourceVertices.InsertCellPoint(id)

id = sourcePoints.InsertNextPoint(0.0, 0.1, 11.0)
sourceVertices.InsertNextCell(1)
sourceVertices.InsertCellPoint(id)

source = vtk.vtkPolyData()
source.SetPoints(sourcePoints)
source.SetVerts(sourceVertices)
if vtk.VTK_MAJOR_VERSION <= 5:
    source.Update()

print("Displaying source points...")
# ============ display source points ==============
pointCount = 3
for index in range(pointCount):
    point = [0,0,0]
    sourcePoints.GetPoint(index, point)
    print("source point[%s]=%s" % (index,point))

pnt1 = [0,0,0]
sourcePoints.GetPoint(0, pnt1)
pnt2 = [0,0,0]
sourcePoints.GetPoint(1, pnt2)
print("dist:%s" % dist(pnt1, pnt2))

sourcePoints.GetPoint(2, pnt2)
print("dist:%s" % dist(pnt1, pnt2))

#============ create target points ==============
print("Creating target points...")
targetPoints = vtk.vtkPoints()
targetVertices = vtk.vtkCellArray()

id = targetPoints.InsertNextPoint(1.0, 0.0, 0.0)
targetVertices.InsertNextCell(1)
targetVertices.InsertCellPoint(id)

id = targetPoints.InsertNextPoint(0.0, 1.0, 0.0)
targetVertices.InsertNextCell(1)
targetVertices.InsertCellPoint(id)

id = targetPoints.InsertNextPoint(0.0, 0.0, 1.0)
targetVertices.InsertNextCell(1)
targetVertices.InsertCellPoint(id)

target = vtk.vtkPolyData()
target.SetPoints(targetPoints)
target.SetVerts(targetVertices)
if vtk.VTK_MAJOR_VERSION <= 5:
    target.Update()


# ============ display target points ==============
print("Displaying target points...")
pointCount = 3
for index in range(pointCount):
    point = [0,0,0]
    targetPoints.GetPoint(index, point)
    print("target point[%s]=%s" % (index,point))

targetPoints.GetPoint(0, pnt1)
targetPoints.GetPoint(1, pnt2)
print("dist:%s" % dist(pnt1, pnt2))

targetPoints.GetPoint(2, pnt2)
print("dist:%s" % dist(pnt1, pnt2))

print("Running ICP ----------------")
# ============ run ICP ==============
icp = vtk.vtkIterativeClosestPointTransform()
icp.SetSource(source)
icp.SetTarget(target)
icp.GetLandmarkTransform().SetModeToRigidBody()
#icp.DebugOn()
icp.SetMaximumNumberOfIterations(50)
icp.StartByMatchingCentroidsOn()
icp.Modified()
icp.Update()

icpTransformFilter = vtk.vtkTransformPolyDataFilter()
if vtk.VTK_MAJOR_VERSION <= 5:
    icpTransformFilter.SetInput(target)
else:
    icpTransformFilter.SetInputData(target)

icpTransformFilter.SetTransform(icp)
icpTransformFilter.Update()

transformedSource = icpTransformFilter.GetOutput()

transMat = icp.GetMatrix()
print(transMat)

# ============ display transformed points ==============
pointCount = 3
for index in range(pointCount):
    point = [0,0,0]
    transformedSource.GetPoint(index, point)
    print("transformed source point[%s]=%s" % (index,point))

transformedSource.GetPoint(0, pnt1)
transformedSource.GetPoint(1, pnt2)
print("dist:%s" % dist(pnt1, pnt2))
transformedSource.GetPoint(2, pnt2)
print("dist:%s" % dist(pnt1, pnt2))

