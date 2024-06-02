
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


