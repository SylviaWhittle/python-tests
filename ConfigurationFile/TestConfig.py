
import configparser
# import io
import os

# Test if config file exists
# If it doesn't, create a new config file with default parameters
# If it does, load the config parameters
if(not os.path.isfile("Config.ini")) :

    print("No config file found named 'Config.ini'")
    print("Creating Default Config File")

    config = configparser.ConfigParser(allow_no_value=True)

    # General parameters
    config.add_section("MainSection")
    config.set("MainSection", "; File path - the directory where the files are")
    config.set("MainSection", "path", './')
    config.set("MainSection", "; Set the sample type here")
    config.set("MainSection", "sample_type","DNA")
    config.set("MainSection", "; Set the file type to look for")
    config.set("MainSection", "fileend", "('.spm','.gwy','*.[0-9]')")
    config.set("MainSection", "filetype", '*.[0-9]')
    config.set("MainSection", "; Set the extension of exported files")
    config.set("MainSection", "extension", '.tiff')
    config.set("MainSection", "; Set height scale values")
    config.set("MainSection", "minheightscale", '-0e-9')
    config.set("MainSection", "maxheightscale", '3e-9')
    config.set("MainSection", "; Set the size of the cropped window / 2 in pixels")
    config.set("MainSection", "cropwidth", '40e-9')
    config.set("MainSection", "splitwidth", '2e-6')
    config.set("MainSection", "; Set the number of bins")
    config.set("MainSection", "bins", '25')

    config.set("MainSection", "; Set the value of different valriables, based on the type of the sample.")
    config.set("MainSection", "; Minarea is the minimum size for grain determination")
    config.set("MainSection", "; Maxdeviation and mindeviation are the allowable deviations from the median pixel size for removal of large and small objects")

    # DNA Specific parameters 
    config.add_section("DNA")
    config.set("DNA","minarea", '300e-9')
    config.set("DNA","maxdeviation", '1.3')
    config.set("DNA","mindeviation", '0.7')
    config.set("DNA","gaussian", '0.1e-9')
    config.set("DNA","thresholdingcriteria", '0.75')
    
    # Protein specific parameters
    config.add_section("PROTIEN")
    config.set("PROTIEN","minarea", '50e-9')
    config.set("PROTIEN","maxdeviation", '2.0')
    config.set("PROTIEN","mindeviation", '0.3')
    config.set("PROTIEN","gaussian", '0.1e-9')
    config.set("PROTIEN","thresholdingcriteria", '0.5')

    # MAC specific parameters
    config.add_section("MAC")
    config.set("MAC","minarea", '1000e-9')
    config.set("MAC","maxdeviation", '1.5')
    config.set("MAC","mindeviation", '0.5')
    config.set("MAC","gaussian", '0.25e-09')
    config.set("MAC","thresholdingcriteria", '2.1')

    # Write the config to file
    cfgfile = open("Config.ini",'w')
    config.write(cfgfile)
    cfgfile.close()

# If a config file does exist, read the config file and load the parameters
else:
    print("Config file, 'Config.ini' found")
    print("Reading config file")

    config = configparser.ConfigParser()
    config.read("Config.ini")

    print("Config loaded: ")
    print(" ")

    # Print the current parameters
    # Main section
    path = config.get("MainSection", "path")
    print("Path: " + path)
    sample_type = config.get("MainSection","sample_type")
    print("Sample type: " + sample_type)
    fileend = config.get("MainSection", "fileend")
    print("File end: " + fileend)
    filetype = config.get("MainSection", "filetype")
    print("File type: " + filetype)
    extension = config.get("MainSection", "extension")
    print("Extension: " + extension)
    minheightscale = config.get("MainSection", "minheightscale")
    print("Min height scale: " + minheightscale)
    maxheightscale = config.get("MainSection", "maxheightscale")
    print("Max height scale: " + maxheightscale)
    cropwidth = config.get("MainSection", "cropwidth")
    print("Crop width: " + cropwidth)
    splitwidth = config.get("MainSection", "splitwidth")
    print("Split width: " + splitwidth)
    bins = config.get("MainSection", "bins")
    print("Bins: " + bins)

    # Sample type specific section
    minarea = config.get(sample_type, "minarea")
    print("Min area: " + minarea)
    maxdeviation = config.get(sample_type, "maxdeviation")
    print("Max deviation: " + maxdeviation)
    mindeviation = config.get(sample_type, "mindeviation")
    print("Min deviation: " + mindeviation)
    gaussian = config.get(sample_type, "gaussian")
    print("Gaussian: " + gaussian)
    thresholdingcriteria = config.get(sample_type, "thresholdingcriteria")
    print("Thresholding criteria: " + thresholdingcriteria)
    print(" ")
