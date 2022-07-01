def getinfo():
        miles = int(input('enter miles driven/year : '))
        costpgallon = float(input("enter cost/gallon : "))
        costmod = float(input("enter cost of modification : "))
        mpg_before = float(input("enter mpg before modification : "))
        mpg_after = float(input("enter mpg after modification : "))
        
        return miles,costpgallon,costmod,mpg_before,mpg_after

def getyearlycost():
        miles,costpgallon,costmod,mpg_before,mpg_after = getinfo()
       
       
        gallon_yearb = miles/mpg_before
        gallon_yeara = miles/mpg_after
        year_cost_b = gallon_yearb * (costpgallon)
        year_cost_a = round(gallon_yeara * (costpgallon),2)
        
        return year_cost_b,year_cost_a,costmod

def getbreakevenpoint():
        year_cost_b,year_cost_a,costmod = getyearlycost()
        
        diff = year_cost_b - year_cost_a
        mod_pay = round((costmod/diff)*365)
        mod_pay_y = mod_pay // 365
        mod_pay_d = mod_pay%365
        
        return mod_pay_y,mod_pay_d,year_cost_b,year_cost_a

