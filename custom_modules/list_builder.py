#!/usr/bin/env python3
""" A play on python lists

    Build custom lists
"""
# TODO: play with nester?
class ListBuilder(list):
    """ Class methods build and play with lists

        Inherits from the built-in list class
    """
    def __init__(self, the_list= []):
        """ (ListBuilder, list) -> list

            Initialize attributes
        """
        self.extend(the_list)

    def csv_file_to_list(self, file_path):
        """ (ListBuilder, file) -> list

            Reads <file_path> and returns list (Empty if file doesn't exist)
        """
        try:
            with open(file_path) as file_obj:    # Open the file
                file_data = file_obj.readlines() # read the data
                for item in file_data: # Process csv and append to list
                    self.extend(item.strip().split(','))
            return self
        except IOError as ioerr:
            print('File IOError: {0}'.format(ioerr))
            return self
    
    def list_of_floats(self):
        """ (ListBuilder) -> list

            Builds a list of integers/floats from input provided by user
            Returns the list
        """
        done = False
        while not done:
            in_val = input('Enter Integer/Float [Q/q to Finish]: ')
            if in_val.strip().upper() == 'Q':
                print('Done...')
                done = True
            else:
                try:
                    in_val = float(in_val)
                    self.append(in_val)  # Add item to list
                except ValueError as verr:
                    print('ValueError : Expected Integer/Float : {0}'
                        .format(verr))
                    print('Try again')
                    continue # 
        return self

    def avg_list_of_num(self, the_list=None):
        """ (ListBuilder, list) -> float

            Averages numbers in <the_list> provided, if none, build list 
            Returns the average of list members
        """
        total = 0.0 # Init
        if the_list == None: # Build your own
            self.extend(self.list_of_floats())
        for lst_item in self:             
            try:
                total += lst_item               
            except Exception as err:
                return err
        return total / len(self)

    def prefix_and_sufix_a_list(self, the_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        """ (ListBuilder, list) -> str

            Prints all the prefixes and suffixes of <the_list>
            Returns (Default):
            
            Prefixes of [1, 2, 3, 4, 5, 6, 7, 8, 9]
            <[]>
            <[1]>
            <[1, 2]>
            <[1, 2, 3]>
            <[1, 2, 3, 4]>
            <[1, 2, 3, 4, 5]>
            <[1, 2, 3, 4, 5, 6]>
            <[1, 2, 3, 4, 5, 6, 7]>
            <[1, 2, 3, 4, 5, 6, 7, 8]>
            <[1, 2, 3, 4, 5, 6, 7, 8, 9]>
            <[1, 2, 3, 4, 5, 6, 7, 8, 9]>
            <[2, 3, 4, 5, 6, 7, 8, 9]>
            <[3, 4, 5, 6, 7, 8, 9]>
            <[4, 5, 6, 7, 8, 9]>
            <[5, 6, 7, 8, 9]>
            <[6, 7, 8, 9]>
            <[7, 8, 9]>
            <[8, 9]>
            <[9]>
            <[]>
            Suffixes of [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        self.extend(the_list)

        print('Prefixes of {0}'.format(repr(self)))
        for lst_item in range(0, len(self) + 1):
            print('<{0}>'.format(self[0 : lst_item]))

        for lst_item in range(0, len(the_list) + 1):
            print('<{0}>'.format(self[lst_item : len(self) + 1]))
        print('Suffixes of {0}'.format(repr(self)))
                

         
if __name__ == '__main__':
    help(ListBuilder)


    