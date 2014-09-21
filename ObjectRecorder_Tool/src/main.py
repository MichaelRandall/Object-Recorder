#!/usr/bin/python

import sys, os, time
import pandas as pd
from pandasql import sqldf

import numpy as np

def clear():
    if os.name in ['nt', 'win32', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

def title():
    print '''
    \t\t-------------------------------------------
    \t\t
    \t\t  Welcome to Simple Contacts, version 1.0
    \t\t         Copyright 2014 (c) by M66
    \t\t
    \t\t-------------------------------------------
    \n\n
    '''
    time.sleep(2)
    clear()
    
def menu():
    menu_items = '''
    \n\tSelect an Option:
    \t-------------------
    \t1) View objects
    \t2) Add object
    \t3) Update object
    \t4) Search objects
    \t-------------------
    \n\n
    '''
    return menu_items
    
def addObject():
    #add object details
    print('hamburger')

def viewObjects():
    objectList = pd.read_csv('C:\Users\Mike\git\Local ObjectRecorder_Tool\ObjectRecorder_Tool\collateral\object_holder.csv')
    #objectItem = raw_input('Who would you like to know about: ')
    
    print objectList
    
    #view a list of objects
    
def updateObject():
    #update an object's details
    print('update')
    
def searchObjects():
    #search for an object by typing part of its name
    print('search')

def getInput():
    user_input = raw_input('Enter a selection number: ')
    print user_input
    

if __name__ == '__main__':
    viewObjects()
    #title()
    #print menu()
    #getInput()