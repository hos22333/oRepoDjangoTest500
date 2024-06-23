import math

##########################
#         Screen        #
##########################
class cScreen:
    def __init__(self):
        ################################ INPUT ################################
        ################################ INPUT ################################
        self.ScreenWidth        = None   
        self.ChannelHeight      = None  
        self.SprocketDiameter   = None
        self.Velocity           = None
        self.FOS                = None
        self.LoadPerMeterSq     = None
        self.Eff                = None

        self.WaterLevel         = None
        self.BarSpacing         = None
        self.BarThickness       = None
        self.BarWidth           = None
        self.InclinationDegree  = None
        ################################
        self.MaterialCostLEKG   = None     #Material Cost LE/KG
        
        self.GearMotor          = None
        self.Bearing            = None
        self.Chain              = None
        self.DriveShaft         = None
        self.Sprocket           = None
        self.Rake               = None
        self.Accessories        = None
        self.ControlPanel       = None
        self.DifferentialLevel  = None
        
        self.Supervision        = None
        self.Manufacturing      = None
        self.Transportation     = None
        self.Consumables        = None
        self.Packing            = None

        self.MarginFactor       = None
        self.RiskFactor         = None

        ################################ OUTPUT ################################
        ################################ OUTPUT ################################
        self.weight_result  = None
        self.power_result   = None
        self.speed_result   = None

        self.MaterialCost_result            = None
        self.StandardCost_Total_Out         = None
        self.ManufacturingCost_Total_Out    = None
        self.SumOfCost_Out                  = None
        self.Price                          = None
        self.TotalPrice                     = None
        
        self.DrawingCode                    = None

        self.oTest = None
        

    def mWeight_calculation(self):
        screen_width = self.ScreenWidth / 1000
        channel_height = self.ChannelHeight / 1000
        weight_per_sq_meter = 100
        weight_fix_added = 300
        weight = weight_fix_added + (weight_per_sq_meter * screen_width * (float(channel_height) + 2))
        self.weight_result = weight

    def mPower_calculation(self):
        screen_width = self.ScreenWidth / 1000
        channel_height = self.ChannelHeight / 1000
        force = self.LoadPerMeterSq * 10 * screen_width * channel_height
        calc_power = force * self.Velocity
        total_power = (calc_power * self.FOS) / self.Eff
        self.power_result = "Power: {:.2f} Wat..".format(total_power)

    def mSpeed_calculation(self):
        speed_rps = self.Velocity / (3.14 * (self.SprocketDiameter / 1000))
        speed_rpm = speed_rps * 60
        self.speed_result = "Speed: {:.2f} RPM..".format(speed_rpm)

    def mCost(self):

        self.MaterialCost_result = self.MaterialCostLEKG * self.weight_result

        self.StandardCost_Total_Out = (self.GearMotor + 
                                       self.Bearing + 
                                       self.Chain + 
                                       self.DriveShaft + 
                                       self.Sprocket + 
                                       self.Rake + 
                                       self.Accessories+ 
                                       self.ControlPanel+ 
                                       self.DifferentialLevel)                                        
        
        self.ManufacturingCost_Total_Out = (self.Supervision + 
                                            self.Manufacturing + 
                                            self.Transportation + 
                                            self.Consumables + 
                                            self.Packing)  

        self.SumOfCost_Out = (self.MaterialCost_result + 
                                    self.StandardCost_Total_Out + 
                                    self.ManufacturingCost_Total_Out) 

        self.Price = self.SumOfCost_Out * self.MarginFactor

        self.TotalPrice = self.Price * self.RiskFactor 
        
    def dataSheet(self):
        self.oTest = 66

    def mDrawingCode(self):

        digit_to_letter = {
        '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E',
        '6': 'F', '7': 'G', '8': 'H', '9': 'I', '0': 'J'
        }
        concatenated_string = (str(self.ScreenWidth) + '$' + 
                            str(self.ChannelHeight) + '$' +
                            str(self.WaterLevel) + '$' +
                            str(self.BarSpacing) + '$' +
                            str(self.BarThickness) + '$' +
                            str(self.BarWidth) + '$' +
                            str(self.InclinationDegree))

        self.DrawingCode = ''.join(digit_to_letter.get(char, char) for char in concatenated_string)

##########################
#         Belt           #
##########################
class cBelt:
    def __init__(self, length, width, belt_weight_per_meter, part_weight_per_meter, friction, velocity, fos, eff):
        self.length                 = length/1000
        self.width                  = width/1000
        self.belt_weight_per_meter  = belt_weight_per_meter
        self.part_weight_per_meter  = part_weight_per_meter
        self.friction               = friction
        self.velocity               = velocity
        self.fos                    = fos
        self.eff                    = eff

        self.Power = None

    def calculate_power(self):

        self.Power = 552

        # Log the result (placeholder function for WriteToSheetBelt)
        self.log_to_sheet(self.length, self.belt_weight_per_meter, self.part_weight_per_meter, self.friction, self.velocity, self.fos, self.eff, power_str, "0", "0")
        


##########################
#         Gritremoval    #
##########################
class cGrit:
    def __init__(self, G500var1, G500var2, G500var3, G500var4, G500var5, G500var6, G500var7, G500var8, G500var9):
        self.n_channel          = G500var1
        self.channel_width      = G500var2 / 1000
        self.civil_width        = G500var3 / 1000
        self.bridge_length      = G500var4 / 1000
        self.friction           = G500var5
        self.velocity           = G500var6 / 1000
        self.fos                = G500var7
        self.eff                = G500var8
        self.wheel_diameter     = G500var9 / 1000
        
        self.Power = None
        self.DriveRPM = None
        self.Weight_Total = None
        self.Weight_steel = None
        self.Weight_scraper = None
        self.Power_lifting = None

    def calculate(self):
        
        self.Weight_Total = 5622
        self.Weight_steel = 2533
        self.Weight_scraper = 2544
        
        self.Power = 653

        
        self.Power_lifting = 354

        
        self.DriveRPM =  256
           
        #self.log_to_sheet(self.n_channel, self.channel_width * 1000, self.civil_width * 1000, self.bridge_length * 1000, self.friction, self.velocity * 1000, self.fos, self.eff, self.wheel_diameter * 1000, power_str, total_weight, total_weight_steel, weight_scraper_total, lifting_motor_power_str, str_speed_rpm)



##########################
#         PST            #
##########################
class cPST:
    def __init__(self, P500var1, P500var2, P500var3, P500var4, P500var5):
        self.walkway_length     = P500var1/2000
        self.friction           = P500var2
        self.velocity           = P500var3
        self.fos                = P500var4
        self.eff                = P500var5
                
        self.Power = None
        self.Weight_Total = None
        self.Weight_steel = None
        self.Weight_scraper = None


    def calculate(self):
        
        self.Weight_Total = 454
        self.Weight_steel = 4277
        self.Weight_scraper = 578
        
        self.Power = 354
 
##########################
#        Thickener       #
##########################
class cThickener:
    def __init__(self, T500var1, T500var2, T500var3, T500var4, T500var5, T500var6):
        self.diameter           = T500var1/1000
        self.n_arm              = T500var2
        self.velocity           = T500var3
        self.fos                = T500var4
        self.eff                = T500var5
        self.load_per_meter     = T500var6
        
        self.Power = None

    def calculate(self):
        

        self.Power = 539

  

##########################
#        Mixer Rec       #
##########################
class MixerRec500:
    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9):
        self.length = var1
        self.width = var2
        self.water_depth = var3
        self.impeller_coefficient = var4
        self.velocity_gradient = var5
        self.impeller_diameter_factor = var6
        self.water_kinematic_viscosity = var7
        self.water_density = var8
        self.safety_factor = var9
        self.eff_from_impeller_to_water = 0.8
        self.eff_motor = 0.9
        self.eff_gearbox = 0.9

    def calculate(self):

        return "6655"

