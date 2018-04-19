import os

regions = {
    "AFR",
    "ANZ",
    "ASP",
    "EUR",
    "IPM",
    "LTA",
    "NRA",
    "UKI"
}

files = {
    "Delta_ExecutiveInsight.bat",
    "Delta_FD.bat",
    "Delta_NFD.bat",
    "Delta_OwnerShip.bat",
    "Delta_Price.bat",
    "Delta_PriceMultipleRatio.bat",
    "Delta_SayOnPay.bat",
    "Delta_ShareCorporeateAction.bat",
    "Delta_VotingReport.bat"
}

path = "D:\Work\SourceTree\GEDF\ge-gedf-old\EquityDataFeed\JobCommands\Dev\Delta_Region"

DeliveryRegion = "/DeliveryRegions="

def write_content(file, content):
    with open(file, "w") as f:
        f.write(content)

def get_content(file):
    content = ""
    with open(file, "r") as f:
        for line in f.readlines():
            content += line
    return content

def process():
    for file in files:
        for region in regions:
            file_name = file[:-4].split("_")[0] + "_" + region + "_" + file[:-4].split("_")[1] + file[-4:]
            content = get_content(os.path.join(path, file))
            add_content = DeliveryRegion + region
            replace_content = content.replace("EquityDataFeed.exe", "EquityDataFeed.exe " + add_content)
            write_content(os.path.join(path, file_name), replace_content)

process()