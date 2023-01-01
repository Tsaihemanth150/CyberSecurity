import phonenumbers
import functools
import operator
from phonenumbers import geocoder, carrier, timezone

num=input("enter the phone number with country code: ")  ##Input

num1=phonenumbers.parse(num,"CH")  ### FOR THE country
print("Country/City:",geocoder.description_for_number(num1,"en"))

num2=phonenumbers.parse(num,"RO") #### For the operator/carrier
print("Operator/carrier:",carrier.name_for_number(num2,"en"))

num3=phonenumbers.parse(num)

timeZone = timezone.time_zones_for_number(num3)      #for the TimeZone
valid = phonenumbers.is_valid_number(num3)           ## for Validating a phone number
possible = phonenumbers.is_possible_number(num3)     ### Checking possibility of a number

print(num3)
print(" ")
print("TimeZone of the Number:",timeZone)
print("Is Number Valid:",valid)
print("Is is possible number??:",possible)

##################################################

report = open("output.txt","a") # outout will be stored in this file

converted_num = str(num3)

def convertTuple(tup):
    strTimeZone = functools.reduce(operator.add,(tup))
    return strTimeZone

tuple = timeZone
strTimeZone = convertTuple(tuple)
#############################################
value = valid
strValid =str(value)
value1 =possible
strpossible=str(value1)
#############################################
# Here it saves output in text file #
report.write(converted_num)
report.write("\n")
report.write("Country/City:")
report.write(geocoder.description_for_number(num1,"en"))
report.write("\n")
report.write("Operator/carrier:")
report.write(carrier.name_for_number(num2,"en"))
report.write("\n")
report.write("Timezone: ")
report.write(strTimeZone)
report.write("\n")
report.write("Is this Valid:")
report.write(strValid)
report.write(" \n")
report.write("Any number possible ??:")
report.write(strpossible)
report.write("\n")
report.write("\n")
report.close()
########################################################
def convert_file(file):
    pdf = FPDF()
    pdf.add_page()

    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial","B",size=18) # For title text
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=15) # For paragraph text
            pdf.multi_cell(w=0,h=10,txt=text,align="L")
    pdf.output("output.pdf")
    print("Successfully converted!")
file = open("output.txt","r")

convert_file(file)



#################################################
# requried package is phonenumbers
# installtion:- pip install phonenumbers, FPDF

#function to convert the TXT to PDF
