#shell script for downloading the EEB pages:

curl https://www.eeb.ucla.edu/seminars.php?id=[1-800] > 1.html

#python script:

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("1.html"))
main = soup.find(id="main-content")
section_div = main.find_all("div", class_="clear-fix right-wide-column")
for section in section_div:
    div = section.find("div", class_="section")
    name = div.h4
    date = div.p
    print name, date

#the code is wrong but what I wanted to do was find all the ids with EcoEvoPub
#input all those pages with EcoEvoPub into a file object
#parse the file object to print the names and dates
#but I had trouble parsing and finding the right sections in the element inspector 
#that would display the names and date
