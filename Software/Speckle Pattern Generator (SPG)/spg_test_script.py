"""
    Speckle Pattern Generator (SPG)
    -- Test Script

    Fluvio L Lobo Fenoglietto 03/17/2017
"""

try:
    from    dxfwrite    import  DXFEngine   as  dxf

    status = 0
    
except ImportError as iErr:
    print iErr
    print "Download the dxfwrite module using pip"

    status = -1

if status == 0:

    drawing = dxf.drawing('test.dxf')
    drawing.add(dxf.arc(radius=20.0, center=(2.0, 2.0)))
    drawing.save()
