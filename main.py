import math

# TA KLASA TYCZY SIE NOWEGO ALGORYTMU POSTEPOWANIA ( DO OBLICZANIA ILOSCI PANELI NA DZIALCE LUB DACHU)
        
    # funckje do obliczania ilosci rzedow paneli na podstawie podania powierzchni pod instalacja ( w zaleznosci od usytuowania czy poziomo czy pionoowo )
    # czyli trzeba wziac pod uwage parametry paneli
    # w celu obliczenia ilosci paneli oraz rzedow 
    # nalezy na koncu dac informacje o tym ze aplikacja nie bierze pod uwage zacienienia czyli obiektow znajdujacych sie obok instalacji
    # mozna dac na koniec sume wszystkich paneli czy calkowita moc instalacji pv 
    # w trakcie obliczania doboru rzedow i ilosci paneli wziac trzeba pod uwage elementy charakterystyczne dla np dachu ze 0,5m od krawedzi zgodnie z norma jakos tam itp 
    # dla instalcji na ziemi natomiast musi pojawic sie (input np w zaleznosci od danych inwestora) lub podobnie jak w przypadku dachu dac np 1m od krawedzi dzialki
class farm_PV:
    
    def __init__(self, straight_angle, acute_angle, angles, space_table=0.1):
        self.straight_angle = straight_angle
        self.acute_angle = acute_angle
        self.angles = angles
        self.space_table = space_table
        self.Width_of_area = int(input('Please enter width of area PV [m]'))
        self.lenght_of_area = int(input('Please enter lenght of area PV [m]'))
        self.Width_table = float(input('Please enter width of table PV [m]: '))
        self.Lenght_edge = float(input('Please enter lenght of the table PV [m]: '))
        self.Width_geographic = int(input('Please enter width geographic [*]: '))
        self.Angle_panel = int(input('Please enter inclination angle of panels [*]: '))
        #self.Height_edge = float(input('Please enter height from the bottom edge [m]: '))
        
    def __str__(self):
        print('Parameters accepted...') # cos tu nie dziala
        
    def minimum_distance_x(self):
        self.result = (self.straight_angle - self.Width_geographic - self.acute_angle)
        result_1 = (math.sin(math.radians(self.Angle_panel)) * self.Width_table)/(math.tan(math.radians(self.result)))
        print('='*35,f'Calculations for {self.__class__.__name__}...','='*35)
        return (f'Result the minimum distance between tables ("in the light") [m]: {result_1:.2f} ')
        print(result_1)

    def minimum_distance_z(self):
        result_2 = (self.Width_table * math.sin(math.radians(self.angles - self.result - self.Angle_panel))/(math.sin(math.radians(self.result))))
        return (f'Result the minimum distance between tables [m]: {result_2:.2f} ')
    
    def number_panels_row(self):
        self.result_3 = (self.Width_of_area // (self.Width_table + self.space_table))
        return (f'Number of panels in a row {self.result_3:.2f}')
    
    def number_panels_column(self): # tu cos nie halo, nie dziala ta metoda, rozkminic od tego
        self.result_4 = (self.lenght_of_area // (self.Lenght_edge + self.result_3)) # tu cos z obliczeniami do poprawy
        return (f'Number of panels in a column {self.result_4:.2f}')
    
    def suma(self):
        total = self.result_3 + self.result_4
        return (f'Total of all panels {total}')

    # ewentualny zapis do pliku tekstowego
class farm_roof(farm_PV):
    pass
    '''
    def __init__(self, straight_angle, acute_angle, angles):
        super().__init__(straight_angle, acute_angle, angles)
    '''    
    
    
#if __name__ == "__main__":
while True:
    print('-'*70)
    examples = int(input('Enter 1-if PV farm or 2-if rooftop farm PV: '))
    if examples == 1:
        print('You have chosen calculations for a PV farm on the ground')
        print('='*70)
        distance = farm_PV(90,23.27,180)
        print('\n',distance.minimum_distance_x(),'\n',distance.minimum_distance_z(),'\n',distance.number_panels_row(),'\n',distance.number_panels_column(),'\n', distance.suma())
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
        print(distance_1.minimum_distance_x())
        print('-'*70)
        end_program = input('Do you want to end the program, y-yes, n-no?: ')
        if end_program == 'N' or end_program == 'n':  
            continue
        else:
            print('End')
            break
    else:
        print("Please enter value 1 or 2")
        
