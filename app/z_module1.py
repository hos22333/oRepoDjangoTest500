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
        # Calculate belt weight
        belt_weight = self.belt_weight_per_meter * self.length * self.width * 2

        # Calculate part weight
        part_weight = self.part_weight_per_meter * self.length * self.width

        # Calculate normal force
        normal_force = (belt_weight + part_weight) * 10

        # Calculate horizontal force
        horizontal_force = normal_force * self.friction

        # Calculate power
        calc_power = horizontal_force * self.velocity

        # Calculate total power
        total_power = (calc_power * self.fos) / self.eff

        # Format the power string
        power_str = f"{total_power:.2f}"
        self.Power = power_str

        # Log the result (placeholder function for WriteToSheetBelt)
        self.log_to_sheet(self.length, self.belt_weight_per_meter, self.part_weight_per_meter, self.friction, self.velocity, self.fos, self.eff, power_str, "0", "0")
        

    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetBelt
        print(f"Logging to sheet: {args}")

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
        weight_per_meter_sheet = 80
        weight_per_meter_ipn = 15
        weight_per_meter_other = 25
        weight_per_meter_total = weight_per_meter_sheet + weight_per_meter_ipn + weight_per_meter_other
        weight_one_end_carriage = 220
        weight_per_meter_handrail = 8
        weight_per_meter_scraper = 70

        # Weight calculations
        walkway_weight = weight_per_meter_total * self.bridge_length
        weight_end_carriage_total = weight_one_end_carriage * 2
        weight_handrail_total = weight_per_meter_handrail * self.bridge_length * 2
        weight_scraper_total = weight_per_meter_scraper * self.channel_width * self.n_channel * 2

        total_weight_steel = walkway_weight + weight_end_carriage_total + weight_handrail_total
        total_weight = total_weight_steel + weight_scraper_total
        
        self.Weight_Total = f"{total_weight:.2f}"
        self.Weight_steel = f"{total_weight_steel:.2f}"
        self.Weight_scraper = f"{weight_scraper_total:.2f}"

        # Power calculations
        normal_force = total_weight * 10
        horizontal_force = normal_force * self.friction
        calc_power = horizontal_force * self.velocity
        total_power = (calc_power * self.fos) / self.eff
        self.Power = f"{total_power:.2f}"


        # Lifting power calculations
        lifting_wheel_dia = 0.2
        lifting_rpm = 3.6
        lifting_velocity = (3.14 * lifting_wheel_dia * lifting_rpm) / 60
        lifting_weight = weight_per_meter_scraper * self.channel_width * self.n_channel
        lifting_power = lifting_weight * 10 * lifting_velocity
        lifting_motor_power = (lifting_power * self.fos) / 0.7
        self.Power_lifting = f"{lifting_motor_power:.2f}"

        # Speed calculations
        speed_rps = self.velocity / (3.14 * self.wheel_diameter)
        speed_rpm = speed_rps * 60
        self.DriveRPM =  f"{speed_rpm:.2f}"
           
        #self.log_to_sheet(self.n_channel, self.channel_width * 1000, self.civil_width * 1000, self.bridge_length * 1000, self.friction, self.velocity * 1000, self.fos, self.eff, self.wheel_diameter * 1000, power_str, total_weight, total_weight_steel, weight_scraper_total, lifting_motor_power_str, str_speed_rpm)



    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetGritremoval
        print(f"Logging to sheet: {args}")

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
        weight_per_meter_sheet = 80
        weight_per_meter_ipn = 15
        weight_per_meter_other = 25
        weight_per_meter_total = weight_per_meter_sheet + weight_per_meter_ipn + weight_per_meter_other
        weight_one_end_carriage = 220
        weight_per_meter_handrail = 8
        weight_per_meter_scraper = 70

        # Weight calculations
        walkway_weight = weight_per_meter_total * self.walkway_length
        weight_end_carriage_total = weight_one_end_carriage * 2
        weight_handrail_total = weight_per_meter_handrail * self.walkway_length * 2
        weight_scraper_total = weight_per_meter_scraper * self.walkway_length * 2

        total_weight_steel = walkway_weight + weight_end_carriage_total + weight_handrail_total
        total_weight = total_weight_steel + weight_scraper_total

        self.Weight_Total = total_weight
        self.Weight_steel = total_weight_steel
        self.Weight_scraper = weight_scraper_total

        # Power calculations
        normal_force = total_weight * 10
        horizontal_force = normal_force * self.friction
        calc_power = horizontal_force * self.velocity
        total_power = (calc_power * self.fos) / self.eff
        self.Power = total_power
 
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
        # Weight calculations
        hor_force = self.load_per_meter * (self.diameter / 2) * self.n_arm
        calc_power = hor_force * self.velocity
        total_power = (calc_power * self.fos) / self.eff

        ret_str1 = f"Power: {total_power} Wat"

        self.Power = total_power

  

    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetThickener
        print(f"Logging to sheet: {args}")

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
        area = self.length * self.width
        volume = self.length * self.width * self.water_depth
        equivalent_diameter = math.sqrt((4 * area) / math.pi)
        impeller_diameter = equivalent_diameter * self.impeller_diameter_factor

        power11 = (self.velocity_gradient ** 2) * self.water_kinematic_viscosity * volume
        speed_rps = ((power11) / (self.impeller_coefficient * self.water_density * (impeller_diameter ** 5))) ** (1/3)
        speed_rpm = speed_rps * 60
        power22 = self.impeller_coefficient * self.water_density * (speed_rps ** 3) * (impeller_diameter ** 5)

        power_needed = (power11 * self.safety_factor) / (self.eff_from_impeller_to_water * self.eff_motor * self.eff_gearbox)

        power_needed_str = f"{power_needed:.2f}"
        power11_str = f"{power11:.2f}"
        impeller_diameter_str = f"{impeller_diameter:.2f}"
        speed_rpm_str = f"{speed_rpm:.2f}"

        self.log_to_sheet(self.length, self.width, self.water_depth, self.impeller_coefficient, self.velocity_gradient, self.impeller_diameter_factor, self.water_kinematic_viscosity, self.water_density, self.safety_factor, power_needed_str, impeller_diameter_str, speed_rpm_str, "0", "0", "0")

        result = {
            "value1": f"Power: {power_needed_str} Wat",
            "value2": f"ImpellerDiameter: {impeller_diameter_str} Meter",
            "value3": f"Speed: {speed_rpm_str} RPM",
        }

        return result

    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetMixer
        print(f"Logging to sheet: {args}")

##########################
#        Mixer Cir       #
##########################
class MixerCir500:
    def __init__(self, var1, var3, var4, var5, var6, var7, var8, var9):
        self.length = var1
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
        area = (math.pi / 4) * self.length * self.length
        volume = area * self.water_depth
        equivalent_diameter = math.sqrt((4 * area) / math.pi)
        impeller_diameter = equivalent_diameter * self.impeller_diameter_factor

        power11 = (self.velocity_gradient ** 2) * self.water_kinematic_viscosity * volume
        speed_rps = ((power11) / (self.impeller_coefficient * self.water_density * (impeller_diameter ** 5))) ** (1/3)
        speed_rpm = speed_rps * 60
        power22 = self.impeller_coefficient * self.water_density * (speed_rps ** 3) * (impeller_diameter ** 5)

        power_needed = (power11 * self.safety_factor) / (self.eff_from_impeller_to_water * self.eff_motor * self.eff_gearbox)

        power_needed_str = f"{power_needed:.2f}"
        power11_str = f"{power11:.2f}"
        impeller_diameter_str = f"{impeller_diameter:.2f}"
        speed_rpm_str = f"{speed_rpm:.2f}"

        self.log_to_sheet(self.length, "0", self.water_depth, self.impeller_coefficient, self.velocity_gradient, self.impeller_diameter_factor, self.water_kinematic_viscosity, self.water_density, self.safety_factor, power_needed_str, impeller_diameter_str, speed_rpm_str, "0", "0", "0")

        result = {
            "value1": f"Power: {power_needed_str} Wat",
            "value2": f"ImpellerDiameter: {impeller_diameter_str} Meter",
            "value3": f"Speed: {speed_rpm_str} RPM",
        }

        return result

    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetMixer
        print(f"Logging to sheet: {args}")

##########################
#         Tanks Rec      #
##########################

class RecTankCalc500:
    def __init__(self, RT500var1, RT500var2, RT500var3, RT500var4, RT500var5, RT500var6, RT500var7):
        self.c2 = RT500var1
        self.c3 = RT500var2
        self.c4 = RT500var3
        self.c5 = RT500var4
        self.c6 = RT500var5
        self.c20 = RT500var6
        self.c23 = RT500var7

    def calculate(self):
        pl_shell = ((self.c2 + self.c2 + self.c3 + self.c3) / 1000) * (self.c4 / 1000) * (self.c5 / 1000) * 8000
        pl_base = (self.c2 / 1000) * (self.c3 / 1000) * (self.c6 / 1000) * 8000
        pl_split = (self.c3 / 1000) * (self.c4 / 1000) * (self.c5 / 1000) * 8000 * self.c20
        total_plates = pl_shell + pl_base + pl_split

        n_of_lvls = self.c4 / 500
        stif_horizontal = n_of_lvls * ((self.c2 + self.c2 + self.c3 + self.c3) / 1000) * self.c23
        stif_vertical = ((self.c2 + self.c2 + self.c3 + self.c3) / 1000) * (self.c4 / 1000) * self.c23
        stif_base = (((self.c2 / 1000) * (self.c3 / 1000)) + (3 * (self.c2 / 1000))) * self.c23
        stif_inner = n_of_lvls * (self.c3 / 1000) * self.c23 * self.c20

        total_stif = stif_horizontal + stif_vertical + stif_base + stif_inner

        total_weight = 1 * (total_plates + total_stif)
        total_weight = round(total_weight, 2)

        self.log_to_sheet(self.c2, self.c3, self.c4, self.c5, self.c6, self.c20, self.c23, total_weight, "0")

        result = {
            "value1": total_weight,
        }

        return result

    def log_to_sheet(self, *args):
        # Placeholder function for WriteToSheetRecTank
        print(f"Logging to sheet: {args}")


