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
    status_no_doc = None
    library_path = None
    verbose = False
    
    def __init__(self, filename, test_script, library_path):
    
        self.test_script = test_script

        self.wb_file = filename
        self.wb = xlsxwriter.Workbook(self.wb_file)
        self.ws = self.wb.add_worksheet()
        self.row = 0
        self.header_text = self.wb.add_format({'bold': True, 'font_size': 18})
        self.status_good = self.wb.add_format({'bg_color':'green'})
        self.status_bad = self.wb.add_format({'bg_color':'red'})
        self.status_no_doc = self.wb.add_format({'bg_color':'orange'})
        self.library_path = library_path
                    
    def checkFunctionTestList(self, library_name, documentation_path_and_name, parent_library="", grandparent_library=""):

        self.PrintWS(2, "")
        self.PrintWS(2, "Function check")
        all_functions_tested = True;
        f_validation_code = open( os.path.dirname(os.path.realpath(__file__)) + '\\' + self.test_script, 'r')
        validation_code = f_validation_code.readlines()
        f_validation_code.close()
        
        print("\nChecking function usage...")
        f_library = open(self.library_path + '/' + library_name + '.py', 'r')
        library_data = f_library.readlines();    
        f_library.close()

        
        class_name = ""
        
        for line in library_data:
            if "class" in line:
                if line[0] == "c":
                    if ":" in line:
                        class_name = line[6:len(line)-2]

                        index = class_name.find("(")
                        if (index >= 0):
                            class_name = class_name[0:index]

                        print("Class name: {}".format(class_name))


        print("\nObject list:")
        class_object_list = []
        for line in validation_code:
            if (line.find(class_name + "(") >=0):
                temp_string = line

                index = temp_string.find("=")
                if (index >= 0):
                    temp_string = temp_string[0:index]
                    temp_string = temp_string.lstrip()
                    temp_string = temp_string.rstrip()

                    class_object_list.append(temp_string)

                    print("{}".format(temp_string))
            
        
            

        # main library        
        for line in library_data:
            if "def " in line:
                function_name = line.lstrip()
                function_name = function_name[4:function_name.find('(')]
                
                if (function_name[0] != "_"):
                    if (function_name != "__init__"):
                        doc_function_name = function_name
                        #function_name = "." + function_name
                        
                        found_function_usage = False

                        for line in validation_code:
                            
                            for object_name in class_object_list:                   
                                search_name = object_name + "." + function_name + "("
                            
                                if (line.find(search_name) >=0):
                                    found_function_usage = True
                                    break

                            if (found_function_usage == True):
                                break
                        


                        if (found_function_usage == False):
                            print("*** {} not tested".format(function_name))
                            all_functions_tested = False
                            if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                self.PrintWS(0, function_name)
                            else:
                                self.PrintWS(4, function_name)
                                print("*** {} not documented".format(function_name))
                        else:
                            if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                self.PrintWS(1, function_name)
                            else:
                                self.PrintWS(3, function_name)
                                print("*** {} not documented".format(function_name))

        # parent library     
        if not(parent_library==""):
            f_library = open(self.library_path + '/' + parent_library + '.py', 'r')
            library_data = f_library.readlines();    
            f_library.close()

            for line in library_data:
                if "def " in line:
                    function_name = line.lstrip()
                    function_name = function_name[4:function_name.find('(')]
                
                    if (function_name[0] != "_"):
                        if (function_name != "__init__"):
                            doc_function_name = function_name
                            #function_name = "." + function_name
                        
                            found_function_usage = False

                            for line in validation_code:
                            
                                for object_name in class_object_list:                   
                                    search_name = object_name + "." + function_name + "("
                            
                                    if (line.find(search_name) >=0):
                                        found_function_usage = True
                                        break

                                if (found_function_usage == True):
                                    break
                        


                            if (found_function_usage == False):
                                print("*** {} not tested".format(function_name))
                                all_functions_tested = False
                                if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                    self.PrintWS(0, function_name)
                                else:
                                    self.PrintWS(4, function_name)
                                    print("*** {} not documented".format(function_name))
                            else:
                                if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                    self.PrintWS(1, function_name)
                                else:
                                    self.PrintWS(3, function_name)
                                    print("*** {} not documented".format(function_name))

        # grandparent library     
        if not(grandparent_library==""):
            f_library = open(self.library_path + '/' + grandparent_library + '.py', 'r')
            library_data = f_library.readlines();    
            f_library.close()

            for line in library_data:
                if "def " in line:
                    function_name = line.lstrip()
                    function_name = function_name[4:function_name.find('(')]
                
                    if (function_name[0] != "_"):
                        if (function_name != "__init__"):
                            doc_function_name = function_name
                            #function_name = "." + function_name
                        
                            found_function_usage = False

                            for line in validation_code:
                            
                                for object_name in class_object_list:                   
                                    search_name = object_name + "." + function_name + "("
                            
                                    if (line.find(search_name) >=0):
                                        found_function_usage = True
                                        break

                                if (found_function_usage == True):
                                    break
                        


                            if (found_function_usage == False):
                                print("*** {} not tested".format(function_name))
                                all_functions_tested = False
                                if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                    self.PrintWS(0, function_name)
                                else:
                                    self.PrintWS(4, function_name)
                                    print("*** {} not documented".format(function_name))
                            else:
                                if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                    self.PrintWS(1, function_name)
                                else:
                                    self.PrintWS(3, function_name)
                                    print("*** {} not documented".format(function_name))

        if (class_name.find('(QLabsActor)') >= 0):
            CheckQLabsActorParentClass = True

            f_library = open(self.library_path + '/library_qlabs_actor.py', 'r')
            library_data = f_library.readlines();    
            f_library.close()


            
            for line in library_data:
                if "def " in line:
                    function_name = line.lstrip()
                    function_name = function_name[4:function_name.find('(')]
                
                    if (function_name[0] != "_"):
                        if (function_name != "__init__"):
                            doc_function_name = function_name
                            #function_name = "." + function_name
                            search_name = class_name + "." + function_name
                            if not(search_name in validation_code):
                                print("*** {} not tested".format(function_name))
                                all_functions_tested = False
                                self.PrintWS(0, function_name)
                            else:
                                if self.checkFunctionIsDocumented(documentation_path_and_name, library_name, doc_function_name, class_name):
                                    self.PrintWS(1, function_name)
                                else:
                                    self.PrintWS(3, function_name)
                                    print("*** {} not documented".format(function_name))

                        
                        
        
        
        if (all_functions_tested == True):
            print("\nAll functions tested")

    def checkFunctionIsDocumented(self, documentation_path_and_name, library_name, function_name, class_name):
        
        try:
            f_documentation = open(documentation_path_and_name, 'r')
            doc_data = f_documentation.readlines();
            f_documentation.close()
            
            if (class_name.find('(') >= 0):
                class_name = class_name[0:class_name.find('(')]

            search_name = library_name + "." + class_name + "." + function_name
            found_function = False

            for line in doc_data:
                if search_name in line:
                    test_case = line[line.find(".. automethod:: ")+16:]
                    test_case = test_case.lstrip()
                    test_case = test_case.rstrip()
                    if search_name == test_case:
                        found_function = True

            return found_function
        except:
            print("Failure searching {}".format(documentation_path_and_name))
            return False
                    
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
            if (self.verbose):
                print('{}: {}'.format(text, status))
        elif (status == 0):
            self.ws.write(self.row, 0, "", self.status_bad)
            if (self.verbose):
                print('*** ERROR! *** {}: {}'.format(text, status))
        elif (status == 3):
            self.ws.write(self.row, 0, "ND", self.status_no_doc)
            if (self.verbose):
                print('{}: {} (No Documentation)'.format(text, status))
        elif (status == 4):
            self.ws.write(self.row, 0, "ND", self.status_bad)
            if (self.verbose):
                print('*** ERROR! *** (And no documentation) {}: {}'.format(text, status))
            
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