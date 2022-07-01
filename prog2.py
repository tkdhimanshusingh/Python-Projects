from mpg import *
def main():

    mod_pay_y,mod_pay_d,year_cost_b,year_cost_a = getbreakevenpoint()
    print("yearly cost before modification is: ",year_cost_b)
    print("yearly cost after modification is: ",year_cost_a)
    print(f"modification should pay off in {mod_pay_y} year and {mod_pay_d} days")
    

main()
