def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
  
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power)*100
    
    if 100 >= efficiency >= 80:
        return "green"
    elif 60 <= efficiency < 80:
        return "orange"
    elif 30 <= efficiency < 60:
        return "red"
    elif efficiency < 30:
        return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    ratio = temperature * neutrons_produced_per_second
    
    if ratio < threshold*(9/10):
        return "LOW"
    elif threshold * (9/10) < ratio < threshold * (11/10):
        return "NORMAL"
    else:
        return "DANGER"
