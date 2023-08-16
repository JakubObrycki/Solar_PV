import math
class farm_PV:

    def __init__(self, straight_angle, acute_angle, angles):
        self.straight_angle = straight_angle
        self.acute_angle = acute_angle
        self.angles = angles
        self.Width_geographic = int(input('Please enter width geographic [*]: '))
        # tutaj warunek trzeba dac ze tylko int
        self.Width_table = float(input('Please enter width of table PV [m]: '))
        # tutaj warunek trzeba dac ze int i float moze 
        self.Lenght_edge = float(input('Please enter lenght of the table PV [m]: '))
        self.Angle_panel = int(input('Please enter inclination angle of panels [*]: '))
        # tutaj warunek trzeba dac ze tylko int
        #self.Height_edge = float(input('Please enter height from the bottom edge [m]: '))
        # tutaj warunek trzeba dac ze int i float moze
        
    def minimum_distance_x(self):
        self.result = (self.straight_angle - self.Width_geographic - self.acute_angle)
        result_1 = (math.sin(math.radians(self.Angle_panel)) * self.Width_table)/(math.tan(math.radians(self.result)))
        print('='*35,f'Calculations for {self.__class__.__name__}...','='*35)
        return(f'Result the minimum distance between tables ("in the light") [m]: {result_1:.2f} ')

    def minimum_distance_z(self):
        result_2 = (self.Width_table * math.sin(math.radians(self.angles - self.result - self.Angle_panel))/(math.sin(math.radians(self.result))))
        return(f'Result the minimum distance between tables [m]: {result_2:.2f} ')
    
class farm_roof(farm_PV):
    
    '''
    to moze sie przydac przy dodawaniu nowych zmiennych
    def __init__(self, straight_angle, acute_angle, angles):
        super().__init__(straight_angle, acute_angle, angles)
    '''    
    def minimum_distance_pionowo(self): # tutaj to nie potrzebne bo dziedziczy po wyzszej klasie ale trzeba dac def jako nadpisz na zmaiany na dachu pionowe i poziome
        self.result = (self.straight_angle - self.Width_geographic - self.acute_angle)
        result_1 = (math.sin(math.radians(self.Angle_panel)) * self.Width_table)/(math.tan(math.radians(self.result)))
        print('='*35,f'Calculations for {self.__class__.__name__}...','='*35)
        return(f'Result the minimum distance between tables ("in the light") [m]: {result_1:.2f} ')
    
    def minimum_distance_poziomo(self):
        self.result = (self.straight_angle - self.Width_geographic - self.acute_angle)
        result_1 = (math.sin(math.radians(self.Angle_panel)) * self.Width_table)/(math.tan(math.radians(self.result)))
        print('='*70)
        return(f'Result the minimum distance between tables ("in the light") [m]: {result_1:.2f} ')

    def minimum_distance_z(self):
        result_2 = (self.Width_table * math.sin(math.radians(self.angles - self.result - self.Angle_panel))/(math.sin(math.radians(self.result))))
        return(f'Result the minimum distance between tables [m]: {result_2:.2f} ')
    
    
distance = farm_PV(90,23.27,180)
print(distance.minimum_distance_x())
print(distance.minimum_distance_z())
print('-'*70)
distance_1 = farm_roof(90,23.27,180)
print(distance_1.minimum_distance_x())
print(distance_1.minimum_distance_z())
