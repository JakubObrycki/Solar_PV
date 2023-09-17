import math

class farm_PV:
    
    def __init__(self, straight_angle, acute_angle, angles, space_table=0.1):
        self.straight_angle = straight_angle
        self.acute_angle = acute_angle
        self.angles = angles
        self.space_table = space_table
        self.Width_of_area = int(input('Please enter width of area PV [m]'))
        self.lenght_of_area = int(input('Please enter lenght of area PV [m]'))
        self.lenght_table = float(input('Please enter lenght of table PV [m]: '))
        self.width_edge = float(input('Please enter width of the table PV [m]: '))
        self.Width_geographic = int(input('Please enter width geographic [*]: '))
        self.Angle_panel = int(input('Please enter inclination angle of panels [*]: '))
        
    def __str__(self):
        title = ('Parameters accepted...')
        return title
        
    def minimum_distance_x(self):
        self.result = (self.straight_angle - self.Width_geographic - self.acute_angle)
        self.result_1 = (math.sin(math.radians(self.Angle_panel)) * self.lenght_table)/(math.tan(math.radians(self.result)))
        print('='*35,f'Calculations for {self.__class__.__name__}...','='*35)
        return (f'Result the minimum distance between tables ("in the light") [m]: {self.result_1:.2f} ')
        print(result_1)

    def minimum_distance_z(self):
        result_2 = (self.lenght_table * math.sin(math.radians(self.angles - self.result - self.Angle_panel))/(math.sin(math.radians(self.result))))
        return (f'Result the minimum distance between tables [m]: {result_2:.2f} ')
    
    def number_panels_row(self):
        self.result_3 = (self.Width_of_area // (self.width_edge + self.space_table))
        return (f'Number of panels in a row {self.result_3:.2f}')
    
    def number_panels_column(self): 
        self.result_4 = (self.lenght_of_area // (self.lenght_table + self.result_1)) # tu cos z obliczeniami do poprawy delikatnie !!
        return (f'Number of panels in a column {self.result_4:.2f}')
    
    def sum(self):
        total = self.result_3 + self.result_4
        return (f'Total of all panels {total}')
        
        
class farm_roof(farm_PV):
    
    def __init__(self, straight_angle, acute_angle, angles, edge_distance=0.5):
        super().__init__(straight_angle, acute_angle, angles) 
        self.edge_distance = edge_distance
        
    def number_panels_row(self):
        self.result_3 = (self.Width_of_area // (self.width_edge + self.space_table + (2*self.edge_distance)))
        return (f'Number of panels in a row {self.result_3:.2f}')
    
    def number_panels_column(self): 
        self.result_4 = (self.lenght_of_area // (self.lenght_table + self.result_1)) # tu cos z obliczeniami do poprawy delikatnie !!
        return (f'Number of panels in a column {self.result_4:.2f}')

if __name__ == "__main__":
while True:
    print('-'*70)
    examples = int(input('Enter 1-if PV farm or 2-if rooftop farm PV: '))
    if examples == 1:
        print('You have chosen calculations for a PV farm on the ground')
        print('='*70)
        distance = farm_PV(90,23.27,180)
        print('\n',distance.minimum_distance_x(),'\n',distance.minimum_distance_z(),'\n',distance.number_panels_row(),'\n',
        distance.number_panels_column(),'\n', distance.sum())
        print('-'*70)
        end_program = input('Do you want to end the program, y-yes, n-no?: ')
        if end_program == 'N' or end_program == 'n':  
            continue
        else:
            print('End')
            break
           
    elif examples == 2:
        print('You have chosen calculations for a rooftop PV farm')
        print('='*70)
        distance_1 = farm_roof(90,23.27,180)
        print('\n',distance_1.minimum_distance_x(),'\n',distance_1.number_panels_row(),'\n',
        distance_1.number_panels_column(),'\n',distance_1.sum())
        print('-'*70)
        end_program = input('Do you want to end the program, y-yes, n-no?: ')
        if end_program == 'N' or end_program == 'n':  
            continue
        else:
            print('End')
            break
    else:
        print("Please enter value 1 or 2")
    main()
        
