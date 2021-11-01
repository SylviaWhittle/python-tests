import configparser
import io
import os

# Test if config file exists
# If it doesn't, create a new config file with default parameters
if(not os.path.isfile("Config.ini")) :

    print("No config file found named 'Config.ini'")
    print("Creating Default Config File")

    config = configparser.ConfigParser()
    config.add_section("MainSection")
    config.set("MainSection","sample_type","DNA")

    config.add_section("DNA")
    config.set("DNA","minarea", '300e-9')
    config.set("DNA","maxdeviation", '1.3')
    config.set("DNA","mindeviation", '0.7')
    config.set("DNA","gaussian", '0.1e-9')
    config.set("DNA","thresholdingcriteria", '0.75')
    
    config.add_section("PROTIEN")
    config.set("PROTIEN","minarea", '50e-9')
    config.set("PROTIEN","maxdeviation", '2.0')
    config.set("PROTIEN","mindeviation", '0.3')
    config.set("PROTIEN","gaussian", '0.1e-9')
    config.set("PROTIEN","thresholdingcriteria", '0.5')

    config.add_section("MAC")
    config.set("MAC","minarea", '1000e-9')
    config.set("MAC","maxdeviation", '1.5')
    config.set("MAC","mindeviation", '0.5')
    config.set("MAC","gaussian", '0.25e-09')
    config.set("MAC","thresholdingcriteria", '2.1')

    cfgfile = open("Config.ini",'w')
    config.write(cfgfile)
    cfgfile.close()

# If it does, read the config file and load the parameters
else:
    print("Config file, 'Config.ini' found")
    print("Reading config file")

    config = configparser.ConfigParser()
    config.read("Config.ini")


    print("Config loaded: ")
    print(" ")

    # Print the current parameters
    sample_type = config.get("MainSection","sample_type")
    print(sample_type)
    minarea = config.get(sample_type, "minarea")
    print(minarea)
    maxdeviation = config.get(sample_type, "maxdeviation")
    print(maxdeviation)
    mindeviation = config.get(sample_type, "mindeviation")
    print(mindeviation)
    gaussian = config.get(sample_type, "gaussian")
    print(gaussian)
    thresholdingcriteria = config.get(sample_type, "thresholdingcriteria")
    print(thresholdingcriteria)

    print(" ")
