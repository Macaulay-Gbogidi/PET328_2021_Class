#...TTOWG!

# input statements
co2_comp = input('What is the CO2 composition?')
n2_comp = input('What is the n2 composition?')
h2s_comp = input('What is the h2s composition?')
h2o_comp = input('What is the h2o composition?')
gas_gravity = input('What is the measured gas gravity?')

 # convert inputs to numerals
co2_comp = float(co2_comp)
n2_comp = float(n2_comp)
h2s_comp = float(h2s_comp)
h2o_comp = float(h2o_comp)
gas_gravity = float(gas_gravity)

# the if statement

if co2_comp > 0.12 or n2_comp > 0.03 or h2s_comp > 0:
    gas_gravity = (gas_gravity - (1.1767*h2s_comp) - \
                      (1.5196*co2_comp) - (0.9672*n2_comp) - \
                       (0.622*h2o_comp))/(1- h2s_comp - co2_comp - n2_comp - h2o_comp)
    print('The corrected gas gravity is', gas_gravity)
    

# continuing after the if block

# computing pseudo-critical pressure and temperature of the hydrocarbon mixture

pseudo_critical_press = 756.8 - (131*gas_gravity) - (3.6*gas_gravity**2)
pseudo_critical_temp = 169.2 + (349.5*gas_gravity) - (74.0*gas_gravity**2)

# displaying the results.
print('The pseudo-critical pressure is {0:.2f} psia'.format(pseudo_critical_press))
print('The pseudo-critical temperature is {0:.2f} deg Rankine'.format(pseudo_critical_temp))
 
# computing pseudo-pressure and pseudo-temperature for the entire mixture

pseudo_pressure = ((1- h2s_comp - co2_comp - n2_comp - h2o_comp)*(756.8 - (131*gas_gravity) - (3.6*gas_gravity**2)))+\
               (1306*h2s_comp)+(1071*co2_comp)+(493.1*n2_comp)+(3200*h2o_comp)

pseudo_temperature = ((1-h2s_comp-co2_comp-n2_comp-h2o_comp)*(169.2 + (349.5*gas_gravity) - (74.0*gas_gravity**2)))+\
              (672.35*h2s_comp)+(547.58*co2_comp)+(227.16*n2_comp)+(1164.9*h2o_comp)

#displaying the results.
print('The pseudo-pressure is {0:.2f} psia'.format(pseudo_pressure))
print('The pseudo-temperature is {0:.2f} deg Rankine'.format(pseudo_temperature))
               
