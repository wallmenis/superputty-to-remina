import csv 
import requests 
import xml.etree.ElementTree as ET 
  
# def loadRSS(): 
#   
#     # url of rss feed 
#     url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
#   
#     # creating HTTP response object from given url 
#     resp = requests.get(url) 
#   
#     # saving the xml file 
#     with open('topnewsfeed.xml', 'wb') as f: 
#         f.write(resp.content) 
          
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for news items 
    connectionitems = [] 
    
    #print(root.findall("SessionData"))

    #print()
  
    # iterate news items 
    for item in root.findall("SessionData"): 
  
        # empty news dictionary 
        # connection = {} 
        # print(item.tag)
        # print(item.attrib['SessionId'])
        connection="[remmina]\ndisconnect-prompt=0\nexeccommand=ssh" + str(item.attrib['Username']) + "@" + str(item.attrib['Host']) + " " + str(item.attrib['ExtraArgs']) + "\nssh_tunnel_password=\npostcommand=\nserver=\nkill_proc=0\nssh_tunnel_enabled=0\nprofile-lock=0\nname=" + str(item.attrib['SessionName']) + "\nprecommand=\ngroup=Imported\nssh_tunnel_certfile=\nrunasync=0\nprotocol=EXEC\nssh_tunnel_server=\nenable-autostart=0\nssh_tunnel_auth=0\nignore-tls-errors=1\nnotes_text=\nlabels=\nssh_tunnel_username=\nssh_tunnel_loopback=0\nssh_tunnel_passphrase=\nssh_tunnel_privatekey=\n"
        # iterate child elements of item 
#         for child in item:
#             connection[child.tag] = child.text.encode('utf8')
#             # # special checking for namespace object content:media 
#             # if child.tag == '{http://search.yahoo.com/mrss/}content': 
#             #     news['media'] = child.attrib['url'] 
#             # else: 
#             #     news[child.tag] = child.text.encode('utf8') 
#   
#         # append news dictionary to news items list 
        connectionitems.append(connection) 
      
    # return news items list 
    return connectionitems 
  
  
def savetoFile(connectionitems): 
        count=0
        for i in connectionitems:
            f = open("connection"+str(count)+".remmina", "w")
            f.write(i)
            f.close()
            count=count+1

def main(): 
    # load rss from web to update existing xml file 
    # loadRSS() 
  
    # parse xml file 
    connections = parseXML('Sessions_November_2023.XML') 
    
  
    # store news items in a csv file 
    savetoFile(connections) 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 
