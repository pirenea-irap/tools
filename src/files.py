#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
src.filenames Created on 13 déc. 2017
"""
import os


class PireneaFiles(object):
    """
    Manage the files generated by PIRENEA : renaming, converting
    """

    def __init__(self, folder="D:\PIRENEA\DATA_1"):
        """
        Constructor. Raises ValueError if input folder does not exist.
        """
        self.folder = os.path.abspath(folder)
        if not os.path.isdir(self.folder):
            raise ValueError("Not a valid directory")
        if "PIRENEA" not in self.folder.upper() or "DATA" not in self.folder.upper():
            raise ValueError("Not a valid PIRENEA DATA directory")

    def add_prefix(self, prefix="P0"):
        """
        Search all files recursively and add a prefix to them.
        P0 : PIRENEA files produced with the Villa setup
        P1 : PIRENEA files produced from the IRAP setup
        P2 : PIRENEA files produced from the PILAB setup
        """
        self.__check_prefix(prefix)
        prefix += "_"
        for path, _dirs, files in os.walk(self.folder):
            for filename in files:
                if filename.startswith("P"):
                    print("File {0} has already a prefix.".format(filename))
                else:
                    new_filename = prefix + filename
                    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))

    def remove_prefix(self, prefix="P0"):
        """
        Search all files recursively and remove their prefix.
        """
        self.__check_prefix(prefix)
        prefix += "_"
        for path, _dirs, files in os.walk(self.folder):
            for filename in files:
                if filename.startswith(prefix):
                    f = filename.split(prefix)
                    new_filename = prefix.join(f[1:])
                    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                else:
                    print("File {0} does not begin with prefix : {1}.".format(filename, prefix[:2]))

    def __check_prefix(self, prefix="P0"):
        """
        Check if a prefix is valid.
        """
        prefix_list = {"P0", "P1", "P2"}
        if prefix not in prefix_list:
            raise ValueError("Not a valid prefix for a PIRENEA setup : (P0, P1 or P2 only)")


if __name__ == '__main__':
    """
    test within one directory """
    try:
        input_folder = input("Root directory for Pirenea: ")
        p = PireneaFiles(input_folder)
        print("Working directory is: {0}".format(os.path.abspath(p.folder)))

        do_prefix = input("Add or Remove a prefix (A/R): ")
        if "A" in do_prefix.upper():
            """
            Add a prefix """
            input_prefix = input("Choose a prefix to rename files (P0, P1, P2): ")
            print("Your input prefix is: {} ".format(input_prefix))
            p.add_prefix(input_prefix)
            print("... renaming with prefix is DONE !")
        elif "R" in do_prefix.upper():
            """
            Remove a prefix """
            input_prefix = input("Choose a prefix to remove (P0, P1, P2): ")
            print("Your input prefix is: {} ".format(input_prefix))
            p.remove_prefix(input_prefix)
            print("... removing the prefix is DONE !")

    except ValueError as err:
        print("Error: {0}".format(err))

else:
    print("\nImporting... ", __name__)
