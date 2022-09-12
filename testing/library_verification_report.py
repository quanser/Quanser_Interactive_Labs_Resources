import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os



class verificationReport:


    ignore_list = []
    row = 0
    test_script = ''
    wb_file = None
    wb = None
    ws = None
    header_text = None
    status_good = None
    status_bad = None
    library_path = None
    
    def __init__(self, filename, test_script, library_path):
    
        self.test_script = test_script

        self.wb_file = filename
        self.wb = xlsxwriter.Workbook(self.wb_file)
        self.ws = self.wb.add_worksheet()
        self.row = 0
        self.header_text = self.wb.add_format({'bold': True, 'font_size': 18})
        self.status_good = self.wb.add_format({'bg_color':'green'})
        self.status_bad = self.wb.add_format({'bg_color':'red'})
        self.library_path = library_path
                    
    def checkFunctionTestList(self, library_name):

        self.PrintWS(2, "")
        self.PrintWS(2, "Function check")
        all_functions_tested = True;
        f_validation_code = open( os.path.dirname(os.path.realpath(__file__)) + '\\' + self.test_script, 'r')
        validation_code = f_validation_code.read()
        f_validation_code.close()
        
        print("\nChecking function usage...")
        f_library = open(self.library_path + '/' + library_name + '.py', 'r')
        library_data = f_library.readlines();    
        f_library.close();
        
        class_name = ""
        
        for line in library_data:
            if "class" in line:
                if line[0] == "c":
                    if ":" in line:
                        class_name = line[6:len(line)-2]
                        print("Class name: {}".format(class_name))
        
        for line in library_data:
            if "def " in line:
                function_name = line.lstrip()
                function_name = function_name[4:function_name.find('(')]
                
                if (function_name[0] != "_"):
                    if (function_name != "__init__"):
                        function_name = class_name + "()." + function_name + "("
                        if not(function_name in validation_code):
                            print("*** {} not tested".format(function_name))
                            all_functions_tested = False
                            self.PrintWS(0, function_name)
                        else:
                            self.PrintWS(1, function_name)

                        
                        
        
        
        if (all_functions_tested == True):
            print("All functions tested")
                    
    def checkValidationLibraryList(self):
        #load this file for self checking
        f_validation_code = open( os.path.dirname(os.path.realpath(__file__)) + '\\' + self.test_script, 'r')
        validation_code = f_validation_code.read()
        f_validation_code.close()
        
        for f in os.listdir(self.library_path):
            if os.path.isfile(os.path.join(self.library_path, f)):
                filename, file_extension = os.path.splitext(f)
                if (file_extension == ".py"):
                    if not(filename in self.ignore_list):
                        if not(filename in validation_code):
                            print("*** {} not loaded in verification".format(filename))
                            self.PrintWS(0, filename)
                        else:
                            self.PrintWS(1, filename)
                            

    def PrintWSHeader(self, text):

        if self.row > 0:
            self.row = self.row + 2
        self.ws.write(self.row, 0, text, self.header_text)
        self.row = self.row + 2
        
    def PrintWS(self, status, text):
        if (status == 1):
            self.ws.write(self.row, 0, "", self.status_good)
        elif (status == 0):
            self.ws.write(self.row, 0, "", self.status_bad)
            
        self.ws.write(self.row, 1, text)
        self.row = self.row + 1


    def WriteFileBuffer(self):

        self.ws.set_column(0,0,2.5)
        self. ws.set_column(1,1,40)

        try:
            self.wb.close()
            os.startfile(self.wb_file)
        except:
            print("\n\n*** Couldn't write the Excel file.")