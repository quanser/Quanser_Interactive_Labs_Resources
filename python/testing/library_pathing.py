import sys

def append_path(pathToCommon):  
    pythonApplicationLibrariesPath = '../../../Python_application_libraries/'
    sys.path.append(pythonApplicationLibrariesPath+'application_modules/')
    sys.path.append(pythonApplicationLibrariesPath+'quanser_products/')
    sys.path.append(pythonApplicationLibrariesPath+'utilities/')
    sys.path.append(pythonApplicationLibrariesPath+'quanser_interactive_labs/')